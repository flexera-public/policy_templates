# Azure AHUB Utilization with Manual Entry

## What It Does

This policy template checks all virtual machines in Azure to determine how many are using AHUB and raises an incident when that number does not match a user-specified number of licenses.

## How It Works

The policy leverages the Azure Resource Manager API to get data for all virtual machines and compares that to the user-specified number of licenses. Each license is good for one virtual machine with up to 16 cores or two virtual machines with up to 8 cores.

- If more licenses have been allocated than consumed, the policy will report on virtual machines without AHUB that may benefit from having AHUB enabled.
- If more licenses have been consumed than allocated, the policy will report on virtual machines with an AHUB license that may benefit from disabling AHUB.
- If license allocation and consumption match exactly, the policy will not report on any virtual machines and no incident will be raised by this policy.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Azure Endpoint* - Select the API endpoint to use for Azure. Use default value of management.azure.com unless using Azure China.
- *Licenses Allowed* - The number of AHUB licenses permitted.
- *Allow/Deny Subscriptions* - Whether to treat Allow/Deny Subscriptions List parameter as allow or deny list. Has no effect if Allow/Deny Subscriptions List is left empty.
- *Allow/Deny Subscriptions List* - Filter results by subscription ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/vmSizes/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
