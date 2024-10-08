# Budget Alerts by Cloud Account

## Deprecated

This policy template is no longer being updated. The [Budget Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_report_alerts/) policy template can be used instead by specifying a cloud account in the relevant filtering parameter.

## What It Does

This Policy uses Optima to determine if a Cloud Account has exceeded its monthly cost budget. The policy should be run daily and will take into account data from 3 days ago to ensure there is a complete set.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## How It Works

- This policy supports a single target (ie. 1 specific Cloud Account). In order to apply a budget alert for multiple targets, you will need to apply this policy multiple times.
- Actual Spend budget alerts will raise an incident when the target has exceeded the budget for the month
- Forecasted Spend budget alerts will raise an incident when the target's run-rate is on track to exceed the budget for the month
- First 3 days of the month are not reported until after the 4th day to insure all bill data is retrieved before creating an incident.
- Cost data isn't fully retrieved from the cloud bill for 2-3 days.  Therefore this policy will evaluate Optima data 3 days earlier than the run date.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Monthly Budget* - specify the monthly budget.  Currency is irrelevant; the policy will default to whichever currency is used in Optima.
- *Cloud Vendor Account Name* - the name of the Cloud Vendor Account that the budget should be enforced against
- *Cost Metric* - specify options for amortized vs non-amortized and blended vs unblended costs
- *Budget Alert Type* - Actual Spend or Forecasted Spend
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not incur any cloud costs.
