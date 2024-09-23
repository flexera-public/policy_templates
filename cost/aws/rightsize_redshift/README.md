# AWS Rightsize Redshift

## What It Does

This policy template checks the AWS Redshift clusters in the AWS account for low CPU usage. A report is created listing all clusters with a downsize recommendation. Optionally, this report can be emailed and the clusters in question can be downsized.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the underutilized cluster is downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the cluster for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- The savings is the difference in cost between the current cluster cost and the estimated cost of the recommended cluster node size.
- Since the costs of individual clusters are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the cluster cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each cluster `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter clusters containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all clusters with the specified tag key.
  - `Key==Value` - Filter all clusters with the specified tag key:value pair.
  - `Key!=Value` - Filter all clusters missing the specified tag key:value pair. This will also filter all clusters missing the specified tag key.
  - `Key=~/Regex/` - Filter all clusters where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all clusters where the value for the specified key does not match the specified regex string. This will also filter all clusters missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter clusters containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Statistic Lookback Period* - How many days back to look at CPU data for clusters. This value cannot be set higher than 90 because AWS does not retain metrics for longer than 90 days.
- *Threshold Statistic* - Statistic to use when determining if an cluster is underutilized
- *Maximum CPU Usage Target (%)* - Maximum predicted CPU usage for recommended node types. For example, if set to '90', only recommendations where the new size would not result in > 90% CPU usage will be included in the results.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Downsize Redshift Nodes" action while applying the policy, all the resources that didn't satisfy the policy condition will have their nodes downsized.

## Policy Actions

- Sends an email notification
- Downsize Redshift clusters after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `cloudwatch:GetMetricData`
  - `ec2:DescribeRegions`
  - `redshift:DescribeClusters`
  - `redshift:ModifyCluster`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:GetCallerIdentity",
                  "cloudwatch:GetMetricData",
                  "ec2:DescribeRegions",
                  "redshift:DescribeClusters",
                  "redshift:ModifyCluster"
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

This policy template does not incur any cloud costs.
