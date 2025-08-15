#!/usr/bin/env python3
"""
Bump patch versions in .pt files and update CHANGELOG.md
for directories that contain any .pt file with:
    datasource "ds_get_parent_policy" do

Usage:
  python bump_pt_versions.py [ROOT_DIR] [--apply] [--replace-existing]
       [--entry "Your bullet text"]

Defaults:
  ROOT_DIR = current working directory
  Dry run (no writes) unless --apply is provided.
  By default, if CHANGELOG already has the new version section, it is left unchanged.
  Use --replace-existing to replace that whole section with the generated one.

Exit code:
  0 on success, 1 if any error occurs.
"""
from __future__ import annotations
import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Optional, Tuple

TARGET_SNIPPET = 'datasource "ds_get_parent_policy" do'
VERSION_RE = re.compile(r'(?P<prefix>\bversion\s*:\s*")(?P<maj>\d+)\.(?P<min>\d+)\.(?P<patch>\d+)(")')
CHANGELOG_HEADER_RE = re.compile(r'(?mi)^#\s*Changelog\s*$')
# Matches a whole version section starting at "## vX.Y.Z" up to (but not including) the next "## v..."
def changelog_section_re(version: str) -> re.Pattern:
    escaped = re.escape(version)
    return re.compile(rf'(?ms)^##\s+v{escaped}\s*\n.*?(?=^##\s+v|\Z)')

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Bump .pt patch versions and update CHANGELOGs.")
    p.add_argument("root", nargs="?", default=".", help="Root directory to scan (default: .)")
    p.add_argument("--apply", action="store_true", help="Write changes to files (default: dry run)")
    p.add_argument("--replace-existing", action="store_true",
                   help="If a CHANGELOG section for the new version exists, replace it instead of leaving it.")
    p.add_argument("--entry", default="– Updated internal datasource handling. Functionality unchanged.",
                   help='Bullet text for the new CHANGELOG entry (default: "Updated internal datasource handling...")')
    return p.parse_args()

def bump_patch(ver: Tuple[int, int, int]) -> Tuple[int, int, int]:
    return (ver[0], ver[1], ver[2] + 1)

def parse_semver_tuple(s: str) -> Tuple[int, int, int]:
    parts = s.strip().split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        raise ValueError(f"Not a semver: {s}")
    return (int(parts[0]), int(parts[1]), int(parts[2]))

def semver_to_str(t: Tuple[int, int, int]) -> str:
    return f"{t[0]}.{t[1]}.{t[2]}"

def find_pt_files(dirpath: Path) -> List[Path]:
    return sorted([p for p in dirpath.iterdir() if p.is_file() and p.suffix == ".pt"])

def file_contains_target(path: Path) -> bool:
    try:
        return TARGET_SNIPPET in path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False

def bump_versions_in_pt_files(pt_paths: List[Path], apply: bool) -> List[Tuple[Path, str, str]]:
    """
    Returns list of (path, old_ver, new_ver) for files that were (or would be) changed.
    """
    changes = []
    for pt in pt_paths:
        try:
            content = pt.read_text(encoding="utf-8")
        except Exception as e:
            print(f"!! Could not read {pt}: {e}", file=sys.stderr)
            continue

        def _repl(m: re.Match) -> str:
            old_tuple = (int(m.group("maj")), int(m.group("min")), int(m.group("patch")))
            new_tuple = bump_patch(old_tuple)
            old_ver = semver_to_str(old_tuple)
            new_ver = semver_to_str(new_tuple)
            changes.append((pt, old_ver, new_ver))
            return f'{m.group("prefix")}{new_ver}{m.group(5)}'

        new_content, nsubs = VERSION_RE.subn(_repl, content, count=1)
        if nsubs > 0 and apply:
            try:
                pt.write_text(new_content, encoding="utf-8")
            except Exception as e:
                print(f"!! Could not write {pt}: {e}", file=sys.stderr)
    return changes

def ensure_changelog(dirpath: Path) -> Path:
    cl = dirpath / "CHANGELOG.md"
    if not cl.exists():
        cl.write_text("# Changelog\n\n", encoding="utf-8")
    return cl

def highest_version_from_changes(changes: List[Tuple[Path, str, str]]) -> Optional[str]:
    if not changes:
        return None
    # Use the highest *new* version among changed .pt files for the directory’s CHANGELOG entry.
    new_vers = [parse_semver_tuple(nv) for _, _, nv in changes]
    return semver_to_str(max(new_vers))

def insert_or_replace_changelog_entry(changelog_path: Path, new_version: str, bullet_text: str,
                                      replace_existing: bool, apply: bool) -> str:
    """
    Returns a string describing what would be/were done.
    """
    try:
        text = changelog_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"!! Could not read {changelog_path}: {e}"

    # Ensure main header
    if not CHANGELOG_HEADER_RE.search(text):
        text = "# Changelog\n\n" + text

    # Prepare new section
    new_section = f"## v{new_version}\n\n- {bullet_text}\n\n"

    sect_re = changelog_section_re(new_version)
    if sect_re.search(text):
        if replace_existing:
            updated = sect_re.sub(new_section, text, count=1)
            action = f"replaced existing v{new_version} section"
            if apply:
                changelog_path.write_text(updated, encoding="utf-8")
            return f"{action} in {changelog_path.name}"
        else:
            return f"left existing v{new_version} section as-is in {changelog_path.name}"
    else:
        # Insert after "# Changelog" header
        m = CHANGELOG_HEADER_RE.search(text)
        insert_pos = m.end()
        # Find the end of that line and following blank lines
        line_end = text.find("\n", insert_pos)
        if line_end == -1:
            line_end = len(text)
        # ensure exactly two newlines after header before new section
        head = text[:line_end].rstrip() + "\n\n"
        tail = text[line_end:].lstrip("\n")
        updated = head + new_section + tail
        if apply:
            changelog_path.write_text(updated, encoding="utf-8")
        return f"inserted v{new_version} section at top of {changelog_path.name}"

def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        print(f"Root directory not found: {root}", file=sys.stderr)
        return 1

    any_errors = False
    total_dirs_considered = 0
    total_dirs_changed = 0

    for dirpath, dirnames, filenames in os.walk(root):
        d = Path(dirpath)
        # Only operate at each directory level; don't aggregate across siblings.
        pt_files = [d / f for f in filenames if f.endswith(".pt")]
        if not pt_files:
            continue

        total_dirs_considered += 1

        # Only proceed if ANY .pt in this directory contains the target snippet
        if not any(file_contains_target(p) for p in pt_files):
            continue

        # Bump all .pt versions in this directory (only first version occurrence per file)
        changes = bump_versions_in_pt_files(pt_files, apply=args.apply)
        if not changes:
            # No version strings found = nothing to do here
            continue

        total_dirs_changed += 1
        # Determine what version to record in CHANGELOG (highest new version among changed files)
        new_version = highest_version_from_changes(changes)
        if not new_version:
            continue

        # Update CHANGELOG
        changelog = ensure_changelog(Path(dirpath))
        action_msg = insert_or_replace_changelog_entry(
            changelog, new_version, args.entry, args.replace_existing, args.apply
        )

        # Report
        print(f"\nDirectory: {dirpath}")
        for path, oldv, newv in changes:
            print(f"  {path.name}: {oldv} -> {newv}")
        print(f"  CHANGELOG: {action_msg}")

    mode = "APPLIED" if args.apply else "DRY-RUN"
    print(f"\nDone ({mode}). Directories scanned with .pt files: {total_dirs_considered}. "
          f"Directories updated: {total_dirs_changed}.")
    return 0 if not any_errors else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nAborted by user.", file=sys.stderr)
        sys.exit(1)

