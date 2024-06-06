# Azure Rightsize Synapse SQL Pools

## What It Does

This policy checks for Synapse Dedicated SQL Pools instances that have inefficient utilization for the last N days and recommend downsizes or pauses them after approval.

## How It Works

- The policy leverages the Azure API to check all Synapse SQL Pools and then checks the instance metrics (DWU Used Percent, CPU Percent, Memory Used Percent, Connections) over a user-specified number of days.
- The policy identifies all instances that have metrics below the user-specified thresholds and provides the relevant recommendation.
- The recommendation provided for idle instances (no connections) is a pause action. These instances can be paused in an automated manner or after approval.
- The Recommendations to downsize underutilized instances are also generated for review and approval. 

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for idle resources if the resource is paused, and for underutilized resources if the resource is downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day by 30.44, which is the average number of days in a month.
- For idle resources, the savings is the full cost of the resource. For underutilized resources, the savings is the difference between the current cost and the cost after downsizing.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email addresses* - A list of email addresses to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Use the default value of management.azure.com unless using Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as an allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all regions.
- *Threshold* - Threshold to use when determining if a pool is underutilized.
- *Statistic Lookback Period* - How many days back to look at metrics. This value cannot be set higher than 90 because Azure does not retain metrics for longer than 90 days.
- *Minimum Time Active (Days)* - Only include pools in the results if they have not been paused for at least the number of specified days. Set to '0' to disable this filter and not consider minimum time active in the results.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Enable Automatic Pausing* - When this value is set, this policy will automatically pause the selected underutilized Synapse SQL Pools.

## Policy Actions

- Sends an email notification
- Pause Synapse SQL Pools (if idle) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Insights/metrics/read`
  - `Microsoft.Synapse/workspaces/read`
  - `Microsoft.Synapse/sqlPools/read`
  - `Microsoft.Synapse/sqlPools/pause/action`
  - `Microsoft.Synapse/sqlPools/resume/action`
  - `Microsoft.Synapse/sqlPools/write`
  - `Microsoft.Synapse/sqlPools/delete`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
