# AWS Old Snapshots

## What it does

This policy finds AWS snapshots in the given account which are older than the specified days and deletes them after user approval. For a snapshot, if images are created then we can't delete the snapshot without deleting the images. So, if the user selects Yes, the snapshot will be deleted along with the images, and if No the snapshot will not be considered for deletion. Account specific snapshots are determined by filtering based on the owner-id. The account number is used as an owner-id.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is n/a. The incident header includes the sum of each resource Estimated Monthly Savings in the Incident Header as Total Estimated Monthly Savings.

The Estimated Monthly Savings and Total Estimated Monthly Savings rounded to 3 decimal places, so the savings value will display $0.000 if estimated savings is less than $0.0005.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS. If in case disabled regions are entered then the policy will throw an error. Leave blank to consider all the regions.
- *Email addresses* - A list of email addresses to notify.
- *Snapshot age* - The number of days since the snapshot was created.
- *Deregister Image* - If Yes, the snapshot will be deleted along with the images, and if No the snapshot will not be considered for deletion.
- *Exclude Tags* - List of tags that a snapshot can have to exclude it from the list.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete Snapshots" action while applying the policy, all the snapshots that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete old snapshots after an approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin, and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Required Flexera Role: billing_center_viewer (note: this role must be applied at the Organization level).

Provider tag value to match this policy: `aws` , `aws_sts`

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
                "ec2:DescribeRegions"      
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
