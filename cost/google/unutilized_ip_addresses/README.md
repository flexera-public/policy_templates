# Google Unutilized IP Addresses

## What it does

Checks Google for Unutilized IP Addresses and deletes them after approval.

## Functional Details

- If APIs & Services are not enabled for a project, the policy will skip that particular project. On the next run if APIs & Services are enabled, then the project will be considered for execution.
- This policy uses Google Cloud to get a list of IP addresses, internal and external, that are not in use.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Exclusion Label Key:Value* - A Google native label to ignore IP addresses that you don't want to consider for deletion
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete IP Addresses" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Sends an email notification
- Delete the IP Addresses after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `compute.addresses.delete` permission
- The `compute.addresses.list` permission
- The `compute.addresses.get` permission
- The `compute.regions.list` permission
- The `resourcemanager.projects.get` permission

## Supported Clouds

- Google

## Cost

This Policy Template does not incur any cloud costs.