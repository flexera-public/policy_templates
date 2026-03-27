# AWS Idle Lambda Functions

## What It Does

This policy template reports AWS Lambda functions that have zero or near-zero invocations over a configurable trailing window of 30, 60, or 90 days. Functions with total invocations at or below the configured threshold are considered idle and are surfaced as deletion candidates. Idle Lambda functions represent ongoing waste from Lambda code storage costs and any provisioned concurrency charges. The policy optionally deletes reported functions after manual or automatic approval.

## How It Works

- The policy uses the AWS CloudWatch `GetMetricData` API to retrieve the `Invocations` metric (Sum statistic) for each Lambda function over the configured lookback window. Functions whose total invocation count is at or below the **Minimum Invocations Threshold** parameter are flagged as idle and recommended for deletion.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the idle Lambda function is deleted.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is calculated from the function's code storage size: `code size (bytes) / (1024³) × $0.09/GB-month`.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Default is 0.
- *Statistic Lookback Period* - How many days back to look at CloudWatch invocation data. Minimum: 1, Maximum: 90. Default: 30.
- *Minimum Invocations Threshold* - Functions with total invocations at or below this number over the lookback period are considered idle. Set to 0 (default) to report only functions with zero invocations. Increase this value to also capture near-zero usage functions.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; please see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the 'Exclusion Tags' field.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action. Allowed values: `Delete Idle Lambda Functions`.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Delete Idle Lambda Functions" action while applying the policy template, all the resources that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Send an email notification
- Delete idle Lambda functions after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `sts:GetCallerIdentity`
  - `lambda:ListFunctions`
  - `lambda:ListTags`
  - `lambda:DeleteFunction`*
  - `cloudwatch:GetMetricData`

  \* Only required for taking action (deletion); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
