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

- Edit the file [AWS_Publicly_Accessible_RDS_Instances](https://github.com/rightscale/policy_templates/tree/master/security/aws/rds_publicly_accessible/AWS_Publicly_Accessible_RDS_Instances.pt)
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

This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe AWS RDS instances, list RDS tags, modify RDS instances and delete RDS instances.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

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
