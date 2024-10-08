# AWS Rightsize EC2 Instances

## What It Does

This policy checks all the instances in an AWS Account for CPU and Memory usage over a user-specified number of days. If the usage is less than the user provided Idle Instance CPU/Memory percentage threshold then the Virtual Machine is recommended for termination. If the usage is less than the user provided Underutilized Instance CPU/Memory percentage threshold then the Virtual Machine is recommended for downsizing. Both sets of Virtual Machines returned from this policy are emailed to the user.

## How It Works

- The policy leverages the AWS API to retrieve all instances and then uses the AWS CloudWatch API to check the instance average CPU and Memory utilization over a specified number of days.
- The utilization data is provided for the following statistics: Average, Maximum, Minimum, 99th percentile, 95th percentile, 90th percentile.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Idle Instance CPU/Memory Threshold(s) defined by the user. The recommendation provided for Idle Instances is a termination action; termination can be performed in an automated manner or after approval.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Underutilized Instance CPU/Memory Threshold(s) defined by the user. The recommendation provided for Inefficient/Underutilized Instances is a downsize action; downsizing can be performed in an automated manner or after approval.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for idle resources if the resource is stopped, terminated, and for underutilized resources if the resource is downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- For idle resources, the savings is the full cost of the resource. For underutilized resources, the savings is 50% of the cost of the resource.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Idle Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore CPU utilization for idle instance recommendations.
- *Idle Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore memory utilization for idle instance recommendations.
- *Underutilized Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore CPU utilization for underutilized instance recommendations.
- *Underutilized Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore memory utilization for underutilized instance recommendations.
- *Idle/Utilized for both CPU/Memory or either* - Set whether an instance should be considered idle and/or underutilized only if both CPU and memory are under the thresholds or if either CPU or memory are under. Has no effect if other parameters are configured such that only CPU or memory is being considered.
- *Threshold Statistic* - Statistic to use when determining if an instance is idle/underutilized.
- *Statistic Lookback Period* - How many days back to look at CPU and/or memory data for instances in Cloudwatch.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification
- Stop virtual machines (if idle) after approval
- Terminate virtual machines (if idle) after approval
- Downsize virtual machines (if underutilized but not idle) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `ec2:DescribeInstanceStatus`*
  - `ec2:DescribeTags`
  - `ec2:ModifyInstanceAttribute`*
  - `ec2:StartInstances`*
  - `ec2:StopInstances`*
  - `ec2:TerminateInstances`*
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:GetMetricData`
  - `cloudwatch:ListMetrics`
  - `sts:GetCallerIdentity`

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeInstances",
                  "ec2:DescribeInstanceStatus",
                  "ec2:DescribeTags",
                  "ec2:ModifyInstanceAttribute",
                  "ec2:StartInstances",
                  "ec2:StopInstances",
                  "ec2:TerminateInstances",
                  "cloudwatch:GetMetricStatistics",
                  "cloudwatch:GetMetricData",
                  "cloudwatch:ListMetrics",
                  "sts:GetCallerIdentity"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Memory Support

By default, only CPU metrics are available from CloudWatch. To enable support for memory metrics, you must have the CloudWatch Agent installed on your EC2 instance(s) to collect memory metrics. Please reference [AWS Docs > Install CloudWatch Agent on EC2 Instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) for more information.

### Windows Support

To enable Windows support, add the following to your Cloudwatch config.json and restart the Cloudwatch agent:

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

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
