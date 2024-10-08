# Azure Blob Storage Optimization

## What It Does

This policy checks Azure storage containers for blobs to move to the 'Cool' or 'Archive' storage tiers based on blob age. The user can opt to either delete the blobs or move them to the recommended storage tier.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Storage Account List* - A list of Azure Storage Accounts to assess blobs in. Leave blank to assess blobs in all accounts.
- *Allow/Deny Subscriptions* - Allow or Deny entered Subscriptions to filter results.
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. Leave blank to check all Subscriptions.
- *Allow/Deny Regions* - Allow or Deny entered regions to filter results.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Leave blank to check all Subscriptions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *New Storage Tier* - Whether to move blobs to Cool or Archive if they meet the specified age thresholds. Select 'Both' to consider moving blobs to either one based on the specified age thresholds
- *Cool Age Threshold (Days)* - Time in days since blob was last modified to change storage tier to Cool. Not applicable if 'Archive' is selected for New Storage Tier.
- *Archive Age Threshold (Days)* - Time in days since blob was last modified to change storage tier to Archive. Not applicable if 'Cool' is selected for New Storage Tier.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Blobs" action while applying the policy, all of the blobs that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Change object storage tier after approval
- Delete object after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Storage/storageAccounts/read`

- [**Azure Storage Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121576) (*provider=azure_storage*). Note that a credential can be made with access to several storage accounts by setting `resource` to `https://storage.azure.com` in the Additional Parameters when creating this credential in Flexera One. This credential should have the following permissions for every storage account whose blobs you want to assess:
  - `Storage Blob Data Owner`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
