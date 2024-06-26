# Azure Rightsize Managed Disks

## What It Does

This policy template checks managed disks in Azure subscriptions and identifies underutilized disks based on disk performance metrics over a lookback period and a threshold specified by the user; if underutilized disks are found, then disk type downgrade is recommended. An email will be sent to the user-specified email addresses.

Note: It is preferred to keep the disk LUN number constant when detaching and re-attaching a data disk to a virtual machine. LUN number is used to retrieve disk performance metrics (IOPs and throughput).

Note: This policy template does not currently produce recommendations or reporting on used disk space. This is because disk space usage is not something that can easily be assessed for managed disks. Disk space usage is contextual based on how the disk is partitioned and used by an operating system and can't meaningfully be assessed outside of that context.

### Policy Saving Details

The policy includes the estimated monthly savings. The estimated monthly savings are recognized if the resource is resized to the suggested size.

- The `Estimated Monthly Savings` is calculated by obtaining the price of the disk per month from the Azure Pricing API.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
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
- *SKU Ignore List* - A list of disk SKUs to ignore and not include in the results. To remove HDDs from the results, add `Standard_LRS` and `Standard_ZRS` to this list. Leave blank to produce recommendations for all SKUs.
- *IOPS Threshold (%)* - The IOPS threshold percentage at which to consider a managed disk to be underutilized.
- *IOPS Threshold Statistic* - Statistic to use for IOPS when determining if a managed disk is underutilized.
- *Throughput Threshold (%)* - The throughput threshold at which to consider a managed disk to be underutilized.
- *Throughput Threshold Statistic* - Statistic to use for throughput when determining if a managed disk is underutilized.
- *Lookback Period* - How many days back to look at disk IOPS and throughput data. This value cannot be set higher than 90 because Azure does not retain metrics for longer than 90 days.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/disks/read`
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Insights/metrics/read`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
