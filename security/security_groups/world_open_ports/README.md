# Security Group Rules with public ports

## What it does

This Policy Template reviews your security group and alerts if any security group rules are open to the public.  Deletion of the Security Group Rules only occur after approval.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Example: noreply@example.com
- *List of security groups allowed to have open ports to the world.* - a list of security groups to ignore.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Security Groups" action while applying the policy, all the security groups that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- After approval, delete the security group rules found to violate the policy.
- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, networks, security_groups and security_group_rules).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
