## AWS VPC Name Tag Sync Policy Template

### What it does

This Policy Template is used to automatically synchronize the AWS VPC names to Cloud Management.
When applied, the policy will iterate through all VPCs in all AWS regions and ensure the matching network reference in Cloud Management has the correct name.

### Functional Details

This policy performs the following action:

- Synchronizes AWS VPC names to Networks in Cloud Management

### Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Network name in Cloud Management updated to match VPC name in AWS

### Cloud Management Required Permissions

This policy requires permissions to access Cloud Management resources; Clouds and Networks.  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or at the Organization level. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - observer
- Cloud Management - admin or credential_viewer
- Cloud Management - security_manager

### AWS Required Permissions

This policy requires permissions to describe AWS VPCs and tags.
The Cloud Management Platform automatically creates two Credentials when connecting AWS to Cloud Management; AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. The IAM user credentials contained in those credentials will require the following permissions:

```javascript
{
    "Version": "2012-10-17",
    "Statement":[{
    "Effect":"Allow",
    "Action":["ec2:DescribeVpcs",
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
