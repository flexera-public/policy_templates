# AWS Rightsize GPU EC2 Instances

## What It Does

This policy template identifies AWS GPU EC2 instances that are idle or underutilized based on four metrics collected over a configurable lookback period: CPU utilization, memory utilization, GPU compute utilization (`nvidia_smi_utilization_gpu`), and GPU memory used (`nvidia_smi_memory_used`). Instances where all four metrics fall below 5% are flagged as idle and recommended for termination. Instances that are not idle but could be moved to a smaller instance in the same GPU family — one that satisfies the workload's resource requirements with a user-configurable safety margin — are flagged as underutilized and recommended for downsizing. GPU CloudWatch Agent metrics are required; instances without them are excluded from analysis.

## How It Works

The policy retrieves all running EC2 instances in the configured regions, filters them to GPU instance types only (those present in `data/aws/aws_ec2_instance_types.json` with a GPU count greater than zero), and then discards any that do not have GPU CloudWatch Agent metrics reporting to AWS. For the remaining instances, it queries six statistical variants (Average, Minimum, Maximum, p99, p95, p90) for all four metrics over the configured lookback window.

### Idle Detection

An instance is considered **idle** when all four metric values (using the configured threshold statistic) are below the hard-coded idle threshold of **5%**:

- CPU utilization (from `AWS/EC2:CPUUtilization`)
- Memory utilization (from `CWAgent:mem_used_percent` or `CWAgent:Memory % Committed Bytes In Use`)
- GPU compute utilization (max across all GPU indices from `CWAgent:nvidia_smi_utilization_gpu`)
- GPU memory utilization percentage (derived from total GPU memory used across all GPU indices ÷ total GPU memory capacity × 100)

Idle instances are recommended for **termination**.

### Downsize Detection

An instance is considered **underutilized** when it is not idle but a smaller instance in the same GPU family exists that can satisfy the workload's resource requirements. The policy computes the minimum required resources using a **1.5× safety margin**:

```text
required_vcpus       = ceil(current_vcpus × cpu_pct / 100 × 1.5)
required_ram_mib     = ceil(current_ram_mib × mem_pct / 100 × 1.5)
required_gpu_count   = max(1, ceil(current_gpu_count × gpu_util_pct / 100 × 1.5))
required_gpu_mem_mib = ceil(total_gpu_mem_used_mib × 1.5)
```

The policy then searches the same GPU family (sorted by vCPU count ascending) for the **smallest instance** that satisfies all four constraints simultaneously. If a qualifying smaller instance is found, the current instance is flagged for downsizing.

**Why a simple threshold does not work for GPU instances:** GPU count is not monotonically correlated with vCPU count within GPU families. For example, in the `g5` family: `g5.8xlarge` has 32 vCPUs and 1 GPU, `g5.12xlarge` has 48 vCPUs and 4 GPUs, and `g5.16xlarge` has 64 vCPUs and 1 GPU. A flat "downsize by one size" rule would recommend `g5.8xlarge` for a `g5.12xlarge` even when 2+ GPUs are required. The constraint-satisfaction approach used here accounts for this non-monotonic relationship.

### GPU metric aggregation

Because an instance may have multiple GPUs, GPU metrics are aggregated across all GPU indices before comparison:

- `nvidia_smi_utilization_gpu` → **maximum** across GPU indices (worst-case utilization)
- `nvidia_smi_memory_used` → **sum** across GPU indices (total memory consumed)

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is terminated or downsized.

- For **idle** instances: `Estimated Monthly Savings` equals the full monthly cost from Flexera CCO (amortized, 30.44-day equivalent).
- For **underutilized** instances: `Estimated Monthly Savings = actual monthly CCO spend × (1 - new_instance_list_price / current_instance_list_price)`. On-demand list prices are sourced from `data/aws/aws_ec2_pricing.json`. If no pricing entry exists for the instance type and operating system combination, savings are estimated using the vCPU count ratio as a cost proxy: `savings_multiplier = 1 - new_vcpus / current_vcpus`.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Default is 0.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions.
- *Threshold Statistic* - Statistic to use when evaluating whether an instance is idle or underutilized. Applies to all four metrics (CPU, memory, GPU utilization, GPU memory). Options: `Average`, `Maximum`, `p99`, `p95`, `p90`. Default is `Average`.
- *Statistic Lookback Period* - How many days back to look at CloudWatch data. Cannot exceed 90 days (AWS CloudWatch retention limit). Default is 30 days.
- *Rightsizing Safety Margin (%)* - The percentage of headroom to add on top of observed peak utilization when selecting a smaller instance type. For example, a value of 50 means the recommended instance must be able to handle 1.5x the observed workload — so if GPU utilization peaked at 30%, the policy will look for an instance that can handle 45% utilization. Higher values produce more conservative (larger) recommendations; lower values produce more aggressive (smaller) ones. Default is 50.
- *Automatic Actions* - When set, the policy will automatically take the selected action(s) without manual approval. Options: `Downsize Instances`, `Stop Instances`, `Terminate Instances`.
- *Attach CSV To Incident Email* - Whether to attach a CSV export of the incident data to the notification email.
- *Incident Table Rows for Email Body (#)* - Number of rows to include in the incident table in the notification email. Set to `0` to omit the table; `100000` to include all rows.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy template, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance:

- Send an email report with a list of idle or underutilized GPU EC2 instances.
- Stop the selected GPU EC2 instances after approval.
- Downsize the selected GPU EC2 instances after approval.
- Terminate the selected GPU EC2 instances after approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `cloudwatch:GetMetricData`
  - `cloudwatch:ListMetrics`
  - `sts:GetCallerIdentity`
  - `ec2:ModifyInstanceAttribute`*
  - `ec2:StopInstances`*
  - `ec2:StartInstances`*
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
                  "ec2:ModifyInstanceAttribute",
                  "ec2:StopInstances",
                  "ec2:StartInstances",
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

### GPU CloudWatch Agent Requirements

The following must be in place on each GPU instance before this policy can produce GPU-aware recommendations:

1. **CloudWatch Agent installed** — The CloudWatch Agent must be installed and running on each instance. See the [CloudWatch Agent installation guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) for details.

1. **NVIDIA GPU stats plugin enabled** — The CloudWatch Agent configuration must enable the `nvidia_gpu` (or `nvidia_smi`) metrics plugin to publish `nvidia_smi_utilization_gpu` and `nvidia_smi_memory_used` metrics to the `CWAgent` namespace. See [Collect NVIDIA GPU metrics with the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html) for the required agent configuration.

1. **NVIDIA drivers installed** — NVIDIA drivers must be installed on the instance for the `nvidia-smi` tool to report metrics.

Instances that do not publish `nvidia_smi_utilization_gpu` metrics to CloudWatch are automatically excluded from the incident results.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
