## AWS Unused RDS Policy

### What it does

This policy template checks for Unused RDS instances by reviewing the DBconnections and terminates them after user approval.

### Functional Details

- This policy gets's a list of RDS instances and uses CloudWatch DBConnection metric to check for connections over a 30 day period.  If there are no DBConnections the policy will terminate the RDS instance after the user approval.

#### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Exclusion Tag Key* - A RDS tag to exclude from the instance list. Example: mytag:value

### Cloud Management Required Permissions/AWS Required Permissions
- Cloud Management - The `credential_viewer`,`observer` roles
- Cloud Management - The `policy_designer`, `policy_manager` & `policy_publisher` roles
- AWS - The `CloudWatchReadOnlyAccess` AWS IAM Policy

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

### Supported Clouds

- Amazon

### Cost

This Policy Template does not incur any cloud costs.
