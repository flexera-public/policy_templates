# Budget Alerts Policy

## What it does

This policy uses the Optima Budgets API to determine if the selected budget expense is exceeded. The policy can also be run for all exists budgets. The policy should be run daily to calculate projected expenses and how much they exceed the current monthly budget.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (_provider=flexera_)

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy supports a single target (1 specific Budget). In order to apply a budget alert for multiple budgets, you will need to apply this policy multiple times.
- Actual expense budget alerts will trigger an incident if the actual budget's spend exceeds the budget
- Forecasted Spend budget alerts will raise an incident when the target's run-rate is on track to exceed the budget for the month
- Data can be grouped by Dimensions.
- The policy allows the customer to include or exclude non-budget funds.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- _Budget Name or ID_ - if the scope is "Budget", supply the name or Id of the target Budget. When left blank the policy reports on all the Budgets in the CMP Organization.
- _Threshold Percentage_ - Percentage of budget amount to alert on
- _Budget Alert Type_ - can be "Actual" or "Forecasted". Actual Spend alerts are based off incurred costs. Forecasted Spend alerts are based off monthly runrates.
- _Degree of Summarization_ - use this parameter to specify how to group the data. Can be "Summarized" or "By dimensions".
- _Unbudgeted spend_ - parameter that allows including or excluding unbudgeted funds in the calculation
- _Email addresses_ - A list of email addresses to notify

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not incur any cloud costs.
