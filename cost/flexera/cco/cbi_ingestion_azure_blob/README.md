# Common Bill Ingestion from Azure Blob Storage

## What It Does

This policy template uploads a file containing cloud costs from Azure Blob Storage into the Flexera Cloud Cost Optimization (CCO) platform via [Common Bill Ingestion](https://docs.flexera.com/flexera/EN/Optima/OptimaBillConnectConfigsCBI.htm). Both [Common Bill Ingestion Format](https://docs.flexera.com/flexera/EN/Optima/OptimaBillConnectConfigsCBIDefaultFormat.htm) and [FOCUS Format](https://docs.flexera.com/flexera/EN/Optima/FOCUS.htm) are supported. Optionally, an email is sent indicating that this has happened.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when billing data is uploaded
- *Billing Month* - Month to upload costs for. Select `Specific Month` to specify a month.
- *Specific Month* - Month to upload costs for in YYYY-MM format. Only relevant if `Specific Month` is selected for the Billing Month parameter.
- *CBI (Common Bill Ingestion) Endpoint Type* - Whether costs are being sent to an endpoint for [Common Bill Ingestion Format](https://docs.flexera.com/flexera/EN/Optima/OptimaBillConnectConfigsCBIDefaultFormat.htm) or [FOCUS Format](https://docs.flexera.com/flexera/EN/Optima/FOCUS.htm).
- *CBI (Common Bill Ingestion) Endpoint ID* - The ID of CBI endpoint to create/use for ingested costs. Leave blank to have this generated and managed automatically. Ex: cbi-oi-optima-laborcosts
- *Cloud Vendor* - The value the fixed cost should have for the `Cloud Vendor` dimension in Flexera CBI. Only has an effect when the CBI endpoint is first created. This is because the `Cloud Vendor` dimension isn't based on billing data but is configured for the CBI endpoint itself.
- *Azure Blob Storage Hostname* - The hostname for the Azure Blob Storage container that stores the costs. Ex: billing-files.blob.core.windows.net
- *Azure Blob Storage Path/Prefix* - The path and prefix for the name of the object in the Azure Blob Storage container. The actual objects should always have the year and month in YYYY-MM format at the end of the object name along with the ".csv" file extension.
  - For example, if you set this parameter to `bills/labor-costs-`, the object with the costs for October 2024 should be named `bills/labor-costs-2024-10.csv`

## Policy Actions

- Uploads stored billing data to Flexera CCO
- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Storage Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121576) (*provider=azure_storage*). Note that a credential can be made with access to several storage accounts by setting `resource` to `https://storage.azure.com` in the Additional Parameters when creating this credential in Flexera One. This credential should have the following permissions for the storage account with the cost data:
  - `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_bill_upload_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- All

## Cost

This Policy Template does not incur any cloud costs
