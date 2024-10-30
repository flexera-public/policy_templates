# Budget Alerts (Legacy)

## Deprecated

This policy is no longer being updated.

## What It Does

This Policy uses Optima to determine if a Billing Center or the entire Organization has exceeded its monthly cost budget. The policy should be run daily and will take into account data from 3 days ago to ensure there is a complete set.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (_provider=flexera_) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## How It Works

- This policy supports a single target (ie. 1 specific Billing Center or the entire Organization). In order to apply a budget alert for multiple targets, you will need to apply this policy multiple times.
- Actual Spend budget alerts will raise an incident when the target has exceeded the budget for the month
- Forecasted Spend budget alerts will raise an incident when the target's run-rate is on track to exceed the budget for the month
- First 3 days of the month are not reported until after the 4th day to insure all bill data is retrieved before creating an incident.
- Cost data isn't fully retrieved from the cloud bill for 2-3 days. Therefore this policy will evaluate Optima data 3 days earlier than the run date.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- _Monthly Budget_ - specify the monthly budget. Currency is irrelevant; the policy will default to whichever currency is used in Optima.
- _Threshold Percentage_ - Percentage of budget amount to alert on
- _Billing Center Name or Id_ - if the scope is "Billing Center", supply the name or Id of the target Billing Center. When left blank the policy reports on all the billing centers in the CMP Organization.
- _Cost Metric_ - specify options for amortized vs non-amortized and blended vs unblended costs
- _Budget Alert Type_ - Actual Spend alerts are based off incurred costs. Forecasted Spend alerts are based off monthly runrates
- _Email addresses_ - A list of email addresses to notify

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This policy template does not incur any cloud costs.
