## AWS AWS Elastic Load Balancer Encryption Check Policy Template

### What it does

Checks for unecrypted listeners on Classic, Network, and Application ELBs. If a listener is using an unecrypted protocol (eg: NOT HTTPS, SSL, or TLS) an incident report will show for the ELB listener and an email will be sent to the user-specified email address.

### Input Parameters

This policy has the following input parameters required when launching the policy.

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
