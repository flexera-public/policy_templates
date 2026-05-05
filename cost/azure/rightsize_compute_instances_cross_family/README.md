# Azure Rightsize Compute Instances (Cross-Family)

## What It Does

This policy template identifies Azure virtual machines that are idle or underutilized and recommends the cheapest available instance type across all Azure VM families that satisfies the workload's requirements. Unlike within-family rightsizing, this template scans every available VM SKU in the region and selects the optimal replacement based on observed p95 CPU and memory utilization, a configurable safety factor, and a set of hard compatibility gates. Idle instances (those whose average CPU utilization falls below a configurable threshold) are flagged for termination or power-off. Underutilized instances are recommended for cross-family rightsizing when a cheaper, compatible alternative is available. The policy integrates with Flexera Cloud Cost Optimization (CCO) to calculate estimated monthly savings from each recommendation.

## How It Works

For each running Azure virtual machine, the policy collects CPU and memory metrics from Azure Monitor over the configured lookback period at 15-minute granularity. It then determines whether the instance is idle or underutilized:

- **Idle detection:** If the average CPU utilization over the lookback period falls below a size-adjusted threshold, the instance is flagged as idle. The threshold scales with vCPU count to account for the fact that larger instances handling real workloads typically show lower overall CPU percentages: ≤2 vCPUs → 5%, ≤4 vCPUs → 4%, ≤8 vCPUs → 3%, ≤16 vCPUs → 2%, >16 vCPUs → 1%. The estimated monthly savings equals the full CCO-reported monthly cost.
- **Cross-family rightsizing:** For non-idle instances, the policy computes required vCPUs and memory using the p95 utilization values multiplied by the `Rightsizing Safety Factor`. It then scans all available VM SKUs in the subscription and region, filtering candidates through compatibility gates, and selects the cheapest qualifying candidate that is also cheaper than the current instance. The estimated monthly savings is the CCO cost multiplied by the ratio of the price reduction.

**Compatibility gates applied to every candidate instance:**

1. Must be available in the VM's subscription and region (via the Azure vmSizes API)
1. Must share the same CPU architecture (x86_64 or Arm64) — never cross architecture families
1. Intel/AMD vendor match enforced by default (configurable via `Allow Intel/AMD Recommendations`)
1. Must meet the required vCPU count (p95 usage × safety factor, rounded up)
1. Must meet the required memory (p95 usage × safety factor; current memory used as minimum when memory data unavailable)
1. Must support all Hyper-V generations supported by the current instance
1. Premium storage support preserved (if current instance supports Premium IO, candidate must too)
1. Local/temporary disk preserved (if current instance has local disk, candidate must too)
1. Data disk capacity preserved (candidate must support at least as many data disks as currently attached)
1. NIC count preserved (candidate must support at least as many NICs as currently attached)
1. Accelerated networking preserved (if current instance has accelerated networking, candidate must too)

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is resized, deleted, or powered off.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- For rightsizing recommendations, the savings is further scaled by the ratio `(currentListPrice - recommendedListPrice) / currentListPrice` derived from the Azure VM pricing data.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.
- Instances for which memory utilization data is not available (Azure Monitor Agent not installed) will use the current memory size as the minimum memory requirement. These recommendations are marked with `Memory Data Available: No` in the incident report.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Azure Endpoint* - Select the API endpoint to use for Azure. Use default value of `management.azure.com` unless using Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Allow/Deny Subscriptions* - Allow or Deny entered subscriptions. See the README for more details.
- *Allow/Deny Subscriptions List* - A list of allowed or denied subscription IDs/names. See the README for more details.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Allow Intel/AMD Recommendations* - Whether to allow rightsizing recommendations that change the CPU manufacturer between Intel and AMD (both x86_64 architecture). Such recommendations are generally safe but may affect licensing or workload performance.
- *Statistic Lookback Period* - How many days back to look at CPU and memory data for instances. This value cannot be set higher than 90 because Azure does not retain metrics for longer than 90 days.
- *Rightsizing Safety Factor* - A multiplier applied to p95 utilization when computing the required resources for a rightsized instance. For example, 1.5x means the recommended instance must handle 1.5 times the observed peak utilization.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action. Allowed values: `Downsize Underutilized Instances`, `Power Off Idle Instances`, `Delete Idle Instances`.
- *Power Off Type* - Whether to perform a graceful shutdown or a forced shutdown when powering off idle instances.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Delete Idle Instances" action while applying the policy template, all idle virtual machines will be deleted.

## Policy Actions

- Sends an email notification
- Power off virtual machines (if idle) after approval
- Delete virtual machines (if idle) after approval
- Downsize virtual machines (if underutilized) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#azure-resource-manager) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Insights/metrics/read`
  - `Microsoft.Compute/locations/vmSizes/read`
  - `Microsoft.Compute/virtualMachines/write`*
  - `Microsoft.Compute/virtualMachines/powerOff/action`*
  - `Microsoft.Compute/virtualMachines/delete`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This policy template does not incur any cloud costs.
