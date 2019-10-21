## Azure - Ensure AHUB Utilization with Manual Entry

### What it does

This policy checks all instances in Azure to determine how many are using AHUB and report when that number falls outside or inside the specified license number.

### Functional Details

The policy leverages the cloud API to get data for all instances and compares that to the allowed AHUB number specified by the user.
Each license is good for one VM with up to 16 cores or two VM's with up to 8 cores. The policy will report on the instances that are missing AHUB license and show which instance have the potential for the AHUB license.
 
### Prerequesites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`
  
### Required RightScale Roles

- policy_designer
- policy_manager
- policy_publisher
- Cloud Management - credential_viewer

### Azure Required Permissions

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/locations/vmSizes/read

### Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)


### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Allowed AHUB licenses* - Number of AHUB licenses that are allowed to be run on Azure
- *Exclusion Tag Key* - Azure VMs instance tag to ignore instance that are with AHUB enabled. Only supply the tag key. The policy assumes that the tag value is irrelevant.

### Supported Clouds

- Azure

### Cost

This policy does not incur any cloud costs.


