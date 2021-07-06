# Azure Storage Accounts without Lifecycle Management Policies

## What it does

This policy will look at a list of storage accounts and determine if lifecycle policies are enabled.

## Functional Details

This policy checks all the Storage Accounts for a Azure Subscription. If a storage account does not have lifecycle management policies enabled it will create and incident for it.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tag Key* - Cloud native tag key to ignore instances. Example: exclude_utilization
- *Email addresses* - Email addresses of the recipients you wish to notify

## Actions

- Sends an email notification

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Storage/storageAccounts/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
