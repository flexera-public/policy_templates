# Azure Resources with public IP address

## What it does

This policy checks all the resources in the Azure Subscription with a public IP address.

## Functional Details

The policy leverages the Azure API to identify the resouces that have public IP address associated with them and them produces the report of these instances.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Network/publicIPAddresses

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
