# Google Schedule Instance

## What It Does

This policy schedules Google VM instances to start and stop at specific times based on a configuration stored in the instance's labels. The user can also perform a variety of ad hoc actions on the instance from the incident page.

## How To Use

This policy uses the schedule label value (default key: `schedule`) for scheduling the instance. The appropriate value should be added to as a label to every instance you want to manage via this policy.

### Example Schedule Labels

- `schedule` = `0000-1200_sa-sun`
  Start at 12am (midnight) and stop at 12pm (noon) on Saturday and Sunday (UTC timezone)
- `schedule` = `0815-1730_mo-tu-we-th-fr_america-new_york`
  Start at 8:15am and stop at 5:30pm every weekday in US Eastern Time (America/New York)

### Schedule Label Format

`<Schedule Label>` = `<Hours>_<Days of the Week>[_<Optional Timezone>]`

The Schedule Label value is a string consisting of 2 or 3 underscore-separated (`_`) substrings (Hours, Days of the Week, and optional Timezone) with the following format:

- *Hours* - Start and stop hours are in 4-digit 24-hour format without any colons or other separator (`HHMM-HHMM`). For example, a value of `0815-1730` will start instances at 8:15am and stop them at 17:30 (5:30 pm). If the minute field is left blank, the minute value of `00` will be assumed.
- *Days of the Week* - Hyphen-separated (`-`) list of days indicated by their two-letter abbreviation value from the following list: `su`,`mo`,`tu`,`we`,`th`,`fr`,`sa`.
  For example, a value of `mo-tu-we-th-fr` will start and stop the instances on weekdays (Monday-Friday) but not on weekends (Saturday or Sunday).
- Optional: *Timezone* - Timezone in [tz database format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).  Due to limitations for Google Labels the `/` character is replaced with a hyphen (`-`), spaces (` `) replaced with underscores (`_`), and all characters converted to lowercase. For example, a schedule label value of `america-new_york` would translate to `America/New York`. Defaults to UTC if no Timezone value is defined in schedule.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Schedule Label Key* - Label key that schedule information is stored in. Default is recommended for most use cases.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Labels` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report.
- *Execute Schedules* - Start or stop the resources as needed based on their schedules
- *Update Schedules* - Update the schedule tag on the resources with a new schedule
- *Delete Schedules* - Delete all schedule tags from the resource so that it is no longer powered on or off by this policy
- *Start Instances* - Start the resources if they are not currently running.
- *Stop Instances* - Stop the resources if they are currently running.
- *Delete Instances* - Delete the resources.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

This Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `compute.zones.list`
  - `compute.instances.list`
  - `compute.instances.get`
  - `compute.instances.start`
  - `compute.instances.stop`
  - `compute.instances.delete`†
  - `compute.instances.setLabels`*

† Only required for `Terminate Instance` Action; the policy will still start/stop instance without this permission.

\* Only required for `Update Schedule` Action; the policy will still start/stop instance without this permission.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs. This policy is not running on an instance and running it does not incur any costs.
