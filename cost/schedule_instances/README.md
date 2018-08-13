### Schedule Instances Policy Template

**What it does**

This Policy Template allows you to schedule start and stop times for your compute.

**How to Use**

This policy relies on a RightScale tag 'instance:schedule' to stop and start instances based on a schedule.  The tag value defines the schedule with a start hour, stop hour and days of the week.  The start and stop hour are in 24 hour format, and the days of the week are two character abbreviation for example: MO, TU, WE. See full example below..  Use a Timezone TZ value to indicate a timezone to stop/start the instance(s)

***instance:schedule Tag Example***

Start and Stop hours are 24 hour format: for example 8-17 is start at 8am, and stop at 5pm.
Days of the week: SU,MO,TU,WE,TH,FR,SA
Timezone: Use the TZ designator from the timezone list.  For Eastern time use America/New_York

Example: instance:schedule=8-17;MO,TU,WE,TH,FR;America/New_York. Stops instances at 5pm, starts instance at 8am, Monday - Friday, Eastern Time.  

Instances are off during the weekend and start back up on Monday morning and are off at 5p every weekday.
Times are UTC unless the Timezone field is provided.

Use the (Untagged Resource Policy)[https://github.com/rightscale/policy_templates/tree/master/compliance/tags/tag_checker] to automate creating the instance:schedule tag.

## Supported Clouds

The following clouds are supported:
- AWS
- Azure
- Google
- vSphere
- any RightScale supported instance that supports stop/start functionality

**Cost**

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs.  This policy is not running on an instance and running it does not incur any costs.
