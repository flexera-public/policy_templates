# Using GitHub Copilot CLI to Build Policy Templates

This guide explains how to use GitHub Copilot CLI together with the `policy-dev` agent to create, edit, and review Flexera policy templates in this repository.

---

## What Is GitHub Copilot CLI?

GitHub Copilot CLI is an AI-powered terminal assistant that brings Copilot's agentic coding capabilities directly to your command line. It can read and write files, run shell commands, search the codebase, and carry on a multi-turn conversation — all without leaving your terminal.

### Installation

```bash
# macOS / Linux / WSL2
curl -fsSL https://gh.io/copilot-install | bash

# macOS with Homebrew
brew install copilot-cli

# Windows (WinGet)
winget install GitHub.Copilot

# npm (cross-platform)
npm install -g @github/copilot
```

### Starting a session

```bash
cd /path/to/policy_templates   # always launch from the repo root
copilot
```

On first launch, follow the on-screen instructions to log in with your GitHub account. An active Copilot subscription is required.

---

## The `policy-dev` Agent

The repository ships with a custom agent at `.github/agents/policy-dev.agent.md`. It is a specialist that knows:

- The Flexera policy template DSL (`.pt` files)
- Repository directory conventions, file naming, and versioning rules
- Style-guide requirements enforced by the Dangerfile
- Standard parameter patterns, credential boilerplate, and common JavaScript patterns
- README and CHANGELOG format requirements
- Which automation files (`validated_policy_templates.yaml`, `default_template_files.yaml`) need updating

### Activating the agent

Type `/agent` in the Copilot CLI prompt and select **policy-dev** from the list, or mention it by name in your first message:

```text
@policy-dev create a new AWS cost policy that identifies unattached EBS volumes
```

Using `@policy-dev` at the start of a prompt automatically routes the request to the specialist agent.

---

## Common Tasks

### 1. Create a New Policy Template from Scratch

Provide the agent with enough context to generate production-ready files:

```text
@policy-dev Create a new cost policy for AWS that finds EC2 instances that have
been stopped for more than 30 days and recommends terminating them.
The policy should support region filtering, tag-based exclusions, and meta policies.
```

The agent will:

1. Choose the correct directory path (e.g. `cost/aws/stopped_ec2_instances/`)
1. Write the `.pt` file starting with `publish: "false"` in the `info()` block
1. Run `fpt check` to validate syntax (requires `~/.fpt.yml` credentials)
1. Generate `README.md` and `CHANGELOG.md`
1. Add the path to `tools/policy_master_permission_generation/validated_policy_templates.yaml`
1. Optionally add it to `tools/meta_parent_policy_compiler/default_template_files.yaml`

### 2. Create a Policy for a Specific Provider

Include the provider, service, and category so the agent places the files in the right location:

```text
@policy-dev Create an Azure compliance policy that checks all Storage Accounts
for public blob access and reports any that have it enabled.
Place it in compliance/azure/storage_public_access/.
```

### 3. Modify an Existing Policy Template

Point the agent to the file and describe the change:

```text
@policy-dev Update cost/aws/old_snapshots/aws_delete_old_snapshots.pt to add
a minimum savings threshold parameter. Follow the style guide conventions.
```

The agent will:

- Read the existing `.pt`, `README.md`, and `CHANGELOG.md`
- Apply the change following style-guide rules
- Bump the version (MAJOR / MINOR / PATCH) as appropriate
- Update the CHANGELOG with a user-facing description

### 4. Review a Policy Template

Ask the agent to review a file before you open a pull request:

```text
@policy-dev Review cost/aws/old_snapshots/aws_delete_old_snapshots.pt for style
guide compliance, correct README format, and valid CHANGELOG entries.
```

The agent checks:

- `info()` block completeness (version, provider, service, publish)
- Directory structure and snake_case naming
- Section order in `.pt` file
- README section order and required content
- CHANGELOG format (`# Changelog`, `## vX.Y.Z` headings)
- Semantic versioning correctness
- No hardcoded secrets or credentials

### 5. Validate Syntax

After writing or editing a `.pt` file, ask the agent to run the linter:

```text
@policy-dev Run fpt check on cost/aws/old_snapshots/aws_delete_old_snapshots.pt
and fix any errors.
```

> **Note:** `fpt check` requires valid Flexera credentials in `~/.fpt.yml`. The agent will prompt you to confirm before running any `fpt` command other than `check`. See [policy_sdk](https://github.com/flexera-public/policy_sdk) for credential setup.

### 6. Generate a Meta Parent Policy

If your template supports Meta Policies, ask the agent to compile the parent:

```text
@policy-dev Add meta policy support to cost/aws/stopped_ec2_instances/
and generate the meta parent template.
```

The agent will update `tools/meta_parent_policy_compiler/default_template_files.yaml` and run the compiler if it is available.

---

## Useful Prompting Tips

| Goal | Prompt pattern |
| --- | --- |
| New catalog template | `@policy-dev Create a [cost/compliance/operational/security] policy for [provider] that [does X]` |
| Based on an existing template | `@policy-dev Create a new policy similar to [path/to/existing.pt] but for [different resource]` |
| Add a feature | `@policy-dev Add [feature] to [path/to/policy.pt], bump the version, and update the CHANGELOG` |
| Full review | `@policy-dev Review [path/to/policy.pt] against the style guide and README requirements` |
| Explain code | `@policy-dev Explain how the billing datasource in [path/to/policy.pt] works` |
| Fix Dangerfile errors | `@policy-dev Fix the Dangerfile errors reported on PR #NNNNN` |

---

## Modes and Keyboard Shortcuts

| Shortcut | Effect |
| --- | --- |
| `Shift+Tab` | Cycle through modes: **Interactive → Plan → Autopilot** |
| `Ctrl+S` | Run the current command while preserving the input |
| `Ctrl+C` | Cancel the current operation or clear input |
| `/plan` | Ask Copilot to produce an implementation plan before writing code |
| `/diff` | Review all file changes made in the current session |
| `/undo` | Revert the last turn's file changes |
| `/model` | Switch AI models (e.g. Claude Sonnet, GPT-5) |

Use **Plan mode** (`Shift+Tab` until you see `[plan]`) for larger tasks — Copilot will outline its approach and wait for your approval before touching any files.

---

## Contribution Workflow with Copilot CLI

Below is the recommended end-to-end flow for adding a new template to the catalog:

```text
1.  git checkout -b POL-XXXX-my-new-policy
2.  copilot                              # launch Copilot CLI in repo root
3.  @policy-dev Create a new [category] policy for [provider] that [does X]
4.  # Agent writes .pt, README.md, CHANGELOG.md and updates automation YAML files
5.  # Review generated files; iterate with the agent as needed
6.  @policy-dev Run fpt check on [path/to/new_policy.pt] and fix any errors
7.  git add -A && git commit -m "POL-XXXX Add [policy name]"
8.  gh pr create --title "POL-XXXX [Policy Name]" --label "NEW POLICY TEMPLATE,UNPUBLISHED"
9.  # Dangerfile runs automatically; ask the agent to fix any reported issues:
10. @policy-dev Fix the Dangerfile errors on PR #NNNNN
```

---

## Key Repository Resources

| Resource | Purpose |
| --- | --- |
| [`STYLE_GUIDE.md`](STYLE_GUIDE.md) | Naming, versioning, formatting conventions |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Branch, PR, and merge workflow |
| [`README.md`](README.md) | Catalog overview and template list |
| [`README_META_POLICIES.md`](README_META_POLICIES.md) | Meta policy architecture and usage |
| [`tools/policy_master_permission_generation/`](tools/policy_master_permission_generation/) | Permission scraping — add new template paths here |
| [`tools/meta_parent_policy_compiler/`](tools/meta_parent_policy_compiler/) | Meta parent compiler — add meta-enabled template paths here |
| [Flexera Automation Docs](https://docs.flexera.com/flexera-one/automation/) | Official policy template language reference |
| [policy_sdk (fpt)](https://github.com/flexera-public/policy_sdk) | CLI tool for syntax checking and live testing |

---

## Frequently Asked Questions

**Q: Do I need Flexera credentials to use the agent?**
A: No — the agent can write, review, and search files without credentials. You only need `~/.fpt.yml` credentials when you want to run `fpt check` (syntax validation) or `fpt run` (live testing). The agent will alert you before issuing those commands.

**Q: Will the agent commit or push my changes automatically?**
A: No. The agent creates and edits files locally, but all `git` operations (commit, push, PR creation) remain under your control unless you explicitly ask the agent to run those commands.

**Q: What if the agent produces code that fails `fpt check`?**
A: Show the agent the error output and ask it to fix the issues. The policy template DSL has strict syntax requirements; the agent is tuned for them but occasionally needs a correction loop. Example: `@policy-dev fpt check returned the following error — please fix it: [paste error]`

**Q: Can I use Copilot CLI to work on non-catalog (private or internal) templates?**
A: Yes. The `policy-dev` agent is useful for any `.pt` file regardless of whether it is destined for the public catalog. Just omit the catalog-specific steps (automation YAML updates, Dangerfile label requirements) from your workflow.

**Q: What's the difference between Interactive and Autopilot mode?**
A: In **Interactive** mode (default), the agent pauses to ask for confirmation before running shell commands or making large changes. In **Autopilot** mode (experimental, `Shift+Tab` twice), it works autonomously until the task is done. Use Autopilot for well-defined tasks and Interactive mode when you want to review each step.
