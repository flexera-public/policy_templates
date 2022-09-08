# Cloud Spend Forecast - Straight-Line (Linear Regression Model)

## What it does

This Policy uses Optima to determine a cloud spend forecast for a Billing Center or the entire Organization. The policy uses the specified previous number of months, not including the current month to to determine a straight-line forecast using a linear regression model.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy supports a group of Billing Centers or the entire Organization.
- This policy uses the last month before current to guarantee full data.
- This policy supports different dimensions to break down costs by, such as Category, Service and Region.
- This policy produces a straight-line forecast by calculating a line of best fit (linear regression line) from the historical dataset and then extrapolating this to calculate forecasted costs.
- This policy omits costs for Commitments, as refunds are difficult to forecast.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - List of Billing Center Names to check
- *Lookback Months* - Number of months to lookback to generate forecast
- *Months to forecast* - Number of months in the future to forecast
- *Cost Metric* - specify options for amortized blended or amortized unblended costs
- *Dimension* - Select dimension, leave blank for no dimensions
- *Email addresses* - A list of email addresses to notify

## Supported Clouds

- All configured clouds

## Cost

This Policy Template does not incur any cloud costs.
