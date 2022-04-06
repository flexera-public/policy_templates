# Azure Ensure Storage Account Default Network Access Set To Deny

## What it does

This policy checks all Azure storage accounts to verify that their default network access is set to "Deny". If any storage accounts are found where this is not the case, an incident is raised with a list of the affected accounts.

## Functional Details

The Azure Resource Manager API is used to get a list of subscriptions and storage accounts within those subscriptions. The policy then checks "properties.networkAcls.defaultAction" for each account to verify that it is set to "Deny".

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag values to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/read
- Microsoft.Storage/storageAccounts/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
