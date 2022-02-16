# Azure Unused SQL Databases

## What it does

This Policy template checks for Azure SQL Databases that are unused by reviewing the DB connections and delete them after user approval.

## Functional Details

This policy gets a list of Azure SQL Databases and uses the DB Connection metric to check for successful connections over a 30-day period. If there are no successful DB Connections the policy will terminate the SQL databases after the user approval.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. Optima is used to receive the estimated savings which is the product of the most recent full day's cost of the resource * 30. The savings is displayed in the Estimated Monthly Savings column. If the resource can not be found in Optima the value is 0.0. The incident message detail includes the sum of each resource Estimated Monthly Savings as Total Estimated Monthly Savings.
If the user is missing the minimum required role of `billing_center_viewer` or if there is no enough data received from Optima to calculate savings, appropriate message is displayed in the incident detail message along with the estimated monthly savings column value as 0.0 in the incident table.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key* - Azure-native SQL Database tag key to ignore databases. Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Whitelist* - Whitelisted Subscriptions, if empty, all subscriptions will be checked
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the instances that didn't satisfy the policy condition will be terminated.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Sql/servers/databases/read
- Microsoft.Sql/servers/databases/delete
- Microsoft.Sql/servers/databases/metrics/read

## Actions

- Sends an email notification
- Delete unused SQL Databases after approval

## Supported Clouds

- Azure

## Cost

This policy does not incur any cloud costs.
