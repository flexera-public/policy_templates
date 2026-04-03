# Active Policy List Generation

A Rake task that generates the active policy list JSON file consumed by the Flexera Public Policy Catalog.

## Overview

The `generate_policy_list` task scans all policy template (`.pt`) files in the repository and builds a JSON catalog of every published, versioned policy template. For each template it fetches the date of the most recent commit from the GitHub API and records it alongside the template's metadata.

Output is written to `dist/active-policy-list.json`. The automated workflow then copies this file to `data/active_policy_list/active_policy_list.json` and opens a pull request.

## Usage

Run from the repository root:

```bash
bundle exec rake -f tools/active_policy_list_generation/Rakefile generate_policy_list
```

The `GITHUB_API_TOKEN` environment variable must be set to a GitHub personal access token or the `GITHUB_TOKEN` secret provided by GitHub Actions.

## Automated Workflow

There is an automated [GitHub Workflow](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-active-policy-list.yaml) that runs every time the [Test Policies](https://github.com/flexera-public/policy_templates/actions/workflows/test-policies.yaml) workflow completes successfully against the master branch. It generates an updated `data/active_policy_list/active_policy_list.json` and automatically opens a pull request with the updated file, which can be approved by the Policy Template Maintainers.

## Output Format

The output JSON contains a top-level `policies` array. Each entry includes:

- `name` — Policy template display name
- `file_name` — Repository-relative path to the `.pt` file
- `version` — Semantic version from the template header
- `change_log` — Repository-relative path to the template's `CHANGELOG.md`
- `readme` — Repository-relative path to the template's `README.md`
- `description` — Short description from the template header
- `category` — Template category (e.g. `Cost`, `Compliance`)
- `severity` — Incident severity (`low`, `medium`, `high`, `critical`)
- `provider` — Cloud provider (e.g. `AWS`, `Azure`, `Google`)
- `service` — Cloud service (e.g. `Compute`, `Storage`)
- `policy_set` — Recommendation grouping label
- `recommendation_type` — `Usage Reduction` or `Rate Reduction` (if applicable)
- `updated_at` — ISO 8601 timestamp of the most recent commit that touched the file
- `generally_recommended` — Whether the template is in the generally-recommended list for its provider
- `deprecated` — Whether the template is marked as deprecated
- `hide_skip_approvals` — Whether the "Skip Approval" UI button is hidden

The policies array is sorted alphabetically by name to minimize diffs between runs.
