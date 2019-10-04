## Google Open Buckets Policy Template

### What it does

This Policy Template will check your account for Google Cloud Storage buckets with public permission.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Email to alert when it finds google buckets that meet the criteria
- *Google Cloud Project* - The Google Cloud Project to run this policy against.

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (credentials).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - credential_viewer or admin
- Cloud Management - Observer

### Google Required Permissions

- storage.buckets.list
- storage.buckets.getIamPolicy2

### Supported Clouds

- Google

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
