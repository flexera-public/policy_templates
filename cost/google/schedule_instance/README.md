# Google Schedule Instance

## What it does

This Policy Template allows you to schedule start and stop times for your instance, along with the option to terminate instance, update and delete schedule.         

## How to Use

This policy relies on a label with format 'schedule' to stop and start instances based on a schedule. The label value defines the schedule with a start time(start hour and start minute), stop time(stop hour and stop minute), days of the week and timezone. The start and stop time are in 24 hour format, and the days of the week are two character abbreviation for example: mo, tu, we. See full example below.. Use a Timezone TZ value to indicate a timezone to stop/start the instance(s) 

## schedule Label Example

Since label supports only `-`, `_`, lowercase characters, numbers and International characters, We are replacing `:` with `m` in start and stop time, and ASCII code for special character `/` and `+` in timezone, surrounded by `_`.

Start and Stop time are 24 hour format: for example 8m30-17m15 is start at 8:30am, and stop at 5:15pm.

Days of the week: su-mo-tu-we-th-fr-sa

Timezone: Use the TZ database name from the timezone list in the mentioned format. For example use America/New_York as america_47_new_york for Eastern time and Etc/GMT+7 as etc_47_gmt_43_7.

Example: schedule=8m30-17m15_mo-tu-we-th-fr_america_47_new_york. Stops instances at 5:15pm, starts instance at 8:30am, Monday - Friday, Eastern Time.
Please note that `_` is being used for separating the start-stop time, days of the week and the timezone.

Instances are off during the weekend and start back up on Monday morning at 8:30am and are off at 5:15pm every weekday. Times are UTC unless the Timezone field is provided.

Note: On leaving the minute field blank, policy will consider the minute as `00` and same will be added to the schedule label value.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify  
- *Exclusion Tags* - A list of Google tags to ignore instances. Format: Key=Value. 
- *Automatic Action(s)* -(Optional) When this value is set, this policy will automatically take the selected action(s)

## Policy Actions 

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report  
- stop  - stop a selected instance
- start - start a selected instance
- terminate - terminates or deletes the selected instance.
- update schedule - change existing schedule tag.  input to provide a new stop/start schedule
- delete schedule - removes the schedule tag

## Prerequisites

### Schedule Label Format

This policy uses `schedule` label value for scheduling the instance. The format should be like `8m30-17m15_mo-tu-we-th-fr_america_47_new_york`. Please refer to `Schedule Label Example` section for more details.
On leaving the minute field blank, policy will consider the minute as `00` and same will be added to the schedule label value.

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the  cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If  there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential  that is compatible with this policy. The information below should be consulted when creating the credential.   

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `gce`

Required permissions in the provider:

- The `compute.instances.list` permission
- The `compute.instances.delete` permission
- The `compute.instances.setLabels` permission
- The `compute.instances.start` permission
- The `compute.instances.stop` permission
- The `resourcemanager.projects.get` permission
- The `compute.zones.list` permission

## Supported Clouds

- Google

## Cost

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs. This policy is not running on an instance and running it does not incur any costs.
