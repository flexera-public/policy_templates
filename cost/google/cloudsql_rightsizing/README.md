# Google CloudSQL RightSizing

## What it does

This Policy Template gathers stackdriver monitoring data for cloudsql instances on 30 day intervals and provides rightsizing recommendations.  Once recommendations are generated, instances can be rightsized in an automated manner or after approval.

## Functional Details

- This policy identifies all CloudSQL instances reporting performance metrics to stackdriver whose CPU utilization is below the thresholds set in the **Average used CPU % - Downsize Threshold** and **Average used CPU % - Upsize Threshold** parameters.
- The **Exclusion Tag Key:Value** parameter is a string value.  Supply the Tag Key & Value.  If the exclusion tag is used on an CloudSQL Instance, that Instance is presumed to be exempt from this policy.
- The rightsizing escalation can be automated, executed after approval, or skipped.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - A list of email addresses to notify
- *Google Cloud Project* - a Google Cloud Project name
- *Average used CPU % - Upsize threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU % - Downsize Threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key:Value* - Cloud native label to ignore instances. Format: Key:Value

### Cloud Management Required Permissions/Google Required Permissions

- Cloud Management - The `credential_viewer`,`observer` roles
- Google - The `Monitoring Viewer` Role, and the `sqlservice.admin` permissions

### Supported Clouds

- Google

### Cost

This Policy Template does not incur any cloud costs.
