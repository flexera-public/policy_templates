##  AWS Disallowed Regions

### What it does

This policy checks all instances in a set of disallowed regions. The user is given the option to Terminate the instance after approval.

### Functional Details

- The policy leverages the AWS API to check all instances that exist in a disallowed region.
- When an EC2 instances in disallowed region is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to terminate instances after manual approval if needed.

### Input Parameters
 
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Exclusion Tag* - List of tags that will exclude EC2 instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'.
- *Disallowed Regions(s)* - List of regions to disallow.Multiple regions are separated by a comma. Example: 'us-east-1,us-west-1'.
Note: Refer Region column under Amazon Elastic Compute Cloud (Amazon EC2) in below link for AWS supported regions \n See the [README](https://docs.aws.amazon.com/general/latest/gr/rande.html). 

### Actions

- Sends an email notification.
- Terminate reported instances after approval.

### Required RightScale Roles
 
- policy_designer
- policy_manager
- policy_publisher
- credential_viewer

### AWS Required Permissions

This policy requires permissions to describe AWS ECS DescribeInstances.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

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

### Supported Clouds

- AWS

### Cost
 
This Policy Template does not incur any cloud costs.
