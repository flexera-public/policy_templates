# AWS Unencrypted Volumes

## What it does

This policy checks all Elastic Block Store (EBS) volumes in a given account and reports on any that are not encrypted.

## Functional Details

The policy leverages the AWS EC2 API to determine volume encryption settings.

## Input Parameters

- Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- Ignore tags* - EBS volumes with any of these tags will be ignored
 
## Policy Actions

- Send an email report

## Prerequisites

- This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.
- The credential must contain the value *AWS* in the Provider field. Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe EBS volumes.
The IAM user will require the following permissions:

```javascript
{
    "Version": "2016-11-15",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeVolumes"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.