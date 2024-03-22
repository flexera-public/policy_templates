# Azure Storage Accounts without Lifecycle Management Policies

## What it does

This policy will look at a list of storage accounts and determine if lifecycle policies are enabled.

## Functional Details

This policy checks all the Storage Accounts for a Azure Subscription. If a storage account does not have lifecycle management policies enabled it will create and incident for it.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tag Key* - Cloud native tag key to ignore instances. Example: exclude_utilization
- *Email addresses* - Email addresses of the recipients you wish to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked
- *Azure API Wait Time* - Amount of time to wait between Azure API requests to avoid throttling (seconds)

## Actions

- Sends an email notification

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Storage/storageAccounts/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
