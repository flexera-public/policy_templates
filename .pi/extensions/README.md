# github-agents

A [Pi](https://pi.dev) extension that loads agent instruction files from `.github/agents/` and injects them into the system prompt on every agent turn.

## Why

Pi natively loads `AGENTS.md` files from the current directory and its parents. But if your repo already has agent instructions in `.github/agents/` (for GitHub Copilot or other tools), maintaining a separate `AGENTS.md` is redundant. This extension bridges the gap so Pi picks up those files automatically.

Injecting via `before_agent_start` means the instructions are re-added fresh on every prompt, so they **survive compaction** — unlike `AGENTS.md` content which can be summarized away over a long session.

## Install

**Note: Installation is not needed if running [Pi](https://pi.dev) from the root directory of the [flexera-public/policy_templates](https://github.com/flexera-public/policy_templates) Github repository. It will automatically detect and load the extension.**

Copy the extension into your repo's `.pi/extensions/` directory and commit it:

```sh
mkdir -p .pi/extensions
cp github-agents.ts .pi/extensions/
```

Pi auto-discovers extensions in `.pi/extensions/`, so every contributor gets the agent instructions loaded automatically when they run `pi` from the repo root. No extra configuration needed.

## Usage

The extension loads silently on startup and notifies you which files were found:

```text
github-agents: loaded 2 files: coding.md, security.md
```

If `.github/agents/` doesn't exist or contains no `.md` or `.txt` files, you'll see a warning and the extension stays inactive.

### Commands

| Command | Description |
| --- | --- |
| `/github-agents-reload` | Reload files from disk without restarting pi. Useful if you edit a file mid-session. |
| `/github-agents-status` | Show loaded files, character counts, and a content preview. Good for auditing what's actually in the prompt. |

## File support

The extension loads all `.md` and `.txt` files from `.github/agents/`, sorted alphabetically. Empty files are skipped. Files are concatenated in the system prompt, each wrapped in an HTML comment header identifying its source:

```text
<!-- .github/agents/coding.md -->
...content...

---

<!-- .github/agents/security.md -->
...content...
```

## Notifications

| Situation | Behavior |
|---|---|
| Startup | Notifies with loaded file names, or warns if none found |
| `/new`, `/fork`, session resume | Cache refreshed silently (no toast) |
| `/github-agents-reload` | Always notifies with result |
| File read error | Error toast shown at startup and on explicit reload only |

## Requirements

- [Pi coding agent](https://pi.dev) (`@mariozechner/pi-coding-agent`)
- The extension file must remain `.ts` — Pi loads extensions via [jiti](https://github.com/unjs/jiti) and expects TypeScript. Renaming to `.js` will break it.
