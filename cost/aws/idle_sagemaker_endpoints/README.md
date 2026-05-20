# AWS Idle SageMaker Endpoints

## What It Does

This policy template reports AWS SageMaker real-time inference endpoints in `InService` status that have zero or near-zero invocations over a configurable lookback window. Idle endpoints represent ongoing waste because dedicated compute instances are billed continuously by the hour regardless of whether predictions are being served. The policy optionally deletes reported endpoints after manual or automatic approval.

Endpoints configured for [SageMaker Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) are excluded from results — serverless endpoints do not provision dedicated instances and incur no continuous compute cost, so there is no spend to eliminate by deleting them.

## How It Works

- The policy uses the AWS SageMaker `ListEndpoints` API to enumerate all `InService` endpoints in each enabled region.
- For each endpoint, `DescribeEndpoint` is called to retrieve production variant details including instance type and instance count. Endpoints where all production variants use [Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) (i.e. have no dedicated instance type) are excluded from evaluation.
- The AWS CloudWatch `GetMetricData` API is used to retrieve the `Invocations` metric (Sum statistic) from the `AWS/SageMaker` namespace for each endpoint over the configured lookback window. Endpoints whose total invocation count is at or below the **Minimum Invocations Threshold** parameter are flagged as idle and recommended for deletion.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the idle SageMaker endpoint is deleted.

- The `Estimated Monthly Savings` is calculated by summing, across all production variants, the product of the on-demand hourly rate × instance count × 730.5 (average hours per month). This equals the full monthly cost of keeping the endpoint running.
- On-demand hourly rates are sourced from [`data/aws/aws_sagemaker_pricing.json`](../../../data/aws/aws_sagemaker_pricing.json), which is generated weekly from the [AWS Price List API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html).
- If a production variant's instance type is not present in the pricing data, its cost contribution is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Default is 0.
- *Statistic Lookback Period* - How many days back to look at CloudWatch invocation data. Minimum: 1, Maximum: 90. Default: 30.
- *Minimum Invocations Threshold* - Endpoints with total invocations at or below this number over the lookback period are considered idle. Set to 0 (default) to report only endpoints with zero invocations. Increase this value to also capture near-zero usage endpoints.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; please see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the 'Exclusion Tags' field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Delete Idle SageMaker Endpoints" action while applying the policy template, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Send an email notification
- Delete idle SageMaker endpoints after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `sts:GetCallerIdentity`
  - `sagemaker:ListEndpoints`
  - `sagemaker:DescribeEndpoint`
  - `sagemaker:ListTags`
  - `cloudwatch:GetMetricData`
  - `sagemaker:DeleteEndpoint`*

  \* Only required for taking action (deletion); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `sts:GetCallerIdentity`
  - `sagemaker:ListEndpoints`
  - `sagemaker:DescribeEndpoint`
  - `sagemaker:ListTags`
  - `cloudwatch:GetMetricData`
  - `sagemaker:DeleteEndpoint`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "sts:GetCallerIdentity",
                  "sagemaker:ListEndpoints",
                  "sagemaker:DescribeEndpoint",
                  "sagemaker:ListTags",
                  "cloudwatch:GetMetricData",
                  "sagemaker:DeleteEndpoint"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
