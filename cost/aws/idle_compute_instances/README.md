# AWS Idle Compute Instances Policy

## Deprecated

This policy is no longer being updated. The [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/) policy now includes this functionality and is the recommended policy for getting idle compute recommendations.

## What It Does

This Policy Template checks for idle instance in AWS EC2 and then terminates them upon approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `ec2:DescribeTags`
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:GetMetricData`
  - `cloudwatch:ListMetrics`

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
                  "ec2:DescribeTags",
                  "cloudwatch:GetMetricStatistics",
                  "cloudwatch:GetMetricData",
                  "cloudwatch:ListMetrics"
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

By default only CPU metrics are available from CloudWatch.  To enable support for memory utilization, you must have the CloudWatch Agent installed on your EC2 instance(s) to collect memory metrics.  Please reference [AWS Docs > Install CloudWatch Agent on EC2 Instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) for more information.

### Windows Support

To enable windows support you will need to add the following to your cloudwatch config.json and restart cloudwatch agent

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

## How It Works

- This policy identifies all instances reporting performance metrics to CloudWatch whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters. These thresholds are what you would consider to be and idle instance.
- The **Exclusion Tag Key:Value** parameter is a string value. If the exclusion tag is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy can terminate instances after approval for instances that match the criteria.
- If you get an **N/A** in a field you will need to install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) on the instance to get those metrics.
- This policy only pulls running instances, as it is unable to get correct monitoring metrics from instances in other states.

### Policy Savings Details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day's cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is 0.0. The incident detail message includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings. The savings value is rounded off to 3 decimal places.
If the user is not having the minimum required role of `billing_center_viewer` or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as 0.0 in the incident table.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Used Memory Threshold* - The threshold at which to consider an instance to be 'idle'. Set to -1 to ignore memory utilization
- *Used CPU Threshold* - The threshold at which to consider an instance to be 'idle'. Set to -1 to ignore CPU utilization
- *Idle for both CPU/Memory or either* - Set to Both CPU and Memory to consider an instance idle only if it is below both the CPU and memory utilization parameters. Set to Either CPU or Memory to consider an instance idle if either CPU or memory are below the parameter values. Has no effect if either of the utilization parameters are set to -1.
- *Threshold Statistic* - Statistic to use for the metric threshold
- *Exclusion Tag Key:Value* - Cloud native tag to ignore instances. Format: Key:Value
- *CloudWatch API Wait Time* - The amount of time in seconds to wait between requests to the CloudWatch API to avoid being throttled by AWS. Default is recommended.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification
- Terminates instances after approval

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
