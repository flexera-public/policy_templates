# AWS VPC Name Tag Sync

## What it does

This Policy Template is used to automatically synchronize the AWS VPC names to Cloud Management.
When applied, the policy will iterate through all VPCs in all AWS regions and ensure the matching network reference in Cloud Management has the correct name.

## Functional Details

This policy performs the following action:

- Synchronizes AWS VPC names to Networks in Cloud Management

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Network name in Cloud Management updated to match VPC name in AWS

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

## AWS Required Permissions

This policy requires permissions to describe AWS VPCs and tags.
The IAM user will require the following permissions:

```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeVpcs",
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
