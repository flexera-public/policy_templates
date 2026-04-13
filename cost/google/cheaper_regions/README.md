# Google Cheaper Regions

## What It Does

This policy template uses billing data stored in Flexera Cloud Cost Optimization (CCO) to report on Google Cloud regions with spend in the current month that have less expensive alternatives. In such cases, there is potential for savings by migrating resources to the cheaper region. Optionally, this report can be emailed.

## How It Works

- This policy template gathers aggregated cost data for Google Cloud for the current month from Flexera CCO via the [Flexera Bill Analysis API](https://reference.rightscale.com/bill_analysis/#). The previous month is used if the policy template executes during the first two days of a month, since it is possible that there will not be any useful data for the current month.
- This data is sorted by region with any region-less costs being filtered out.
- The above data is then filtered just for regions with a cheaper available region. The source of truth for cheaper regions and their cost ratios is the [Google Regions JSON file in the GitHub repository](https://github.com/flexera-public/policy_templates/blob/master/data/google/regions.json).
- For each region with a cheaper alternative, an estimated monthly savings is calculated by applying the region's `cheaper_ratio` to the total spend for that region.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resources currently deployed in the source region are moved to the recommended cheaper region.

- The `Estimated Monthly Savings` for each region is calculated as: `Total Region Spend × (1 - cheaper_ratio)`. For example, a region with $10,000 of monthly spend and a `cheaper_ratio` of `0.85` would yield an estimated savings of $10,000 × (1 - 0.85) = $1,500.
- The `cheaper_ratio` values stored in the [Google Regions JSON file](https://github.com/flexera-public/policy_templates/blob/master/data/google/regions.json) represent the approximate ratio of the recommended region's general-purpose compute pricing to the source region's general-purpose compute pricing. They were derived by comparing representative on-demand machine type pricing (e.g., general-purpose machine families) between each source region and its recommended cheaper alternative. A ratio of `0.85` means the recommended region is approximately 15% cheaper for comparable compute workloads.
- Since the costs used in this calculation are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The `Estimated Monthly Savings` is an approximation based on compute pricing ratios. Actual savings may vary depending on the specific mix of services, resource types, data transfer costs, and other region-specific factors.
- The incident message detail includes the sum of each region's `Estimated Monthly Savings` as `Total Estimated Monthly Savings`.
- Both `Estimated Monthly Savings` and `Total Estimated Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - A list of email addresses to notify.
- *Cost Metric* - The cost metric to use for per-region spend in the report.
- *Incident Table Size* - Maximum number of rows to include in the incident table in the email. Larger values may cause email delivery issues.
- *Attach Incident CSV* - Whether or not to attach a CSV of the incident data to the incident email.
- *Allow/Deny Regions* - Allow or Deny entered regions.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Both region IDs, such as `us-east1`, and names, such as `US East Moncks Corner, South Carolina, USA`, are accepted. Leave blank to check all regions.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to check all Billing Centers.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
