# AWS Old Snapshots

## What it does

This policy finds AWS snapshots in the given account which are older than the specified days and deletes them after user approval. Snapshots with an associated AMI can be included or excluded depending on the settings selected when applying the policy; if included, the AMI will be deleted along with the snapshot if the snapshot is deleted.

### Policy savings details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is terminated. The estimated monthly savings is calculated by multiplying the actual cost of the resource for 1 day, as found within Flexera CCO, by 30.4375, which is the average number of days in a month. The savings are�displayed in the *Estimated Monthly Savings*�column. If the resource cannot be found in Flexera CCO, the estimated savings is 0. The incident header includes the sum of each resource *Estimated Monthly Savings* as *Potential Monthly Savings*.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Service Types* - Exclude the selected services (EC2 or RDS). If left blank, all services will be analyzed.
- *Exclusion EC2 Snapshot Description* - Exclude EC2 snapshots with the provided descriptions. If left blank, all EC2 snapshots will be analyzed. This setting has no effect on RDS snapshots.
- *Exclusion RDS Snapshot Types* - Exclude the selected RDS snapshot types. If left blank, all types will be analyzed. This setting has no effect on EC2 snapshots.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore instances that you don't want to consider for deletion. Format: Key:Value
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Snapshot Age* - The number of days since the snapshot was created to consider it old.
- *Include Snapshots with AMI* - Whether or not to produce recommendations for snapshots with an associated registered AMI (Amazon Machine Image).
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete Snapshots" action while applying the policy, all the snapshots that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeImages`
  - `ec2:DescribeSnapshots`
  - `ec2:DeregisterImage`*
  - `ec2:DeleteSnapshot`*
  - `rds:DescribeDBInstances`
  - `rds:DescribeDBSnapshots`
  - `rds:DescribeDBClusters`
  - `rds:DescribeDBClusterSnapshots`
  - `rds:DeleteDBClusterSnapshot`*
  - `rds:DeleteDBSnapshot`*
  - `sts:GetCallerIdentity`

  \* Only required for taking action (deletion); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeImages",
                  "ec2:DescribeSnapshots",
                  "ec2:DeregisterImage",
                  "ec2:DeleteSnapshot"
                  "rds:DescribeDBInstances",
                  "rds:DescribeDBSnapshots",
                  "rds:DescribeDBClusters",
                  "rds:DescribeDBClusterSnapshots",
                  "rds:DeleteDBSnapshot",
                  "rds:DeleteDBClusterSnapshot",
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

This Policy Template does not launch any instances, and so does not incur any cloud costs.
