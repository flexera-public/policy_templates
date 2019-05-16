## AWS Unencrypted RDS Instances
 
### What it does

This policy checks all Relational Database Service (RDS) instances and reports on any that are unencrypted. When such a RDS instance is detected, the user can choose to delete by enabling 'delete action' option as mentioned in Enable delete action section below.

### Functional Details
 
When a Unencrypted RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the RDS instance after manual approval if needed. 
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - RDS instances with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer

### Enable delete action

Perform below steps to enable delete action.

- *Edit the file [AWS_Unencrypted_RDS_Instances](https://github.com/rightscale/policy_templates/tree/master/security/aws/rds_unencrypted/AWS_Unencrypted_RDS_Instances.pt)
- *uncomment the line which contains 'escalate $delete_unEncripted_RDS_instances_approval' and save the changes.
- *upload the modified file and apply the policy.

Note: 
- *RDS Instances with 'DB Instance Status' other than 'Available' and RDS instances with 'delete Protection enabled' cannot be deleted
- *When delete action is performed, DB snapshot gets created with name '<--DB_Instance_Identifier-->-finalSnapshot' Ex mySQL-DBinstance-finalSnapshot before deleting DB instance.
- *For Aurora instance, policy creates Cluster snapshot Since DB instance snapshot cannot be created directly.

### AWS Required Permissions

This policy requires permissions to describe AWS Unencrypted RDS instances, tags and Delete RDS instances.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
    "Version": "2014-10-31",
    "Statement":[{
    "Effect":"Allow",
    "Action":["rds:DescribeDBInstances",
	      "rds:ListTagsForResource",
	      "rds:CreateDBClusterSnapshot",
		  "rds:DescribeDBClusterSnapshots",
		  "rds:DeleteDBInstance"],
    "Resource":"*"
    }
  ]
}

```

### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.
