# Cloud Spend Moving Average Report

## What It Does

This policy template pulls cost data from Flexera Cloud Cost Optimization (CCO) and produces a graph and report showing the moving average over time. Optionally, this report can be emailed.

## How It Works

- Aggregated monthly cloud costs are gathered from Flexera CCO via the [Flexera Bill Analysis API](https://reference.rightscale.com/bill_analysis/).
  - The number of months gathered is defined by the `Look Back Months (#)` parameter.
  - If the `Allow/Deny Billing Center List` and `Allow/Deny Billing Centers` parameters are used, costs are only gathered for the relevant Billing Centers. Otherwise, all costs for the entire Flexera organization are gathered.
- A moving average for each month is calculated from the total cost of that month and previous months.
  - The number of months considered is defined by the `Moving Average Months` parameter. For example, if this parameter is set to `3`, the average will be calculated by taking the sum of the costs from the current month and previous two months and dividing it by 3.
  - If the current month plus the number of prior months in the requested data set is less than the `Moving Average Months` parameter, the average is calculated using the data available. It is expected that the average and the gathered costs will be identical for the earliest month in the data set due to a lack of prior data.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to send the scheduled report to.
- *Cost Metric* - The cost metric to use when calculating and reporting the moving average.
- *Allow/Deny Billing Centers* - Allow or Deny entered Billing Centers.
- *Allow/Deny Billing Center List* - A list of allowed or denied Billing Center names/IDs. Leave blank to produce forecast for entire Flexera organization.
- *Look Back Months (#)* - Number of months into the past to use for generating forecast.
- *Moving Average Months* - Number of prior months to use to calculate moving average.

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
