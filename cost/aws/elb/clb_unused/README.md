# AWS Unused Classic Load Balancers (CLB)

## What it does

This policy checks all Classic Load Balancers (CLB) to determine if any are unused (have no healthy instances) and allows them to be deleted by the user after approval.

Note:Elastic Load Balancing (ELB) supports three types of load balancers: Application Load Balancers, Network Load Balancers and Classic Load Balancers.

### Policy savings details

The policy includes the estimated savings.  The estimated savings is recognized if the resource is terminated.   Optima is used to receive the estimated savings which is the product of the most recent full day’s cost of the resource * 30.  The savings is displayed in the Estimated Monthly Savings column.  If the resource can not be found in Optima the value is n/a.  The incident header includes the sum of each resource Estimated Monthly Savings in the Incident Header as Total Estimated Monthly Savings.
If the user is not having the minimum required role of `billing_center_viewer`, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as N/A in the incident table.

## Functional Details

The policy leverages the AWS elasticloadbalancing API to determine if the CLB is in use.

When an unused CLB is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to delete the CLB after manual approval if needed.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - CLB with any of these tags will be ignored
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Load Balancers" action while applying the policy, all the identified unused load balancers will get deleted.

## Policy Actions

- Sends an email notification.
- Delete unused CLB after approval.

## Prerequisites

- This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.
- billing_center_viewer (note: this role must be applied at the Organization level).

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
              "elasticloadbalancing:DescribeInstanceHealth",
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
