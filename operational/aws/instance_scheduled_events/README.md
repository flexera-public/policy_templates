## AWS Instance Scheduled Events

### What it does
This policy checks for any scheduled event on EC2 instances that could cause operational issues, such as an instance reboot, stop, retirement, system reboot and system maintenance.
 
### Functional Details
 
The policy leverages the AWS EC2 API to discover any scheduled events on EC2 instances and provides the details in a report emailed to the specified users.
 
### Input Parameters
 
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Tags to ignore* - List of tags that will exclude resources from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer

### AWS Required Permissions

This policy requires permissions to describe AWS EC2 instance status, list EC2 tags.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
  "Version": "2016-11-15",
  "Statement":[{
  "Effect":"Allow",
  "Action":["ec2:DescribeInstanceStatus",
            "ec2:DescribeTags"],
    "Resource":"*"
    }
  ]
}
```
 
### Supported Clouds
 
- AWS
 
### Cost
 
This Policy Template does not incur any cloud costs.
