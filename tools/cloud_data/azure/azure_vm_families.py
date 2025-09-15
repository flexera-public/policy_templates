import csv
import io
import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

CSV_URL = "https://aka.ms/isf"
OUTPUT_PATH = Path("data/azure/azure_vm_families.json")

# Map CSV column names -> desired JSON field names
RENAME_MAP = {
    "InstanceSizeFlexibilityGroup": "instance_family",
    "ArmSkuName": "instance_type",
    "Ratio": "ratio",
}

NULL_LITERALS = {"", "na", "n/a", "null", "none", "nil", "-"}

def decode_bytes(b: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8", "utf-16", "utf-16-le", "utf-16-be", "cp1252", "latin-1"):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            continue
    return b.decode("latin-1", errors="replace")

def coerce_value(s: str):
    if s is None:
        return None
    v = str(s).strip()
    lower = v.lower()
    if lower in NULL_LITERALS:
        return None
    if lower in {"true", "false"}:
        return lower == "true"
    if lower in {"yes", "no"}:
        return lower == "yes"
    try:
        if v and (v.isdigit() or (v.startswith("-") and v[1:].isdigit())):
            return int(v)
    except ValueError:
        pass
    try:
        if any(ch.isdigit() for ch in v):
            return float(v)
    except ValueError:
        pass
    return v

def sniff_dialect(sample: str):
    try:
        return csv.Sniffer().sniff(sample)
    except csv.Error:
        return csv.excel

def download_csv(url: str) -> str:
    req = Request(url, headers={"User-Agent": "python-urllib/3"})
    try:
        with urlopen(req, timeout=60) as resp:
            data = resp.read()
    except HTTPError as e:
        print(f"HTTP error {e.code} when downloading {url}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except URLError as e:
        print(f"Network error when downloading {url}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    return decode_bytes(data)

def csv_to_json_rows(csv_text: str):
    """Read CSV and output ONLY the renamed fields defined in RENAME_MAP."""
    sample = csv_text[:8192]
    dialect = sniff_dialect(sample)
    f = io.StringIO(csv_text)
    reader = csv.DictReader(f, dialect=dialect)

    rows = []
    for row in reader:
        out = { new: coerce_value(row.get(old)) for old, new in RENAME_MAP.items() }
        rows.append(out)
    return rows

def ensure_parent_dir(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)

def main():
    print("Downloading CSV from aka.ms/isf ...")
    csv_text = download_csv(CSV_URL)
    if not csv_text.strip():
        print("Downloaded CSV appears to be empty.", file=sys.stderr)
        sys.exit(1)

    print("Converting CSV to JSON with renamed fields ...")
    rows = csv_to_json_rows(csv_text)
    if not rows:
        print("No rows found in the CSV. Nothing to write.", file=sys.stderr)
        sys.exit(1)

    ensure_parent_dir(OUTPUT_PATH)
    print(f"Writing {len(rows)} records to {OUTPUT_PATH} ...")
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    print("Done.")

if __name__ == "__main__":
    main()
