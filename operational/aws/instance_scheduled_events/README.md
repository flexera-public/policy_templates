# AWS Instance Scheduled Events

## What it does

This policy checks for any scheduled event on EC2 instances that could cause operational issues, such as an instance reboot, stop, retirement, system reboot and system maintenance.

## Functional Details

The policy leverages the AWS EC2 API to discover any scheduled events on EC2 instances and provides the details in a report emailed to the specified users.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude resources from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
for connecting to the cloud -- in order to apply this policy you must have a
 credential registered in the system that is compatible with this policy. If
 there are no credentials listed when you apply the policy, please contact your
 cloud admin and ask them to register a credential that is compatible with this
  policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html)
to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

```javascript
{
  "Version": "2012-10-17",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ec2:DescribeInstanceStatus",
            "ec2:DescribeTags",
            "ec2:DescribeRegions"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
