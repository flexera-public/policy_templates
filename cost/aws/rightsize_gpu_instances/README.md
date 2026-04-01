# AWS Rightsize GPU EC2 Instances

## What It Does

Reports on AWS GPU EC2 instances that are idle or underutilized based on GPU and CPU utilization data gathered from Amazon CloudWatch. Recommendations are made to downsize or terminate instances that fall below the configured utilization thresholds. Optionally, the policy can automatically take action upon approval.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is terminated or downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Default is 0.
- *Threshold Statistic* - Statistic to use when evaluating whether an instance is idle or underutilized. Options: `Average`, `Maximum`, `p99`, `p95`, `p90`. Default is `Average`.
- *Statistic Lookback Period* - How many days back to look at CPU and GPU CloudWatch data for instances. Cannot be set higher than 90 because AWS does not retain metrics for longer than 90 days. Default is 30.
- *Idle Instance GPU Threshold (%)* - The GPU utilization threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore GPU utilization. Default is 5.
- *Underutilized Instance GPU Threshold (%)* - The GPU utilization threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore GPU utilization. Default is 40.
- *Idle Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'idle' and therefore be flagged for termination. Set to -1 to ignore CPU utilization. Default is 5.
- *Underutilized Instance CPU Threshold (%)* - The CPU threshold at which to consider an instance to be 'underutilized' and therefore be flagged for downsizing. Set to -1 to ignore CPU utilization. Default is 40.
- *Idle/Utilized for both GPU/CPU or either* - Whether an instance must have both GPU and CPU below the thresholds (AND logic) or either one (OR logic) to be considered idle or underutilized. Only applies when both GPU and CPU thresholds are enabled (not set to -1). Default is `Either GPU or CPU`.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; please see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the 'Exclusion Tags' field.
- *Automatic Actions* - When set, the policy will automatically take the selected action(s) without manual approval. Options: `Downsize Instances`, `Stop Instances`, `Terminate Instances`.
- *Attach Incident CSV* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Size* - The number of results to include in the incident table in the incident email. Set to `0` to not show an incident table at all, and `100000` to include all results.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy template, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Send an email report
- Downsize EC2 instances after approval
- Stop EC2 instances after approval
- Terminate EC2 instances after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `cloudwatch:GetMetricData`
  - `cloudwatch:ListMetrics`
  - `sts:GetCallerIdentity`
  - `ec2:ModifyInstanceAttribute`*
  - `ec2:StartInstances`*
  - `ec2:StopInstances`*
  - `ec2:TerminateInstances`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Amazon Web Services

## Cost

This policy template does not incur any additional costs.
