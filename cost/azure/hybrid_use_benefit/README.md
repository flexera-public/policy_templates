## Azure Hybrid Use Benefit Policy

### What it does

This Policy Template is used to automatically apply the Azure Hybrid Use Benefit (AHUB) to all eligible VMs in an Azure Subscription.

### Prerequesites

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

### Functional Details

_ The policy identifies all Windows server instances that are not currently using [Azure Hybrid Use Benefit](https://azure.microsoft.com/en-us/pricing/hybrid-benefit/). It raises an incident for all applicable VMs not currently using AHUB, which once approved, will enable AHUB on all identified instances.
- The Exclusion Tag parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy does not track licenses or availability. It is you responsibility to ensure you are not underlicensed.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication
- *Exclusion Tag Key* - an Azure-native instance tag to ignore instances that you don't want AHUB applied to. Only supply the tag key
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Supported Clouds

- Azure Resource Manager

### Cost

This Policy Template does not incur any cloud costs.
