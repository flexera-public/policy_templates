# Azure Sentinel Commitment Tier Recommendations

## What It Does

This policy template identifies Azure Log Analytics workspaces with [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/) enabled where purchasing or upgrading a daily ingestion Commitment Tier would reduce costs compared to the current pricing tier. It queries each workspace's actual ingestion data over the user-specified lookback period and compares the cost of the current pricing tier (Pay-As-You-Go or an existing commitment level) against each available higher commitment tier using real-time pricing data from the Azure Retail Prices API. When a higher commitment tier is found to produce lower overall monthly costs, an incident is raised with a recommendation to upgrade.

## How It Works

The policy template performs the following steps:

1. All Azure subscriptions are enumerated and filtered based on the configured allow/deny list.
1. All Log Analytics workspaces in each subscription are listed.
1. For each workspace, the Microsoft Sentinel onboarding state is checked via the SecurityInsights API; workspaces without Sentinel enabled are excluded.
1. For each Sentinel-enabled workspace, the Log Analytics Query API is used to retrieve daily billable data ingestion volumes (in GB) over the configured lookback period.
1. The Azure Retail Prices API is queried for the current pricing for each workspace's Azure region, including the Pay-As-You-Go per-GB rate and each available Commitment Tier daily rate.
1. For each workspace, the estimated daily cost is calculated at the current tier and at each available higher tier.
1. The tier with the lowest estimated cost that is higher than the current tier is identified as the recommended tier.
1. An incident is raised if the recommended tier saves more than the configured minimum savings threshold.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the workspace's pricing tier is upgraded to the recommended Commitment Tier.

- Pricing data (Pay-As-You-Go per-GB rate and Commitment Tier daily rates) is retrieved in real time from the [Azure Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices) for each workspace's Azure region.
- The `Estimated Monthly Savings` is calculated as the difference between the current estimated monthly cost and the estimated monthly cost at the recommended tier, multiplied by 30.44 (average days per month).
- The estimated monthly cost at a given tier is: `(Tier Daily Rate + max(0, Average Daily Ingestion − Tier GB Level) × PAYG Rate per GB) × 30.44`. For Pay-As-You-Go: `Average Daily Ingestion × PAYG Rate per GB × 30.44`.
- `Average Daily Ingestion` is computed from the Log Analytics `Usage` table over the configured lookback period using only billable data (`IsBillable == true`).
- If no pricing data is available for the workspace's region, the workspace is excluded from recommendations.
- The incident message detail includes the sum of each workspace's `Estimated Monthly Savings` as `Potential Monthly Savings`.
- All cost values are reported in the currency configured for the Flexera organization.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Azure Endpoint* - Select the API endpoint to use for Azure. Use default value of `management.azure.com` unless using Azure China.
- *Minimum Savings Threshold* - Minimum potential monthly savings required to generate a recommendation.
- *Statistic Lookback Period* - How many days back to look at Log Analytics ingestion data when calculating average and peak daily ingestion volumes.
- *Allow/Deny Subscriptions* - Allow or Deny entered subscriptions. See the README for more details.
- *Allow/Deny Subscriptions List* - A list of allowed or denied subscription IDs/names. See the README for more details.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

## Policy Actions

- Sends an email notification with the list of recommended Commitment Tier upgrades.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.OperationalInsights/workspaces/read`
  - `Microsoft.SecurityInsights/onboardingStates/read`
  - `Microsoft.OperationalInsights/workspaces/query/read`

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
