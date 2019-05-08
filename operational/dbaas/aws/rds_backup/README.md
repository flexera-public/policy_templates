## AWS RDS Backup Policy Template

### What it does

This Policy Template will check your account for Amazon RDS Instances with non-compliant backup settings.


### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Email to alert when it finds S3 buckets that meet the criteria.
- *Backup Retention Period* - Example value: `7`
- *Preferred Backup Window* - Example value: `08:00-08:30`

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (credentials).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - credential_viewer or admin

### Supported Clouds

- AWS

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
