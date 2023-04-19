# Azure Ensure PostgreSQL Servers Sufficient Log Retention

## What it does

This policy checks all Azure PostgreSQL Servers to ensure that they have log retention configured for more than 3 days. An incident is raised with the offending PostgreSQL Servers if any are found that don't.

## Functional Details

The Azure Resource Manager API is used to get a list of subscriptions and PostgreSQL Servers within those subscriptions. The policy then checks the "log_retention_days" configuration endpoint for each server to verify that it has a value greater than 3.

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
- Microsoft.DBForPostgreSql/servers/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
