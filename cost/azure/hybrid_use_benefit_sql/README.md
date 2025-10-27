# Azure Hybrid Use Benefit for SQL

## What It Does

This policy template reports on any Azure SQL resources that may be eligible for Azure Hybrid Use Benefit (AHUB) but are not currently receiving the benefit. Optionally, this report can be emailed, and AHUB can automatically be enabled on these resources.

## How It Works

- The policy identifies all SQL databases in Azure that are not currently using [Azure Hybrid Use Benefit](https://azure.microsoft.com/en-us/pricing/hybrid-benefit/). These can be SQL Virtual Machines, SQL Elastic Pools, SQL Databases or SQL Managed Instances. It raises an incident for all applicable instances not currently using AHUB, which once approved, will enable AHUB on all identified instances.
- This policy template does not track licenses or availability. It is your responsibility to ensure that you have valid licenses for all resources that AHUB is enabled for.
- The hourly cost of a SQL resource is calculated by dividing the total cost of the SQL resource for the last 30 days by the hours of usage for that same time period.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Allow/Deny Subscriptions* - Allow or Deny entered Subscriptions to filter results.
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. Leave blank to check all Subscriptions.
- *Allow/Deny Regions* - Allow or Deny entered regions to filter results.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Leave blank to check all Subscriptions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *SQL Resource Types* - A list of SQL resource types to report on. Resource types not listed here will be ignored. Allowed values: SQL Virtual Machines, SQL Elastic Pools, SQL Databases, SQL Managed Instances
- *SQL Virtual Machine Image SKUs* - A list of SQL Virtual Machine image SKUs to report on. SQL Virtual Machine resources without one of the SKUs specified here will be ignored. Allowed values: Developer, Enterprise, Express, Standard, Web
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Apply Hybrid Use Benefit" action while applying the policy, all of the resources without AHUB that qualify will have AHUB enabled.

## Policy Actions

- Sends an email notification
- Apply AHUB benefit to resource after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.SqlVirtualMachine/sqlVirtualMachines/read`
  - `Microsoft.SqlVirtualMachine/sqlVirtualMachines/write`*
  - `Microsoft.Sql/servers/read`
  - `Microsoft.Sql/servers/write`*
  - `Microsoft.Sql/managedInstances/read`
  - `Microsoft.Sql/managedInstances/write`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
