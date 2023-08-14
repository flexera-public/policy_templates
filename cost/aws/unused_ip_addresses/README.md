# AWS Unused IP Addresses

## What it does

This Policy Template scans all IP addresses in the given account and identifies any unused IP addresses. If any are found, an incident report will show the IP addresses, and related information, and an email will be sent to the user-specified email address. If the user approves that the IP addresses should be deleted, the policy will delete the IP addresses. Optionally, the user can specify one or more tags that if found on an IP address will exclude the IP address from the list, as well as specify a minimum number of days for an IP address to be unattached before considering it unused.

## Functional Details

The policy utilizes the AWS EC2 API to get a list of unattached IP addresses and the AWS CloudTrail API to determine when the IP address was detached from an instance. An incident is raised with any unattached IP addresses that have been detached for longer than the user-specified threshold.

### Policy savings details

The policy includes the estimated savings. The estimated savings is recognized if the resource is terminated. The savings is�calculated using the per hour cost of unused IPs for a period of 30 days and is displayed in the Estimated Monthly Savings�column and the total estimated sum of all the unused IPs is displayed in the incident detail message.

If the Flexera organization is configured to use a currency other than USD, the savings values will be converted from USD using the exchange rate at the time that the policy executes.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Days Unattached* - The number of days an IP address needs to be detached to be considered unused. This value cannot be set above 90 due to CloudTrail only storing 90 days of log data. If this value is set to 0, all unattached IP addresses will be considered unused.
- *Allow/Deny Regions* - Whether to treat regions parameter as allow or deny list.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags (Key:Value)* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Use Key:Value format for specific tag key/value pairs, and Key:\* format to match any resource with a particular key, regardless of value. Examples: env:production, DO_NOT_DELETE:\*
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "*Automatic Actions*" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave it blank for *manual* action.
For example if a user selects the "Terminate Resources" action while applying the policy, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete unused IP addresses after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeAddresses`
  - `ec2:ReleaseAddress`*
  - `pricing:GetProducts`
  - `sts:GetCallerIdentity`

  \* Only required for taking action (releasing an IP address); the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "ec2:DescribeAddresses",
                  "ec2:ReleaseAddress",
                  "pricing:GetProducts",
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

This Policy Template does not launch any instances, and so does not incur any cloud costs.
