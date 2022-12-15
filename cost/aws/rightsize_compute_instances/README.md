# AWS Rightsize Compute Instances

## What it does

This policy checks all the instances in an AWS Account for CPU and Memory usage over the last 30 days. If the usage is less than the user provided Idle Instance CPU/Memory percentage threshold then the Virtual Machine is recommended for termination. If the usage is less than the user provided Underutilized Instance CPU/Memory percentage threshold then the Virtual Machine is recommended for downsizing. Both sets of Virtual Machines returned from this policy are emailed to the user.

## Functional Details

- The policy leverages the AWS API to check all instances and then uses the AWS CloudWatch API to check the instance average CPU and Memory utilization over the past 30 days.
- The utilization data is provided for the following statistics: Average, 99th percentile, 95th percentile, 90th percentile.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Idle Instance CPU/Memory Threshold/s defined by the user, to provide a recommendation.
- (Coming soon) The recommendation provided for Idle Instances is a termination action. These instancse can be terminated in an automated manner or after approval.
- The policy identifies all instances that have CPU utilization and/or Memory utilization below the Underutilized Instance CPU/Memory Threshold/s defined by the user, to provide a recommendation.
- (Coming soon) The recommendation provided for Inefficient/Underutilized Instances is a downsize action. These instancse can be downsized in an automated manner or after approval.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated, or downsized. Optima is used to receive the estimated savings which is the cost of the resource for the last full month. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is 0.0. The incident message detail includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Idle Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore CPU utilization.
- *Idle Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore memory utilization.
- *Underutilized Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore CPU utilization.
- *Underutilized Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore memory utilization.
- *Idle/Utilized for both CPU/Memory or either* - Set whether an instance should be considered idle and/or underutilized only if both CPU and memory are under the thresholds or if either CPU or memory are under. Note: this parameter is only valid when at least one Memory Utilization threshold and one CPU Utilization threshold is NOT set to -1.
- *Threshold Statistic* - Statistic to use for the metric threshold.
- *Exclusion Tag Key:Value* - Cloud native tag to ignore instances that you don't want to consider for downsizing or termination. Format: Key:Value
- *CloudWatch API Wait Time* - The amount of time in seconds to wait between requests to the CloudWatch API to avoid being throttled by AWS. Default is recommended.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Subscription Whitelist* - Whitelisted Subscriptions, if empty, all subscriptions will be checked.
- *Log to CM Audit Entries* - Boolean for whether or not to log any debugging information from actions to CM Audit Entries, this should be left set to No on Flexera EU.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification
- (Coming soon) Terminate virtual machines (if idle) after approval
- (Coming soon) Downsize virtual machines (if underutilized) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

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
