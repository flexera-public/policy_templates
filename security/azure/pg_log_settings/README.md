# Azure Ensure Correct PostgreSQL Servers Log Settings

## What it does

This policy checks all Azure PostgreSQL Servers to ensure that they have proper log settings enabled. An incident is raised with the offending PostgreSQL Servers if any are found that don't.

## Functional Details

The Azure Resource Manager API is used to get a list of subscriptions and PostgreSQL Servers within those subscriptions. The policy then checks the configuration endpoint for the Log Setting parameter to verify that it is turned on.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Log Setting* - Log setting to check the status of
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag values to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/read
- Microsoft.DBForPostgreSql/servers/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
