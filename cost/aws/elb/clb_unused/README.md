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
