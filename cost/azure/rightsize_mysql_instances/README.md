# Azure Rightsize MySQL Databases

## What it does

This policy will look at Utilization of Azure MySQL single and flexible databases and recommend up or down sizing after user approval.

## Functional Details

This policy checks all the Azure MySQL databases for a Azure Subscription. It does a Average CPU usage over the last 30 days. It then checks if the Utilization is Lower than the Downsize Threshold or higher that Upsize Threshold. Finally it displays the found data, recommendations and provides option to Downsize or Upsize the SQL database after the user approval.

- This policy does not support databases which are in Elastic pool
- This policy applies only for Upsize or Downsize of DTUs/vCores within tiers.
- This policy will not be applicable to resize between service tiers.
- If the MySQL server can not downsize because it's already at its minimum size or can not upsize because it's already at its max. then in the 'Recommended Capacity' column shows as 'N/A' and 'Recommendation' column shows as 'Change tier' for resize within tiers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *CPU % - Upsize threshold* - Percentage of CPU utilization to identify an Upsize is recommended
- *CPU % - Downsize Threshold* - Percentage of CPU utilization to identify an Downsize is recommended
- *Threshold Statistic* - Determines whether to use minimum CPU usage, maximum CPU usage, or average CPU usage when determining recommendations.
- *Exclusion Tag Key* - Cloud native tag key to ignore instances. Example: exclude_utilization
- *Email addresses* - Email addresses of the recipients you wish to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Log to CM Audit Entries* - Boolean for whether or not to log any debugging information from actions to CM Audit Entries, this should be left set to No on Flexera EU.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Resize Instances" action while applying the policy, all the identified resources will be resized as per the recommendation.

## Actions

- Sends an email notification
- Rightsize MySQL Databases after approval

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.DBforMySQL/servers/databases/read
- Microsoft.DBforMySQL/servers/databases/update
- Microsoft.DBforMySQL/servers/databases/metrics/read
- Microsoft.DBforMySQL/flexibleServers/databases/read
- Microsoft.DBforMySQL/flexibleServers/databases/update
- Microsoft.DBforMySQL/flexibleServers/databases/metrics/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
