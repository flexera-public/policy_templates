# Azure Ensure No Custom Subscription Owner Roles

## What it does

This policy checks all existing role definitions for any that are at a global or subscription level and grant full "*" access. If any such role definitions are found, an incident is raised with a list of the offending role definitions and their details.

## Functional Details

A list of subscriptions is obtained via the Azure REST API. A separate list is then obtained of role definitions for each subscription. Those role definitions are checked for whether they are at the global "/" or subscription level, and whether any of their actions are a simple "*", granting broad access across the platform. Role definitions that have the type "BuiltInRole" are ignored.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequesites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/read
- Microsoft.Authorization/roleDefinitions/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
