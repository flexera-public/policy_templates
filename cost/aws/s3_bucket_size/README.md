# AWS Bucket Size Check

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

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

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
