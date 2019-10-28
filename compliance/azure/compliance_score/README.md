## Azure Regulatory Compliance

### What it does

This Policy Template will provide an overview for the various Regulatory Compliance controls and compliance scores. The policy will generate an email notification.

### Pre-requisites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`
- The `policy_designer`, `policy_manager`, `credential_viewer` & `policy_publisher` roles


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
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Supported Clouds

- Azure

### Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
