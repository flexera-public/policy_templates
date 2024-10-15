# AWS EC2 Instances Time Stopped Report

## What It Does

This policy template checks all of the EC2 instances in the AWS account for how much time they have spent in a `stopped` state over a user-specified number of days. A report is produced with all EC2 instances that are stopped for greater than or less than the user-specified percentage threshold. Optionally, an email of this report is sent, and the instances can be stopped or terminated.

__NOTE: The most recent 3 days are ignored when performing the assessment. This is because cloud billing data is used to assess usage, and this data is not reported by AWS in real time and may be unreliable for up to 72 hours. For example, if performing the assessment for 7 days, the assessment will begin 10 days ago and end 3 days ago.__

## How It Works

- The policy leverages the AWS API to retrieve all EC2 instances in the account.
- The policy leverages the Flexera Bill Analysis API to gather usage data for each instance.
- For each instance, the total number of hours in the specified time frame is compared to the number of hours in the usage data to determine the percentage of time the instance is stopped. The following formula is used for this calculation: (`Look Back Period (Days)` \* 24) - `Hours Of Usage` / (`Look Back Period (Days)` \* 24)
- The hourly cost is calculated by dividing the total cost of the instance across the `Look Back Period (Days)` by `Hours Of Usage`. This is the estimated hourly cost of the instance while it is running.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Look Back Period (Days)* - How many days back to look when assessing the amount of time an instance is stopped for.
- *Maximum Time Powered Off (%)* - Instances that are stopped for more than the specified percentage will be included in the report. Set to `100` to not perform this assessment.
- *Minimum Time Powered Off (%)* - Instances that are stopped for less than the specified percentage will be included in the report. Set to `0` to not perform this assessment.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action. For example if a user selects the "Terminate Instances" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification
- Stop virtual machines after approval
- Terminate virtual machines after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `ec2:DescribeInstanceStatus`*
  - `ec2:StopInstances`*
  - `ec2:TerminateInstances`*
  - `sts:GetCallerIdentity`

  \* Only required for taking action (stopping or terminating); the policy will still function in a read-only capacity without these permissions.

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
                  "ec2:DescribeInstanceStatus",
                  "ec2:StopInstances",
                  "ec2:TerminateInstances",
                  "sts:GetCallerIdentity"
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

This policy template does not incur any cloud costs.
