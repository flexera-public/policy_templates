## Budget Alerts Policy

### What it does

This Policy Template is used to determine if a Billing Center or the entire Organization has exceeded its monthly cost budget.  

### Functional Details

- This policy supports a single target (ie. 1 specific Billing Center or the entire Organization). In order to apply a budget alert for multiple targets, you will need to apply this policy multiple times.
- This policy will generate an incident if the target has exceeded its monthly budget.  This is an actual budget alert, not a forecasted budget alert.

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Monthly Budget* - specify the monthly budget.  Currency is irrelevant; the policy will default to whichever currency is used in Optima.
- *Budget Scope* - Organization or Billing Center
- *Billing Center Name* - if the scope is "Billing Center", supply the name of the target Billing Center 
- *Amoritzation & Blending Option* - specify options for amortized vs nonamortized and blended vs unblended costs
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not incur any cloud costs.
