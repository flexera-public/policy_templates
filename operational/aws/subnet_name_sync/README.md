# AWS Subnet Name Tag Sync Policy Template

## What it does

This Policy Template is used to automatically synchronize the AWS Subnet names to Cloud Management.
When applied, the policy will iterate through all VPCs in all AWS regions and ensure the matching subnet reference in Cloud Management has the correct name.

## Functional Details

This policy performs the following action:
- Synchronizes AWS Subnet names to Subnets in Cloud Management

## Input Parameters

This policy has the following input parameter required when launching the policy.

- Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Subnet name in Cloud Management updated to match Subnet name in AWS

## Prerequisites

- This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials from the list for your tenant. If such credential doesn't exist please contact your  cloud admin to create the Credential.
- The credential must contain the value *AWS* in the Provider field. Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe AWS Subnets and tags.
The IAM user will require the following permissions:

```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeSubnets",
              "ec2:DescribeTags"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
