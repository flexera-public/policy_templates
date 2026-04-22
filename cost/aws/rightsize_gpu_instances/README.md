# AWS Rightsize GPU EC2 Instances

## What It Does

Reports on AWS GPU EC2 instances that are idle or underutilized based on GPU and CPU utilization data gathered from Amazon CloudWatch. Recommendations are made to downsize or terminate instances that fall below the configured utilization thresholds. Optionally, the policy can automatically take action upon approval.

## How It Works

1. **Instance discovery** — The policy enumerates all running EC2 instances across the configured regions and filters to GPU instance types (e.g. `p3`, `p4d`, `g4dn`, `g5`).
1. **Metric collection** — For each GPU instance, the following CloudWatch metrics are retrieved over the configured lookback period (default: 30 days). The selected statistic (`Average`, `Maximum`, `p99`, `p95`, or `p90`) is used for all threshold comparisons:
   - **CPU utilization** — standard `CPUUtilization` metric from EC2.
   - **Memory utilization** — `mem_used_percent` (Linux) or `Memory % Committed Bytes In Use` (Windows), published by the CloudWatch Agent.
   - **GPU compute utilization** — `nvidia_smi_utilization_gpu`, published by the CloudWatch Agent NVIDIA GPU plugin.
   - **GPU memory used** — `nvidia_smi_fb_memory_usage_used` (MiB), published by the CloudWatch Agent NVIDIA GPU plugin. GPU memory utilization percentage is derived by dividing this value by the total GPU memory of the instance type.
1. **Idle detection** — An instance is classified as **idle** when all enabled metric checks pass. The thresholds are configurable individually via the *Idle Instance CPU Threshold (%)*, *Idle Instance Memory Threshold (%)*, *Idle Instance GPU Utilization Threshold (%)*, and *Idle Instance GPU Memory Threshold (%)* parameters (set any to `-1` to disable that specific check). Memory and GPU memory data are optional — if those metrics are unavailable, those checks are skipped automatically. Idle instances are recommended for **termination**, with estimated monthly savings equal to the full current monthly cost of the instance.
1. **Rightsizing** — Instances that are not idle are assessed for downsizing. The required resources are computed by applying the configured Safety Factor to the observed peak utilization:

   ```text
   required_vcpus        = ceil(current_vcpus        × cpu_stat  / 100 × safety_factor)
   required_ram_mib      = ceil(current_ram_mib       × mem_stat  / 100 × safety_factor)
   required_gpu_count    = max(1, ceil(current_gpu_count × gpu_stat  / 100 × safety_factor))
   required_gpu_mem_mib  = ceil(gpu_mem_used_mib × safety_factor)
   ```

   The policy searches **all GPU instance types** available in the region (across all GPU families) for the cheapest instance type that satisfies all resource requirements and has a lower list price than the current instance. Savings are estimated using the list price ratio between the current and recommended instance types applied to the CCO monthly cost:

   ```text
   estimated_monthly_savings = current_monthly_cost × (1 - new_list_price / current_list_price)
   ```

1. **Cost data** — Instance costs are retrieved from Flexera CCO's Bill Analysis API. List prices are sourced from the `data/aws/aws_ec2_pricing.json` file in this repository.
1. **Instances without metrics** — Instances missing CPU utilization or GPU compute utilization CloudWatch metrics are excluded from analysis. Memory utilization and GPU memory utilization metrics are both optional — if either is unavailable, that specific check is skipped. See the [CloudWatch Agent Requirements](#cloudwatch-agent-requirements) section for setup details.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is terminated or downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- For downsize recommendations, the savings are estimated using the ratio of the recommended instance type's list price to the current instance type's list price, applied to the CCO monthly cost. List prices are sourced from the AWS EC2 pricing data bundled with this policy template repository.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Default is 0.
- *Threshold Statistic* - Statistic to use when evaluating whether an instance is idle or underutilized. Options: `Average`, `Maximum`, `p99`, `p95`, `p90`. Default is `Average`.
- *Statistic Lookback Period* - How many days back to look at CPU and GPU CloudWatch data for instances. Cannot be set higher than 90 because AWS does not retain metrics for longer than 90 days. Default is 30.
- *Rightsizing Safety Factor* - A multiplier applied to the peak utilization when computing the required resources for a rightsized instance. For example, a value of 1.5 means the recommended instance type must be able to handle 1.5 times the observed peak utilization. Set a higher value for more headroom. Default is 1.5.
- *Idle Instance CPU Threshold (%)* - The CPU utilization threshold at or below which an instance is considered idle and recommended for termination. Set to -1 to disable idle detection based on CPU utilization. Default is 5.
- *Idle Instance Memory Threshold (%)* - The memory utilization threshold at or below which an instance is considered idle and recommended for termination. Set to -1 to disable idle detection based on memory utilization. If memory metrics are unavailable, this check is skipped automatically. Default is 5.
- *Idle Instance GPU Utilization Threshold (%)* - The GPU compute utilization threshold at or below which an instance is considered idle. Set to -1 to disable idle detection based on GPU compute utilization. Note: An instance is only flagged as idle when all enabled metric checks pass. Default is 5.
- *Idle Instance GPU Memory Threshold (%)* - The GPU memory utilization threshold at or below which an instance is considered idle. Set to -1 to disable idle detection based on GPU memory utilization. If GPU memory metrics are unavailable, this check is skipped automatically. Default is 5.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Minimum Instance Age (Days)* - The minimum age in days that an instance must be before it is considered for rightsizing or termination recommendations. Set to 0 to evaluate instances of any age. Default is 7.
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
  - `ec2:DescribeInstanceStatus`*
  - `ec2:ModifyInstanceAttribute`*
  - `ec2:StartInstances`*
  - `ec2:StopInstances`*
  - `ec2:TerminateInstances`*

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
                  "ec2:DescribeInstances",
                  "cloudwatch:GetMetricData",
                  "cloudwatch:ListMetrics",
                  "sts:GetCallerIdentity",
                  "ec2:DescribeInstanceStatus",
                  "ec2:ModifyInstanceAttribute",
                  "ec2:StartInstances",
                  "ec2:StopInstances",
                  "ec2:TerminateInstances"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### CloudWatch Agent Requirements

This policy relies on Amazon CloudWatch metrics published by the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) running on each GPU EC2 instance. Without these metrics, the policy cannot collect GPU utilization data and will skip the instance. The following must be in place on each instance before the policy can collect GPU metrics:

1. **CloudWatch Agent installed and running** — The CloudWatch Agent must be installed, configured, and actively running on the instance. See [Installing the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) for instructions.
1. **NVIDIA GPU metrics plugin enabled** — The CloudWatch Agent configuration must include the `nvidia_gpu` input plugin, which uses `nvidia-smi` to collect GPU utilization (`nvidia_smi_utilization_gpu`) and GPU memory usage (`nvidia_smi_fb_memory_usage_used`) metrics. See [Collect NVIDIA GPU metrics with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html) for configuration details.
1. **Memory utilization metric enabled** — The CloudWatch Agent must also be configured to report the `mem_used_percent` metric (Linux) or `Memory % Committed Bytes In Use` metric (Windows) to CloudWatch for memory utilization data. See [Metrics collected by the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-collected-by-CloudWatch-agent.html) for details.

Instances missing CPU utilization or GPU compute utilization metrics will be excluded from the policy results. Memory utilization and GPU memory utilization metrics are optional — instances missing these metrics will still be analyzed, but the corresponding idle checks will be skipped.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any additional costs.
