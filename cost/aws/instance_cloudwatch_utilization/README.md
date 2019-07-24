## AWS Instance CloudWatch Utilization Policy

### What it does

This Policy Template gathers AWS CloudWatch data for instances on 30 day intervals. This is meant to be run as a monthly policy. 

### Cloud Management Required Permissions/AWS Required Permissions
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles
- AWS - The `CloudWatchReadOnlyAccess` AWS IAM Policy

### Functional Details

- This policy identifies all instances reporting performance metrics to CloudWatch whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters.
- The **Exclusion Tag Key** parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy sets the tag defined in the **Action Tag Key:Value** parameter on the underutilized instances that were identified.
-  If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics. 

#### Windows Support

To enable windows support you will need to add the following to your cloudwatch config.json and restart
```json
	"metrics": {
		"append_dimensions": {
			"AutoScalingGroupName": "${aws:AutoScalingGroupName}",
			"ImageId": "${aws:ImageId}",
			"InstanceId": "${aws:InstanceId}",
			"InstanceType": "${aws:InstanceType}"
    }
  }
```
#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Average used memory percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key* - An Azure-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key
- *Action Tag Key:Value* - The tag key:value pair to set on an instance that is underutilized.

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.
```json
	"metrics": {
		"append_dimensions": {
			"AutoScalingGroupName": "${aws:AutoScalingGroupName}",
			"ImageId": "${aws:ImageId}",
			"InstanceId": "${aws:InstanceId}",
			"InstanceType": "${aws:InstanceType}"
    }
```
