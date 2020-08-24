# AWS Unencrypted Volumes

## What it does

This policy checks all Elastic Block Store (EBS) volumes in a given account and reports on any that are not encrypted.

## Functional Details

The policy leverages the AWS EC2 API to determine volume encryption settings.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - EBS volumes with any of these tags will be ignored

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
    "Action":["ec2:DescribeVolumes",
                "ec2:DescribeRegions"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
