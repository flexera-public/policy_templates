# AWS Internet-facing ELBs & ALBs

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

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:
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
    "Version":"2015-12-01",
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
