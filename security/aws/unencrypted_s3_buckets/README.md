# AWS Unencrypted S3 Buckets

## What it does

This policy checks all S3 buckets in the AWS account and reports on any that do not have default encryption set. When an unencrypted S3 bucket is detected, the user can choose to enable default encryption (AES-256) after approval and the user can also choose to delete the unencrypted S3 Buckets by enabling 'delete action' as mentioned in Enable delete action section below after approval.

## Functional Details

The policy leverages the AWS API to determine the encryption settings for each S3 bucket.

When an unencrypted bucket is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have an option to modify configuration after manual approval, and even Users can perform delete action if required.

encrypt - modifies the configuration of the unencrypted S3 Bucket by enabling the Default encryption i.e. AES-256

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude resources from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'

## Policy Actions

Perform below steps to enable delete action.

- Edit the pt file in this location [AWS_Unencrypted_S3_Buckets] <https://github.com/flexera/policy_templates/tree/master/security/aws/unencrypted_s3_buckets>
- uncomment below mentioned line

```javascript
   escalate $delete_unencrypted_s3_buckets_approval
```

- upload the modified file and apply the policy.

## Prerequisites

- This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.
- The credential must contain the value *AWS* in the Provider field. Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to list of AWS S3 Buckets, location of S3 Buckets, tagging S3 Buckets, encryption of S3 Buckets, modify unencrypted S3 Buckets and delete unencrypted S3 Buckets.
The IAM user will require the following permissions:

```javascript
{
  "Version": "2006-03-01",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListAllMyBuckets",
        "s3:GETBucketlocation",
        "s3:GETBucketencryption",
        "s3:GETBuckettagging",
        "s3:PUTBucketencryption",
        "s3:DELETEBucket"
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
