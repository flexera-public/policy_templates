# Azure HTTPs for Storage Accounts

## What it does

This Policy checks for Azure Storage Accounts with HTTPs not enforced.

## Functional Details

- This Policy identifies all Azure Storage Accounts where the property `supportsHttpsTrafficOnly` is set to false.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

Please create separate credentials for each storage account by selecting Credential Type as OAuth2 and mention the storage account name in the Additional Parameters resource URL.
Example resource : `https://my_azure_storage_account.blob.core.windows.net/` , replace my_azure_storage_account with the name of the storage account.

For more details, please refer [API Usage](https://docs.rightscale.com/policies/users/guides/credential_management.html#provider-specific-credentials--azure--) to create Azure RM credentials with oauth2.

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Storage Account List

## Supported Clouds

- Azure

## Cost

This policy does not incur any cloud costs.
