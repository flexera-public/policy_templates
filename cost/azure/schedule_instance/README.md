# Azure Schedule Instance

## What it does

This Policy Template allows you to schedule start and stop times for your instance, along with the option to terminate instance, update and delete schedule.         

## How to Use

This policy relies on a tag with format 'schedule' to stop and start instances based on a schedule. The tag value defines the schedule with a start time (start hour and start minute), stop time (stop hour and stop minute) and days of the week and timezone. The start and stop time are in 24-hour format, and the days of the week are two character abbreviation for example: MO, TU, WE. See full example below. Use a Timezone TZ value to indicate a timezone to stop/start the instance(s) 

## Schedule Tag Example

Start and Stop hours are 24-hour format: for example 8:15-17:30 is start at 8:15am, and stop at 5:30pm.

Days of the week: SU, MO, TU, WE, TH, FR, SA

Timezone: Use the TZ database name from the timezone list. For example, use America/New_York for Eastern time.

Example: schedule=8:15-17:30;MO,TU,WE,TH,FR;America/New_York. Starts instances at 8:15am, stops instance at 5:30pm, Monday - Friday, Eastern Time.

Instances are off during the weekend and start back up on Monday morning at 8:15am and are off at 5:30pm every weekday. Times are UTC unless the Timezone field is provided.

Note: On leaving the minute field blank, policy will consider the minute as `00`
and same will be added to the schedule label value.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify  
- *Exclusion Tags* - List of tags that an Instance can have to exclude it from the list. Format: Key=Value.
- *Automatic Actions(s)* - (Optional)When this value is set, this policy will automatically take the selected action(s).

## Policy Actions 

The following policy actions are taken on any resources found to be out of compliance.
 
- Send an email report  
- stop - stop a selected instance
- start - start a selected instance
- terminate - terminates or deletes the selected instance.
- update schedule - change existing schedule tag.  input to provide a new stop/start schedule
- delete schedule - removes the schedule tag

## Prerequisites

### Schedule Label Format

This policy uses `schedule` tag value for scheduling the instance. The format should be like `8:15-17:30;MO,TU,WE,TH,FR;America/New_York`. Please refer to `Schedule Tag Example` section for more details.
On leaving the minute field blank, policy will consider the minute as `00` and same will be added to the schedule tag value.

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin, and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.   

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure`

Required permissions in the provider:

- Microsoft.Compute/virtualMachines/read
- Microsoft.Compute/virtualMachines/write
- Microsoft.Compute/virtualMachines/delete
- Microsoft.Compute/virtualMachines/start/action
- Microsoft.Compute/virtualMachines/powerOff/action

## Supported Clouds

- Azure

## Cost

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs. This policy is not running on an instance and running it does not incur any costs.
