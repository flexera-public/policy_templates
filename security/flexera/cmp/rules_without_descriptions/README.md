# Security Group Rules without Descriptions Policy Template

## Deprecated

This policy is no longer being updated.

## What It Does

This Policy Template reviews your security group and alerts if any security group rules do not have descriptions. It will resolve when all security group rules have descriptions.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Example: noreply@example.co

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

## Cost

This policy template does not incur any cloud costs.
