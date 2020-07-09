# Azure Blob Storage Optimization

## What it does

This Policy checks Azure Blob Storage for older objects and can move old object to the Cool or Archive tier after a given period of time.

## Functional Details

- This policy identifies all Azure Blob Storage objects last modified outside of the specified timeframe
- For all objects identified as old, the user can choose to move the object to Cool or Archived tiers after user approval

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Storage Account* - Name of Storage account to search for blobs
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Move to Cool tier after days last modified* - leave blank to skip moving
- *Move to Archive tier after days last modified* - leave blank to skip moving
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Modify Blob storage" action while applying the policy, all the identified older objects can be moved to Cool or Archive tier.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Storage Blob Data Owner

## Supported Clouds

- Azure

## Cost

This policy does not incur any cloud costs.

## Notes

1. 'Storage Blob Data Owner' permission need to be added for storage account to fetch the container/blobs list, before calling List Containers/List Blobs API's.
1. Enter 'Standard Type' storage account with account kind type as 'StorageV2 (general purpose v2) / BlobStorage' to search for blobs.
1. Blob with type 'PageBlob' or 'AppendBlob' will not support moving object to 'cool tier' and 'archive tier'.
