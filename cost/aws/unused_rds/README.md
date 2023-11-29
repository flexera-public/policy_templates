# AWS Unused RDS Instances

## Deprecated

This policy is no longer being updated. The [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/) policy now includes this functionality and is the recommended policy for getting unused RDS instance recommendations.

## What It Does

This policy template checks for Unused RDS instances by reviewing CloudWatch DBconnections and terminates them after user approval.

## Functional Details

This policy gets a list of RDS instances and uses CloudWatch DBConnection metric to check for connections over a user-specified period of days. If there are no DBConnections, the policy will terminate the RDS instance after the user approval.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is terminated.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Unused Days* - The number of days an RDS instance has been unused. The days should be greater than zero.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Terminate AWS RDS instances after approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `cloudwatch:GetMetricData`
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:ListMetrics`
  - `rds:DeleteDBInstance`*
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
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
                  "cloudwatch:GetMetricData",
                  "cloudwatch:GetMetricStatistics",
                  "cloudwatch:ListMetrics",
                  "rds:DeleteDBInstance",
                  "rds:DescribeDBInstances",
                  "rds:ListTagsForResource",
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

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
