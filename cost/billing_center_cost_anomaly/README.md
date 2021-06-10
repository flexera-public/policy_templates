# Billing Center Cost Anomaly Policy

## What it does

The Cost Anomaly Policy will analyze the spend of all Billing Centers in an Organization over a specified time period.  If the percentage change of the most recent period compared to the previous period exceeds the specified threshold, then an Incident will be raised.

## Functional Details

- The policy polls all Billing Centers, looking for any that have exceeded the Percent Change threshold and the Minimum Period Spend requirement
- The last 2 days are not included in the analysis, due to potential delays of the cloud providers updating their billing data

### Input Parameters

- *Time Period* - Number of days to analyze in each period. For example, if `6` days is set, then the latest time period will be 8 days ago to 3 days ago (to account for cloud provider bill delays) and the previous time period will be 14 days ago to 9 days ago.
  - Minimum Value: 1
  - Maximum Value: 31
- *Anomaly Threshold* - Percentage change threshold.  If the percentage change of Billing Center spend from the latest time period compared to the previous time period exceeds this value, then an Incident will be raised.
- *Minimum Period Spend* - The spend of a billing center for either the previous period or current period must exceed this threshold to raise an Incident.
- *Cost Metric* - Specify options for amortized vs nonamortized and blended vs unblended costs.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Billing Center List* - List of Billing Center names you want to report on. Names must be exactly as shown in Optima.
   Leave the field blank to report on all Billing Centers.

### Required RightScale Roles

- policy_manager
- billing_center_viewer

Alternatively, a version of the policy is provided that uses OAuth2 Flexera credentials (e.g. for use in the EU region).
It requires policy credentials of type OAuth2 against the FlexeraOne application (e.g. in the EU, via URL `https://login.flexera.eu/oidc/token`).
Those credentials should be associated with a user with the right permissions, ie those mentioned above.

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not incur any cloud costs.

