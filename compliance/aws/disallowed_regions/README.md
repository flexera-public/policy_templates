# AWS Disallowed Regions

## What it does

This policy checks all instances outside of a set of allowed regions. The user is given the option to Terminate the instance after approval.

## Functional Details

- The policy leverages the AWS API to check all instances that exist outside of an allowed region.
- When an EC2 instance in disallowed region is detected, an email action is triggered automatically to notify the specified users of the incident. Users then have the option to terminate instances after manual approval if needed.

## Input Parameters

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Exclusion Tag* - List of tags that will exclude EC2 instances from being evaluated by this policy. Multiple tags are evaluated as an 'OR' condition. Tag keys or key/value pairs can be listed. Example: 'test,env=dev'.
- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Note:Refer Region column under Amazon Elastic Compute Cloud (Amazon EC2) in below link for AWS supported regions \n See the [README](https://docs.aws.amazon.com/general/latest/gr/rande.html).

Also please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy, all the identified instances that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification.
- Terminate reported instances after approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `ec2:TerminateInstances`*

  \* Only required for taking action (deletion); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeInstances",
                  "ec2:TerminateInstances"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
