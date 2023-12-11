# Reserved Instances Coverage

## What it does

This Policy Template leverages the Reserved Instance Coverage report. Retrieves the reservation coverage for your account.
It will email the user specified in `Email addresses of the recipients you wish to notify`

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of days in the past to view Reserved Instance Coverage* - allowed values 7,14,30,90,180,365
- *Email addresses* - A list of email addresses of the recipients you wish to notify
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ce:GetReservationCoverage`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ce:GetReservationCoverage"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
