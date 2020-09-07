# AWS Unused RDS Policy

## What it does

This policy template checks for Unused RDS instances by reviewing the DBconnections and terminates them after user approval.

## Functional Details

- This policy gets a list of RDS instances and uses CloudWatch DBConnection metric to check for connections over a 30 days period.  If there are no DBConnections the policy will terminate the RDS instance after the user approval.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day's cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource cannot be found in Optima the value is N/A. The incident message detail includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.
If the user is not having the minimum required role of `billing_center_viewer`, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as N/A in the incident table.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key:Value* - AWS tag key to ignore instances. Format: Key:Value
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- delete AWS RDS instances after approval.

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
      "Action":["cloudwatch:GetMetricStatistics","cloudwatch:ListMetrics"],
      "Resource":"*",
      "Condition":{
         "Bool":{
            "aws:SecureTransport":"true"
            }
         }
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

This Policy Template does not incur any cloud costs.
