# Azure Network Security Groups with inbound 3389 open

## What it does

This policy checks all azure subscriptions for Network Security Groups that have 3389 open to the internet.

## Functional Details

The policy leverages the Azure API to identify the network security groups which have port 3389 or a port range containing 3389 open to the internet and produces a report on them.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Network/networkSecurityGroups/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
