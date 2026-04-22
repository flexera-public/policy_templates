# Azure Hybrid Use Benefit for SQL

## What It Does

This policy template identifies Azure SQL resources — including SQL Virtual Machines, SQL Elastic Pools, SQL Databases, and SQL Managed Instances — that are eligible for [Azure Hybrid Use Benefit](https://azure.microsoft.com/en-us/pricing/offers/hybrid-benefit/) (AHUB) but do not currently have it enabled. AHUB for SQL allows organizations to apply existing on-premises SQL Server licenses with active Software Assurance to Azure SQL resources, significantly reducing the SQL Server license cost for those resources. The policy estimates monthly savings for each resource based on its vCore count and SQL Server edition, using license pricing data sourced from the Azure Retail Prices API. An incident report is generated for all qualifying resources, and optionally, AHUB can be enabled automatically or after manual approval.

**NOTE: This policy template does not check actual license inventory, availability, or compliance. It identifies SQL resources that are technically eligible for AHUB based on their Azure configuration alone. You must verify that you have sufficient available SQL Server licenses with active Software Assurance coverage before enabling AHUB. Enabling AHUB without adequate license entitlements may result in non-compliance with Microsoft licensing terms.**

## How It Works

- The policy identifies all SQL databases in Azure that are not currently using [Azure Hybrid Use Benefit](https://azure.microsoft.com/en-us/pricing/offers/hybrid-benefit/). These can be SQL Virtual Machines, SQL Elastic Pools, SQL Databases or SQL Managed Instances. It raises an incident for all applicable instances not currently using AHUB, which once approved, will enable AHUB on all identified instances.
- This policy template does not track licenses or availability. It is your responsibility to ensure that you have valid licenses for all resources that AHUB is enabled for.
- The hourly cost of a SQL resource is calculated by dividing the total cost of the SQL resource for the last 30 days by the hours of usage for that same time period.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if AHUB is applied to the resource.

- The `Estimated Monthly Savings` for **SQL Elastic Pools**, **SQL Databases**, and **SQL Managed Instances** is calculated using the resource's vCore count (`SKU Capacity`) and the SQL Server license price per vCPU from the [Azure Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices). The formula is: `license_price_per_vcpu × vcpu_count × 730`.
- The `Estimated Monthly Savings` for **SQL Virtual Machines** is calculated using the SQL Server edition (`Image SKU`) and the vCPU count derived from the underlying Azure VM size. The vCPU count is parsed from the VM size name (e.g., `Standard_D4s_v3` → 4 vCPUs). The formula is: `license_price_per_vcpu × vcpu_count × 730`.
- License prices per vCPU are sourced from the [`azure_sql_license_pricing.json`](https://github.com/flexera-public/policy_templates/blob/master/data/azure/azure_sql_license_pricing.json) data file. SQL Server editions map to license prices as follows: `BusinessCritical` tier → Enterprise, `GeneralPurpose` and `Hyperscale` tiers → Standard; SQL Virtual Machines use the `Image SKU` field directly.
- If the vCPU count or edition cannot be determined for a resource, the `Estimated Monthly Savings` is 0 and the resource is still reported.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Allow/Deny Subscriptions* - Allow or Deny entered Subscriptions to filter results.
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. Leave blank to check all Subscriptions.
- *Allow/Deny Regions* - Allow or Deny entered regions to filter results.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Leave blank to check all Subscriptions.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Resources whose estimated savings are below this threshold will be excluded from results. Resources whose savings cannot be calculated will still be reported.
- *SQL Resource Types* - A list of SQL resource types to report on. Resource types not listed here will be ignored. Allowed values: SQL Virtual Machines, SQL Elastic Pools, SQL Databases, SQL Managed Instances
- *SQL Virtual Machine Image SKUs* - A list of SQL Virtual Machine image SKUs to report on. SQL Virtual Machine resources without one of the SKUs specified here will be ignored. Allowed values: Developer, Enterprise, Express, Standard, Web
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Apply Hybrid Use Benefit" action while applying the policy template, all of the resources without AHUB that qualify will have AHUB enabled.

## Policy Actions

- Sends an email notification
- Apply AHUB benefit to resource after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.SqlVirtualMachine/sqlVirtualMachines/read`
  - `Microsoft.SqlVirtualMachine/sqlVirtualMachines/write`*
  - `Microsoft.Sql/servers/read`
  - `Microsoft.Sql/servers/databases/read`
  - `Microsoft.Sql/servers/databases/write`*
  - `Microsoft.Sql/servers/elasticPools/read`
  - `Microsoft.Sql/servers/elasticPools/write`*
  - `Microsoft.Sql/managedInstances/read`
  - `Microsoft.Sql/managedInstances/write`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for meta-policy self-termination; not required if not using the meta parent of this policy template.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
