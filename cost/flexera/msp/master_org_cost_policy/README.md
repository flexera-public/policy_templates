# Master Org Cost Policy

## What It Does

**As a best practice, this policy should only be applied to the Master Account, and not to each individual RightScale Account.**

This policy allows you to set up cross organization scheduled reports that will provide summaries of cloud cost across all resources in the billing centers you specify, delivered to any email addresses you specify. The policy will report the following:

Chart of the previous 6 months of utilization based on whichever [Reporting Dimension](https://docs.rightscale.com/optima/reference/rightscale_dimensions.html) you select (only bill data and RightScale-generated dimensions are supported).
Daily Average - Weekly: Daily average costs calculated from Monday of the previous week through today.
Daily Average - Monthly: Daily average costs calculated from the 1st of the previous month through today.
Previous - Weekly: Total costs during previous full week (Monday-Sunday).
Previous - Monthly: Total costs during previous full month.
Current - Weekly: Total costs during current (incomplete) week.
Current - Monthly: Total costs during current (incomplete) month.

We recommend running this policy on a weekly cadence and applying it to your master account.

_Note 1: The last 3 days of data in the current week or month will contain incomplete data._
_Note 2: The account you apply the policy to is unimportant as Optima metrics are scoped to the Org._
_Note 3: If it excluding orgs is needed use only either 'Excluded Organizations' or 'Exclucded organizations IDs' parameter, not both._

## Cost Metrics

There are four cost metrics to choose from.

- Unamortized Unblended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Amortized Unblended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Savings from reserved instances are applied first to matching instances in the account where it was purchased.
- Unamortized Blended - One-time and upfront costs are shown at the time of purchase. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.
- Amortized Blended - One-time and upfront costs are spread evenly over the term of the item purchased. (AWS Only) Saving from reserved instances are shared equally by all matching instances in all accounts.

## Input Parameters

- *Email list* - Email addresses of the recipients you wish to notify
- *Excluded Organizations* - Names of organizations to exclude
- *Cost Metric* -  See Cost Metrics above for details on selection.
- *Graph Dimension* - The cost dimension to break out the cost data in the embedded bar chart image

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This Policy Template does not incur any cloud costs
