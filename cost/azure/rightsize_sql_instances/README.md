# Azure Rightsize SQL Databases

## What It Does

This policy template checks usage for all Azure SQL single database instances in Azure Subscriptions over a user-specified number of days. If there were no connections to the instance, the instance is recommended for deletion. If there were connections but the average CPU/DTU usage was below a user-specified threshold, the instance is recommended for downsizing. Both sets of instances returned from this policy are emailed to the user.

## How It Works

- The policy template leverages the Azure API to check all Azure SQL single database instances and then checks the number of connections and utilization over a user-specified number of days.
  - Utilization is based on CPU usage for vCore-model databases.
  - Utilization is based on DTU usage for DTU-model databases.
- The policy template identifies all instances that either have had no connections over a user-specified number of days and provides the relevant recommendation.
- The recommendation provided for unused instances is a deletion action. These instances can be deleted in an automated manner or after approval.
- The policy template identifies all instances that have had connections but have average usage below the user-specified threshold over a user-specified number of days and provides the relevant recommendation.
- The recommendation provided for underutilized instances is a downsize action. These instances can be downsized in an automated manner or after approval.

### Policy Savings Details

The policy template includes the estimated monthly savings. The estimated monthly savings is recognized for unused resources if the resource is terminated, and for underutilized resources if the resource is downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- For unused resources, the `Estimated Monthly Savings` is the full cost of the resource.
- For underutilized resources, the savings is the difference of the current cost of the resource and the estimated cost of the recommended resource type.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy template with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Minimum Age (Days)* - The minimum age, in days, since a SQL database was created to produce recommendations for it. Set to 0 to ignore age entirely.
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
- *Threshold Statistic* - Statistic to use when determining if a SQL instance is underutilized.
- *Statistic Interval* - The interval to use when gathering Azure metrics data. Smaller intervals produce more accurate results at the expense of policy memory usage and completion time due to larger data sets.
- *Statistic Lookback Period* - How many days back to look at connection and CPU/DTU utilization data for instances. This value cannot be set higher than 90 because Azure does not retain metrics for longer than 90 days.
- *Report Unused or Underutilized* - Whether to report on unused instances, underutilized instances, or both. If both are selected, unused instances will not appear in the list of underutilized instances regardless of CPU usage.
- *Underutilized Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Only applies to vCore-model SQL databases (GeneralPurpose, BusinessCritical, Hyperscale)
- *Underutilized Instance DTU Threshold (%)* - The DTU threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Only applies to DTU-model SQL databases (Basic, Standard, Premium)
- *Skip Instance Sizes* - Whether to recommend downsizing multiple sizes. When set to 'No', only the next smaller size will ever be recommended for downsizing. When set to 'Yes', more aggressive downsizing recommendations will be made when appropriate.
- *Automatic Actions* - When this value is set, this policy template will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Unused Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Sends an email notification
- Delete Azure SQL single database instance (if unused) after approval
- Downsize Azure SQL single database instance (if underutilized) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Sql/servers/read`
  - `Microsoft.Sql/servers/databases/read`
  - `Microsoft.Sql/servers/databases/metrics/read`
  - `Microsoft.Sql/servers/databases/update`*
  - `Microsoft.Sql/servers/databases/delete`*
  - `Microsoft.Insights/metrics/read`

  \* Only required for taking action (deleting or downsizing); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
