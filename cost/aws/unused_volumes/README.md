# AWS Unused Volumes

## What it does

This Policy Template scans all volumes in the given account and identifies any unused volumes and if no read/writes operations performed within the number of user-specified days. If any are found, an incident report will show the volumes, and related information and an email will be sent to the user-specified email address. Cloud watch metrics are used to find the volume read/write operations

If the user approves that the volumes should be deleted, the policy will delete the volumes.
If the volume is not able to be deleted, say, due to it being locked, the volume will be tagged to indicate the CloudException error that was received.
If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unused volumes report will reflect the updated set of unused volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Unused days* - The number of days a volume has been unused. The days should be greater than zero.
- *Email addresses* - A list of email addresses to notify
- *Exclude Tags.* - A list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unused volumes after approval
- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

The following AWS permissions must be allowed for the policy to run.

```javascript
{
    "Version": "2016-11-15",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeVolumes","ec2:CreateTags","ec2:CreateSnapshot","ec2:DescribeSnapshots","ec2:DeleteVolume"],
    "Resource":"*"
    }
  ]
}

{
  "Version": "2012-10-17",
  "Statement":[{
    "Effect":"Allow",
    "Action":["cloudwatch:GetMetricStatistics"],
    "Resource":"*",
    "Condition":{
      "Bool":{
        "aws:SecureTransport":"true"
      }
     }
  }]
}

```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
