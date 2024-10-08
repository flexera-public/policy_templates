# Azure Resources with public IP address

## Deprecated

This policy is no longer being updated.

## What It Does

This policy checks all the resources in the Azure Subscription with a public IP address, so that those IP's can be removed.

## How It Works

The policy leverages the Azure API to identify the resources that have public IP address associated with them and them produces the report of these instances.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Network/publicIPAddresses

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
