# AWS Lambda Functions with high error rate

## What it does

Checks for lambda functions with errors, and lambda function over the `Error Rate Percentage` will be reported on.

## Functional Details

The policy leverages the AWS ec2 API to examine vpc and flowlog details. When a vpc without flowlogs enabled is detected, an email action is triggered automatically to notify the specified users of the incident.

## Input Parameters

- *Allowed Regions* - A list of allowed regions for an AWS account. Please enter the allowed regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Error Rate Percentage* - Items above this percentage will be reported on. `Number Only!`
- *Ignore tags* - Lambda Functions with any of these tags will be ignored

## Policy Actions

- Send an email report

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws` , `aws_sts`

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
```

```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":["lambda:ListFunctions"],
    "Resource":"*"
    },
    {
      "Effect":"Allow",
      "Action":["ec2:DescribeRegions"],
      "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
