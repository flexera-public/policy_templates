# Azure Ensure MySQL Flexible Servers Use Secure TLS

## What it does

This policy checks all Azure MySQL Flexible Servers to ensure that they only allow the use of secure TLS versions. An incident is raised with the offending MySQL Flexible Servers if any are found that don't.

## Functional Details

The Azure Resource Manager API is used to get a list of subscriptions and MySQL Flexible Servers within those subscriptions. The policy then checks the configuration endpoint "tls_version" for each server to verify the TLS versions allowed are secure.

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
- Microsoft.DBforMySQL/flexibleServers/read
- Microsoft.DBforMySQL/flexibleServers/configurations/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
