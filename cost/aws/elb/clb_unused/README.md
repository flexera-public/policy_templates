# AWS Unused Classic Load Balancers (CLB)

## What it does

This policy checks all Classic Load Balancers (CLB) to determine if any are unused (have no healthy instances) and allows them to be deleted by the user after approval.

Note:Elastic Load Balancing (ELB) supports three types of load balancers: Application Load Balancers, Network Load Balancers and Classic Load Balancers.

## Functional Details

The policy leverages the AWS elasticloadbalancing API to determine if the CLB is in use.

When an unused CLB is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the CLB after manual approval if needed.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - CLB with any of these tags will be ignored

## Policy Actions

- Sends an email notification.
- Delete unused CLB after approval.

## Prerequisites

This policy requires the AWS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe AWS LoadBalancers, InstanceHealth, tags and DeleteLoadBalancer.
The AWS credentials will require the following permissions:

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

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
