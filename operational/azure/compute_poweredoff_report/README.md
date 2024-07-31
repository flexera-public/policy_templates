# Azure Compute Instances Time Powered Off Report

## What It Does

This policy template checks all of the virtual machines in Azure for how much time they have spent in a powered off state over a user-specified number of days. A report is produced with all virtual machines that are powered off for greater than or less than the user-specified percentage threshold. Optionally, an email of this report is sent, and the instances can be powered off or terminated.

__NOTE: The most recent 3 days are ignored when performing the assessment. This is because cloud billing data is used to assess usage, and this data is not reported by Azure in real time and may be unreliable for up to 72 hours. For example, if performing the assessment for 7 days, the assessment will begin 10 days ago and end 3 days ago.__

## How It Works

- The policy leverages the Azure API to retrieve a list of all virtual machines.
- The policy leverages the Flexera Bill Analysis API to gather usage data for each virtual machine.
- For each virtual machine, the total number of hours in the specified time frame is compared to the number of hours in the usage data to determine the percentage of time the virtual machine is powered off. The following formula is used for this calculation: (`Look Back Period (Days)` \* 24) - `Hours Of Usage` / (`Look Back Period (Days)` \* 24)
- The hourly cost is calculated by dividing the total cost of the instance across the `Look Back Period (Days)` by `Hours Of Usage`. This is the estimated hourly cost of the instance while it is powered on.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclude Stopped Virtual Machines* - Whether or not to filter stopped virtual machines from the results. If set to `Yes`, only running virtual machines will be included in the results.
- *Exclude Databricks* - Whether or not to filter virtual machines used for Azure Databricks from the results. If set to `Yes`, virtual machines for Azure Databricks will not be included in the results.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Look Back Period (Days)* - How many days back to look when assessing the amount of time a virtual machine is powered off for.
- *Maximum Time Powered Off (%)* - Virtual machines that are powered off for more than the specified percentage will be included in the report. Set to `100` to not perform this assessment.
- *Minimum Time Powered Off (%)* - Virtual machines that are powered off for less than the specified percentage will be included in the report. Set to `0` to not perform this assessment.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Power Off Type* - Whether to perform a graceful shutdown or a forced shutdown when powering off idle instances. Only applicable when taking action against instances.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action. For example if a user selects the "Delete Instances" action while applying the policy, all the virtual machines that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Sends an email notification
- Power off virtual machines after approval
- Delete virtual machines after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`*
  - `Microsoft.Compute/virtualMachines/powerOff/action`*
  - `Microsoft.Compute/virtualMachines/delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
