## Azure Publicly Accessible SQL Managed Instances

### What it does

This policy checks all Azure SQL Managed instances and reports on any that are publicly accessible. When such an instance is detected, the user can choose to disable public data endpoint or delete it. For deleting the user needs to enable 'delete action' option as mentioned in "To enable delete action" section below.

### Prerequesites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`
  
### To enable delete action

Perform below steps to enable delete action.

- Edit the file [Check_for_publicly_accessible_Azure_SQL_Managed_Instance](https://github.com/rightscale/policy_templates/tree/master/security/azure/sql_publicly_accessible_managed_instance)
- uncomment the line which conatins 'escalate $esc_delete_Managed_instances_approval' and save the changes.
- upload the modified file and apply the policy.

### Required RightScale Roles
- policy_designer
- policy_manager
- policy_publisher

### Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

### Functional Details

When a publicly accessible Azure SQL Managed Instance is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have multiple actions that they are able to take after approval:
- *delete* - deletes the Azure SQL managed instance
- *Note: by default *delete* action has been disabled, the user can follow the steps mentioned in "To enable delete action" section above to enable delete action.*
- *disable public data endpoint* - modifies the configuration of virtual network of the particular SQL managed instance that allows public accessibility

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key* - Azure SQL Managed instance tag to ignore instance that are with public data endpoint enabled. Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication

### Supported Clouds

- Azure Resource Manager

### Cost

This Policy Template does not incur any cloud costs.