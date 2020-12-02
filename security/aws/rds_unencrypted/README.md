# AWS Unencrypted RDS Instances

## What it does

This policy checks all Relational Database Service (RDS) instances and reports on any that are unencrypted. When such a RDS instance is detected, the user can optionally delete them.

## Functional Details

When a Unencrypted RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the RDS instance after manual approval if needed.

## Input Parameters

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - RDS instances with any of these tags will be ignored
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete RDS Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Send an email report
- RDS instances with 'DB Instance Status' other than 'Available' and RDS instances with 'Delete Protection Enabled' cannot be deleted.
- When delete action is performed, DB snapshot gets created with name '<--RDS Instance Name-->-finalSnapshot' Ex mySQL-DBinstance-finalSnapshot before deleting DB instance.
- For Aurora instance, policy creates cluster snapshot since DB instance snapshot cannot be created directly.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":["rds:DescribeDBInstances",
              "rds:ListTagsForResource",
              "rds:CreateDBClusterSnapshot",
              "rds:DescribeDBClusterSnapshots",
              "rds:DeleteDBInstance"
             ],
    "Resource":"*"
    },
    {
      "Effect":"Allow",
      "Action":["ec2:DescribeRegions"],
      "Resource":"*"
    }]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
