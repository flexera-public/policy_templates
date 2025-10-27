# AWS Schedule Instance

## What It Does

This policy template schedules AWS EC2 instances to start and stop at specific times based on a configuration stored in the instance's tags. The user can also perform a variety of ad hoc actions on the instance from the incident page.

## How To Use

This policy template uses the schedule tag value (default key: schedule) for scheduling the instance. The appropriate value should be added to as a tag to every instance you want to manage via this policy.

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

### Schedule Action Tag (Optional)

You can optionally use a Schedule Action tag (default key: schedule_action) to specify the behavior during and outside the scheduled window. Supported values are:

- `startstop` (default if not specified) - Start instances during the window, stop them outside the window
- `start` - Only start instances during the window, never automatically stop them
- `stop` - Only stop instances during the window, never automatically start them

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Schedule Tag Key* - Tag key that schedule information is stored in. Default is recommended for most use cases.
- *Schedule Action Tag Key (Optional)* - Optional tag key to specify what action to use. Expected values are "startstop", "start", "stop". Default behavior is "startstop" if not specified.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Enforce Schedules* - Whether to enforce schedules on instances that are not in the correct state. If set to 'No', the policy will not action if the instance is not in the expected state when an action is to be taken.

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Schedule Instances" action while applying the policy, the identified resources will be stopped or started as per the schedule.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report.
- *Execute Schedules* - Power the resources on or off as needed based on their schedules
- *Update Schedules* - Update the schedule tag on the resources with a new schedule
- *Delete Schedules* - Delete all schedule tags from the resource so that it is no longer powered on or off by this policy
- *Start Instances* - Start the resources if they are not currently running.
- *Stop Instances* - Stop the resources if they are currently running.
- *Terminate Instances* - Terminate the resources.

## Error Handling and Retry Logic

This policy includes sophisticated error handling and retry mechanisms:

- Each start/stop operation is attempted up to 3 times if it fails
- Detailed error messages are collected and reported for troubleshooting
- The policy verifies that instances reach the expected state after operations
- If all retry attempts fail, comprehensive error information is provided in the incident

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeInstances`
  - `ec2:StartInstances`*
  - `ec2:StopInstances`*
  - `ec2:DeleteTags`*
  - `ec2:DescribeRegions`
  - `kms:CreateGrant`*§
  - `kms:Decrypt`*§
  - `ec2:CreateTags`*†
  - `ec2:TerminateInstances`*‡

  \* These permissions enable taking actions against cloud resources.

  † Only required for `Update Schedule` Action; the policy will still start/stop instance without this permission.

  ‡ Only required for `Terminate Instance` Action; the policy will still start/stop instance without this permission.

  § Only required if using Customer Managed KMS Key on Volumes mounted by EC2 Instance(s)

  Example IAM Permission Policy:

  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
            "ec2:DescribeInstances",
            "ec2:StartInstances",
            "ec2:StopInstances",
            "ec2:TerminateInstances",
            "ec2:CreateTags",
            "ec2:DeleteTags",
            "ec2:DescribeRegions",
            "kms:CreateGrant",
            "kms:Decrypt"
        ],
        "Resource": "*"
      }
    ]
  }
  ```

  If Customer Managed KMS Keys are used to encrypt volumes that are mounted by the EC2 Instance then the KMS Key(s) Permission Policy needs to allow `kms:CreateGrant` and `kms:Decrypt` permissions to the IAM Role used by Flexera Policy Template.

  Here's an example Statement entry for the KMS Permission Policy:

  ```json
  {
      "Sid": "Allow use of the key",
      "Effect": "Allow",
      "Principal": {
          "AWS": "arn:aws:iam::123456789012:role/FlexeraAutomationAccessRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*"
  },
  {
      "Sid": "Allow attachment of persistent resources",
      "Effect": "Allow",
      "Principal": {
          "AWS": "arn:aws:iam::123456789012:role/FlexeraAutomationAccessRole"
      },
      "Action": "kms:CreateGrant",
      "Resource": "*",
      "Condition": {
          "Bool": {
              "kms:GrantIsForAWSResource": "true"
          }
      }
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs. This policy template is not running on an instance and running it does not incur any costs.
