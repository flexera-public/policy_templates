## Azure: Tag Resources with Resource Group Name

### What it does

This Policy Template will scan all resources in an Azure Resource Manager Subscription, and will raise an incident if any resources are not properly tagged with their corresponding Resource Group name.  When an incident is raised, the Policy escalation will execute Cloud Workflow to tag the resources with the correct Resource Group name.

### Pre-reqs

- Azure Active Directory Application with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`
- The `policy_designer`, `policy_manager`, `credential_viewer` & `policy_publisher` roles

### Azure Required Permissions

- Microsoft.Resources/subscriptions/resources/read
- Microsoft.Resources/subscriptions/providers/read

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
- *Tag Key* - the tag key to scan on resources and to utilize when applying new/updated tags on resources  
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- An email is sent to the Email lists provided of the resources out of compliance
- Tag resources with the name of their Resource Group

### Supported Clouds

- Azure Resource Manager

### Limitations

**Note:** Azure Classic (Azure Service Manager / ASM) resources are not supported by this Policy.

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
