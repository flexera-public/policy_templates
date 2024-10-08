# Azure HTTPs for Storage Accounts

## Deprecated

This policy is no longer being updated. The [Azure Storage Accounts Without Secure Transfer](https://github.com/flexera-public/policy_templates/tree/master/security/azure/secure_transfer_required/) policy now includes this functionality.

## What It Does

This Policy checks for Azure Storage Accounts with HTTPs not enforced.

## How It Works

- This Policy identifies all Azure Storage Accounts where the property `supportsHttpsTrafficOnly` is set to false.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Storage Account List

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
