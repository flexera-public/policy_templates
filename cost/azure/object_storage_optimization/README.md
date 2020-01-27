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

## Prerequesites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

## Supported Clouds

- Azure

## Cost

This policy does not incur any cloud costs.

## Notes

1.'Storage Blob Data Owner' permission need to be added for storage account to fetch the container/blobs list, before calling List Containers/List Blobs API's.
2.Enter 'Standard Type' storage account with account kind type as 'StorageV2 (general purpose v2) / BlobStorage' to search for blobs.
3.Blob with type 'PageBlob' or 'AppendBlob' will not support moving object to 'cool tier' and 'archive tier'.