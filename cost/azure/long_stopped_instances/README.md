# Azure Long Stopped Compute Instances

## What It Does

This policy template finds Azure virtual machines which have been stopped for more than a user-specified number of days and emails a report containing a list of the offending instances along with a potential savings estimate for each instance if it is deleted. Optionally, the policy will delete the instances after user approval.

NOTE: Azure only stores log data for virtual machines for 90 days. If the virtual machine was stopped over 90 days ago, it is not possible to know precisely how long it has been stopped for. Such virtual machines will be reported as having been stopped for "> 90" days in the incident.

## How It Works

- The policy leverages the Azure API to check all instances and then checks the status of the incident to see if it is stopped.
- The policy then leverages the stored logs for the instance to determine when the instance was powered off. If no such logs exist, it is assumed the instance has been powered off for longer than 90 days.
- Any stopped instances that have been stopped more than the user-specified number of days are reported.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for long stopped instances if the resource is deleted.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- The calculated savings is the full cost of the resource, and optionally, the full cost of any disks attached to the resource. Note that, depending on whether the virtual machine is stopped or fully deallocated, there may not be a cost for the virtual machine itself.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Stopped Days* - The number of days an instance needs to be stopped to include it in the incident report.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Include Disk Savings* - Whether to include savings related to attached disks in the savings estimate for long stopped instances.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Instances" action while applying the policy template, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Sends an email notification
- Delete long stopped Azure virtual machines after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Resources/subscriptions/read`
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/instanceView/read`
  - `Microsoft.Compute/disks/read`
  - `Microsoft.Insights/eventtypes/management/read`
  - `Microsoft.Compute/virtualMachines/delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
