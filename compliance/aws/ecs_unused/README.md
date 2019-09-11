## AWS Unused ECS Clusters
 
### What it does

This policy checks all ECS clusters to determine if any are unused (no registered instances, no running tasks, no pending tasks, no active services) and offers the option to delete the cluster after manual approval.

### Functional Details
 
The policy leverages the AWS API to determine if the ECS cluster is in use.
 
When an unused ECS cluster is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the cluster after manual approval if needed.
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - ECS clusters with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer

### AWS Required Permissions

This policy requires permissions to describe AWS ECS ListClusters, DescribeClusters and DeleteCluster.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
  "Version": "2014-11-13",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ecs:ListClusters",
            "ecs:DescribeClusters",
            "ecs:DeleteCluster"],
    "Resource":"*"
    }
  ]
}
```

### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.

### Limitation

This policy generates a report of upto 100 clusters. 
