## Azure: Disallowed Regions

### What it does

This Policy Template accepts an input that defines which Azure regions are allowed by your compliance policies. Any Azure resource that exists outside of your approved regions will be raised in an Incident. Incidents will escalate to an email notification and will trigger an approval workflow prior to executing Cloud Workflow to delete the resources.

### Pre-reqs

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`
- The `policy_designer`, `policy_manager` & `policy_publisher` roles


### Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)
1. Update `azure_disallowed_regions.pt` Policy Template with your Tenant ID.
   - Replace the 2 occureneces of "AZURE_TENANT_ID" with your Tenant ID
1. Navigate to Policies > Templates, use the `Upload Policy Template` interface to upload the `azure_disallowed_regions.pt` Policy Template

### Supported Clouds

- Azure

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
