# AWS Savings Plan Recommendations

## What It Does

This policy template reports any Savings Plan Purchase Recommendations generated by AWS. The user can adjust which recommendations are reported via policy parameters.

> *NOTE: This Policy Template must be applied to the **AWS Organization Master Payer** account.*

## How It Works

Recommendations are obtained via requests to the [AWS Savings Plans Purchase Recommendation API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html).

### Policy Savings Details

The policy includes the estimated savings. The estimated savings is recognized if the recommended savings plan is purchased. The savings values are provided directly by the [AWS Savings Plans Purchase Recommendation API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html).

If the Flexera organization is configured to use a currency other than the one the [AWS Savings Plans Purchase Recommendation API](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html) returns, the savings values will be converted using the exchange rate at the time that the policy executes.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [more](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Look Back Period* - Number of days of prior usage to analyze
- *Account Scope* - The account scope that you want your recommendations for. Select Payer to produce results only for a Master Payer account, or Linked to produce results for all linked accounts as well.
- *Savings Plan Term* - Length of savings plan term to provide recommendations for.
- *Savings Plan Type* - Type of Savings Plan to provide recommendations for.
- *Payment Option* - Savings Plan purchase option to provide recommendations for.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `ce:GetSavingsPlansPurchaseRecommendation`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ce:GetSavingsPlansPurchaseRecommendation"
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
