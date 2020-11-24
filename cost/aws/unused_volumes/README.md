# AWS Unused Volumes

## What it does

This Policy finds unused volumes in the given account and deletes them after user approval. The user can optionally create a snapshot before deleting the volume. An unused volume is determined by checking for the state as available and uses CloudWatch to determine its use by checking if there are read or write operations within the number of user-specified days. A Policy Incident will be created with all of volumes that fall into these criteria.

If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unused volumes incident will reflect the updated set of unused volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is n/a. The incident detail message includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.
If the user is not having the minimum required role of `billing_center_viewer` or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as N/A in the incident table.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS and enter the region code. If SCP is enabled for an AWS account, then enter only the enabled regions if in case disabled regions are entered then the policy will throw an error. If this field is left blank, then the policy evaluates all the regions fetched using the **DescribeRegions** API call.
- *Unused days* - The number of days a volume has been unused. The days should be greater than zero.
- *Email addresses* - A list of email addresses to notify
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Volumes" action while applying the policy, all the volumes that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unused volumes after approval
- Send an email report

## Prerequisites

- This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.
- billing_center_viewer (note: this role must be applied at the Organization level)

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

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
