# AWS S3 Buckets without Server Access Logging

## What it does

This policy checks for any S3 buckets that don't have Server Access logging enabled and allows the user to enable logging after approval.

## Functional Details

The policy leverages the AWS S3 API to find all buckets and check for any that don't have Server access logging enabled. Optionally, after approval, the policy can configure logging on any S3 bucket.  Use the Target Bucket input parameter to configure logging to an existing bucket.  If you Target Bucket is left blank a new bucket is creating using the source bucket name as the prefix and logging as the suffix, i.e. mybucket-logging

*Note:* Logs can only be written to buckets in the same region, if this policy errors on setting the logging attribute, it will skip. You need 1 policy and bucket for every region.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Target Bucket* - An existing bucket in same reason as source to be used for logging.
- *Target Bucket Prefix* - If using a Target Bucket, this element lets you specify a prefix for the keys that the log files will be stored under.
- *Exclude Target Bucket* - Exclude target bucket as additional fees may incur.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Enable Bucket Logging" action while applying the policy, logging will be enabled for buckets.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Enable Server Access logging after approval.

*Note:* Logs can only be written to buckets in the same region, if this policy errors on setting the logging attribute, it will skip. You need 1 policy and bucket for every region.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```javascript
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListAllMyBuckets",
        "s3:PutBucketLogging",
        "s3:GetBucketLogging",
        "s3:ListBucket"
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