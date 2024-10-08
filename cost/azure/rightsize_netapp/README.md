# Azure Rightsize NetApp Resources

## What It Does

This policy template checks NetApp capacity pools and volumes in Azure Subscriptions. Based on the capacity pool and volume space used and provided thresholds, capacity pools and volumes can be recommended to resize to meet a desired used percentage. For instance, for a volume of 200 GiB with a used capacity of 80 GiB and a threshold of 80%, the recommended volume size will be 100 GiB. Information for capacity pools and volumes recommended to resize will be sent to the user-specified email addresses.

### Policy Saving Details

The policy includes the estimated monthly savings. The estimated monthly savings are recognized if the resource is resized to the suggested size.

- The `Estimated Monthly Savings` is calculated by obtaining the price of the reserved capacity and tier of the pool per month from the Azure Pricing API.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- The policy template can recommend increasing or decreasing the capacity of a resource (capacity pool or volume) to match a user-specified usage threshold; the policy template will only show savings for capacity pool downsize recommendations. Downsizing volumes will not immediately lead to savings, as usage is billed based on the pool's provisioned capacity. We recommend downsizing volumes and then capacity pools to achieve maximum savings. A user can suppress the upsize recommendations using the policy template's parameter *Show upsize recommendations*.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Pool Allocated to Volume Threshold (%)* - The allocation threshold at which to consider a NetApp pool to be 'oversized' and therefore be flagged for downsizing.
- *Volume Consumed Capacity Threshold (%)* - The capacity usage threshold at which to consider a NetApp volume to be 'oversized' and therefore be flagged for downsizing.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Show Upsize Recommendations* - Whether or not to include upsize recommendations for pools and volumes
- *Resource Types* - Whether to produce recommendations only for pools or for both pools and volumes
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Change the size of NetApp pools after approval
- Change the size of NetApp volumes after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.NetApp/netAppAccounts/capacityPools/read`
  - `Microsoft.NetApp/netAppAccounts/capacityPools/write`*
  - `Microsoft.NetApp/netAppAccounts/capacityPools/volumes/read`
  - `Microsoft.NetApp/netAppAccounts/capacityPools/volumes/write`*
  - `Microsoft.Insights/metrics/read`

  \* Only required for taking action (changing the size); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
