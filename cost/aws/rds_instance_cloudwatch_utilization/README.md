## AWS Rightsize RDS Instances

### What it does

This Policy Template gathers AWS CloudWatch data for RDS Instances on 30 day intervals and provides rightsizing recommendations.  Once recommendations are generated, instances can be rightsized in an automated manner or after approval.

### Cloud Management Required Permissions/AWS Required Permissions
- Cloud Management - The `credential_viewer` role
- AWS - Read access to CloudWatch & RDS

### Functional Details

- This policy identifies all RDS instances reporting performance metrics to CloudWatch whose CPU utilization is below the thresholds set in the **Average used CPU % - Downsize Threshold** and **Average used CPU % - Upsize Threshold** parameters.
- The **Exclusion Tag Key:Value** parameter is a string value.  Supply the Tag Key & Value.  If the exclusion tag is used on an RDS Instance, that Instance is presumed to be exempt from this policy.
- The rightsizing escalation can be automated, executed after approval, or skipped.
- After the policy escalation has executed the [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) method on the recommended resources, the RDS Instance will continue to use its original Instance Class until the next Maintenance Window set on the RDS Instance in AWS.  During the next Maintenance Window, the pending Instance Class change will take effect.

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - A list of email addresses to notify
- *Average used CPU % - Upsize threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU % - Downsize Threshold* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key:Value* - An AWS-native instance tag to ignore instances that you don't want to consider for resizing. Only supply the tag key

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.
