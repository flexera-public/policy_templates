# Azure Unused SQL Databases

## What it does

This Policy template checks for Azure SQL Databases that are unused by reviewing the DB connections and delete them after user approval.

## Functional Details

This policy gets a list of Azure SQL Databases and uses the DB Connection metric to check for successful connections over a 30-day period. If there are no successful DB Connections the policy will terminate the SQL databases after the user approval.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Exclusion Tag Key* - Azure-native SQL Database tag key to ignore databases. Only supply the tag key. The policy assumes that the tag value is irrelevant.

## Prerequisites

This policy requires the Azure Resource Manager Credential. When applying the policy select the appropriate credentials from the list for your tenant. If such credential doesn't exist please contact your cloud admin to create the Credential.
The credential must contain the value *azure_rm* in the Provider field. Refer to our documentation for more details on the [Credential Service](https://docs.rightscale.com/credentials/)

## Actions

- Sends an email notification
- Delete unused SQL Databases after approval

## Azure Required Permissions

- Microsoft.Sql/servers/databases/read
- Microsoft.Sql/servers/databases/delete
- Microsoft.Sql/servers/databases/metrics/read

## Supported Clouds

- Azure

## Cost

This policy does not incur any cloud costs.