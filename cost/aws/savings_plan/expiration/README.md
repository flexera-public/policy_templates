# AWS Expiring Savings Plans

## What It Does

This Policy Template leverages the Savings Plan API for savings plan information. It will notify only if expiration is within the timeframe specified in `Number of days to prior to expiration date to trigger incident` field. It will email the user specified in `Email addresses of the recipients you wish to notify`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of days to prior to expiration date to trigger incident* - enter the number of days you want before the Savings Plan expires.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `savingsplans:DescribeSavingsPlans`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "savingsplans:DescribeSavingsPlans"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
