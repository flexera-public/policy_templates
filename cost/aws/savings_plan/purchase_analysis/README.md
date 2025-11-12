# AWS Savings Plan Purchase Analysis

## What It Does

This policy template

## How It Works

Analysis is performed via the [AWS Savings Plans Purchase Analyzer](hhttps://aws.amazon.com/blogs/aws-cloud-financial-management/announcing-savings-plans-purchase-analyzer/) tool included in AWS Cost Explorer.

### Currency Details

If the Flexera organization is configured to use a currency other than the one the [AWS Savings Plans Purchase Analyzer](hhttps://aws.amazon.com/blogs/aws-cloud-financial-management/announcing-savings-plans-purchase-analyzer/) tool returns, currency values will be converted using the exchange rate at the time that the policy executes.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1123608)
- *Account Scope* - The account scope that you want your recommendations for. Select Payer to produce results only for a Master Payer account, or Linked to produce results for all linked accounts as well.
- *Look Back Period* - Number of days of prior usage to analyze
- *Savings Plan Term* - Length of savings plan term to provide recommendations for.
- *Savings Plan Type* - Type of Savings Plan to provide recommendations for.
- *Payment Option* - Savings Plan purchase option to provide recommendations for.
- *Hourly Purchase Commitment* - The amount of currency to commit to spending per hour on Savings Plans. Must be in whatever currency the AWS account is configured to use.
- *Region* - The region to scope the results to. Leave blank to analyze all regions.
- *Instance Family* - The instance family to scope the results to. Leave blank to analyze all instance families.
- *Offering ID* - The offering ID to scope the results to. Leave blank to analyze all offering IDs.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `sts:GetCallerIdentity`
  - `ce:StartCommitmentPurchaseAnalysis`
  - `ce:GetCommitmentPurchaseAnalysis`
  - `ce:ListCommitmentPurchaseAnalyses`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:GetCallerIdentity",
                  "ce:StartCommitmentPurchaseAnalysis",
                  "ce:GetCommitmentPurchaseAnalysis",
                  "ce:ListCommitmentPurchaseAnalyses"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this policy template requires that [AWS Cost Explorer be enabled](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) in the management account.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
