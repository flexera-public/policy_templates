# AWS Savings Realized from Reservations

## What it does

This Policy uses Optima to determine a view of total savings realized from using Compute Reservations, Savings Plans, and Spot Instances in AWS, for the entire Organization or specified billing centers across a period of historical months.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy supports a view of savings realized from AWS Compute Reserved Instances, Savings Plans and Spot Instances
- This policy supports a view of savings realized for a list of specific billing centers or for the entire Organization.
- This policy uses [savings metric](https://docs.flexera.com/flexera/EN/Optima/TabularView.htm#tabularview_3352643092_1192596) calculated as difference between list price and cost.
- This policy produces a bar chart showing savings realized categorized by purchase option vs. total actual spend for the period of historical months specified.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - List of Billing Center Names to check Savings Realized for. Leave blank for whole Organization view
- *Period Start Date* - The starting month of the historical data to analyze (in YYYY-MM format e.g., "2021-10")
- *Period End Date* - The ending month of the historical data to analyze (in YYYY-MM format)
- *Email addresses* - A list of email addresses to notify
- *Chart Type* - The type of bar chart to view savings realized data by

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
