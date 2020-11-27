# AWS RDS Backup

## What it does

This Policy Template will check your account for Amazon RDS Instances with non-compliant backup settings.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS. If in case disabled regions are entered then the policy will throw an error. Leave blank to consider all the regions.
- *Email addresses of the recipients you wish to notify* - Email to alert when it finds S3 buckets that meet the criteria.
- *Backup Retention Period* - Example value: `7`
- *Preferred Backup Window* - Example value: `08:00-08:30`

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

Required permissions in the provider:

```javascript
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"AllowRDSDescribe",
         "Effect":"Allow",
         "Action":"rds:DescribeDBInstances",
         "Resource":"*"
      },
      {
        "Effect":"Allow",
        "Action":["ec2:DescribeRegions"],
        "Resource":"*"
    }]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
