## AWS Publicly Accessible RDS Instances
 
### What it does
This policy checks all Relational Database Service (RDS) instances and reports on any that are publicly accessible. When such an instance is detected, the user can choose to disable the publicly accessible option and the user can also choose to delete by enabling 'delete action' option as mentioned in Enable delete action section below.
 
### Functional Details
 
When a publicly accessible RDS instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have an option to modify configuration after manual approval, and even Users can perform delete action if required. 
- *remove public access rule* - modifies the configuration of the RDS instance by disabling the public access rule
 
### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - RDS instances with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer

### AWS Required Permissions

This policy requires permissions to describe AWS RDS instances, tags, modify and delete instances.
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

### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.


### Enable delete action

Perform below steps to enable delete action.

- Edit the file [AWS_Publicly_Accessible_RDS_Instances](https://github.com/rightscale/policy_templates/tree/master/security/aws/rds_publicly_accessible/AWS_Publicly_Accessible_RDS_Instances.pt)
- uncomment the line which contains 'escalate $delete_publicly_accessible_RDS_instances_approval' and save the changes.
- upload the modified file and apply the policy.

Note: 
- RDS Instances with 'DB Instance Status' other than 'Available' and RDS instances with 'delete Protection enabled' cannot be deleted
- RDS instances with 'DB Instance Status' other than 'Available' can not be modified.
- When delete action is performed, DB snapshot gets created with name '<--DB_Instance_Identifier-->-finalSnapshot' Ex mySQL-DBinstance-finalSnapshot before deleting DB instance.
- For Aurora instance, policy creates Cluster snapshot Since DB instance snapshot cannot be created directly.




