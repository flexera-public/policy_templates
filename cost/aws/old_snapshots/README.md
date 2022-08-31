# AWS Old Snapshots

## What it does

This policy finds AWS snapshots in the given account which are older than the specified days and deletes them after user approval. For a snapshot, if images are created then we can't delete the snapshot without deleting the images. So, if the user selects Yes, the snapshot will be deleted along with the images, and if No the snapshot will not be considered for deletion. Account specific snapshots are determined by filtering based on the owner-id. The account number is used as an owner-id.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource \* 30. The savings are displayed in the *Estimated Monthly Savings* column. If the resource can not be found in Optima the value is 0.0. The incident header includes the sum of each resource *Estimated Monthly Savings* as Total Estimated Monthly Savings.

If the AWS bill for the AWS account is registered in Optima in a different Flexera One org than the project where the policy template is applied, the *Flexera One Org ID for Optima* parameter can be set to the org where the AWS account is registered in Optima. Leaving this parameter set to `current` will result in using the same org as the project where the policy template is applied querying for Optima cost data.

The *Estimated Monthly Savings* and *Total Estimated Monthly Savings* are rounded to 3 decimal places, so the savings value will display 0.0 if the estimated savings is less than $0.0005.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeImages`
  - `ec2:DescribeSnapshots`
  - `sts:GetCallerIdentity`
  - `ec2:DeregisterImage`
  - `ec2:DeleteSnapshot`

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
                  "sts:GetCallerIdentity",
                  "ec2:DeregisterImage",
                  "ec2:DeleteSnapshot"
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
- *Email addresses* - A list of email addresses to notify.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Snapshot age* - The number of days since the snapshot was created.
- *Deregister Image* - If Yes, the snapshot will be deleted along with the images, and if No the snapshot will not be considered for deletion.
- *Exclude Tags* - List of tags that a snapshot can have to exclude it from the list.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Flexera One Org ID for Optima* - The Flexera One org ID for Optima queries used to determine estimated costs, by default the current org is used.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete Snapshots" action while applying the policy, all the snapshots that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
