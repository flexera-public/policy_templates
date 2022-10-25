# Cloud Cost Anomaly Policy

## What it does

The Cost Anomaly Policy will analyze the spend of all Billing Centers in an Organization over a specified time period.  If the percentage change of the most recent period compared to the previous period exceeds the specified threshold, then an Incident will be raised.

## Functional Details

- The policy queries the /anomalies/report endpoint for the bill analysis api and based on the parameters returns values that are deemed anomalies by the api
- The granularity of the policy is only for daily, maximum of 31 days

### Input Parameters

- *Time Period* - Number of days to analyze for the policy run.
  - Minimum Value: 1
  - Maximum Value: 31
  - Default: 30
- *Minimum Period Spend* - minimum spend needed to record an anomaly as an incident.
  - Minimum Value: 0
  - Default: 1000
- *Cost Anomaly Dimensions* - Dimensions for filter to run anomoly report. Unable to take in custom tags as a dimension.
  - Default: ["Cloud Vendor Account", "Cloud Vendor", "Service"]
- *Cost Metric* - Specify options for amortized vs nonamortized and blended vs unblended costs.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Window Size* - Window size to use for bollinger bands
  - Minimum Value: 0
  - Default: 10
- *Standard Deviations* - The standard deviation number for the bollinger band"
  - Minimum Value: 0
  - Default: 2
- *Cost Anomaly Limit* - Number of Anomaly rows to return in the response
  - Default: 10

### Required RightScale Roles

- policy_manager
- billing_center_viewer

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not incur any cloud costs.
