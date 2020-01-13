# Check for internet-facing ELBs & ALBs

## What it does

This policy checks all load balancers (both Classic Load Balancers(ELBs) and Application Load Balancers(ALBs)) and reports on any that are internet-facing. When such a load balancer is detected, the user can choose to delete it after approval.

## Functional Details

When an internet-facing load balancer is detected, an email action is triggered automatically to notify the specified users of the incident. Users then can delete the load balancer after approval.

Using this may result in instances with no load balancers.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude load Balancers from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or Key/value pairs can be listed. Example: 'test,env=dev'

## Policy Actions

- Sends an email notification.
- Delete Internet-facing ELB's & ALB's after approval.

## Prerequisites

This policy requires the AWS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe AWS Load Balancers, tags and Delete Load Balancer.
The AWS credentials will require the following permissions:

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

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
