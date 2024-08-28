# AWS CloudTrails Not Integrated With CloudWatch

## What It Does

This policy template reports any CloudTrails in the AWS account that are not integrated with CloudWatch. A CloudTrail is considered to be not integrated if such integration has not been enabled, or if CloudTrail data has not been sent to CloudWatch recently. Optionally, this report can be emailed.

AWS recommends integrating CloudTrails with CloudWatch logs. The intent of this recommendation is to ensure AWS account activity is being captured, monitored, and appropriately alarmed on. CloudWatch Logs is a native way to accomplish this using AWS services.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Last Update (Hours)* - Maximum number of hours since CloudTrail data was last sent to CloudWatch. CloudTrails that have not done so for longer than this will be considered not integrated with CloudWatch and included in the results.

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `cloudtrail:DescribeTrails`
  - `cloudtrail:GetTrailStatus`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:GetCallerIdentity",
                  "cloudtrail:DescribeTrails",
                  "cloudtrail:GetTrailStatus"
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
