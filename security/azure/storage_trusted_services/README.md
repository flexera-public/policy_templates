# Azure Ensure Trusted Microsoft Services Enabled

## What it does

This policy checks all Azure storage accounts to ensure that they allow access from Trusted Microsoft Services. If any are found that do not, an incident is raised with a list of the affected storage accounts.

## Functional Details

The Azure Resource Manager API is used to get a list of subscriptions and storage accounts within those subscriptions. The policy then checks the "properties.networkAcls.bypass" field to make sure that "AzureServices" is listed there.

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
