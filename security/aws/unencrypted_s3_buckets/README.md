## AWS Unencrypted S3 Buckets
 
### What it does
This policy checks all S3 buckets in the AWS account and reports on any that do not have default encryption set. When an unencrypted S3 bucket is detected, the user can choose to enable default encryption (AES-256) after approval and the user can also choose to delete the unencrypted S3 Buckets by enabling 'delete action' as mentioned in Enable delete action section below after approval.
 
### Functional Details
 
The policy leverages the AWS API to determine the encryption settings for each S3 bucket.
 
When an unencrypted bucket is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have an option to modify configuration after manual approval, and even Users can perform delete action if required.

* encrypt - modifies the configuration of the unencrypted S3 Bucket by enabling the Default encryption i.e. AES-256
 
### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - S3 Buckets with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer
 
### AWS Required Permissions

This policy requires permissions to list of AWS S3 Buckets, location of S3 Buckets, tagging S3 Buckets, encryption of S3 Buckets, modify unencrypted S3 Buckets and delete unencrypted S3 Buckets.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

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

### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.

### Enable delete action

Perform below steps to enable delete action.

- Edit the file [AWS_Unencrypted_S3_Buckets](https://github.com/rightscale/policy_templates/tree/master/security/aws/unencrypted_s3_buckets/AWS_Unencrypted_S3_Buckets.pt)
- uncomment below mentioned line
```javascript
   escalate $delete_unencrypted_s3_buckets_approval	
```	
- upload the modified file and apply the policy.



