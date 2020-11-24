# AWS Unencrypted ELB Listeners (CLB)

## What it does

Checks for unecrypted listeners on Classic Load Balancers. If an internet-facing listener is using an unecrypted protocol (eg: NOT HTTPS, SSL, or TLS) an incident report will show for the listener and an email will be sent to the user-specified email address.

Note: Elastic Load Balancing (ELB) supports three types of load balancers: Classic Load Balancers, Application Load Balancers, and Network Load Balancers. There is a separate policy for Application and Network Load Balancers with unencrypted internet-facing listeners.

## Functional Details

The policy leverages the AWS elasticloadbalancing API to examine listener details. When an unencrypted internet-facing listener is detected, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- *Allowed Regions* - A list of allowed regions for an AWS account. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS and enter the region code. If SCP is enabled for an AWS account, then enter only the enabled regions if in case disabled regions are entered then the policy will throw an error. If this field is left blank, then the policy evaluates all the regions fetched using the **DescribeRegions** API call.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - CLB with any of these tags will be ignored

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":["elasticloadbalancing:DescribeLoadBalancers",
              "elasticloadbalancing:DescribeTags"],
    "Resource":"*"
    },
    {
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
