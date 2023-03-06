# Azure Ensure SQL Server VA Periodic Scans Enabled

## What it does

This policy checks all Azure SQL Servers to ensure that they have Vulnerability Assessment periodic scans enabled. An incident is raised with the offending SQL Servers if any are found that don't.

## Functional Details

The Azure Resource Manager API is used to get a list of subscriptions and SQL Servers within those subscriptions. The policy then queries the Vulnerability Assessments endpoint for each SQL Server and checks the "properties.recurringScans.isEnabled" field to ensure periodic scans are enabled.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag values to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/read
- Microsoft.Sql/servers/read
- Microsoft.Sql/servers/vulnerabilityAssessments/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
