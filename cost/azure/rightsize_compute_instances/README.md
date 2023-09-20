# Azure Rightsize Compute Instances

## What it does

This policy checks all the instances in Azure Subscriptions for the average or maximum CPU and/or memory usage over a user-specified number of days. If the usage is less than the user provided Idle Instance CPU and/or memory percentage threshold then the Virtual Machine is recommended for deletion. If the usage is less than the user provided Underutilized Instance CPU and/or Memory percentage threshold then the Virtual Machine is recommended for downsizing. Both sets of Virtual Machines returned from this policy are emailed to the user.

## Functional Details

- The policy leverages the Azure API to check all instances and then checks the instance average or maximum CPU and memory utilization over a user-specified number of days.
- The policy identifies all instances that have CPU and/or memory utilization below the user-specified idle thresholds and provides the relevant recommendation.
- The recommendation provided for Idle Instances is a deletion action. These instances can be deleted in an automated manner or after approval.
- The policy identifies all instances that have CPU and/or memory utilization below the user-specified underutilized thresholds and provides the relevant recommendation.
- The recommendation provided for Underutilized Instances is a downsize action. These instances can be downsized in an automated manner or after approval.

### Policy savings details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is deleted or downsized. Optima is used to retrieve and calculate the estimated savings which is the cost of the resource for a full day (3 days ago) multiplied by 30.44 (the average number of days in a month) or 0 if no cost information for the resource was found in Optima. The savings is displayed in the Estimated Monthly Savings column. The incident message detail includes the sum of each resource *Estimated Monthly Savings* as *Potential Monthly Savings*.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Idle Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'idle' and therefore be flagged for deletion. Set to -1 to ignore CPU utilization for idle instance recommendations.
- *Idle Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'idle' and therefore be flagged for deletion. Set to -1 to ignore memory utilization for idle instance recommendations.
- *Underutilized Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore CPU utilization for underutilized instance recommendations.
- *Underutilized Instance Memory Threshold (%)* - The Memory threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore memory utilization for underutilized instance recommendations.
- *Idle/Utilized for both CPU/Memory or either* - Set whether an instance should be considered idle and/or underutilized only if both CPU and memory are under the thresholds or if either CPU or memory are under. Has no effect if other parameters are configured such that only CPU or memory is being considered.
- *Threshold Statistic* - Statistic to use when determining if an instance is idle/underutilized.
- *Statistic Lookback Period* - How many days back to look at CPU and/or memory data for instances. This value cannot be set higher than 90 because Azure does not retain metrics for longer than 90 days.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore instances that you don't want to consider for downsizing or deletion. Format: Key:Value
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Delete Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Sends an email notification
- Delete virtual machines (if idle) after approval
- Downsize virtual machines (if underutilized) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`*
  - `Microsoft.Compute/skus/read`
  - `Microsoft.Insights/metrics/read`

\* Only required for taking action (deleting or downsizing); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs
