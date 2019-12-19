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

- *Average used CPU % - Upsize threshold* - Percentage of CPU utilization to identify an Upsize is recommended
- *Average used CPU % - Downsize Threshold* - Percentage of CPU utilization to identify an Downsize is recommended
- *Exclusion Tag Key* - Cloud native tag key to ignore instances. Example: exclude_utilization
- *Email addresses* - Email addresses of the recipients you wish to notify

## Actions

- Sends an email notification
- Rightsize SQL Databases after approval

## Prerequisites

This policy requires the Azure Resource Manager Credential. When applying the policy select the appropriate credentials
from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.

The credential must contain the value *Azure RM* in the Provider field.
Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Required Permissions

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


