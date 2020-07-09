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
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Resize Instances" action while applying the policy, all the identified resources will be resized as per the recommendation.

## Actions

- Sends an email notification
- Rightsize SQL Databases after approval

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Sql/servers/databases/read
- Microsoft.Sql/servers/databases/update
- Microsoft.Sql/servers/databases/metrics/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
