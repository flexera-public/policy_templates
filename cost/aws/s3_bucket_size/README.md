# AWS Bucket Size Check Policy Template

## What it does

This Policy Template scans all S3 buckets in the given account and checks if the bucket exceeds a specified byte size provided as an input parameter. Bucket size is harvested via CloudWatch queries. If the a bucket exceeds the threshold, and incident report will show for the S3 buckets, and related information and an email will be sent to the user-specified email address.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Byte size to check (eg: 1000000000 = 1GB)* - enter the S3 bucket size threshold to trigger an incident.
- *Email Address* - Email addresses of the recipients you wish to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy requires the AWS IAM or AWS STS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Required AWS Permissions

This policy requires permissions to list of AWS S3 Buckets, the location of S3 Buckets as well as permissions to list Metrics and Get Metric Statistics from the AWS Cloudwatch API.

The AWS credentials will require the following permissions:

```javascript
{
  "Version": "2012-10-17",
  "Statement":[{
      "Effect":"Allow",
      "Action":["cloudwatch:GetMetricStatistics","cloudwatch:ListMetrics"],
      "Resource":"*",
      "Condition":{
         "Bool":{
            "aws:SecureTransport":"true"
            }
         }
      }
   ]
}

{
  "Version": "2006-03-01",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListAllMyBuckets",
        "s3:GETBucketlocation",
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
