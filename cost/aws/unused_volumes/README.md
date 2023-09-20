# AWS Unused Volumes

## What it does

This Policy finds unused volumes in the given account and deletes them after user approval. The user can optionally create a snapshot before deleting the volume. CloudWatch is used to determine its use by checking if there are read or write operations within the number of user-specified days. The Volume Status parameter will determine whether to include attached volumes in the resulting incident, unattached, or both. Policy Incident will be created with all of volumes that fall into these criteria.

If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unused volumes incident will reflect the updated set of unused volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

### Policy savings details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is terminated or downsized. Optima is used to retrieve and calculate the estimated savings which is the cost of the resource for a full day (3 days ago) multiplied by 30.44 (the average number of days in a month), or 0 if no cost information for the resource was found in Optima. The savings is displayed in the Estimated Monthly Savings column. The incident message detail includes the sum of each resource *Estimated Monthly Savings* as *Potential Monthly Savings*.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Unused Days* - The number of days a volume has been unused. The days should be greater than zero.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Volume Status* - Whether to include attached volumes, unattached, or both in the results.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Volumes" action while applying the policy, all the volumes that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unused volumes after approval
- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeVolumes`
  - `ec2:DescribeSnapshots`
  - `cloudwatch:GetMetricStatistics`
  - `ec2:CreateTags`*
  - `ec2:CreateSnapshot`*
  - `ec2:DetachVolume`*
  - `ec2:DeleteVolume`*

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

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
