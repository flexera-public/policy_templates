# AWS S3 Ensure Bucket Policies Deny HTTP Requests

## What it does

By default, Amazon S3 allows both HTTP and HTTPS requests. In order to only allow HTTPS requests, HTTP requests must be explicitly denied via a bucket policy. This policy will raise an incident if any S3 Buckets are found on the account without policies that explicitly deny HTTP requests.

## Functional Details

The policy leverages the AWS S3 API to gather a list of S3 buckets on the account, their details, and whether they have policies that deny HTTP requests. When one or more S3 buckets are found either without any policy or with a policy that does not deny HTTP requests, an email action is triggered automatically to notify the specified users of the incident. This email report contains a list of affected S3 buckets along with whether the bucket has no policy at all or a policy that does not deny HTTP requests.

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
              "s3:GetBucketPolicy"
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
