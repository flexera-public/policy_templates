# Budget Alerts Policy

## What it does

This policy uses the Optima Budgets API to determine if the selected budget expense is exceeded. The policy can also be run for all exists budgets. The policy should be run daily to calculate projected expenses and how much they exceed the current monthly budget.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*)

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy supports a single target (ie. 1 specific Budget or the entire Organization). In order to apply a budget alert for multiple targets, you will need to apply this policy multiple times.
- Actual expense budget alerts will trigger an incident if the target has exceeded the budget for any month of the period from Start to present.
- Forecasted Spend budget alerts will raise an incident when the target's run-rate is on track to exceed the budget for the month
- Data can be grouped by Dimensions. The API supports two grouping fields: "vendor" and "service"
- Granularity of the sample can be specified: "Monthly" or "Summarized". In the second case, forecasted data is not calculated.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Budget Name or ID* - if the scope is "Budget", supply the name or Id of the target Budget. When left blank the policy reports on all the Budgets in the CMP Organization.
- *Threshold Percentage* - Percentage of budget amount to alert on
- *Granularity* - can be "Monthly" or "Summarized"
- *Start date (yyyy-mm)* - set the year and month of the beginning of sampling. If the budget start date is closer, it will be used.
- *Dimensions* - List of dimension groups for the policy. Can be "vendor" or "service"
- *Email addresses* - A list of email addresses to notify

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not incur any cloud costs.
