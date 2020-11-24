# AWS Internet-facing ELBs & ALBs

## What it does

This policy checks all load balancers (both Classic Load Balancers(ELBs) and Application Load Balancers(ALBs)) and reports on any that are internet-facing. When such a load balancer is detected, the user can choose to delete it after approval.

## Functional Details

When an internet-facing load balancer is detected, an email action is triggered automatically to notify the specified users of the incident. Users then can delete the load balancer after approval.

Using this may result in instances with no load balancers.

## Input Parameters

- *Allowed Regions* - A list of allowed regions for an AWS account. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS and enter the region code. If SCP is enabled for an AWS account, then enter only the enabled regions if in case disabled regions are entered then the policy will throw an error. If this field is left blank, then the policy evaluates all the regions fetched using the **DescribeRegions** API call.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude load Balancers from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or Key/value pairs can be listed. Example: 'test,env=dev'
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete ELBs and ALBs" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Sends an email notification.
- Delete Internet-facing ELB's & ALB's after approval.

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
    "Action":["elasticloadbalancing:DescribeLoadBalancers",
              "elasticloadbalancing:DescribeTags",
              "elasticloadbalancing:DeleteLoadBalancer"],
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
