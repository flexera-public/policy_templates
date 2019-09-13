# Google Idle Compute Instances Policy

## What it does

This Policy Template checks for idle instance in Google Compute Engine and then terminates them upon approval.

## Functional Details

- This policy identifies all instances reporting performance metrics to Google StackDriver and delivers a report, for instances whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters. These thresholds are what you would consider to be and idle instance.
- This policy can terminate instances after approval for instances that match the criteria.
- If you get an **N/A** in a field you will need to install the [StackDriver Agent](https://cloud.google.com/monitoring/agent/install-agent) on the instance to get those metrics.
- This policy only pulls running instances, as it is unable to get correct monitoring metrics from instances in other states

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project* - a Google Cloud Project name
- *Average used memory percentage"* - Set to -1 to ignore memory utilization
- *Average used CPU percentage* - Set to -1 to ignore CPU utilization
- *Exclusion label Key:Value* - Cloud native label to ignore instances. Format: Key:Value

### Cloud Management Required Permissions/Google Required Permissions

- Cloud Management - The `credential_viewer`,`observer` roles
- Google - The `Monitoring Viewer` Role, and the `compute.instances.delete`, `compute.instances.list`, `compute.instances.get` Permissions

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.
