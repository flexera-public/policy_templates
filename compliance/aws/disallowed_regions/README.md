# AWS Disallowed Regions

## What it does

This policy checks all instances in a set of disallowed regions. The user is given the option to Terminate the instance after approval.

## Functional Details

- The policy leverages the AWS API to check all instances that exist in a disallowed region.
- When an EC2 instance in disallowed region is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to terminate instances after manual approval if needed.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Exclusion Tag* - List of tags that will exclude EC2 instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'.
- *Disallowed Regions(s)* - List of regions to disallow.

Note:Refer Region column under Amazon Elastic Compute Cloud (Amazon EC2) in below link for AWS supported regions \n See the [README](https://docs.aws.amazon.com/general/latest/gr/rande.html).

## Policy Actions

- Sends an email notification.
- Terminate reported instances after approval.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider: 
```javascript
{
  "Version": "2016-11-15",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ecs: DescribeInstances"],
    "Resource":"*"
    }
  ]
}
```

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
