# Azure Rightsize Managed Disks

## What it does

This Policy Template scans all volumes in the given account and identifies any volume that meets the user-specified criteria for being oversized. The user can filter volumes based on usage percentage of capacity (GiB used), usage percentage of IOPS, usage percentage of throughput, or any combination of these. Any volumes that meet the user-specified criteria are considered oversized. If any oversized volumes are found, an incident report will show the volumes and related information. An email will be sent to the user-specified email addresses.

- It is important that you keep constant LUN numbers for your data disks because when policy retrieves metrics for them. It will only look for the latest LUN number assigned to the data disk; if changed multiple times before running the policy, only the data points using the current LUN the disk has will be retrieved for analysis.
- Currently the policy only works for righsizing using the disk used IOPS and throughput since disk capacity (GiB) is not retrievable from Azure.

### Policy Saving Details

The policy includes the estimated monthly savings. The estimated monthly savings are recognized if the resource is terminated.

- The `Estimated Monthly Savings` is calculated by obtaining the price of the disk per month from the Azure Pricing API.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.

## Input parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Minimum Used Disk Space %* - The minimum used disk space percentage threshold at which to consider a disk to be 'oversized' and therefore be flagged for downsizing. **Currently this parameter is not supported by the policy due that it is not possible to get the available capacity from Azure.**
- *Minimum Used Disk IOPS %* - The minimum used disk IOPS percentage threshold at which to consider a disk to be 'oversized' and therefore be flagged for downsizing.
- *Aggregation Type For Disk IOPS* - Statistic to use when determining if the disk IOPS is more than the disk actually uses.
- *Minimum Used Disk Throughput %* - The minimum used disk throughput percentage threshold at which to consider a disk to be 'oversized' and therefore be flagged for downsizing.
- *Aggregation Type For Disk Throughput* - Statistic to use when determining if the disk throughput is more than the disk actually uses.
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

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*).

This is only required for the application of the metaparent policy.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
