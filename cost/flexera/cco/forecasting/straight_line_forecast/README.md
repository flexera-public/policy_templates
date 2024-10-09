# Cloud Spend Forecast - Straight-Line

## What It Does

This policy template produces a forecast for monthly cloud spend based on cost data stored in Flexera Cloud Cost Optimization (CCO) and presents this forecast as a chart and table. The user can specify the number of months to look back, the number of months to forecast, the formula used for producing the forecast, and the Flexera CCO dimension to split costs by in the chart. Optionally, this forecast can be emailed.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to send the report to.
- *Cost Metric* - The cost metric to use when calculating the forecast.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to produce forecast for entire Flexera organization.
- *Look Back Months (#)* - Number of months into the past to use for generating forecast.
- *Forecast Months (#)* - Number of months in the future to forecast.
- *Forecast Formula* - Formula to use when projecting costs.
- *Dimension* - The name or ID of the Flexera dimension you want to split costs by in the chart. Enter `Billing Center` to split costs by Billing Center. Leave blank to not split costs by any dimension.

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

This policy template does not incur any cloud costs.
