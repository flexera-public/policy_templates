# Google Schedule Instance

## What It Does

This policy schedules Google VM instances to start and stop at specific times based on a configuration stored in the instance's labels. The user can also perform a variety of ad hoc actions on the instance from the incident page.

## How To Use

This policy uses the schedule label value (default key: schedule) for scheduling the instance. The appropriate value should be added to as a label to every instance you want to manage via this policy.

This value is a string consisting of 3 underscore-separated substrings:

- *Hours* - Start and stop hours are in 4-digit 24-hour format without any colons or other separators. For example, a value of `0815-1730` will start instances at 8:15 and stop them at 17:30 (5:30 pm). If the minute field is left blank, the minute value of `00` will be assumed.
- *Days of the Week* - Hyphen-separated list of days indicated by their two-letter abbreviation value from the following list: su,mo,tu,we,th,fr,sa. For example, a value of `mo-tu-we-th-fr` will start and stop the instances on weekdays but not on weekends.
- *Timezone* - Timezone in [tz database format](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) with the `/` character replaced with a hyphen and all characters converted to lowercase. For example, a value of `america-new_york` would specify US Eastern Time. Defaults to UTC if no Timezone field is provided.

**Example Value:** 0815-1730_mo-tu-we-th-fr_america-new_york

- Starts instances at 8:15am
- Stops instance at 5:30pm
- Monday - Friday, US Eastern Time.

In the above example, instances are off during the weekend and start back up on Monday morning at 8:15am and are off at 5:30pm every weekday. Times are UTC unless the Timezone field is provided.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Schedule Label Key* - Label key that schedule information is stored in. Default is recommended for most use cases.
- *Next Start Label Key* - Label key to use for scheduling instance to start. Default is recommended for most use cases.
- *Next Stop Label Key* - Label key to use for scheduling instance to stop. Default is recommended for most use cases.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Labels (Key:Value)* - Google labels to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific label key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
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

This Policy Template requires that several APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - Permissions
    - `compute.instances.list`
    - `compute.instances.get`
    - `compute.instances.delete`
    - `compute.instances.setLabels`
    - `compute.instances.start`
    - `compute.instances.stop`
    - `compute.zones.list`
    - `resourcemanager.projects.get`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs. This policy is not running on an instance and running it does not incur any costs.
