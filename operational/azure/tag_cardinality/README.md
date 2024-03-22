# Azure Tag Cardinality Report

## What it does

This Policy Template is used to generate a tag cardinality (how many unique values each tag key has) report for Azure, along with a list of those unique values for each tag key. The report includes cardinality for all tag values for Azure Subscriptions, Resource Groups, and Resources.

## Functional Details

This policy performs the following action:

- Connect to the Azure Resource Manager API to get a list of Azure Subscriptions, Resource Groups, and Resources, along with their tags.

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked

## Policy Actions

This read-only policy is purely for reporting purposes and takes no action.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/resources/read`
  - `Microsoft.Resources/subscriptions/providers/read`
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.Resources/resourceGroups/read`
  - `Microsoft.Resources/tags/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
