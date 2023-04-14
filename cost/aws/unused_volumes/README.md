# AWS Unused Volumes

## What it does

This Policy finds unused volumes in the given account and deletes them after user approval. The user can optionally create a snapshot before deleting the volume. CloudWatch is used to determine its use by checking if there are read or write operations within the number of user-specified days. The Volume Status parameter will determine whether to include attached volumes in the resulting incident, unattached, or both. Policy Incident will be created with all of volumes that fall into these criteria.

If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unused volumes incident will reflect the updated set of unused volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource \* 30. The savings are displayed in the *Estimated Monthly Savings* column. If the resource can not be found in Optima the value is 0.0. The incident detail message includes the sum of each resource *Estimated Monthly Savings* as *Total Estimated Monthly Savings*.

If the AWS bill for the AWS account is registered in Optima in a different Flexera One org than the project where the policy template is applied, the *Flexera One Org ID for Optima* parameter can be set to the org where the AWS account is registered in Optima. Leaving this parameter set to `current` will result in using the same org as the project where the policy template is applied querying for Optima cost data.

If the user does not have the minimum required role of `billing_center_viewer` or if there is not enough data received from Optima to calculate savings, an appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as 0.0 in the incident table.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeVolumes`
  - `ec2:DescribeSnapshots`
  - `cloudwatch:GetMetricStatistics`
  - `ec2:CreateTags`
  - `ec2:CreateSnapshot`
  - `ec2:DetachVolume`
  - `ec2:DeleteVolume`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeVolumes",
                  "ec2:DescribeSnapshots",
                  "cloudwatch:GetMetricStatistics",
                  "ec2:CreateTags",
                  "ec2:CreateSnapshot",
                  "ec2:DetachVolume",
                  "ec2:DeleteVolume"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Unused days* - The number of days a volume has been unused. The days should be greater than zero.
- *Volume Status* - Whether to include attached volumes, unattached, or both in the results.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Email addresses* - A list of email addresses to notify
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Flexera One Org ID for Optima* - The Flexera One org ID for Optima queries used to determine estimated costs, by default the current org is used.
- *CloudWatch API Wait Time* - The amount of time in seconds to wait between requests to the CloudWatch API to avoid being throttled by AWS. Default is recommended.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Volumes" action while applying the policy, all the volumes that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unused volumes after approval
- Send an email report

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
