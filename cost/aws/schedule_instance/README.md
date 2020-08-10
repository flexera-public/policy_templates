# AWS Schedule Instance

## What it does

This Policy Template allows you to schedule start and stop times for your instance, along with the option to terminate instance, update and delete schedule.         

## How to Use

This policy relies on a tag with format 'schedule' to stop and start instances based on a schedule. The tag value defines the schedule with a start hour, stop hour and days of the week. The start and stop hour are in 24 hour format, and the days of the week are two character abbreviation for example: MO, TU, WE. See full example below.. Use a Timezone TZ value to indicate a timezone to stop/start the instance(s) 

## Schedule Tag Example

Start and Stop hours are 24 hour format: for example 8:15-17:30 is start at 8:15am, and stop at 5:30pm.

Days of the week: SU,MO,TU,WE,TH,FR,SA

Timezone: Use the TZ database name from the timezone list. For example use America/New_York for Eastern time.

Example: schedule=8:15-17:30;MO,TU,WE,TH,FR;America/New_York. Starts instances at 8:15am, stops instance at 5:30pm, Monday - Friday, Eastern Time.

Instances are off during the weekend and start back up on Monday morning at 8:15am and are off at 5:30pm every weekday. Times are UTC unless the Timezone field is provided.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - A list of email addresses to notify  
- *Exclusion Tags* - A list of AWS tags to ignore instances. Format: Key=Value. 
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Schedule Instances" action while applying the policy, the identified resources will be stopped or started as per the schedule.

## Policy Actions 

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report  
- schedule  - start or stop a selected instance
- terminate - terminates or deletes the selected instance.
- update schedule - change existing schedule tag.  input to provide a new stop/start schedule. The format is schedule=new_schedule
- delete schedule - removes the schedule tag

## Prerequisites

### Schedule Tag Format

This policy uses `schedule` tag value for scheduling the instance. The format should be like `8:15-17:30;MO,TU,WE,TH,FR;America/New_York`. Please refer to `Schedule Tag Example` section for more details.
On leaving the minute field blank, policy will consider the minute as `00` and same will be added to the schedule tag value.

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the  cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If  there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential  that is compatible with this policy. The information below should be consulted when creating the credential.   

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `aws`

Required permissions in the provider:

```
{   
  "Version": "2012-10-17",   
  "Statement": [{      
    "Effect": "Allow",      
    "Action": [         
      "ec2:DescribeInstances",         
      "ec2:StartInstances",
      "ec2:StopInstances",
      "ec2:TerminateInstances",
      "ec2:CreateTags",
      "ec2:DeleteTags"
    ],
    "Resource": "*" 
  }]
} 
```

## Supported Clouds

- AWS

## Cost

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs. This policy is not running on an instance and running it does not incur any costs.
