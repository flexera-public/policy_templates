## Azure Blob Storage Optimization
 
### What it does

This Policy checks Azure Blob Storage for older objects and can move old object to the Cool or Archive tier after a given period of time.

### Functional Details

- This policy identifies all Azure Blob Storage objects last modified outside of the specified timeframe
- For all objects identified as old, the user can choose to move the object to Cool or Archived tiers after user approval
 
### Input Parameters
 
This policy has the following input parameters required when launching the policy.

- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication
- *Storage Account* - Name of Storage account to search for blobs.
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Move to Cool tier after days last modified* - leave blank to skip moving
- *Move to Archive tier after days last modified* - leave blank to skip moving

### Prerequesites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`
  
### Required RightScale Roles

- policy_designer
- policy_manager
- policy_publisher
- credential_viewer
- observer

### Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

### Supported Clouds

- Azure

### Cost

This policy does not incur any cloud costs.

### Notes

1.'Storage Blob Data Owner' permission need to be added for storage account to fetch the container/blobs list, before calling List Containers/List Blobs API's.
2.Enter 'Standard Type' storage account with account kind type as 'StorageV2 (general purpose v2) / BlobStorage' to search for blobs.
3.Blob with type 'PageBlob' or 'AppendBlob' will not support moving object to 'cool tier' and 'archive tier'.