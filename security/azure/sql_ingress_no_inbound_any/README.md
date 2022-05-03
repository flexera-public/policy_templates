# Azure Network Security Groups With Inbound RDP Open

## What it does

This policy checks all Azure subscriptions for SQL Servers that have an ingress firewall rule of 0.0.0.0/0. An incident is raised with the offending SQL Servers if any are found that do allow ingress from 0.0.0.0/0."

## Functional Details

This policy connects to the Azure Resource Manager API to get a list of SQL Servers and their firewall rule configurations. It then checks the rules field of each SQL Server to see if any rules all ingress from 0.0.0.0/0.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Sql/servers/read
- Microsoft.Sql/servers/firewallRules/*

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
