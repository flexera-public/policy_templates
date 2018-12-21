## Security Group with High Open Ports Policy Template

### What it does

This Policy Template leverages the multi cloud RightScale API. It will notify only if a security group has a port higher than `Beginning High Port` field open.

### Parameters

1. Email addresses of the recipients you wish to notify - Example: noreply@example.com
2. Beginning High Port - Any port greater than or equal to this will trigger a report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, networks, security_groups and security_group_rules).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

### Supported Clouds

- AWS
- Azure
- Google

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
