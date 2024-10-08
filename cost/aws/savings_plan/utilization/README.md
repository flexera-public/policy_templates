# AWS Savings Plan Utilization

## What It Does

This Policy Template leverages the [AWS Savings Plans Utilization API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilization.html) to determine if any Savings Plans have low utilization and present a report of any offending Savings Plans. Optionally, this report can be emailed.

> *NOTE: This Policy Template must be applied to the **AWS Organization Master Payer** account.*

## How It Works

- This policy uses [AWS Savings Plans Utilization API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilization.html) to retrieve Savings Plan Utilization data.
- That data is used to produce a pie chart showing Used Commitment, Unused Commitment and Utilization for each Savings Plan.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Look Back Period (Days)* - Specify the number of days of past usage to analyze.
- *Utilization Threshold* - Specify the minimum Savings Plan Utilization threshold as a percentage that should result in an alert.
- *Savings Plan ARNs* - The unique Amazon Resource Names (ARNs) for particular Savings Plans to report on. Leave blank to report on all Savings Plans.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ce:GetSavingsPlansUtilization`
  - `savingsplans:DescribeSavingsPlans`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ce:GetSavingsPlansUtilization",
                  "savingsplans:DescribeSavingsPlans"
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
