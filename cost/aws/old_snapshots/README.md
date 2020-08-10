# AWS Old Snapshots

## What it does

This policy finds AWS snapshots in the given account which are older than the specified days and deletes them after user approval. For a snapshot, if images are created then we can't delete the snapshot without deleting the images. So if the user selects Yes, the snapshot will be deleted along with the images, and if No the snapshot will not be considered for deletion. Account specific snapshots are determined by filtering based on the owner-id. The account number is used as an owner-id.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify
- *Snapshot age* - The number of days since the snapshot was created.
- *Deregister Image* - If Yes, the snapshot will be deleted along with the images, and if No the snapshot will not be considered for deletion. 
- *Exclusion Tags* - List of tags that a snapshot can have to exclude it from the list.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Snapshots" action while applying the policy, all the snapshots that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

The following AWS permissions must be allowed for the policy to run.

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteSnapshot",
                "ec2:DescribeSnapshots"
                "ec2:DescribeImages",
                "ec2:DeregisterImage",
                "sts:GetCallerIdentity",                
            ],
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
