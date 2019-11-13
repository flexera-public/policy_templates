## Long-Stopped Instances

### What it does

This policy checks all instances that are stopped and reports on any that have been stopped for more than a specified period of time. The user is given the option to Terminate the instance after approval.

### Functional Details

The policy leverages the AWS API to check all instances that have been stopped for longer than the specified period. If the action is approved, the instance is terminated.

### Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Exclusion Tag* - List of tags that will exclude EC2 instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'.
- *Stopped days* - Number of days an instance is stopped before it is added to the report.

### Actions

- Sends an email notification.
- Terminate reported instances after approval.

### Cloud Management Required Permissions/AWS Required Permissions

- Cloud Management - The `credential_viewer`, `policy_designer`, `policy_manager` & `policy_publisher` roles
- AWS - The `CloudWatchReadOnlyAccess` AWS IAM Policy

### AWS Required Permissions

This policy requires permissions to describe AWS ECS DescribeInstances and Get Metric Statistics from the AWS Cloudwatch API.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
  "Version": "2016-11-15",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ec2: DescribeInstances"],
    "Resource":"*"
    }
  ]
}
```

```javascript
{
  "Version": "2010-08-01",
  "Statement":[{
      "Effect":"Allow",
      "Action":["cloudwatch:GetMetricStatistics"],
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

- AWS

### Cost

This Policy Template does not incur any cloud costs.