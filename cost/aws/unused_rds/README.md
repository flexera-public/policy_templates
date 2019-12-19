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

This policy requires the AWS IAM User Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *AWS* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Required Permissions

### Required RightScale Roles

- policy_designer
- policy_manager
- policy_publisher
- credential_viewer
- observer

### AWS Required Permissions

This policy requires permissions to list Metrics and Get Metric Statistics from the AWS Cloudwatch API.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

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
