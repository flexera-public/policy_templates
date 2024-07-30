# Azure Hybrid Use Benefit for Windows Server

## What It Does

This Policy Template is used to automatically apply the Azure Hybrid Use Benefit (AHUB) to all eligible Windows VMs in an Azure Subscription and provides a monthly savings value if AHUB were to be enabled.

## How It Works

- The policy identifies all Windows server instances that could utilize [Azure Hybrid Use Benefit](https://azure.microsoft.com/en-us/pricing/hybrid-benefit/) but are not currently using it. It raises an incident for all applicable VMs not currently using AHUB, provides a monthly savings amount if AHUB were to be enabled, and provides the option to automatically enable AHUB on all identified instances.
- This policy does not track licenses or availability. It is your responsibility to ensure you are not under licensed.
- The hourly cost of a virtual machine is calculated by dividing the total cost of the virtual machine for the last 30 days by the hours of usage for that same time period.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the AHUB benefit is enabled for the resource.

- Data retrieved from the Azure Pricing API is used to determine the hourly list price of the instance type with and without AHUB. The `Estimated Monthly Savings` is calculated by taking the difference between the two prices and multiplying by 24 and then 30.44 to get a monthly price.
- Since savings is calculated based on list prices obtained from the Azure Pricing API, they will *not* take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- The savings are displayed in the `Estimated Monthly Savings` column.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- If the Flexera organization is configured to use a currency other than USD, the savings values will be converted from USD using the exchange rate at the time that the policy executes.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - A list of email addresses to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
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
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Apply Hybrid Use Benefit" action while applying the policy, all of the Windows VMs without AHUB that qualify will have AHUB enabled.

## Policy Actions

- Sends an email notification
- Apply AHUB benefit to resource after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`*

  \* Only required for taking action (applying AHUB to VMs); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
