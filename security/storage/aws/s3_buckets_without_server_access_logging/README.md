## AWS S3 Buckets without Server Access Logging

### What it does

This policy checks for any S3 buckets that don't have Server Access logging enabled and allows the user to enable logging after approval.

### Functional Details
The policy leverages the AWS S3 API to find all buckets and check for any that don't have Server access logging enabled. Optionally, after approval, the policy can configure logging on any S3 bucket.  Use the Target Bucket input parameter to configure logging to an existing bucket.  If you Target Bucket is left blank a new bucket is creating using the source bucket name as the prefix and logging as the suffix, i.e. mybucket-logging

*Note:* Logs can only be written to buckets in the same region, if this policy errors on setting the logging attribute, it will skip. You need 1 policy and bucket for every region. 

#### Input Parameters
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Target Bucket* - An existing bucket in same reason as source to be used for logging.  
- *Target Bucket Prefix* - If using a Target Bucket, this element lets you specify a prefix for the keys that the log files will be stored under.
- *Exclude Target Bucket* - Exclude target bucket as additional fees may incur. 

### Required RightScale Roles
- credential_viewer or admin

### AWS Required Permissions

This policy requires permissions to describe AWS Buckets, and to Get/Put bucket logging options.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

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

### Supported Clouds
- AWS

### Cost
This Policy Template does not incur any cloud costs.
