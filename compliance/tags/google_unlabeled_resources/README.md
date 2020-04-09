# Google Unlabeled Resources

## What it does

This policy checks all GCP instances about missing tags for instances and volumes and reports on any that are missing these tags. The user can then enter the missing tags to apply to the selected resources after approval.

## Functional Details

The policy leverages the Google API to check all instances and volumes that have missing tags defined to check for. If the action is approved, the missing tags are being applied on selected resources.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *tags* - A list of tags to check for

## Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Apply the missing tags to all selected instances and volumes

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