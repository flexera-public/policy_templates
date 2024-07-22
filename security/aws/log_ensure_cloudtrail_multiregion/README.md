# AWS CloudTrail Not Enabled In All Regions

## What It Does

This policy template reports if there is not at least one CloudTrail trail that is fully multiregion. Optionally, this report can be emailed.

AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. It is considered good practice to enable CloudTrail across all regions.

## How It Works

The policy leverages the AWS CloudTrail API to obtain a list of trails. Each trail is checked to see if IsMultiRegionTrail is set to "true", IsLogging set to "true", and if the trail has at least one Event Selector with IncludeManagementEvents set to "true" and ReadWriteType set to "All". If no trails are found that meet these criteria, an incident is raised.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `cloudtrail:DescribeTrails`
  - `cloudtrail:GetTrailStatus`
  - `cloudtrail:GetEventSelectors`

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
                  "cloudtrail:GetTrailStatus",
                  "cloudtrail:GetEventSelectors"
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
