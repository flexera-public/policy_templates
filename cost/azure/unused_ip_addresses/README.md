# Azure Unused IP Addresses

## What it does

This Policy Template scans all IP addresses in the given account and identifies any unused IP addresses. An IP address is considered unused if it has been detached for a user-specified number of days. If any are found, an incident report will show the IP addresses, and related information, and an email will be sent to the user-specified email address. If the user approves that the IP addresses should be deleted, the policy will delete the IP addresses. Optionally, the user can filter results by resource tag, subscription ID/name, or region.

### Policy savings details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the IP address is deleted. Optima is used to retrieve and calculate the estimated savings which is the cost of the IP address for a full day (3 days ago) multiplied by 30.44 (the average number of days in a month), or 0 if no cost information for the resource was found in Optima. The savings is displayed in the Estimated Monthly Savings column. The incident message detail includes the sum of each resource *Estimated Monthly Savings* as *Potential Monthly Savings*.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Network/publicIPAddresses/read`
  - `Microsoft.Network/publicIPAddresses/delete`*
  - `Microsoft.Insights/eventtypes/values/read`

\* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Azure Endpoint* - Azure Endpoint to access resources
- *Days Unattached* - The number of days an IP address needs to be detached to be considered unused. This value cannot be set above 90 due to Azure only storing 90 days of log data. If this value is set to 0, all unattached IP addresses will be considered unused.
- *Allow/Deny Subscriptions* - Whether to treat Allow/Deny Subscriptions List parameter as allow or deny list. Has no effect if Allow/Deny Subscriptions List is left empty.
- *Allow/Deny Subscriptions List* - Filter results by subscription ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclude Tags* - Cloud native tags to ignore instances that you don't want to produce recommendations for. Format: Key:Value
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Delete IP Addresses" action while applying the policy, all unused IP addresses will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete unused IP addresses after approval

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
