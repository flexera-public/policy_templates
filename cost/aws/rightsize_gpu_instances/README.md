# AWS Rightsize GPU Instances

## What It Does

This policy template checks all GPU EC2 instances in an AWS Account for GPU utilization over a user-specified number of days. Instances where GPU compute and memory bandwidth utilization never exceeded 5% are recommended for termination. Instances where the current workload — projected onto the next smaller instance in the same GPU family — would exceed 80% GPU, CPU, or system memory utilization are kept as-is; only instances with meaningful headroom on the target are recommended for downsizing. Both sets of GPU EC2 instances returned from this policy are emailed to the user.

Only EC2 instance types that include GPU hardware are analyzed. The policy uses the [AWS EC2 Instance Types](https://github.com/flexera-public/policy_templates/blob/master/data/aws/aws_ec2_instance_types.json) dataset to identify GPU instances and their GPU specifications (model, count, and total GPU memory).

## How It Works

- The policy leverages the AWS API to retrieve all running instances and then filters to only GPU instance types.
- CPU utilization is retrieved from the standard AWS CloudWatch `CPUUtilization` metric and included in the report for context.
- GPU metrics (`nvidia_smi_utilization_gpu`, `nvidia_smi_utilization_memory`, `nvidia_smi_memory_used`) are collected from the CloudWatch Agent using the NVIDIA SMI plugin. See [GPU Metrics Support](#gpu-metrics-support) below.
- System memory utilization (`mem_used_percent` for Linux, `Memory % Committed Bytes In Use` for Windows) is collected from the CloudWatch Agent when available and included in the report for context.
- The utilization data is provided for the following statistics: Average, Maximum, Minimum, 99th percentile, 95th percentile, 90th percentile.
- The policy identifies GPU instances where both GPU compute and memory bandwidth utilization were idle over the entire lookback period. The recommendation for idle instances is termination.
- The policy identifies GPU instances where the current workload — projected onto the next smaller instance in the same GPU family — would fit comfortably. The recommendation for these instances is downsizing.

## How Recommendations Are Produced

### Idle Detection (Termination)

An instance is flagged as **idle** when **all three** of the following hold over the entire lookback period:

1. GPU compute utilization (`nvidia_smi_utilization_gpu`) **Maximum** never exceeded **5%**
2. GPU memory bandwidth utilization (`nvidia_smi_utilization_memory`) **Maximum** never exceeded **5%**
3. Peak GPU memory (VRAM) utilization did **not** exceed **20%** (when data is available)

The Maximum statistic is used for idle detection deliberately — if an instance had even one significant burst of GPU activity during the lookback window, it is not considered idle. The VRAM guard (condition 3) prevents false termination recommendations for model-serving workloads: a deployed model may show near-zero compute and bandwidth activity between requests while still having its weights fully loaded in GPU memory. If VRAM utilization data is absent (CloudWatch Agent not installed or not yet reporting), this guard is skipped and the compute/bandwidth check alone determines idle status.

Instances without CloudWatch Agent GPU metrics installed are never flagged as idle.

### Underutilization Detection (Downsizing)

There is no separate "underutilization threshold" applied to the current instance. Instead, the only criterion is: **"Would the current workload fit comfortably on the next smaller instance?"**

GPU compute utilization, GPU memory bandwidth utilization, CPU utilization, and system memory utilization (all using the **Average** statistic) are projected onto the target instance by multiplying by the relevant ratio. If all projected values are below **80%**, and the VRAM gate passes, the instance is recommended for downsizing. Average is used because it measures the duty cycle across the full lookback period and, combined with the 80% ceiling, creates inherently conservative effective thresholds on current utilization that scale with the instance size ratio. Percentile statistics (p90, p95, p99) are also collected and included in the incident data for workloads where peak behavior is the more relevant signal.

The effective current-utilization ceiling therefore scales automatically with the size difference between current and target:

| GPU count ratio | Effective current-util ceiling |
|---|---|
| 2:1 (e.g., 8→4 GPUs) | < 40% |
| 4:1 (e.g., 4→1 GPU) | < 20% |
| 8:1 (e.g., 8→1 GPU) | < 10% |

Both GPU metrics must meet the projection threshold — an instance with low compute utilization but high memory bandwidth (e.g., a data-loading or inference pipeline) is still actively using the GPU and will not be recommended for downsizing. Instances without CloudWatch Agent GPU metrics are never recommended for downsizing.

### Downsize Target Selection

The recommended target instance type is the **largest available instance in the same GPU family with strictly fewer GPUs that also costs less than the current instance**. For example:

- A `p3.8xlarge` (4× NVIDIA V100) would target `p3.2xlarge` (1× NVIDIA V100) — the only smaller option in the `p3` family.
- A `g5.48xlarge` (8× NVIDIA A10G) would target `g5.24xlarge` (4× NVIDIA A10G).
- Instances that are already the smallest GPU configuration in their family (e.g., `g5.xlarge` with 1 GPU) receive no downsize recommendation.

In most families, smaller GPU counts correspond to lower cost. However, some families have pricing anomalies where a larger-sizeRank instance (fewer GPUs) costs *more* than the current instance — for example, `g4dn.16xlarge` (1 GPU) costs more than `g4dn.12xlarge` (4 GPUs). In these cases the policy skips that candidate and tries the next-largest cheaper option. If no cheaper candidate exists in the family, no recommendation is made.

### Downsize Validation Gates

The following checks determine whether a downsize recommendation is made. All are evaluated together as part of detection — there is no separate "flag then validate" step:

1. **Compute projection**: GPU compute utilization (Average) × GPU count ratio must be below 80%.
2. **Memory bandwidth projection**: GPU memory bandwidth utilization (Average) × GPU count ratio must be below 80%. Memory bandwidth scales with GPU count — a distributed workload concentrates bus traffic onto fewer GPUs.
3. **VRAM gate**: Per-GPU peak VRAM utilization (Maximum) projected onto the target's per-GPU VRAM capacity must be below the configurable `GPU VRAM Gate Threshold` (default: 80%). Maximum is used here because VRAM is a hard capacity limit — peak usage determines whether the workload fits, not average usage.
4. **CPU projection**: CPU utilization (Average) × vCPU count ratio (`current vCPUs / target vCPUs`) must be below 80%. Within a GPU family, smaller instances also have fewer vCPUs in proportion to their fewer GPUs. If the CPU workload would saturate the target's vCPUs, the downsize recommendation is suppressed.
5. **System memory projection**: System memory utilization (Average) × (`current RAM / target RAM`) must be below 80%. RAM does not scale proportionally with GPU count across all families — for example, within the g5 family, the 4-GPU `g5.12xlarge` has 192 GiB while the 1-GPU `g5.8xlarge` has 128 GiB rather than 48 GiB. The gate uses the actual RAM sizes from the AWS EC2 instance types dataset to ensure the workload's memory footprint fits the target. This gate is skipped when the CloudWatch Agent is not installed (no memory metrics available), but a note is added to the recommendation details.

A recommendation is only produced when all five checks pass. For example, an instance with 4 GPUs at 30% average GPU compute utilization would project to 120% on a 1-GPU target, which fails check 1 — no recommendation is made. Similarly, an instance with 4 GPUs at 15% GPU utilization but 70% average CPU utilization would project to 280% CPU on a 1-GPU target (which typically also has 4× fewer vCPUs), failing check 4. An instance using 50% of system memory that would project to 75% × (192/128) ≈ 112% on the target RAM would fail check 5.

The projected values (`Projected GPU Utilization`, `Projected GPU Memory Bandwidth`, `Projected CPU Utilization`, `Projected Memory Utilization`) are included in the incident export so users can verify the basis for each recommendation.

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized for idle resources if the resource is stopped or terminated, and for underutilized resources if the resource is downsized.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- For idle resources, the savings is the full cost of the resource. For underutilized resources, the savings is the difference of the current cost of the resource and the estimated cost of the recommended resource type.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - The Account number for use with the AWS STS Cross Account Role. Leave blank when using AWS IAM Access key and secret. It only needs to be passed when the desired AWS account is different than the one associated with the Flexera One credential. [More information is available in our documentation.](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws)
- *Allow/Deny Regions* - Whether to treat Allow/Deny Regions List parameter as allow or deny list. Has no effect if Allow/Deny Regions List is left empty.
- *Allow/Deny Regions List* - A list of regions to allow or deny for an AWS account. Please enter the regions code if SCP is enabled. See [Available Regions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions) in AWS; otherwise, the policy may fail on regions that are disabled via SCP. Leave blank to consider all the regions.
- *Exclusion Tags* - The policy template will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Minimum Instance Age (Days)* - Age, in days, that a GPU EC2 instance needs to be before it is included in the analysis. This avoids producing recommendations for newly launched instances that may not yet have representative utilization data. Set to 0 to analyze all instances regardless of age.
- *GPU VRAM Gate Threshold (%)* - Maximum GPU memory (VRAM) utilization, projected onto the target instance's per-GPU VRAM, allowed before a downsize recommendation is made. GPU VRAM is often the binding constraint for ML and AI workloads — an instance using significant VRAM cannot safely move to a smaller instance even if compute utilization is low. Set to -1 to disable this check. Default: 80.
- *Statistic Lookback Period* - How many days back to look at GPU metrics for instances.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Terminate Instances" action while applying the policy template, all the resources that didn't satisfy the policy condition will be terminated.

## Policy Actions

- Sends an email notification
- Stop GPU EC2 instances (if idle) after approval
- Terminate GPU EC2 instances (if idle) after approval
- Downsize GPU EC2 instances (if underutilized but not idle) after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) to use with this policy, the following information is needed:

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `ec2:DescribeInstances`
  - `ec2:DescribeInstanceStatus`*
  - `ec2:DescribeTags`
  - `ec2:ModifyInstanceAttribute`*
  - `ec2:StartInstances`*
  - `ec2:StopInstances`*
  - `ec2:TerminateInstances`*
  - `cloudwatch:GetMetricStatistics`
  - `cloudwatch:GetMetricData`
  - `cloudwatch:ListMetrics`
  - `sts:GetCallerIdentity`

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
                  "ec2:DescribeInstanceStatus",
                  "ec2:DescribeTags",
                  "ec2:ModifyInstanceAttribute",
                  "ec2:StartInstances",
                  "ec2:StopInstances",
                  "ec2:TerminateInstances",
                  "cloudwatch:GetMetricStatistics",
                  "cloudwatch:GetMetricData",
                  "cloudwatch:ListMetrics",
                  "sts:GetCallerIdentity"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### GPU Metrics Support

GPU metrics (`nvidia_smi_utilization_gpu`, `nvidia_smi_utilization_memory`, `nvidia_smi_memory_used`) require the CloudWatch Agent with the NVIDIA SMI plugin to be installed and configured on your GPU instances. Without this, the policy will have no data to make recommendations from and all GPU metric fields in the incident report will be empty.

To enable GPU metric collection via CloudWatch Agent:

1. Install the [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) on your GPU instances.

1. Configure the agent to collect NVIDIA SMI metrics. Add the following to your CloudWatch Agent configuration:

```json
{
  "metrics": {
    "metrics_collected": {
      "nvidia_smi": {
        "measurement": [
          "utilization_gpu",
          "utilization_memory",
          "memory_used"
        ],
        "metrics_collection_interval": 60
      }
    }
  }
}
```

1. Restart the CloudWatch Agent.

For more information, see [Collect NVIDIA GPU Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html) in the AWS documentation.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
