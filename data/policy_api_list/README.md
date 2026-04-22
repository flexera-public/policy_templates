# Policy API List

This directory contains auto-generated files listing all API calls made by policy templates in the catalog. **Do not manually modify these files** — they are regenerated automatically.

## Auto-Generated Files

### policy_api_list.json / policy_api_list.csv

**Script:** [`tools/policy_api_list_generation/policy_api_list_generator.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/policy_api_list_generation/policy_api_list_generator.py)

**Workflow:** [Generate Policy API List](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-policy-api-list.yaml) — runs on every push to the default branch and opens a pull request if the output changes.

**Description:** A complete list of every API call made by every policy template in the catalog, extracted by statically analyzing each `.pt` file. The JSON and CSV files contain identical data in different formats. Used by tooling and consumers that need to understand which APIs policy templates depend on, or audit API usage across the catalog.

**Structure (`policy_api_list.json`):** Object with a single `api_calls` key containing an array of API call records.

| Field | Type | Description |
| --- | --- | --- |
| `policy_name` | string | Human-readable name of the policy template |
| `policy_file` | string | Repository-relative path to the `.pt` file |
| `policy_version` | string | Version of the policy template |
| `datasource_name` | string | Name of the datasource block making the API call |
| `api_service` | string | Logical service being called, e.g. `"AWS EC2"` or `"Flexera Billing"` |
| `method` | string | HTTP method, e.g. `"GET"` or `"POST"` |
| `endpoint` | string | Base URL or host of the API endpoint |
| `operation` | string | API operation or path |
| `field` | string | Specific field or resource being accessed |
| `permission` | string | IAM permission required to make this call |

**Example:**

```json
{
  "api_calls": [
    {
      "policy_name": "AWS Idle Compute Instances",
      "policy_file": "cost/aws/idle_compute_instances/idle_compute_instances.pt",
      "policy_version": "4.2.0",
      "datasource_name": "ds_aws_instances",
      "api_service": "AWS EC2",
      "method": "GET",
      "endpoint": "https://ec2.amazonaws.com",
      "operation": "DescribeInstances",
      "field": "instanceId",
      "permission": "ec2:DescribeInstances"
    }
  ]
}
```
