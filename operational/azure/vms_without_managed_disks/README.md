## Azure VMs Not Using Managed Disks

### What it does
This policy checks all Azure VMs and reports on any that are not using Managed Disks, which are the latest offering from Azure and are much easier to manage.

### Functional Details
When a VM that is using unmanaged disks is detected, VM location information as well as unmanaged disk information is reported to the specified users.

### Pre-reqs
- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`

#### Input Parameters
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Exclusion Tag Key* - an Azure-native instance tag to ignore instances that match the disallowed instance type. Only supply the tag key
- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication

### Required RightScale Roles
- credential_viewer or admin

### Azure Required Permissions
- Microsoft.Compute/virtualMachines/read

### Supported Clouds
- Azure Resource Manager

### Cost
This Policy Template does not incur any cloud costs.