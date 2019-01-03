## Unattached IP Addresses

### What it does

This Policy Template will check your account for unattached IP addresses and removes them with approval.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Whitelist of IP Addresses* - Ip addresses will be ignored

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Deletes the IP address with approval
- Send an email report



### Required Permissions

This policy requires permissions to access RightScale resources (clouds and ip_addresses).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

- AWS
- Azure RM

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
