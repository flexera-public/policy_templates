# Azure Rightsize SQL Databases

## What it does

This policy will look at Utilization of Azure SQL databases and recommend up or down sizing after user approval.

## Functional Details

This policy checks all the Azure SQL databases for a Azure Subscription. It does a Average CPU usage over the last 30 days. It then checks if the Utilization is Lower than the Downsize Threshold or higher that Upsize Threshold. Finally it displays the found data, recommendations and provides option to Downsize or Upsize the SQL database after the user approval.

- This policy applies only for Upsize or Downsize of DTUs/vCores within tiers.
- This policy will not be applicable to resize between service tiers.
- If the SQL database can not downsize because it's already at it's min size or can not upsize because it's already at it's max. then in the 'Recommended Capacity' column shows as 'n/a' for resize within tiers.
- Pls refer the following links: <https://docs.microsoft.com/en-us/azure/sql-database/sql-database-dtu-resource-limits-single-databases> and <https://docs.microsoft.com/en-us/azure/sql-database/sql-database-vcore-resource-limits-single-databases> for detailed resource limits of Azure SQL Database using the DTU purchasing model and using the vCore purchasing model.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Azure Tenant ID* - Your Azure tenant ID.  You can find it by following this guide: [Tenant ID](https://docs.microsoft.com/en-us/onedrive/find-your-office-365-tenant-id)
- *Azure Subscription ID* - Your Azure Subscription ID.  You can find it by following this guide: [Subscription ID](https://blogs.msdn.microsoft.com/mschray/2016/03/18/getting-your-azure-subscription-guid-new-portal/)
- *Average used CPU % - Upsize threshold* - Percentage of CPU utilization to identify an Upsize is recommended
- *Average used CPU % - Downsize Threshold* - Percentage of CPU utilization to identify an Downsize is recommended
- *Exclusion Tag Key* - To Identify any instances that should be excluded from the recommendations
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Prerequisites

- Azure Service Principal (AKA Azure Active Directory Application) with the appropriate permissions to manage resources in the target subscription
- The following RightScale Credentials
  - `AZURE_APPLICATION_ID`
  - `AZURE_APPLICATION_KEY`

## Installation

1. Follow steps to [Create an Azure Active Directory Application](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#create-an-azure-active-directory-application)
1. Grant the Azure AD Application access to the necessary subscription(s)
1. [Retrieve the Application ID & Authentication Key](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-application-id-and-authentication-key)
1. Create RightScale Credentials with values that match the Application ID (Credential name: `AZURE_APPLICATION_ID`) & Authentication Key (Credential name: `AZURE_APPLICATION_KEY`)
1. [Retrieve your Tenant ID](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#get-tenant-id)

## Actions

- Sends an email notification
- Rightsize SQL Databases after approval

### Required RightScale Roles

- policy_designer
- policy_manager
- policy_publisher
- credential_viewer
- observer

### Azure Required Permissions

- Microsoft.Sql/servers/databases/read
- Microsoft.Sql/servers/databases/update
- Microsoft.Sql/servers/databases/metrics/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.


