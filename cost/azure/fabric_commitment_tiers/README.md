# Azure Microsoft Fabric Commitment Tier Recommendations

## What It Does

This policy template identifies Azure [Microsoft Fabric](https://learn.microsoft.com/en-us/fabric/) capacities on Pay-As-You-Go (PAYG) pricing where purchasing a 1-year reserved capacity would reduce costs. It queries historical Capacity Unit (CU) utilization data from Azure Monitor over the user-specified lookback period and compares the current estimated PAYG monthly cost against the monthly cost of a 1-year reservation at each available F-SKU tier. When a reservation tier — including a right-sized smaller tier — is found to produce lower overall monthly costs, an incident is raised with a recommendation to switch.

## How It Works

The policy template performs the following steps:

1. All Azure subscriptions are enumerated and filtered based on the configured allow/deny list.
1. All Microsoft Fabric capacities in each subscription are listed via the Azure Resource Manager API.
1. For each capacity, Azure Monitor is queried for daily average and peak CU utilization (as a percentage of the capacity's total CU allocation) over the configured lookback period. **Note:** Azure Monitor platform metrics for `Microsoft.Fabric/capacities` are not formally documented in the public Azure Monitor supported-metrics reference as of this template's initial release. If the metric name `CapacityUnitConsumptionPercent` is incorrect for your environment, all capacities will show zero active days and no recommendations will be generated. To verify the correct metric name, check the Azure Monitor Metrics blade for any Fabric capacity resource in the Azure portal, or query the metrics namespace `microsoft.fabric/capacities` via the Azure CLI (`az monitor metrics list-definitions --resource <resourceId>`).
1. The Azure Retail Prices API is queried for current Pay-As-You-Go hourly pricing and 1-year reservation pricing for the `Microsoft Fabric` service in each capacity's region. Fabric pricing is denominated per-CU (Capacity Unit); there is a single per-CU price entry for all F-SKUs in a given region, not separate entries per F-SKU. The total cost for any F-SKU is calculated by multiplying the per-CU rate by that SKU's CU count.
1. For each capacity with observed active usage, the policy estimates the number of monthly active hours from the ratio of active days (days with non-zero CU utilization) to observed days, multiplied by 24 hours and 30.44 (average days per month). Days with non-zero utilization are treated as fully active (24 hours); capacities started and stopped within a single day may have slightly overstated monthly PAYG costs.
1. The current estimated monthly PAYG cost is calculated as `monthly_active_hours × PAYG_per_CU_hourly_rate × current_SKU_CU_count`.
1. All F-SKU reservation tiers that can handle the observed peak CU demand (with 10% headroom) are evaluated. The tier that produces the greatest savings versus the current PAYG cost is selected as the recommendation. This includes right-sizing to a smaller tier when utilization supports it.
1. Capacities with zero active usage in the lookback period are excluded — a flat reservation would add cost rather than save money for an inactive capacity.
1. An incident is raised if the recommended tier saves more than the configured minimum savings threshold.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the capacity is switched from Pay-As-You-Go to the recommended 1-year reserved F-SKU tier.

- Pricing data is retrieved in real time from the [Azure Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices) for each capacity's Azure region, for the `Microsoft Fabric` service. Both Pay-As-You-Go (hourly) and 1-year reservation prices are fetched and used for all cost calculations. Fabric pricing is per-CU, so both price types are returned as a single per-CU rate per region (not separate rates per F-SKU).
- The current estimated monthly PAYG cost is: `monthly_active_hours × PAYG_per_CU_hourly_rate × current_SKU_CU_count`, where `monthly_active_hours = (active_days / observed_days) × 30.44 × 24`.
- The estimated monthly reservation cost for a candidate F-SKU is: `reservation_annual_cost_per_CU × candidate_SKU_CU_count / 12`.
- The `Estimated Monthly Savings` is the difference between the current estimated monthly PAYG cost and the estimated monthly cost under the recommended reservation tier.
- `active_days` is the count of days within the lookback period where the capacity's average CU utilization was greater than zero, as reported by Azure Monitor.
- **Important limitation:** The template assumes all evaluated capacities are currently on Pay-As-You-Go pricing. The Azure Resource Manager API for `Microsoft.Fabric/capacities` does not indicate whether an active reservation has already been purchased for a capacity. If a capacity is already on a 1-year reservation, the estimated savings figure will be inflated compared to the true incremental savings.
- If no pricing data is available for the capacity's region, or if the capacity had no active usage in the lookback period, it is excluded from recommendations.
- The incident message detail includes the sum of each capacity's `Estimated Monthly Savings` as `Potential Monthly Savings`.
- All cost values are reported in the currency configured for the Flexera organization.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Azure Endpoint* - Select the API endpoint to use for Azure. Use default value of `management.azure.com` unless using Azure China.
- *Minimum Savings Threshold* - Minimum potential monthly savings required to generate a recommendation.
- *Statistic Lookback Period* - How many days back to look at Azure Monitor CU utilization data when calculating average and peak utilization for each capacity.
- *Allow/Deny Subscriptions* - Allow or Deny entered subscriptions. See the README for more details.
- *Allow/Deny Subscriptions List* - A list of allowed or denied subscription IDs/names. See the README for more details.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

## Policy Actions

- Sends an email notification with the list of recommended Commitment Tier upgrades or right-size + reserve combinations.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.Fabric/capacities/read`
  - `Microsoft.Insights/metrics/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for meta-policy self-termination; not required if not using the meta parent of this policy template.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any additional costs.
