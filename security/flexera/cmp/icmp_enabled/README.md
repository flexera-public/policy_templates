# Security Groups with ICMP Enabled

## Deprecated

This policy is no longer being updated.

## What It Does

This Policy Template reviews your security group and alerts if any security group have ICMP types `0,3,8` enabled.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - Example: noreply@example.co

## Policy Actions

This policy has the following input parameters required when launching the policy.

- Send an email report

## Required Permissions

This policy requires permissions to access RightScale resources (clouds, networks and security_groups).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Observer

## Supported Clouds

- AWS
- Azure
- Google

## Cost

This policy template does not incur any cloud costs.
