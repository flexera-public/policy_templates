# Azure Rightsize SQL Database Storage

## What It Does

This policy checks the storage usage for all the Azure SQL database instances purchased using the vCore purchasing model and determines if a smaller maximum storage space would be viable. A report is created with these recommendations that can optionally be emailed.

Only vCore purchases are supported because DTU-purchased databases cannot have their maximum storage space changed independently without changing the entire SKU, including CPU and memory usage. Automatic actions are not supported because a SQL database cannot have its maximum storage space reduced; a new smaller database would need to be provisioned and data would need to be migrated to it.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the SQL database is replaced with a new one using the recommended maximum storage space.

- The `Estimated Monthly Savings` is calculated by subtracting the monthly cost of the recommended maximum storage space from the current maximum storage space.
- Azure list price is used to determine the cost of the current and recommended maximum storage spaces. Pricing is converted from USD to local currency based on current exchange rates when applicable.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Minimum Age (Days)* - The minimum age, in days, since a SQL database was created to produce recommendations for it. Set to 0 to ignore age entirely.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Storage Usage Threshold (%)* - Report instances whose used storage space is below the specified percentage, indicating that they may be overprovisioned.
- *Storage Downgrade Threshold (%)* - The percentage of free storage space that recommendations should always include. Recommendations will always be for a storage size that would result in at least this percentage of free space based on current usage.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Sql/servers/read`
  - `Microsoft.Sql/servers/databases/read`
  - `Microsoft.Sql/servers/databases/metrics/read`
  - `Microsoft.Insights/metrics/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
