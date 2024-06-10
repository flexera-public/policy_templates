# AWS Savings Realized From Rate Reduction Purchases

## What It Does

This policy template produces a report with chart showing the total savings realized from using AWS Reservations, Savings Plans, and Spot Instances. This report can either be for the entire organization or specific Billing Centers. Optionally, this report can be emailed.

## How It Works

- Data is obtained from Flexera's stored cloud cost data via the [Flexera Bill Analysis API](https://reference.rightscale.com/bill_analysis/)
- This policy uses [savings metric](https://docs.flexera.com/flexera/EN/Optima/TabularView.htm#tabularview_3352643092_1192596) calculated as difference between list price and cost.

### Input Parameters

- *Email Addresses* - A list of email addresses to send the report to.
- *Start Date (YYYY-MM)* - The starting month of the historical data to analyze in YYYY-MM format. Example: 2023-02
- *End Date (YYYY-MM)* - The ending month of the historical data to analyze in YYYY-MM format. Example: 2023-07
- *Chart Type* - The type of bar chart to use in the report.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to report on the entire Flexera organization.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
