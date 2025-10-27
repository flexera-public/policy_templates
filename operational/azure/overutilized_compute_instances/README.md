# Azure Overutilized Compute Instances

## What It Does

This policy template checks all the instances in Azure Subscriptions for the average or maximum CPU and/or memory usage over a user-specified number of days. If the usage is greater than the user provided Instance CPU and/or memory percentage threshold then the virtual machine is recommended for upsizing.

## How It Works

- The policy leverages the Azure API to check all instances and then checks the instance average or maximum CPU and memory utilization over a user-specified number of days.
- The policy identifies all instances that have CPU and/or memory utilization above the user-specified thresholds and provides the relevant recommendation.
- The recommendation provided is an upsize action. These instances can be upsized in an automated manner or after approval.

### Policy Costs Details

The policy includes the estimated monthly costs. The estimated monthly costs will be incurred for resources that are upsized.

- The `Estimated Monthly Cost` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- The cost of the upsize action is the full cost of the resource. This is because upsizing a virtual machine doubles the cost.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Cost` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Cost` as `Potential Monthly Cost`.
- Both `Estimated Monthly Cost` and `Potential Monthly Cost` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclude Stopped Virtual Machines* - Whether or not to filter stopped virtual machines from the results. If set to `Yes`, only running virtual machines will be included in the results.
- *Exclude Databricks* - Whether or not to filter virtual machines used for Azure Databricks from the results. If set to `Yes`, virtual machines for Azure Databricks will not be included in the results.
- *Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'overutilized' and therefore be flagged for upsizing. Set to -1 to ignore CPU utilization.
- *Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'overutilized' and therefore be flagged for upsizing. Set to -1 to ignore memory utilization.
- *Both CPU and Memory or Either* - Set whether an instance should be considered overutilized only if both CPU and memory are over the thresholds or if either CPU or memory are over.
- *Threshold Statistic* - Statistic to use when determining if an instance is overutilized.
- *Statistic Interval* - The interval to use when gathering Azure metrics data. Smaller intervals produce more accurate results at the expense of policy memory usage and completion time due to larger data sets.
- *Statistic Lookback Period* - How many days back to look at CPU and/or memory data for instances. This value cannot be set higher than 90 because Azure does not retain metrics for longer than 90 days.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Upsize Overutilized Instances" action while applying the policy template, all reported overutilized virtual machines will be upsized.

## Policy Actions

- Sends an email notification
- Upsize virtual machines after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Insights/metrics/read`
  - `Microsoft.Compute/skus/read`
  - `Microsoft.Compute/locations/vmSizes/read`
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
