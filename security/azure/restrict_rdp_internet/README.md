# Azure Network Security Groups With Inbound 3389 Open

## What it does

This policy checks all Azure subscriptions for Network Security Groups that have 3389 open to the internet. An incident is raised with the offending Network Security Groups if any are found with port 3389 open."

## Functional Details

This policy connects to the Azure Resource Manager API to get a list of Network Security Groups. It then checks the rules field of each group to see if any rules are open inbound on port 3389

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
