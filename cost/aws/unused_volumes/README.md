# AWS Unused Volumes

## What it does

This Policy finds unused volumes in the given account and deletes them after user approval. The user can optionally create a snapshot before deleting the volume. An unused volume is determined by checking for the state as available and uses CloudWatch to determine its use by checking if there are read or write operations within the number of user-specified days. A Policy Incident will be created with all of volumes that fall into these criteria.

If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unused volumes incident will reflect the updated set of unused volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource \* 30. The savings are displayed in the *Estimated Monthly Savings* column. If the resource can not be found in Optima the value is `N/A`. The incident detail message includes the sum of each resource *Estimated Monthly Savings* as *Total Estimated Monthly Savings*.

If the AWS bill for the AWS account is registered in Optima in a different Flexera One org than the project where the policy template is applied, the *Flexera One Org ID for Optima* parameter can be set to the org where the AWS account is registered in Optima. Leaving this parameter set to `current` will result in using the same org as the project where the policy template is applied querying for Optima cost data.

If the user does not have the minimum required role of `billing_center_viewer` or if there is not enough data received from Optima to calculate savings, an appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as `N/A` in the incident table.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Unused days* - The number of days a volume has been unused. The days should be greater than zero.
- *Email addresses* - A list of email addresses to notify
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Flexera One Org ID for Optima* - The Flexera One org ID for Optima queries used to determine estimated costs, by default the current org is used.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Volumes" action while applying the policy, all the volumes that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unused volumes after approval
- Send an email report

## Prerequisites

- This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.
- billing_center_viewer (note: this role must be applied at the Organization level)

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

The following AWS permissions must be allowed for the policy to run.

```json
{
  "Version": "2012-10-17",
  "Statement":[
    {
      "Effect":"Allow",
      "Action":[
        "ec2:DescribeVolumes",
        "ec2:CreateTags",
        "ec2:CreateSnapshot",
        "ec2:DescribeSnapshots",
        "ec2:DeleteVolume",
        "ec2:DescribeRegions"
      ],
      "Resource":"*"
    },
    {
      "Effect":"Allow",
      "Action":["cloudwatch:GetMetricStatistics"],
      "Resource":"*",
      "Condition":{
        "Bool":{
          "aws:SecureTransport":"true"
        }
      }
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
