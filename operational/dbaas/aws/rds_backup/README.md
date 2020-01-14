# AWS RDS Backup

## What it does

This Policy Template will check your account for Amazon RDS Instances with non-compliant backup settings.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Email to alert when it finds S3 buckets that meet the criteria.
- *Backup Retention Period* - Example value: `7`
- *Preferred Backup Window* - Example value: `08:00-08:30`

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy requires the AWS Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## AWS Required Permissions

This policy requires permissions to describe AWS RDS DescribeDBInstances.
The AWS credentials will require the following permissions:

```javascript
{
   "Version":"2014-09-01",
   "Statement":[
      {
         "Sid":"AllowRDSDescribe",
         "Effect":"Allow",
         "Action":"rds:DescribeDBInstances",
         "Resource":"*"
      }
   ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
