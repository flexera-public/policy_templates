# Azure Cloud Data

Various Azure-specific data assets, such as pricing data. Some assets are manually maintained and some are generated through automation; see the [Cloud Data Scripts README](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/README.md) for more information on how these assets are generated.

## azure_compute_instance_types.json / instance_types.json

`azure_compute_instance_types.json` is a newer asset generated and updated through automation. It's data comes directly from the Azure API. This asset should be used in policy templates that need detailed information about Azure virtual machine instance types.

`instance_types.json` is similar but is older and manually maintained. It should not be used in policy templates going forward. This asset will remain in the repository long term to ensure that older policy templates continue to function as intended.

Some data fields in `azure_compute_instance_types.json` are currently imported from `instance_types.json` until we build proper automation to gather/calculate this information:

- superseded
- specs.nfu

## azure_sql_license_pricing.json

**Script:** [`tools/cloud_data/azure/azure_sql_license_pricing.py`](https://github.com/flexera-public/policy_templates/blob/master/tools/cloud_data/azure/azure_sql_license_pricing.py)

**Workflow:** [Generate Azure SQL License Pricing JSON](https://github.com/flexera-public/policy_templates/blob/master/.github/workflows/generate-azure-sql-license-pricing-json.yaml)

**Description:** Hourly SQL Server license prices per vCPU (USD), sourced from the `Virtual Machines Licenses` service in the Azure Retail Prices API. Covers the four standard SQL Server editions: `Enterprise`, `Standard`, `Web`, and `Developer`. These are global prices (not region-specific). The pricing is perfectly linear — the total cost for any vCPU count equals `price_per_vcpu × vcpu_count` — so a single per-vCPU rate is stored for each edition. Used by policy templates that calculate estimated savings from enabling Azure Hybrid Use Benefit on SQL Server resources.

**Structure:** Flat object mapping SQL Server edition name to USD hourly price per vCPU.

| Field | Type | Description |
| --- | --- | --- |
| `Developer` | number | Per-vCPU hourly license price for Developer edition (always 0 — free) |
| `Enterprise` | number | Per-vCPU hourly license price for Enterprise edition |
| `Standard` | number | Per-vCPU hourly license price for Standard edition |
| `Web` | number | Per-vCPU hourly license price for Web edition |

**Example:**

```json
{
  "Developer": 0,
  "Enterprise": 0.375,
  "Standard": 0.1,
  "Web": 0.008
}
```
