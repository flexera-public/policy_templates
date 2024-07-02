# Azure Cheaper Regions

## What It Does

This policy template uses billing data stored in Flexera Cloud Cost Optimization (CCO) to report on Microsoft Azure regions with spend in the current month that have less expensive alternatives. In such cases, there is potential for savings by migrating resources to the cheaper region. Optionally, this report can be emailed.

## How It Works

- This policy template gathers aggregated cost data for Microsoft Azure for the current month from Flexera CCO via the [Flexera Bill Analysis API](https://reference.rightscale.com/bill_analysis/#). The previous month is used if the policy template executes during the first two days of a month, since it is possible that there will not be any useful data for the current month.
- This data is sorted by region with any region-less costs being filtered out.
- The above data is then filtered just for regions with a cheaper available region. The source of truth for cheaper regions is the [Azure Regions JSON file in the GitHub repository](https://github.com/flexera-public/policy_templates/blob/master/data/azure/regions.json).

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - A list of email addresses to notify.
- *Cost Metric* - The cost metric to use for per-region spend in the report.
- *Allow/Deny Regions* - Allow or Deny entered regions.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Both region IDs, such as `eastus2`, and names, such as `East US 2`, are accepted. Leave blank to check all regions.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to check all Billing Centers.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
