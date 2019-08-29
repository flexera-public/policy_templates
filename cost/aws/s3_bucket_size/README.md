## AWS Bucket Size Check Policy Template

### What it does

This Policy Template scans all S3 buckets in the given account and checks if the bucket exceeds a specified byte size provided as an input parameter. Bucket size is harvested via CloudWatch queries. If the a bucket exceeds the threshold, and incident report will show for the S3 buckets, and related information and an email will be sent to the user-specified email address.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Byte size to check (eg: 1000000000 = 1GB)* - enter the S3 bucket size threshold to trigger an incident.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, volumes, deployments, placement groups and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

### Supported Clouds

- AWS

### Cost

This Policy Template does not incur any cloud costs.
