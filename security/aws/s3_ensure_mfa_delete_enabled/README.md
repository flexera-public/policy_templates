# AWS Ensure MFA Delete Enabled For S3 Buckets

## What it does

Adding MFA Delete to an S3 bucket requires additional authentication when you change the version state of your bucket or you delete an object version, adding another layer of security in the event your security credentials are compromised or unauthorized access is granted. This policy will raise an incident if any S3 Buckets are found on the account without MFA Delete enabled.

## Functional Details

The policy leverages the AWS S3 API to gather a list of S3 buckets on the account, their details, and whether they have MFA Delete enabled. When one or more S3 buckets are found without MDA Delete enabled, an email action is triggered automatically to notify the specified users of the incident. This email report contains a list of affected S3 buckets.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

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
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
              "sts:GetCallerIdentity",
              "s3:ListAllMyBuckets",
              "s3:GetBucketLocation",
              "s3:GetBucketVersioning"
            ],
            "Resource": "*"
        }
    ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
