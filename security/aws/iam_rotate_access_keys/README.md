# AWS IAM Users With Old Access Keys

## What It Does

This policy template reports any users with access keys older than a user-specified number of days. Optionally, this report can be emailed.

Access keys consist of an access key ID and secret access key, which are used to sign programmatic requests that you make to AWS. AWS users need their own access keys to make programmatic calls to AWS from the AWS Command Line Interface (AWS CLI), Tools for Windows PowerShell, the AWS SDKs, or direct HTTP calls using the APIs for individual AWS services. It is recommended that all access keys be rotated every 90 days or less.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Maximum Age (Days)* - Maximum age in days for access keys. Users with access keys older than this will be included in the report.

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `iam:GenerateCredentialReport`
  - `iam:GetCredentialReport`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:GetCallerIdentity",
                  "iam:GenerateCredentialReport",
                  "iam:GetCredentialReport"
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
