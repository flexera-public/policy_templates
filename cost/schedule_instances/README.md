### Schedule Instances Policy Template

**What it does**

This Policy Template allows you to schedule start and stop times for your compute.

**How to Use**

This policy relies on a RightScale tag 'instance:schedule' to stop and start instances based on a schedule.  The tag value defines the schedule with a start hour, stop hour and days of the week.  The start and stop hour are in 24 hour format, and the days of the week are two character abbreviation for example: MO, TU, WE. See full example below..  Use a Timezone TZ value to indicate a timezone to stop/start the instance(s)

***instance:schedule Tag Example***

Start and Stop hours are 24 hour format: for example 8-17 is start at 8am, and stop at 5pm.
Days of the week: SU,MO,TU,WE,TH,FR,SA
Timezone: Use the TZ database name from the (timezone list)[https://en.wikipedia.org/wiki/List_of_tz_database_time_zones].  For Example, Eastern time use America/New_York

Example: instance:schedule=8-17;MO,TU,WE,TH,FR;America/New_York. Stops instances at 5pm, starts instance at 8am, Monday - Friday, Eastern Time.  

Instances are off during the weekend and start back up on Monday morning and are off at 5p every weekday.
Times are UTC unless the Timezone field is provided.

Use the (Untagged Resource Policy)[https://github.com/rightscale/policy_templates/tree/master/compliance/tags/tag_checker] to automate creating the instance:schedule tag.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

### Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Stop and Start the instances with the schedule tag.
- Send an email report

### Required Permissions

This policy requires permissions to access RightScale resources (clouds, instances and tags).  Before applying this policy add the following roles to the user applying the policy.  The roles should be applied to all Accounts where the policy will run or the Organization. For more information on modifying roles visit the [Governance Docs](https://docs.rightscale.com/cm/ref/user_roles.html)

- Cloud Management - Actor
- Cloud Management - Observer

## Supported Clouds

The following clouds are supported:
- AWS
- Azure
- Google
- vSphere
- any RightScale supported instance that supports stop/start functionality

**Cost**

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs.  This policy is not running on an instance and running it does not incur any costs.
