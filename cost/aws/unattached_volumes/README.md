# AWS Delete Unattached Volumes

## What it does

This Policy Template scans all volumes in the given account and identifies any unattached volumes that have been unattached for at least the number of user-specified days. If any are found, an incident report will show the volumes, and related information and an email will be sent to the user-specified email address.

If the user approves that the volumes should be deleted, the policy will delete the volumes.
If the volume is not able to be deleted, say, due to it being locked, the volume will be tagged to indicate the CloudException error that was received.
If the issue causing the delete failure is removed, the next run of the policy will delete the volume.
Note: The unattached volumes report will reflect the updated set of unattached volumes on the subsequent run.

Optionally, the user can specify one or more tags that if found on a volume will exclude the volume from the list.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Unattached days* - the number of days a volume has been unattached.
- *Email addresses* - A list of email addresses to notify
- *Exclude Tags.* - a list of tags used to excluded volumes from the incident.
- *Create Final Snapshot* - Boolean for whether or not to take a final snapshot before deleting

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Delete Unattached volumes after approval
- Send an email report

## Prerequisites

This policy requires the AWS Credential.  When applying the policy select the appropriate credentials
from the list for your tenant.  If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *aws* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

### AWS Required Permissions

The following AWS permissions must be allowed for the policy to run.

```javascript
{
    "Version": "2016-11-15",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeVolumes","ec2:CreateTags","ec2:CreateSnapshot","ec2:DescribeSnapshots"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
