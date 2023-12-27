# AWS Savings Plan Utilization

## What it does

This Policy Template leverages the [AWS Savings Plans Utilization API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilization.html). It will raise incidents if the Utilization of the Savings Plan (specified in the *Savings Plan ARN* parameter) is below the *Savings Plan Utilization Threshold* parameter in the policy. It will email the user specified in *Email addresses to notify*.

> *NOTE: This Policy Template must be appled to the **AWS Organization Master Payer** account.*

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

## Functional Details

- This policy produces a pie chart showing Used Commitment, Unused Commitment and Utilization for a Savings Plan.
- This policy uses AWS Savings Plans Utilization API to retrieve Savings Plan Utilization data.
- This policy uses Flexera Bill Analysis API to retrieve currency data, so the correct currency is displayed in the chart.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Look Back Period* - Specify the number of days of past usage to analyze.
- *Savings Plan ARN* - Optional; The unique Amazon Resource Name (ARN) for a particular Savings Plan.  If no ARN is specified, all Savings Plans will have utilization reported.
- *Savings Plan Utilization Threshold* - Specify the minimum Savings Plan Utilization threshold as a percentage that should result in an alert
- *Email addresses to notify* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
