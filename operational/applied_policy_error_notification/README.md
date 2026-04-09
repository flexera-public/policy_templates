# Applied Policy Error Notification

## What it does

Collects all currently applied policies and raises an incident for any in an error state.

## Functional Details

This policy collects all currently applied policies and checks the state of the policies. If any are in `error` it will raise an incident and send an email.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Required Permissions

This policy requires permissions to access Flexera Applied Policies resources.  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Access Management](https://docs.flexera.com/flexera/EN/Administration/flexeraroles.htm#accessmanagement_1179969751_1147018)

- View policies

## Supported Clouds

- NA

## Cost

This Policy Template does not incur any cloud costs.
