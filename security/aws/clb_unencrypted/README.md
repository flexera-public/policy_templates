# AWS Unencrypted ELB Listeners (CLB)

## What it does

Checks for unecrypted listeners on Classic Load Balancers. If an internet-facing listener is using an unecrypted protocol (eg: NOT HTTPS, SSL, or TLS) an incident report will show for the listener and an email will be sent to the user-specified email address.

Note: Elastic Load Balancing (ELB) supports three types of load balancers: Classic Load Balancers, Application Load Balancers, and Network Load Balancers. There is a separate policy for Application and Network Load Balancers with unencrypted internet-facing listeners.

## Functional Details

The policy leverages the AWS elasticloadbalancing API to examine listener details. When an unencrypted internet-facing listener is detected, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- Ignore tags* - CLB with any of these tags will be ignored

## Policy Actions

- Send an email report

## Prerequisites

- This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.
- The credential must contain the value *AWS* in the Provider field. Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe AWS LoadBalancers and AWS LoadBalancer Tags. The IAM user will require the following permissions:

```javascript
{
    "Version": "2012-06-01",
    "Statement":[{
    "Effect":"Allow",
    "Action":["elasticloadbalancing:DescribeLoadBalancers",
              "elasticloadbalancing:DescribeTags"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.