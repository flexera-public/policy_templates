# AWS Unused RDS Policy

## What it does

This policy template checks for Unused RDS instances by reviewing the DBconnections and terminates them after user approval.

## Functional Details

- This policy gets's a list of RDS instances and uses CloudWatch DBConnection metric to check for connections over a 30 day period.  If there are no DBConnections the policy will terminate the RDS instance after the user approval.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key:Value* - AWS tag key to ignore instances. Format: Key:Value

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- decommissions AWS RDS instances after approval.

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
```

## Supported Clouds

- Amazon

## Cost

This Policy Template does not incur any cloud costs.
