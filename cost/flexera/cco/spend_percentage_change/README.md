# Spend Percentage Change Alert

## What It Does

This policy raises an incident if monthly spend increases by more than a user-specified percentage threshold month-over-month for more than a user-specified number of months. This can be based on total spend across the entire organization or broken down by the values of any dimension in the Flexera Cloud Cost Optimization platform. Optionally, this incident can be emailed to act as an alert.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to send the alert to.
- *Cost Dimension* - The name/ID of the cost dimension to track costs for. Use `Billing Center` to track costs by Billing Center. Leave blank to report on all spend. Examples: Category, Billing Center
- *Cost Dimension Filters* - Only alert when the specified values for the specified Cost Dimension have an increase. Leave blank to alert on all values.
- *Maximum Spend Increase (%)* - The maximum month-over-month spend increase to permit as a percentage of total spend. If spend increases more than this, the alert will be triggered.
- *Months Of Increase (#)* - The number of consecutive months that spend has to have increased by more than the 'Maximum Spend Increase (%)' to trigger an alert.
- *Spend Metric* - Select the cost metric to use when gathering spend data.
- *Spend Calculation* - Whether to use average daily spend or monthly spend when calculating percentage change from one month to the next. Average daily spend is recommended to account for the fact that spend will vary from month to month due to the varying number of days in each month even if spend-per-day hasn't changed.

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

This Policy Template does not incur any cloud costs.
