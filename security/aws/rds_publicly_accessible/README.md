# AWS Publicly Accessible RDS Instances

## What it does

This policy checks all Relational Database Service (RDS) instances and reports on any that are publicly accessible. When such an instance is detected, the user can choose to disable the publicly accessible option and the user can also choose to delete by enabling 'delete action' option as mentioned in Enable delete action section below.

## Functional Details

When a publicly accessible RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have an option to modify configuration after manual approval, and even Users can perform delete action if required.

- *remove public access rule* - modifies the configuration of the RDS instance by disabling the public access rule

## Input Parameters

- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Tags to ignore* - List of tags that will exclude resources from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Update RDS Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be updated.

## Policy Actions

- Sends an email notification
- Disable the publicly accessible RDS instances after approval
- Delete publicly accessible RDS instances after approval

Note:

- RDS Instances with 'DB Instance Status' other than 'Available' and RDS instances with 'Delete Protection Enabled' cannot be deleted
- RDS instances with 'DB Instance Status' other than 'Available' can not be modified.
- When delete action is performed, DB snapshot gets created with name '<--RDS Instance Name-->-finalSnapshot' Ex mySQL-DBinstance-finalSnapshot before deleting DB instance.
- For Aurora instance, policy creates Cluster snapshot Since DB instance snapshot cannot be created directly.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
  - `rds:ModifyDBInstance*`
  - `rds:CreateDBClusterSnapshot*`
  - `rds:DescribeDBClusterSnapshots`
  - `rds:DeleteDBInstance*`

\* Only required for taking action (terminating or downsizing); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "rds:DescribeDBInstances",
                  "rds:ListTagsForResource",
                  "rds:ModifyDBInstance",
                  "rds:CreateDBClusterSnapshot",
                  "rds:DescribeDBClusterSnapshots",
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
