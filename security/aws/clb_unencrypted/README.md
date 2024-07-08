# AWS Unencrypted ELB Listeners (CLB)

## Deprecated

This policy is no longer being updated. The [AWS Elastic Load Balancers With Unencrypted Listeners](https://github.com/flexera-public/policy_templates/tree/master/security/aws/elb_unencrypted/) policy now includes this functionality.

## What it does

Checks for unecrypted listeners on Classic Load Balancers. If an internet-facing listener is using an unecrypted protocol (eg: NOT HTTPS, SSL, or TLS) an incident report will show for the listener and an email will be sent to the user-specified email address.

Note: Elastic Load Balancing (ELB) supports three types of load balancers: Classic Load Balancers, Application Load Balancers, and Network Load Balancers. There is a separate policy for Application and Network Load Balancers with unencrypted internet-facing listeners.

## Functional Details

The policy leverages the AWS elasticloadbalancing API to examine listener details. When an unencrypted internet-facing listener is detected, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Ignore tags* - CLB with any of these tags will be ignored

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

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
