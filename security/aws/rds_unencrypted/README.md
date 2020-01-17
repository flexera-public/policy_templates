# AWS Unencrypted RDS Instances

## What it does

This policy checks all Relational Database Service (RDS) instances and reports on any that are unencrypted. When such a RDS instance is detected, the user can choose to delete by enabling 'delete action' option as mentioned in Enable delete action section below.

## Functional Details

When a Unencrypted RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the RDS instance after manual approval if needed.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - RDS instances with any of these tags will be ignored

## Policy Actions

Perform below steps to enable delete action.

- Edit the file [AWS_Unencrypted_RDS_Instances](https://github.com/rightscale/policy_templates/tree/master/security/aws/rds_unencrypted/AWS_Unencrypted_RDS_Instances.pt)
- uncomment below mentioned lines

```javascript
   escalate $delete_unencrypted_RDS_instances_approval
     check logic_or(
       eq(val(item, "delete_protection"), "YES"),
       ne(val(item, "db_instance_status"), "available")
     )
```

- And comment the line which contains 'check eq(val(item, "storage_encrypted"), "false")', save the changes.
- Upload the modified file and apply the policy.

Note:

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

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
