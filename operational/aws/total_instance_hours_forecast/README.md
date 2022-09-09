# AWS Usage Forecast - Number of Instance Hours Used

## What it does

This Policy leverages Optima to determine a usage forecast for a normalized view of AWS instance hours used within the entire Organization. The policy uses the specified previous number of months, not including the current month to to determine a straight-line forecast using a linear regression model.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy uses the last month before current to guarantee full data.
- This policy supports filtering by a specific AWS region or the entire Organization.
- This policy produces a straight-line forecast by calculating a line of best fit (linear regression line) from the historical dataset and then extrapolating this to calculate forecasted costs.
- The forecast is displayed as a stacked-bar chart showing Total Instance Hours by Instance Family for the top 8 most used Instance Families. All other Instance Families will be aggregated and displayed as "Other". Values shown in the graph are for the past 12 months.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Region* - Name of the AWS Region to filter by. Example: 'US West (Oregon)'. Leave this blank for 'Organization' scope
- *Lookback Months* - Number of months to lookback to generate forecast
- *Months to forecast* - Number of months in the future to forecast
- *Email addresses to notify* - A list of email addresses to notify

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
