# Budget Alerts Policy

## What it does

This Policy uses Optima to determine if a Billing Center or the entire Organization has exceeded its monthly cost budget. The policy should be run daily and will take into account data from 3 days ago to ensure there is a complete set.

## Functional Details

- This policy supports a single target (ie. 1 specific Billing Center or the entire Organization). In order to apply a budget alert for multiple targets, you will need to apply this policy multiple times.
- Actual Spend budget alerts will raise an incident when the target has exceeded the budget for the month
- Forecasted Spend budget alerts will raise an incident when the target's run-rate is on track to exceed the budget for the month
- First 3 days of the month are not reported until after the 4th day to insure all bill data is retrieved before creating an incident.
- Cost data isn't fully retrieved from the cloud bill for 2-3 days.  Therefore this policy will evaluate Optima data 3 days earlier than the run date.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Monthly Budget* - specify the monthly budget.  Currency is irrelevant; the policy will default to whichever currency is used in Optima.
- *Billing Center Name* - if the scope is "Billing Center", supply the name of the target Billing Center. When left blank the policy reports on all the billing centers in the CMP Organization.
- *Cost Metric* - specify options for amortized vs non-amortized and blended vs unblended costs
- *Budget Alert Type* - Actual Spend or Forecasted Spend
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Required CMP Roles

- billing_center_viewer (note: this role must be applied at the Organization level)

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not incur any cloud costs.
