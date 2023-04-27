# Budget Alerts Policy

## What it does

This policy utilizes the Flexera Budget API to detect if budget expense has exceeded its allocated value. The policy can be run daily to determine if actual or projected spend exceeded the specified threshold.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (_provider=flexera_)

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy supports a single target (1 specific Budget). In order to apply a budget alert for multiple budgets, you will need to apply this policy multiple times.
- Actual expense budget alerts will trigger an incident if the actual budget's spend exceeds the budget threshold
- Forecasted Spend budget alerts will raise an incident when the target's run-rate is on track to exceed the budget threshold
- Data can be grouped by Dimensions.
- The policy allows the customer to include or exclude unbudgeted spend

## Input Parameters

This policy has the following input parameters required when launching the policy.

- _Budget Name or ID_ - The name or Id of the target Budget.
- _Budget Alert Type_ - can be "Actual" or "Forecasted". Actual Spend alerts are based off incurred costs. Forecasted Spend alerts are based off monthly runrates.
- _Degree of Summarization_ - Determines if budget should be tracked as a whole or per dimension groups, with possible values of Summarized or By dimensions.
- _Unbudgeted spend_ - parameter that allows including or excluding unbudgeted funds in the calculation
- _Threshold Percentage_ - Threshold to raise the alert if reached
- _Email addresses_ - A list of email addresses to notify

## Cost

This Policy Template does not incur any cloud costs.
