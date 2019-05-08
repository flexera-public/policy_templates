## Check for internet-facing ELBs & ALBs 
 
### What it does
This policy checks all load balancers (both Classic Load Balancers(ELBs) and Application Load Balancers(ALBs)) and reports on any that are internet-facing. When such a load balancer is detected, the user can choose to delete it after approval.

### Functional Details
 
When an internet-facing load balancer is detected, an email action is triggered automatically to notify the specified users of the incident. Users then can delete the load balancer after approval. 

Using this may result in instances with no load balancers.
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - load balancer with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer

### AWS Required Permissions

This policy requires permissions to describe AWS Load Balancers, tags and Delete Load Balancer.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
    "Version": "2012-06-01",
    "Statement":[{
    "Effect":"Allow",
    "Action":["elasticloadbalancing:DescribeLoadBalancers",
	      "elasticloadbalancing:DescribeTags",
	      "elasticloadbalancing:DeleteLoadBalancer"],
    "Resource":"*"
    }
  ]
}

{
    "Version": "2015-12-01",
    "Statement":[{
    "Effect":"Allow",
    "Action":["elasticloadbalancing:DescribeLoadBalancers",
	      "elasticloadbalancing:DescribeTags",
	      "elasticloadbalancing:DeleteLoadBalancer"],
    "Resource":"*"
    }
  ]
}
```

### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.
