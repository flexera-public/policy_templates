# Security Group with High Open Ports Policy Template

## Deprecated

This policy is no longer being updated.

## What It Does

This Policy Template leverages the multi cloud RightScale API. It will notify only if a security group has a port higher than `Beginning High Port` field open.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Example: noreply@example.com
- *Beginning High Port* - Any port greater than or equal to this will trigger a report

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Required Permissions

This policy requires permissions to access RightScale resources (clouds, networks, security_groups and security_group_rules).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

## Supported Clouds

- AWS
- Azure
- Google

### Cost

This policy template does not incur any cloud costs.
