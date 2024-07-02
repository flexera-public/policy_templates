# AWS Rightsize RDS Instances

## What It Does

This policy template checks for unused and underutilized RDS instances by reviewing CloudWatch metrics for each RDS instance in the AWS account. Incidents are raised containing unused and underutilized RDS instances, and the user has the option to terminate unused instances or downsize underutilized instances.

## Functional Details

- The policy leverages the AWS API to check all AWS RDS instances and then checks the number of connections and CPU utilization over a user-specified number of days.
- The policy identifies all instances that have had no connections over a user-specified number of days and provides the relevant recommendation.
- The recommendation provided for unused instances is a termination action. These instances can be terminated in an automated manner or after approval.
- The policy identifies all instances that have CPU usage below the user-specified threshold over a user-specified number of days and provides the relevant recommendation. If the user has opted to report on both unused and underutilized instances (default), unused instances are excluded from this analysis. Average CPU utilization is the metric used for this assessment by default, but the user can choose other metrics via the `Threshold Statistic` parameter.
- The policy filters the results by removing any instances that are already at the smallest available size for their particular region and database engine type.
- The recommendation provided for underutilized instances is a downsize action. These instances can be downsized in an automated manner or after approval.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for unused resources if the resource is terminated, and for underutilized resources if the resource is downsized.

- The cost of the resource is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- For unused resources, the `Estimated Monthly Savings` is the full cost of the resource.
- For underutilized resources, the `Estimated Monthly Savings` is the full cost of the resource divided by the number of [NFUs (Normal Form Units)](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/normalization-factor-for-dedicated-ec2-instances.html) for the current resource size, multiplied by the number of NFUs for the recommended resource size, and then subtracted from the current cost of the resource.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Report Unused or Underutilized* - Whether to report on unused instances, underutilized instances, or both. If both are selected, unused instances will not appear in the list of underutilized instances regardless of CPU usage.
- *Underutilized Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be underutilized and therefore be flagged for downsizing.
- *Statistic Lookback Period* - How many days back to look at statistical data for instances to determine if they are underutilized or unused. This value cannot be set higher than 90 because AWS does not retain metrics for longer than 90 days.
- *Threshold Statistic* - CPU statistic to use when determining if an instance is underutilized.
- *Downsize Timeframe* - Whether to downsize underutilized RDS instances immediately or wait until the next maintenance window.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Resize Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be resized.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Sends an email notification
- Terminate AWS RDS instance (if unused) after approval
- Downsize AWS RDS instance (if underutilized) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:GetMetricData`
  - `ec2:DescribeRegions`
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
  - `rds:DescribeOrderableDBInstanceOptions`
  - `rds:ModifyDBInstance`*
  - `rds:DeleteDBInstance`*

\* Only required for taking action (terminating or downsizing); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:GetCallerIdentity",
                  "cloudwatch:GetMetricStatistics",
                  "cloudwatch:GetMetricData",
                  "ec2:DescribeRegions",
                  "rds:DescribeDBInstances",
                  "rds:ListTagsForResource",
                  "rds:ModifyDBInstance",
                  "rds:DeleteDBInstance"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
