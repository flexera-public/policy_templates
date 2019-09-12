# Google Instance StackDriver Utilization Policy

## What it does

This Policy Template gathers Google StackDriver utilization for instances on 30 day intervals. This is meant to be run as a monthly policy.

## Cloud Management Required Permissions/Google Required Permissions

- Cloud Management - The `credential_viewer`,`observer` roles
- Google - The `Monitoring Viewer` Role

## Functional Details

- This policy uses RightScale to get a list of instances, it then polls Google StackDriver for metrics for instance performance and delivers a report. If you get an **N/A** in a field you will need to install the [StackDriver Agent](https://cloud.google.com/monitoring/agent/install-agent) on the instance to get those metrics.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project* - a Google Cloud Project name
- *Average used memory percentage"* - Set to -1 to ignore memory utilization
- *Average used CPU percentage* - Set to -1 to ignore CPU utilization
- *Exclusion Tag Key:Value* - Cloud native tag key to ignore instances. Format: Key:Value

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.
