# Azure Untagged Virtual Machines

## What It Does

This policy template checks for Azure virtual machines missing the user-specified tags. An incident is raised containing the untagged virtual machines, and the user has the option to power off, delete, or tag the virtual machines.

NOTE: This policy is specific to virtual machines (Microsoft.Compute/virtualMachines). The [Azure Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_resources/) policy is recommended for finding untagged resources that are not virtual machines.

## Functional Details

- The policy leverages the Azure API to retrieve a list of all virtual machines in the Azure estate.
- The policy then filters that list based on user-specified parameters.
- The policy then identifies the virtual machines in the filtered list that are missing the tags specified by the user.

## Input Parameters

This policy has the following input parameters required when launching the policy:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Tags* - The policy will report resources missing the specified tags. The following formats are supported:
  - `Key` - Find all resources missing the specified tag key.
  - `Key==Value` - Find all resources missing the specified tag key:value pair.
  - `Key!=Value` - Find all resources that have the specified tag key:value pair.
  - `Key=~/Regex/` - Find all resources where the value for the specified key does not match the specified regex string.
  - `Key!~/Regex/` - Find all resources where the value for the specified key matches the specified regex string.
- *Any / All* - Whether to report on instances missing any of the specified tags or all of them. Only applicable if more than one value is entered in the `Tags` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Power Off Type* - Whether to perform a graceful shutdown or a forced shutdown when powering off instances.

This policy has the following input parameters required when adding tags to resources from a raised incident:

- *Add Tags (Key=Value)* - Cloud native tags to add to resources with missing tags. Use Key=Value format. Examples: env=production, team=finance

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Sends an email notification
- Power off Azure virtual machine automatically or after approval
- Delete Azure virtual machine automatically or after approval
- Tag Azure virtual machine after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`*

\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
