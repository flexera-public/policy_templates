# AWS Tag Cardinality Report

## What It Does

This Policy Template is used to generate a tag cardinality (how many unique values each tag key has) report for AWS, along with a list of those unique values for each tag key. The report includes cardinality for all tag values for both AWS Accounts and Resources.

> *NOTE: This Policy Template must be applied to the **AWS Organization Master Payer** account.*

## How It Works

This policy performs the following action:

- Connect to the AWS Organizations API to get a list of AWS Accounts and their tags.
- Connect to the AWS Tagging API to get a list of AWS Resources and their tags.

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

This read-only policy is purely for reporting purposes and takes no action.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121575) (*provider=aws*) which has the following permissions:
  - `tag:GetResources`
  - `ec2:DescribeRegions`
  - `organizations:ListAccounts`
  - `organizations:ListTagsForResource`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "tag:GetResources",
                  "ec2:DescribeRegions",
                  "organizations:ListAccounts",
                  "organizations:ListTagsForResource"
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

This Policy Template does not incur any cloud costs.
