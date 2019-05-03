## Google Instance StackDriver Utilization Policy

### What it does

This Policy Template gathers Google StackDriver utilization for instances on 30 day intervals

### Cloud Management Required Permissions/Google Required Permissions
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles
- Google - The `Monitoring Viewer ` Role

### Functional Details

- This policy uses RightScale to get a list of instances, it then polls Google StackDriver for metrics for instance performance and delivers a report. If you get an **N/A** in a field you will need to install the [StackDriver Agent](https://cloud.google.com/monitoring/agent/install-agent) on the instance to get those metrics. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Google Cloud Project* - a Google Cloud Project name

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.