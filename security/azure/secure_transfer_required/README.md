# Azure Storage Accounts Without Secure Transfer

## What it does

This policy checks all Azure storage accounts to ensure that they are configured to require secure transfer. An incident is raised with the offending storage accounts if any are found that don't.

## Functional Details

The Azure Resource Manager API is used to get a list of subscriptions. This list is then used to query the "/providers/Microsoft.Storage/storageAccounts" endpoint iteratively to gather the relevant metadata for each storage account.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/read
- Microsoft.Storage/storageAccounts/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
