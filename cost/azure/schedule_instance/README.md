# Azure Schedule Instance

## What It Does

This Policy Template allows you to schedule start and stop times for your instance, along with the option to delete instance, update and delete schedule.

## How to Use

This policy relies on a tag (default key: schedule) to stop and start instances based on a schedule. The tag value defines the schedule with a start hour, stop hour and days of the week. The start and stop hour are in 24 hour format, and the days of the week are two character abbreviation for example: MO, TU, WE. See full example below. Use a Timezone TZ value to indicate a timezone to stop/start the instance(s)

### Schedule Tag Format

This policy uses `schedule` tag value for scheduling the instance. The format should be like `8:15-17:30;MO,TU,WE,TH,FR;America/New_York`. Please refer to `Schedule Tag Example` section for more details.
On leaving the minute field blank, policy will consider the minute as `00` and same will be added to the schedule tag value.

### Schedule Tag Example

Start and Stop hours are 24 hour format: for example 8:15-17:30 is start at 8:15am, and stop at 5:30pm.

Days of the week: SU,MO,TU,WE,TH,FR,SA

Timezone: Use the TZ database name from the timezone list. For example use America/New_York for Eastern time.

Example: schedule=8:15-17:30;MO,TU,WE,TH,FR;America/New_York. Starts instances at 8:15am, stops instance at 5:30pm, Monday - Friday, Eastern Time.

Instances are off during the weekend and start back up on Monday morning at 8:15am and are off at 5:30pm every weekday. Times are UTC unless the Timezone field is provided.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Schedule Tag Key* - Tag key that schedule information is stored in. Default is recommended for most use cases.
- *Next Start Tag Key* - Tag key to use for scheduling instance to start. Default is recommended for most use cases.
- *Next Stop Tag Key* - Tag key to use for scheduling instance to stop. Default is recommended for most use cases.
- *Allow/Deny Subscriptions* - Determines whether the Allow/Deny Subscriptions List parameter functions as an allow list (only providing results for the listed subscriptions) or a deny list (providing results for all subscriptions except for the listed subscriptions).
- *Allow/Deny Subscriptions List* - A list of allowed or denied Subscription IDs/names. If empty, no filtering will occur and recommendations will be produced for all subscriptions.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the regions.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
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

### Credential configuration

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

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
