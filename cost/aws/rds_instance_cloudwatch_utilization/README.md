## AWS RDS Instances RightSizing Recommendations Policy

### What it does

This Policy Template gathers AWS CloudWatch data for RDS Instances on 30 day intervals.

### Cloud Management Required Permissions/AWS Required Permissions
- Cloud Management - The `credential_viewer` role
- AWS - Read access to CloudWatch & RDS

### Functional Details

- This policy identifies all RDS instances reporting performance metrics to CloudWatch whose CPU utilization is below the thresholds set in the **Average used CPU % - Downscale Threshold** and **Average used CPU % - Upscale Threshold** parameters.
- The **Exclusion Tag Key:Value** parameter is a string value.  Supply the Tag Key & Value.  If the exclusion tag is used on an RDS Instance, that Instance is presumed to be exempt from this policy.

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - A list of email addresses to notify
- *Average used CPU % - Upscale threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU % - Downscale Threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key:Value* - An Azure-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.
