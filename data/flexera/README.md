# Flexera Data

This directory contains manually-maintained reference data for the Flexera platform.

## Manually Maintained Files

### iam_roles.json

**Description:** A reference list of all Flexera platform IAM role definitions. Used by policy templates and tooling that need to validate, enumerate, or display Flexera IAM roles — for example, policies that audit IAM role assignments or generate permission reports.

**Structure:** Array of IAM role objects.

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Role identifier used in the Flexera API, e.g. `"billing_center_viewer"` |
| `category` | string | Grouping category for the role |
| `displayName` | string | Human-readable role name as shown in the Flexera UI |

**Categories:** Automation, Cloud, Data and Analytics, Discovery and Inventory, IT Visibility, Other, Platform Administration, SCA Data Library, Self-service CloudApps, Software Bill Of Materials, Technology Spend

**Example:**

```json
[
  {
    "name": "billing_center_viewer",
    "category": "Cloud",
    "displayName": "Billing Center Viewer"
  },
  {
    "name": "policy_manager",
    "category": "Automation",
    "displayName": "Policy Manager"
  }
]
```
