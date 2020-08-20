# AWS Unencrypted RDS Instances

## What it does

This policy checks all Relational Database Service (RDS) instances and reports on any that are unencrypted. When such a RDS instance is detected, the user can optionally delete them.

## Functional Details

When a Unencrypted RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the RDS instance after manual approval if needed.

## Input Parameters

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

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```javascript
{
    "Version": "2014-10-31",
    "Statement":[{
    "Effect":"Allow",
    "Action":["rds:DescribeDBInstances",
              "rds:ListTagsForResource",
              "rds:CreateDBClusterSnapshot",
              "rds:DescribeDBClusterSnapshots",
              "rds:DeleteDBInstance"
             ],
    "Resource":"*"
    }
    ]
}
```

```javascript
{
  "Version": "2016-11-15",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ec2:DescribeRegions"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
