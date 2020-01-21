# AWS Publicly Accessible RDS Instances

## What it does

This policy checks all Relational Database Service (RDS) instances and reports on any that are publicly accessible. When such an instance is detected, the user can choose to disable the publicly accessible option and the user can also choose to delete by enabling 'delete action' option as mentioned in Enable delete action section below.

## Functional Details

When a publicly accessible RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have an option to modify configuration after manual approval, and even Users can perform delete action if required.

- *remove public access rule* - modifies the configuration of the RDS instance by disabling the public access rule

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude resources from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'

## Policy Actions

- Sends an email notification
- Disable the publicly accessible RDS instances after approval
- Delete publicly accessible RDS instances after approval (optional)

Perform below steps to enable delete action.

- Edit the file [AWS_Publicly_Accessible_RDS_Instances](/security/aws/rds_publicly_accessible/aws_publicly_accessible_rds_instances.pt)
- uncomment below mentioned lines

```javascript
   escalate $delete_publicly_accessible_RDS_instances_approval
     check logic_or(
      eq(val(item, "delete_protection"), "YES"),
      ne(val(item, "db_instance_status"), "available")
    )
```

- And comment the line which contains 'check eq(val(item, "publicly_accessible"), "false")', save the changes.
- upload the modified file and apply the policy.

Note:

- RDS Instances with 'DB Instance Status' other than 'Available' and RDS instances with 'Delete Protection Enabled' cannot be deleted
- RDS instances with 'DB Instance Status' other than 'Available' can not be modified.
- When delete action is performed, DB snapshot gets created with name '<--RDS Instance Name-->-finalSnapshot' Ex mySQL-DBinstance-finalSnapshot before deleting DB instance.
- For Aurora instance, policy creates Cluster snapshot Since DB instance snapshot cannot be created directly.

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
            "rds:ModifyDBInstance",
            "rds:CreateDBClusterSnapshot",
            "rds:DescribeDBClusterSnapshots",
            "rds:DeleteDBInstance"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
