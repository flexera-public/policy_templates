# AWS Overutilized EC2 Instances

## What It Does

This policy template checks all of the EC2 instances in an AWS Account for CPU and Memory usage over a user-specified number of days. If the usage is above the user provided CPU/Memory percentage thresholds then the EC2 instance is recommended for upsizing. Optionally, a list of oversized EC2 instances is emailed.

## How It Works

- The policy leverages the AWS API to retrieve all instances and then uses the AWS CloudWatch API to check the instance CPU and Memory utilization over a specified number of days.
- The utilization data is provided for the following statistics: Average, Maximum, Minimum, 99th percentile, 95th percentile, 90th percentile.
- The policy identifies all instances that have CPU utilization and/or Memory utilization above the CPU/Memory Threshold(s) defined by the user. The recommendation provided for oversized EC2 instances is upsizing.

### Policy Costs Details

The policy includes the estimated monthly costs. The estimated monthly costs will be incurred for resources that are upsized.

- The `Estimated Monthly Cost` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- The cost of the upsize action is the full cost of the resource. This is because upsizing an EC2 instance doubles the cost.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Cost` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Cost` as `Potential Monthly Cost`.
- Both `Estimated Monthly Cost` and `Potential Monthly Cost` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *CPU Threshold (%)* - The CPU threshold at which to consider an instance to be overutilized and therefore be flagged for upsizing. Set to -1 to ignore CPU utilization for overutilized instance recommendations.
- *Memory Threshold (%)* - The Memory threshold at which to consider an instance to be overutilized and therefore be flagged for upsizing. Set to -1 to ignore memory utilization for overutilized instance recommendations.
- *Both CPU and Memory or Either* - Set whether an instance should be considered overutilized only if both CPU and memory are under the thresholds or if either CPU or memory are under. Has no effect if other parameters are configured such that only CPU or memory is being considered.
- *Threshold Statistic* - Statistic to use when determining if an instance is overutilized.
- *Statistic Lookback Period* - How many days back to look at CPU and/or memory data for instances in Cloudwatch.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Upsize Instances" action while applying the policy template, all reported overutilized EC2 instances will be upsized.

## Policy Actions

- Sends an email notification
- Upsize EC2 instances after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

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

This policy template does not incur any cloud costs.
