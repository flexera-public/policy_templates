## AWS App/Network Load Balancers w/Internet-facing Unencrypted Listeners
 
### What it does
Checks for unecrypted listeners on Application and Network Load Balancers. If an internet-facing listener is using an unecrypted protocol (eg: NOT HTTPS, SSL, or TLS) an incident report will show for the listener and an email will be sent to the user-specified email address.

Note: Elastic Load Balancing (ELB) supports three types of load balancers: Classic Load Balancers, Application Load Balancers, and Network Load Balancers. There is a separate policy for Classic Load Balancers with unencrypted internet-facing listeners.

### Functional Details
 
The policy leverages the AWS elasticloadbalancing API to examine listener details. When an unencrypted internet-facing listener is detected, an email action is triggered automatically to notify the specified users of the incident.
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - CLB with any of these tags will be ignored 
 
### Required RightScale Roles
 
- admin or credential_viewer

### AWS Required Permissions

This policy requires permissions to describe AWS LoadBalancers, AWS LoadBalancer Tags, and AWS LoadBalancer Listeners.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
    "Version": "2015-12-01",
    "Statement":[{
    "Effect":"Allow",
    "Action":["elasticloadbalancing:DescribeLoadBalancers",
              "elasticloadbalancing:DescribeTags",
              "elasticloadbalancing:DescribeListeners"],
    "Resource":"*"
    }
  ]
}
```

### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.
