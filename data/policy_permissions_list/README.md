# Policy Permissions List

This directory contains auto-generated files listing all permissions required by policy templates in the catalog. **Do not manually modify these files** — they are regenerated automatically.

See [`tools/policy_master_permission_generation/`](https://github.com/flexera-public/policy_templates/tree/master/tools/policy_master_permission_generation) for the scripts that produce these files.

## Auto-Generated Files

### master_policy_permissions_list.json / .csv / .yaml / .pdf

**Script:** [`tools/policy_master_permission_generation/generate_policy_master_permissions.rb`](https://github.com/flexera-public/policy_templates/blob/master/tools/policy_master_permission_generation/generate_policy_master_permissions.rb)

**Workflow:** [Generate Policy Master Permissions Assets](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-master-permissions-json.yaml)

**Description:** A comprehensive list of all IAM permissions required by every policy template in the catalog, organized by policy template and cloud provider. The same data is published in JSON, CSV, YAML, and PDF formats for different consumer use cases. Used by security auditors, platform administrators, and customers who need to set up appropriate IAM permissions before deploying policy templates.

**Structure (`master_policy_permissions_list.json`):** Object with a single `values` key containing an array of policy permission objects.

| Field | Type | Description |
| --- | --- | --- |
| `id` | string | Repository-relative path to the `.pt` file |
| `name` | string | Human-readable policy template name |
| `version` | string | Policy template version string |
| `providers` | array | Array of provider permission objects (see below) |

Each object in `providers` contains:

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Provider identifier, e.g. `"aws"`, `"azure"`, `"flexera"` |
| `permissions` | array | Array of permission objects for this provider |

Each object in `permissions` contains:

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Permission name, e.g. `"ec2:DescribeInstances"` or `"billing_center_viewer"` |
| `read_only` | boolean | Whether this permission is read-only |
| `required` | boolean | Whether this permission is required for the policy to function |
| `description` | string | (Optional) Explanation of why this permission is needed |

**Example:**

```json
{
  "values": [
    {
      "id": "./cost/aws/idle_compute_instances/idle_compute_instances.pt",
      "name": "AWS Idle Compute Instances",
      "version": "4.2.0",
      "providers": [
        {
          "name": "aws",
          "permissions": [
            { "name": "ec2:DescribeInstances", "read_only": true, "required": true },
            { "name": "ec2:TerminateInstances", "read_only": false, "required": false }
          ]
        },
        {
          "name": "flexera",
          "permissions": [
            { "name": "billing_center_viewer", "read_only": true, "required": true },
            {
              "name": "policy_manager",
              "read_only": true,
              "required": false,
              "description": "Only required for meta-policy self-termination."
            }
          ]
        }
      ]
    }
  ]
}
```

### master_policy_permissions_list_aws.pdf / _azure.pdf / _google.pdf / _oracle.pdf

**Script:** Same as above (`generate_policy_master_permissions.rb`)

**Workflow:** Same as above

**Description:** Provider-specific subsets of the master permissions list in PDF format, one file per cloud provider. These are convenience files for teams that only need permissions for a single provider.

### missing_policy_templates.json / .yaml

**Script:** [`tools/policy_master_permission_generation/generate_missing_permission_list.rb`](https://github.com/flexera-public/policy_templates/blob/master/tools/policy_master_permission_generation/generate_missing_permission_list.rb)

**Workflow:** [Generate Policy Master Permissions Missing Templates JSON/YAML](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-master-permission-missing-templates.yaml)

**Description:** A list of policy template file paths that exist in the repository but are not yet included in the master permissions list. Used to track which templates still need permission metadata added.

**Structure (`missing_policy_templates.json`):** Object with a single `missing_templates` key containing an array of file path strings.

**Example:**

```json
{
  "missing_templates": [
    "./automation/aws/aws_rbd_from_org_tag/aws_rbd_from_org_tag.pt"
  ]
}
```
