## AWS Burstable Instance CloudWatch Utilization Policy

### What it does

This Policy Template gathers AWS CloudWatch data for instances on 30 day intervals. Information on Burst Credits can be found [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-monitoring-cpu-credits.html). This policy will then take the appropriate actions based on which check fails and resize the instance.

### Cloud Management Required Permissions/AWS Required Permissions
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles
- AWS - The `CloudWatchReadOnlyAccess` AWS IAM Policy

### Functional Details

- This policy identifies all instances reporting performance metrics to CloudWatch whose CPU, Burst Credit Balance, Surplus Burst Credit Balance meet specified thresholds set forth in the parameters.
- The **Exclusion Tag Key** parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy sets the tag defined in the **Action Tag Key:Value** parameter on the underutilized instances that were identified.
-  If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics. 

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Number of Surplus Credits to alert on* - Number of CPU Surplus Credits to report on, Set to -1 to ignore cpu burst credits
- *Enable checking burst credit balance against max* - checks burst credit balance against max_earnable_credits, if they are equal it will report. 
- *Exclusion Tag Key* - An Azure-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key
- *Cooldown Days* - Days to cooldown between checks of same instance

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.