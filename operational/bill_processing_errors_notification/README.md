# Bill Processing Error Notification

## What it does

Collects all bill connects and raises an incident for any in an error state.

## Functional Details

This policy collects all bill connects, checks the state of each bill connect, compares when the bill was downloaded versus the policy execution time. If there is an error or the processing time exceeds 24 hours, it will raise an incident

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Hours Processing* - Number of hours between downloading and processing complete to be reported

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Required Permissions

This policy requires permissions to access Flexera Applied Policies resources.  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Access Management](https://docs.flexera.com/flexera/EN/Administration/flexeraroles.htm#accessmanagement_1179969751_1147018)

- View policies
- Manage Organization

## Supported Clouds

- NA

## Cost

This Policy Template does not incur any cloud costs.
