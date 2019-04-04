## AWS Unused Classic Load Balancers (CLB) 
 
### What it does
This policy checks all CLB to determine if any are unused (have no healthy instances) and allows them to be deleted by the user after approval.

Note:Elastic Load Balancing (ELB) supports three types of load balancers: Application Load Balancers, Network Load Balancers, and Classic Load Balancers.

### Functional Details
 
The policy leverages the AWS elasticloadbalancing API to determine if the CLB is in use.
 
When an unused CLB is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the CLB after manual approval if needed.
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - CLB with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer

### AWS Required Permissions

This policy requires permissions to describe AWS LoadBalancers,InstanceHealth, tags and DeleteLoadBalancer. 
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
    "Version": "2012-06-01",
    "Statement":[{
    "Effect":"Allow",
    "Action":["elasticloadbalancing:DescribeLoadBalancers",
              "elasticloadbalancing:DescribeInstanceHealth",
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