# AWS Schedule Instance

## What It Does

This Policy Template allows you to schedule start and stop times for your instance, along with the option to terminate instance, update and delete schedule.

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
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Schedule Tag Key* - Tag key that schedule information is stored in. Default is recommended for most use cases.
- *Next Start Tag Key* - Tag key to use for scheduling instance to start. Default is recommended for most use cases.
- *Next Stop Tag Key* - Tag key to use for scheduling instance to stop. Default is recommended for most use cases.
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

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

## Prerequisites

### Credential configuration

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeInstances`
  - `ec2:StartInstances`
  - `ec2:StopInstances`
  - `ec2:TerminateInstances`
  - `ec2:CreateTags`
  - `ec2:DeleteTags`
  - `ec2:DescribeRegions`
  - `kms:CreateGrant` `*`
  - `kms:Decrypt` `*`

  `*` Only required if using Customer Managed KMS Key on Volumes mounted by EC2 Instance(s)

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

The policy template will start instances and those instances will incur costs. The stopped instances will not incur costs. This policy is not running on an instance and running it does not incur any costs.
