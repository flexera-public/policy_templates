# Azure Expiring Reserved Instances

## What it does

This Policy Template leverages the Optima Bill Data Azure Reserved Instances. It will notify only if expiration is within the time frame specified in `Number of days to prior to expiration date to trigger incident` field. It will email the user specified in Email addresses of the recipients you wish to notify.


## Required Permissions

This policy requires permissions to access RightScale resources (Optima).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied at the Organization level. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Optima - ca_user (at the organization level)

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Number of days to prior to expiration date to trigger incident* - Number of days before a RI expires to alert on

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
