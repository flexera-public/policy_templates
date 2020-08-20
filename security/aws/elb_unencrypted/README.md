# AWS Unencrypted ELB Listeners (ALB/NLB)

## What it does

Checks for unecrypted listeners on Application and Network Load Balancers. If an internet-facing listener is using an unecrypted protocol (eg: NOT HTTPS, SSL, or TLS) an incident report will show for the listener and an email will be sent to the user-specified email address.

Note: Elastic Load Balancing (ELB) supports three types of load balancers: Classic Load Balancers, Application Load Balancers, and Network Load Balancers. There is a separate policy for Classic Load Balancers with unencrypted internet-facing listeners.

## Functional Details

The policy leverages the AWS elasticloadbalancing API to examine listener details. When an unencrypted internet-facing listener is detected, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - ALB/NLB with any of these tags will be ignored

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

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

```javascript
{
  "Version": "2016-11-15",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ec2:DescribeRegions"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
