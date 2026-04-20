# Active Policy List

This directory contains data assets related to the published policy template catalog. Some files are auto-generated and some are manually maintained.

## Auto-Generated Files

The following files are produced by scripts in [`tools/active_policy_list_generation/`](https://github.com/flexera-public/policy_templates/tree/master/tools/active_policy_list_generation) and are kept up to date by GitHub Actions workflows.

### active_policy_list.json

**Script:** [`tools/active_policy_list_generation/generate_active_policy_list.rb`](https://github.com/flexera-public/policy_templates/blob/master/tools/active_policy_list_generation/generate_active_policy_list.rb)

**Workflow:** [Update Active Policy List](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/update-active-policy-list.yaml) — runs every time a pull request is merged.

**Description:** A complete list of all policy templates published to the Flexera policy catalog, with their metadata. This is the authoritative source for policy catalog tooling; automation scripts and customer integrations use it to discover available templates.

**Structure:** Object with a single `policies` key containing an array of policy template objects.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Human-readable policy template name |
| `file_name` | string | Relative path to the `.pt` file within the repository |
| `version` | string | Current version string, e.g. `"3.1.2"` |
| `change_log` | string | Relative path to the `CHANGELOG.md` file |
| `description` | string | Short description of what the policy does |
| `category` | string | Top-level category, e.g. `"Cost"`, `"Security"`, `"Operational"` |
| `severity` | string | Default incident severity: `"low"`, `"medium"`, `"high"`, or `"critical"` |
| `readme` | string | URL to the README on GitHub |
| `provider` | string | Cloud provider, e.g. `"aws"`, `"azure"`, `"google"`, `"flexera"` |
| `service` | string | Cloud service the policy targets, e.g. `"Compute"`, `"Storage"` |
| `policy_set` | string | Logical grouping within the catalog |
| `recommendation_type` | string | Type of recommendation the policy makes, e.g. `"Usage Reduction"` |
| `updated_at` | string | ISO 8601 timestamp of the last update |
| `generally_recommended` | boolean | Whether this template is in the generally recommended list |
| `deprecated` | boolean | Whether this template has been deprecated |
| `hide_skip_approvals` | boolean | Whether to hide the skip approvals option in the UI |

**Example:**

```json
{
  "policies": [
    {
      "name": "AKS Node Pools Without Autoscaling",
      "file_name": "operational/azure/aks_nodepools_without_autoscaling/aks_nodepools_without_autoscaling.pt",
      "version": "3.1.2",
      "change_log": "operational/azure/aks_nodepools_without_autoscaling/CHANGELOG.md",
      "description": "Raise an incident if there are any AKS user node pools without autoscaling enabled.",
      "category": "Operational",
      "severity": "medium",
      "readme": "https://github.com/flexera-public/policy_templates/tree/master/operational/azure/aks_nodepools_without_autoscaling",
      "provider": "azure",
      "service": "Compute",
      "policy_set": "AKS",
      "recommendation_type": "",
      "updated_at": "2024-10-01T00:00:00Z",
      "generally_recommended": false,
      "deprecated": false,
      "hide_skip_approvals": false
    }
  ]
}
```

## Manually Maintained Files

### generally_recommended_templates.json

**Description:** Defines which policy templates are considered "generally recommended" for each cloud provider. This list is curated by the Flexera Solution Architect and Advisor teams and includes templates recommended for all customers who use the respective cloud vendor. The automation that generates `active_policy_list.json` reads this file to set the `generally_recommended` field.

Policy templates on this list should:

- Be well tested in the field
- Have default values for all required parameters
- Have validated outcomes from customers

**Structure:** Object keyed by cloud provider name, each value being an array of policy template name strings.

**Provider keys:** `flexera`, `aws`, `azure`, `google`

**Example:**

```json
{
  "aws": [
    "AWS Idle Compute Instances",
    "AWS Unused Volumes"
  ],
  "azure": [
    "Azure Idle Compute Instances",
    "Azure Unused Managed Disks"
  ]
}
```
