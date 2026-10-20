# Azure Sentinel Commitment Tier Recommendations

## What It Does

This policy template identifies Azure Log Analytics workspaces with [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/) enabled where purchasing, changing, or removing a daily ingestion Commitment Tier would reduce costs compared to the current pricing tier. It queries each workspace's actual daily ingestion over the user-specified lookback period and compares the cost of the current pricing tier (Pay-As-You-Go or an existing commitment level) against Pay-As-You-Go and every available commitment tier, using pricing data from the Azure Retail Prices API. When another tier is found to produce lower overall monthly costs, an incident is raised with a recommendation to upgrade, downgrade, or switch to Pay-As-You-Go.

**Only workspaces on [Microsoft Sentinel simplified pricing](https://learn.microsoft.com/en-us/azure/sentinel/enroll-simplified-pricing-tier) are evaluated.** Classic pricing bills Log Analytics and Microsoft Sentinel as separate meters with independently set tiers, and is not supported. Microsoft prices each simplified tier as the sum of the corresponding Log Analytics tier and Classic Microsoft Sentinel tier, so moving a workspace from Classic to simplified pricing does not change its cost. Customers with workspaces on Classic pricing can switch them to simplified pricing in order to have them evaluated by this policy template. Please review [Microsoft's documentation](https://learn.microsoft.com/en-us/azure/sentinel/enroll-simplified-pricing-tier) before switching, as the change cannot be reverted from the Microsoft Sentinel portal.

## How It Works

The policy template performs the following steps:

1. All Azure subscriptions are enumerated and filtered based on the configured allow/deny list.
1. All Log Analytics workspaces in each subscription are listed. Workspaces linked to a dedicated cluster and workspaces on a legacy SKU (`LACluster`, `Free`, `Standalone`, `PerNode`, `Standard`, or `Premium`) are excluded.
1. For each remaining workspace, the Microsoft Sentinel onboarding state is checked via the SecurityInsights API; workspaces without Sentinel enabled are excluded.
1. For each Sentinel-enabled workspace, the pricing scheme is determined by checking the `Microsoft.OperationsManagement/solutions/SecurityInsights({workspaceName})` resource. Only workspaces whose solution SKU name is `Unified` (simplified pricing) are kept. All other workspaces, including those on Classic pricing, are dropped before any ingestion query is run for them.
1. The current commitment tier is the `capacityReservationLevel` set for the workspace on that solution. A missing or `0` level means Pay-As-You-Go. If the solution reports no level but the workspace itself is on the `CapacityReservation` SKU, the level set on the workspace is used, so a workspace that already has a commitment tier is never mistaken for Pay-As-You-Go.
1. For each remaining workspace, the Log Analytics Query API is used to retrieve billable, Analytics-plan data ingestion (in GB) for each complete UTC day in the configured lookback period. The current, partial day is not included. Days with no ingestion between the first and last returned day count as 0 GB.
1. The Azure Retail Prices API is queried for `Sentinel` pricing in each workspace's Azure region. Each rate comes from one specific meter: `Pay-as-you-go Analysis` for Pay-As-You-Go, and `{n} GB Commitment Tier Capacity Reservation` (billed per day) for each commitment tier. Meters for Classic pricing, Basic and Auxiliary logs, data lake, and other non-Analytics products are ignored, and no other meter is ever used as a substitute. If a region has no Pay-As-You-Go rate, is missing a rate that is needed, or has a Pay-As-You-Go rate that is not higher than the effective per-GB rate of every commitment tier, its pricing is considered unreliable and its workspaces are skipped.
1. For each workspace with at least 7 complete days of ingestion data, the cost of every day is calculated at the current tier, at Pay-As-You-Go, and at each available commitment tier. The estimated monthly cost for each is the mean of those daily costs multiplied by 30.44.
1. The option with the lowest estimated monthly cost is identified as the recommended tier.
1. An incident is raised if the recommended tier saves more than the configured minimum savings threshold.

### Limitations

- Only workspaces on Microsoft Sentinel simplified pricing are evaluated. Workspaces on Classic pricing are not evaluated.
- Savings are calculated from Azure retail list prices, so negotiated rates, such as those in an EA or MCA agreement, are not reflected.
- Microsoft 365 E5/A5/G5 data grants and the Defender for Servers P2 500 MB/day benefit are applied at billing time and are not visible in the `Usage` table, so billable volume may be overstated.
- Workspaces linked to a dedicated cluster and workspaces on legacy pricing tiers are excluded.
- Data lake tier costs are out of scope.
- Only Analytics-plan data is counted, because commitment tiers do not cover Basic or Auxiliary ingestion.
- Commitment tiers can only be lowered 31 days after the last tier change, so downgrade and Pay-As-You-Go recommendations may not be actionable right away. These recommendations say so.
- At least 7 complete days of ingestion data are required for a workspace to be evaluated.
- Workspaces in regions where Azure does not publish a complete, consistent set of simplified pricing meters are skipped.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the workspace's pricing tier is changed to the recommended Commitment Tier or to Pay-As-You-Go.

- Pricing data is retrieved from the [Azure Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices) for each workspace's Azure region, using only the `Sentinel` service listing. Workspaces on simplified pricing are billed through a single Microsoft Sentinel meter per tier that covers both log analytics ingestion and Sentinel analysis, so no separate Log Analytics component is added.
- The cost of one day of ingestion at a Commitment Tier is: `Tier Daily Rate + max(0, Daily Ingestion - Tier GB Level) x (Tier Daily Rate / Tier GB Level)`. The overage rate for a commitment tier is the tier's own effective per-GB rate (`Tier Daily Rate / Tier GB Level`), not the Pay-as-you-go rate, consistent with [Microsoft Sentinel pricing](https://www.microsoft.com/en-us/security/pricing/microsoft-sentinel/). For Pay-As-You-Go: `Daily Ingestion x Pay-as-you-go Rate per GB`.
- Commitment tiers are billed per UTC day, and a day below the commitment still pays the full tier price. The estimated monthly cost of a tier is therefore the mean of the daily costs over every complete day in the lookback period, multiplied by 30.44 (average days per month), rather than the cost of the average day. Costing only the average day would understate the cost of a commitment tier whenever ingestion varies from day to day.
- The `Estimated Monthly Savings` is calculated as the difference between the current estimated monthly cost and the estimated monthly cost at the recommended tier.
- Daily ingestion is computed from the Log Analytics `Usage` table using only complete UTC days and only billable data (`IsBillable == true`) in the Analytics plan. Rows with an empty `Plan`, which were written before Microsoft added that column to the `Usage` table, are treated as Analytics. See the [Usage table reference](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/usage) for more details.
- `Average Daily Ingestion`, `Peak Daily Ingestion`, and `Days Observed` are shown in the incident table for reference. `Days Observed` includes any days with no ingestion that fall between the first and last day returned.
- If the current tier or any pricing data needed for the workspace's region is unavailable, the workspace is excluded from recommendations.
- The incident message detail includes the sum of each workspace's `Estimated Monthly Savings` as `Potential Monthly Savings`.
- All cost values are reported in the currency configured for the Flexera organization.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Azure Endpoint* - Select the API endpoint to use for Azure. Use default value of `management.azure.com` unless using Azure China.
- *Minimum Savings Threshold* - Minimum potential monthly savings required to generate a recommendation.
- *Statistic Lookback Period* - How many complete days (UTC) back to look at Log Analytics ingestion data when calculating daily ingestion volumes. The current partial day is not included.
- *Allow/Deny Subscriptions* - Allow or Deny entered subscriptions. See the README for more details.
- *Allow/Deny Subscriptions List* - A list of allowed or denied subscription IDs/names. See the README for more details.
- *Allow/Deny Resource Groups* - Whether to treat Allow/Deny Resource Groups List parameter as allow or deny list. Has no effect if Allow/Deny Resource Groups List is left empty.
- *Allow/Deny Resource Groups List* - A list of allowed or denied Resource Group names to filter the results by. Entries can be in the format `resource_group_name` to filter all resource groups with that name regardless of subscription, or `subscription_id/resource_group_name` to filter a resource group within a specific subscription. Leave blank to consider all resource groups.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.OperationalInsights/workspaces/read`
  - `Microsoft.OperationalInsights/workspaces/query/action`
  - `Microsoft.OperationsManagement/solutions/read`
  - `Microsoft.SecurityInsights/onboardingStates/read`

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
