## Azure Instances Utilization from Log Analytics

### What it does

This Policy Template uses performance metrics from Log Analytics from the last 30 days to identify underutilized instances. This is meant to be run as a weekly policy. 

### Prerequisites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription.
  - In addition, the Service Principal will need the `Log Analytics Reader` role on all Log Analytics Workspaces the VMs in the subscription are sending performance metrics to.
- The following RightScale Credentials:
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`
- Virtual Machines with the Log Analytics/OMS Agent installed and sending performance metrics to a Azure Log Analytics workspace.

### Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

### Functional Details

- This policy identifies all instances reporting performance metrics to Log Analytics whose CPU or Memory utilization is below the thresholds set in the **Average used memory percentage** and **Average used CPU percentage** parameters.
- The **Exclusion Tag Key** parameter is a string value.  Supply the Tag Key only.  Tag Values are not analyzed and therefore are not need.  If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.
- This policy sets the tag defined in the **Action Tag Key:Value** parameter on the underutilized instances that were identified.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure AD Tenant ID* - the Azure AD Tenant ID used for the Azure API Authentication
- *Azure Subscription ID* - the Azure Subscription ID used for the Azure API Authentication
- *Average used memory percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Average used CPU percentage* - Utilization below this percentage will raise an incident to tag the instance. Providing -1 will turn off this metric for consideration.
- *Exclusion Tag Key* - An Azure-native instance tag to ignore instances that you don't want to consider for downsizing. Only supply the tag key
- *Action Tag Key:Value* - The tag key:value pair to set on an instance that is underutilized.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Required RightScale Roles

- Cloud Management - Actor
- Cloud Management - Observer
- credential_viewer

### Azure Required Permissions

- Microsoft.Compute/skus/read
- Microsoft.OperationalInsights/workspaces/analytics/query/action

### Supported Clouds

- Azure Resource Manager

### Observation Period

By default, this policy calculates utilization over a 30 day period.  

To calculate over a different period of time, you can update the policy template.  
Replace the `30` wherever you see `query "timespan","P30D"` with the new number of days you want to use.

### Cost

This Policy Template does not incur any cloud costs.
