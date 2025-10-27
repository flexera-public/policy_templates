# Google Overutilized VM Instances

## What It Does

This policy template checks all Google VM instances in the account for CPU usage over a user-specified number of days. If the usage is above the user provided CPU percentage threshold, it is recommended for upsizing. Optionally, a list of oversized Google VM instances is emailed.

## How It Works

- The policy leverages the [Google Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com) to retrieve all VM instances and then uses the [Google Cloud Monitoring API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com) to check the instance CPU utilization over a specified number of days.
- The utilization data is provided for the following statistics: Average, Maximum, Minimum, 99th percentile, 95th percentile, 90th percentile. Data is normalized by core count so that 100% represents 100% usage of all cores on the instance.
- The policy identifies all instances that have CPU utilization above the CPU Threshold defined by the user. The recommendation provided for oversized VM instances is upsizing.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects
- *Ignore System Projects* - Whether or not to automatically ignore system projects e.g. projects whose id begins with `sys-`
- *Ignore Google Apps Script Projects* - Whether or not to automatically ignore Google Apps Script projects e.g. projects whose id begins with `app-`
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Labels` field.
- *CPU Threshold (%)* - The CPU threshold at which to consider an instance to be overutilized and therefore be flagged for upsizing.
- *Threshold Statistic* - Statistic to use when determining if an instance is overutilized.
- *Statistic Lookback Period* - How many days back to look at CPU data for instances. This value cannot be set higher than 42 because Google does not retain metrics for longer than 42 days.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example, if a user selects the "Upsize VM Instances" action while applying the policy, all oversized VM instances will be upsized.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Upsize overutilized VM instances after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `monitoring.metricDescriptors.list`
  - `monitoring.timeSeries.list`
  - `compute.instances.list`
  - `compute.instances.get`
  - `compute.instances.start`*
  - `compute.instances.stop`*
  - `compute.instances.setMachineType`*
  - `compute.machineTypes.list`

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Monitoring API](https://console.cloud.google.com/flows/enableapi?apiid=monitoring.googleapis.com)
- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
