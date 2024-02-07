# Azure Rightsize NetApp Files

## What it does

This Policy Template scans all NetApp capacity pools and volumes in the given account and identifies any pool or volume that meets the user-specified criteria for being wrong sized. The user can filter pools and volumes based on usage percentage of the capacity (TiB or GiB). Any pools or volumes that meet the user-specified criteria are considered oversized. If any oversized pools or volumes are found, an incident report will show their information. An email will be sent to the user-specified email addresses.

### Policy Saving Details

The policy includes the estimated monthly savings. The estimated monthly savings are recognized if the resource is resized to the suggested size.

- The `Estimated Monthly Savings` is calculated by obtaining the price of the reserved capacity and tier of the pool per month from the Azure Pricing API.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- The policy can recommend to increase or decrease the capacity of a resource (capacity pool or volume) in order to match a user-specified usage threshold, the policy will only show savings for size decreasing recommendations. A user can select to hide or show size increment recommendations using the parameter *Show size increment recommendations* of the policy.

## Input parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Capacity Pool Allocated Capacity Threshold (%)* - The threshold that should be the new allocated capacity of a pool and therefore be flagged for rightsizing
- *Volume Logical Size Threshold (%)* - The threshold that should be the new logical size of a volume and therefore be flagged for rightsizing.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Show size increment recommendations* - Choose if you want this policy to also show recommendations to increase the size of capacity pools and volumes.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Recommendation mode* - Choose between scanning only pools or pools with their volumes, each will produce different recommendations.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Change the size of the volumes (if oversized) after approval
- Change the size of the pools (if oversized) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:

  - `Microsoft.NetApp/netAppAccounts/capacityPools/read`
  - `Microsoft.NetApp/netAppAccounts/capacityPools/write` *
  - `Microsoft.NetApp/netAppAccounts/capacityPools/volumes/read`
  - `Microsoft.NetApp/netAppAccounts/capacityPools/volumes/write` *
  - `Microsoft.Insights/metrics/read`

* Only required for taking action (changing the size); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*).

This is only required for the application of the metaparent policy.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
