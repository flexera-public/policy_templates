# AWS Lambda Functions with high error rate

## What it does

Checks for lambda functions with errors, and lambda function over the `Error Rate Percentage` will be reported on.

## Functional Details

The policy leverages the AWS ec2 API to examine vpc and flowlog details. When a vpc without flowlogs enabled is detected, an email action is triggered automatically to notify the specified users of the incident.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `lambda:ListFunctions`
  - `lambda:ListTags`
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:ListMetrics`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "lambda:ListFunctions",
                  "lambda:ListTags",
                  "cloudwatch:GetMetricStatistics",
                  "cloudwatch:ListMetrics"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

- *Allowed/Denied Regions* - Whether to treat regions parameter as allow or deny list.
- *Regions* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled, see [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Error Rate Percentage* - Items above this percentage will be reported on. `Number Only!`
- *Ignore tags* - Lambda Functions with any of these tags will be ignored

## Policy Actions

- Send an email report

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
