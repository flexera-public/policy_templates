## Azure Below CPU Utilization
 
### What it does
This policy checks all the instances in the Azure Subscription for the average CPU usage over the the last hour.  If the usage is less than the user provided CPU percentage threshold then the virtual machines are recomended for removal, and the user is emailed.

### Functional Details
 
The policy leverages the Azure API to check all instances and then grab the utilization over the past hour, finally recomendending the low ones for decomissioning
 
#### Input Parameters
 
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *CPU Threshold* - Percentage of CPU utilization
- *Azure Subscription ID* - Your Azure Subscription ID.  You can find it by following this guide: https://docs.bitnami.com/azure/faq/administration/find-subscription-id/
- *Azure Tenant ID* - Your Azure tenant ID.  You can find it by following this guide: https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id
 
### Required RightScale Roles
 
None
 
### Supported Clouds
 
- Azure
 
### Cost
 
This Policy Template does not incur any cloud costs.