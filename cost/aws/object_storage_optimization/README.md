## AWS Object Storage Optimization
 
### What it does

This Policy checks S3 buckets for older objects and can move old object to 'glacier' or 'deep archive' after a given period of time. The user can choose to delete old object by enabling 'delete action' option as mentioned in Enable delete action section below.

### Functional Details
 
- This policy identifies all S3 objects last updated outside of the specified timeframe
- For all objects identified as old, the user can choose to move the object to Glacier or Glacier Deep Archive after the specified timeframe.
 
### Input Parameters
 
This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Move to Glacier after days last modified* - leave blank to skip moving
- *Move to Glacier Deep Archive after days last modified* - leave blank to skip moving
- *Exclude Tag* - exclude object with the included tags 
 
### Required RightScale Roles
 
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles

### Enable delete action

Perform below steps to enable delete action.

- Edit the file [AWS_Unencrypted_RDS_Instances](https://github.com/flexera/policy_templates/tree/master/cost/aws/object_storage_optimization/aws_object_storage_optimization.pt)
- uncomment the line which conatins 'escalate $esc_delete_s3_objects_approval' and save the changes.
- upload the modified file and apply the policy.

### AWS Required Permissions

This policy requires permissions to S3 bucket GET Service, GET Bucket location, GET Bucket (List Objects) Version 2, GET Object tagging, PUT Object - Copy, DELETE Object.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
  "Version": "2006-03-01",
  "Statement":[{
                "Effect":"Allow",
                "Action":["s3:ListAllMyBuckets",
                          "s3:GetBucketLocation",
                          "s3:ListBucket",
                          "s3:GetObject",
                          "s3:GetObjectTagging",
                          "s3:PutObject",
                          "s3:DeleteObject"
                         ],
                "Resource":"*"
              }]
}

```
Note: To get the list and modify S3-objects present in the S3 bucket, user must have READ and Write access to the bucket.

### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.
