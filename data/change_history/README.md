# Change History

This directory contains an auto-generated record of all pull requests merged into the repository. A companion human-readable summary file (`HISTORY.md`) at the root of the repository is also generated.

## Auto-Generated Files

### change_history.json

**Script:** [`tools/change_history/`](https://github.com/flexera-public/policy_templates/blob/master/tools/change_history/)

**Workflow:** [Update Change History](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-change-history.yaml) — runs every time a pull request is merged (excluding PRs that update this file itself).

**Description:** A chronological list of all merged pull requests in the repository, including metadata such as labels, description, and which files were modified. This file feeds the [HISTORY.md](https://github.com/flexera-public/policy_templates/blob/master/HISTORY.md) human-readable changelog at the repository root.

**Structure:** Object with a single `merged_prs` key containing an array of pull request objects.

| Field | Type | Description |
| --- | --- | --- |
| `number` | number | GitHub pull request number |
| `title` | string | Pull request title |
| `description` | string | Pull request description/body text |
| `labels` | array | List of label strings applied to the pull request |
| `href` | string | URL to the pull request on GitHub |
| `created_at` | string | Timestamp when the PR was created (UTC) |
| `merged_at` | string | Timestamp when the PR was merged (UTC) |
| `modified_files` | array | List of repository-relative file paths modified by the PR |

**Example:**

```json
{
  "merged_prs": [
    {
      "number": 1234,
      "title": "Add AWS Idle Compute Instances policy",
      "description": "Adds a new policy template that identifies idle EC2 instances.",
      "labels": ["enhancement", "aws"],
      "href": "https://github.com/flexera-public/policy_templates/pull/1234",
      "created_at": "2024-03-15 10:00:00 UTC",
      "merged_at": "2024-03-15 14:30:00 UTC",
      "modified_files": [
        "cost/aws/idle_compute_instances/idle_compute_instances.pt",
        "cost/aws/idle_compute_instances/README.md"
      ]
    }
  ]
}
```
