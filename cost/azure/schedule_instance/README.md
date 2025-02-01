# Azure Schedule Instance

## What It Does

This policy schedules Azure virtual machines to start and stop at specific times based on a configuration stored in the virtual machine's tags. The user can also perform a variety of ad hoc actions on the virtual machine from the incident page.

## How To Use

This policy uses the schedule tag value (default key: schedule) for scheduling the instance. The appropriate value should be added to as a tag to every instance you want to manage via this policy.

### Example Schedule Tables

- `schedule` = `00:00-12:00;SU,SA`
  Start at 12am (midnight) and stop at 12pm (noon) on Saturday and Sunday (default timezone is UTC)

- `schedule` = `08:15-17:30;MO,TU,WE,TH,FR;America/New_York`
  Start at 8:15am and stop at 5:30pm every weekday in US Eastern Time (America/New York)

### Schedule Label Format

`<Schedule Label>` = `<Hours>;<Days of the Week>[;<Optional Timezone>]`

The Schedule Label value is a string consisting of 2 or 3 semicolon-separated (`;`) substrings (Hours, Days of the Week, and optional Timezone) with the following format:

- *Hours* - Start and stop hours are 24 hour format. For example, a value of `8:15-17:30` will start instances at 8:15 and stop them at 17:30 (5:30 pm). If the minute field is left blank, the minute value of `00` will be assumed.
- *Days of the Week* - Comma-separated list of days indicated by their two-letter abbreviation value from the following list: SU,MO,TU,WE,TH,FR,SA. For example, a value of `MO,TU,WE,TH,FR` will start and stop the instances on weekdays but not on weekends.
- Optional: *Timezone* - Timezone in [tz database format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). For example, a value of `America/New_York` would specify US Eastern Time. Defaults to UTC if no Timezone field is provided.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Schedule Tag Key* - Tag key that schedule information is stored in. Default is recommended for most use cases.
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
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Power Off Type* - Whether to perform a graceful shutdown or a forced shutdown when powering off idle instances. Only applicable when taking action against instances.

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Schedule Instances" action while applying the policy, the identified resources will be stopped or started as per the schedule.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report.
- *Execute Schedules* - Power the resources on or off as needed based on their schedules
- *Update Schedules* - Update the schedule tag on the resources with a new schedule
- *Delete Schedules* - Delete all schedule tags from the resource so that it is no longer powered on or off by this policy
- *Power On Instances* - Power on the resources if they are not currently running.
- *Power Off Instances* - Power off the resources if they are currently running.
- *Delete Instances* - Delete the resources.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`
  - `Microsoft.Compute/virtualMachines/delete`
  - `Microsoft.Compute/virtualMachines/start/action`
  - `Microsoft.Compute/virtualMachines/deallocate/action`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

The policy template will start virtual machines and those virtual machines will incur costs. The stopped virtual machines will not incur costs. This policy is not running on a virtual machine and running it does not incur any costs.
