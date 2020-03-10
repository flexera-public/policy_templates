# Google Unutilized IP Addresses

## What it does

Checks Google for Unutilized IP Addresses and deletes them after approval.

## Functional Details

- This policy uses Google Cloud to get a list of IP addresses, internal and external, that are not in use.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Exclusion Label Key:Value* - A Google native label to ignore IP addresses that you don't want to consider for deletion

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