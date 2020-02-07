# Google Long-Stopped Instances

## What it does

This policy checks all Google instances that are stopped and reports on any that have been stopped for more than a specified period of time. The user is given the option to Terminate the instance after approval.

## Functional Details

The policy leverages the Google API to check all instances that have been stopped for longer than the specified period. If the action is approved, the instance is terminated.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Stopped days* - Number of days an instance is stopped before it is added to the report

## Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete all instances after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `Monitoring Viewer` Role
- The `compute.instances.delete` permission
- The `compute.instances.list`  permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.