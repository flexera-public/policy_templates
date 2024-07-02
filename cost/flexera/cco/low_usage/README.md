# Low Usage Report

## What It Does

This policy template gathers spend, sliced by the user-specified cost dimension and going back the user-specified number of days, and reports on any values for that dimension whose spend is below a user-specified threshold. Optionally, the report can be emailed.

The intended use of this policy template is to enable the user to quickly identify vendor accounts, services, Billing Centers, etc. whose low usage may indicate that it was being used for testing or other temporary purposes. For example, if the `Cloud Vendor Account Name` dimension is used, the report will contain a list of cloud vendor accounts (AWS accounts, Azure subscriptions, etc.) with low spend. In such cases, destroying the relevant resources may result in cost savings.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Cost Metric* - The cost metric to use when assessing usage.
- *Days of Usage* - How many days of past usage to consider when assessing spend.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to run report across entire Flexera organization.
- *Low Account Spend Threshold* - Threshold to consider the user-specified dimension to be low spend. Only values with spend lower than this number will be reported.
- *Minimum Spend Threshold* - Threshold to consider the user-specified dimension to be worth actioning on. Only values with spend higher than this number will be reported.
- *Dimension* - The name or ID of the Flexera dimension whose values you want to check for low usage; for example, `Cloud Vendor Account Name`. Enter `Billing Center` to split costs by Billing Center.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
