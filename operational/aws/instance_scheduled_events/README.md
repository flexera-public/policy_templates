# AWS Instance Scheduled Events

## What it does

This policy checks for any scheduled event on EC2 instances that could cause operational issues, such as an instance reboot, stop, retirement, system reboot and system maintenance.

## Functional Details

The policy leverages the AWS EC2 API to discover any scheduled events on EC2 instances and provides the details in a report emailed to the specified users.

## Input Parameters

- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Tags to ignore* - List of tags that will exclude resources from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm)
for connecting to the cloud -- in order to apply this policy you must have a
credential registered in the system that is compatible with this policy. If
there are no credentials listed when you apply the policy, please contact your
cloud admin and ask them to register a credential that is compatible with this
policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm)
to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`, `aws_sts`

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
