# AWS Delete Unattached Volumes

## What it does

This Policy finds AWS snapshots older than the specified days and deletes them.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Snapshot age* - The number of days since the snapshot was created.
- *Exclusion Tags* - list of tags that a snapshot can have to exclude it from the list.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

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
    "Action":["ec2:DescribeSnapshots","ec2:DeleteSnapshot"],
    "Resource":"*"
    }
  ]
}
```

```javascript
{
    "Version": "2011-06-15",
    "Statement":[{
    "Effect":"Allow",
    "Action":["sts:GetCallerIdentity"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
