# Common Bill Ingestion from Azure Blob Storage (Iterating)

## What It Does

This policy template uploads a file containing cloud costs from Azure Blob Storage into the Flexera Cloud Cost Optimization (CCO) platform via [Common Bill Ingestion](https://docs.flexera.com/flexera/EN/Optima/OptimaBillConnectConfigsCBI.htm). Both [Common Bill Ingestion Format](https://docs.flexera.com/flexera/EN/Optima/OptimaBillConnectConfigsCBIDefaultFormat.htm) and [FOCUS Format](https://docs.flexera.com/flexera/EN/Optima/FOCUS.htm) are supported. An incident is raised on every execution of the policy to provide status information to the user.

NOTE: Because of the complexities involved in this policy template, it is recommended for use only in situations where the standard [Common Bill Ingestion from Azure Blob Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cbi_ingestion_azure_blob) policy template is unable to handle the amount of data being processed for CBI.

## How It Works

- The policy uses the Azure Storage API to connect to the storage container containing the CSV files with cost data and obtain the relevant files for the specified month (or current month if none is specified.)
- The policy then sends those reports, unmodified, into a Flexera CBI endpoint so that they can be ingested and then visible on the platform.
- The policy does this over the course of multiple runs to avoid hitting memory and other constraints. **It is recommended that the default frequency of 15 minutes be used; the policy may not function correctly or as expected if a longer frequency is selected.**
- It is recommended that this policy be applied twice, with Month To Ingest set to Current Month for one instance and with it set to Previous Month for the other. This is to ensure that any changes made to billing data after the month ends are brought into the Flexera platform.

## Input Parameters

This policy template has the following input parameters required when launching the policy.

- *Month To Ingest* - Whether to process bills for the current month, previous month, or a specific month.
- *Billing Period* - The year and month to process bills for in YYYY-MM format. Only relevant if Specific Month is selected for the Month To Ingest parameter. Example: 2022-09
- *Flexera CBI Endpoint* - The name of the Flexera CBI endpoint to use. Example: cbi-oi-optima-laborcosts
- *Azure Blob Storage Hostname* - The hostname for the Azure Blob Storage container that stores the costs. Ex: billing-files.blob.core.windows.net
- *Azure Blob Storage Container* - The name of the Azure Blob Storage container that stores the costs. Ex: cost_reports
- *Block Size* - The number of files to upload with each execution of the policy. The default value of 20 is recommended.
- *Commit Delay (Hours)* - The number of hours to wait between committing bill uploads. This is to avoid overloading the CBI system and to ensure bill ingestion occurs at a predictable cadence. The default value of 12 is recommended.

## Policy Actions

- Uploads stored billing data to Flexera CCO
- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Storage Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121576) (*provider=azure_storage*). Note that a credential can be made with access to several storage accounts by setting `resource` to `https://storage.azure.com` in the Additional Parameters when creating this credential in Flexera One. This credential should have the following permissions for the storage account with the cost data:
  - `Microsoft.Storage/storageAccounts/blobServices/containers/read`
  - `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`
  - `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/list/action`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `csm_bill_upload_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Additional Requirements

The blobs containing costs must have the `.csv` file extension and must contain the year and month in YYYY-MM format. Example: cost_data_2025-04-08.csv

This policy template also requires a valid CBI endpoint created using the [Flexera Bill Connect API](https://reference.rightscale.com/optima-bill/#/CBIBillConnects/CBIBillConnects_create).

## Supported Clouds

- All

## Cost

This policy template does not incur any cloud costs
