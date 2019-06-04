## AWS Unencrypted Volumes

### What it does
This policy checks all Elastic Block Store (EBS) volumes in a given account and reports on any that are not encrypted.
 
### Functional Details
 
The policy leverages the AWS EC2 API to determine volume encryption settings.
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Ignore tags* - EBS volumes with any of these tags will be ignored 
 
### Required RightScale Roles
 
- policy_manager
- admin or credential_viewer

### AWS Required Permissions

This policy requires permissions to describe EBS volumes.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
    "Version": "2016-11-15",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeVolumes"],
    "Resource":"*"
    }
  ]
}
```
 
### Supported Clouds
 
- AWS

### Cost
 
This Policy Template does not incur any cloud costs.