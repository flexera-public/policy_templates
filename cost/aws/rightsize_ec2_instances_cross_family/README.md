# AWS Rightsize EC2 Instances (Cross-Family)

## What It Does

This policy template analyzes AWS EC2 instances using Amazon CloudWatch metrics to identify instances that are idle (candidates for termination) or underutilized (candidates for cross-family rightsizing). Unlike same-family downsizing, cross-family rightsizing searches the entire catalog of current-generation instance types in the same region to find the cheapest option that can still satisfy the observed workload. Incidents report estimated monthly savings and trigger optional automated actions to resize or terminate instances after approval.

## How It Works

### Idle Instance Detection

An instance is flagged as idle when **both** of the following conditions are true over the configured lookback period:

- **CPU utilization (average) is below a size-scaled threshold:**

  | vCPU Count | CPU Idle Threshold |
  | --- | --- |
  | ≤ 2 vCPUs | 5% |
  | ≤ 4 vCPUs | 4% |
  | ≤ 8 vCPUs | 3% |
  | ≤ 16 vCPUs | 2% |
  | > 16 vCPUs | 1% |

- **Average daily network traffic (NetworkIn + NetworkOut) is below 500 MB/day.**

Instances that meet both criteria are recommended for **termination**. No CloudWatch Agent (CWAgent) memory data is required for idle detection.

### Cross-Family Rightsizing

An underutilized instance is one where both CPU and memory utilization indicate the workload could run on a smaller, cheaper instance type from a **different instance family**.

#### Requirements

- AWS CloudWatch Agent (CWAgent) must be installed and configured to publish memory utilization metrics (`mem_used_percent` for Linux; `Memory % Committed Bytes In Use` for Windows) to CloudWatch.
- Instances **without** CWAgent memory data are skipped for rightsizing recommendations entirely. They may still appear as idle candidates if the idle criteria are met.

#### Algorithm

1. **Peak resource requirements** are computed by scaling observed peak metrics by the *Rightsizing Safety Factor* (`param_stats_safety_factor`). For example, with a safety factor of 1.5, if peak CPU was 40% of 4 vCPUs, the required vCPUs = ceil(0.40 × 4 × 1.5) = 3.

2. **Candidate instances** in the same region must satisfy all of the following compatibility constraints:
   - Current generation only (no previous-generation or bare-metal types)
   - Same CPU architecture (x86_64, arm64, etc.)
   - Same CPU burst model (burstable instances only recommend other burstable types)
   - Same GPU presence (instances with a GPU only recommend GPU types; non-GPU instances only recommend non-GPU types)
   - No local instance storage (NVMe/SSD instance store) on the recommended type
   - ENA networking is required if the candidate uses the Nitro hypervisor and the current instance does not have ENA enabled
   - Sufficient EBS attachment slots, network baseline bandwidth, EBS throughput, and EBS IOPS to meet scaled requirements
   - Intel/AMD manufacturer match is enforced by default (configurable via `param_allow_mixed_x86_vendors`)

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is resized or terminated.

- The `Estimated Monthly Savings` for underutilized instances is calculated by multiplying the instance's CCO monthly cost by the ratio of the list price reduction: `cco_cost × (current_list_price − recommended_list_price) / current_list_price`.
- The `Estimated Monthly Savings` for idle instances is the full CCO monthly cost of the instance (since termination eliminates 100% of the spend).
- The CCO monthly cost is derived by multiplying one day's amortized cost from Flexera CCO by 30.44 (the average number of days per month).
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Set to 0 to report all findings.
- *Exclusion Tags* - Cloud native tags to ignore resources. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; please see the [README](https://github.com/flexera-public/policy_templates/tree/master/README.md) for more details.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them.
- *Allow/Deny Regions* - Allow or Deny entered regions.
- *Allow/Deny Regions List* - A list of allowed or denied AWS regions. Leave blank to include all regions.
- *Filter GPU Instances* - Whether or not to exclude GPU-focused EC2 instances from the results.
- *Allow Intel/AMD Recommendations* - Whether to allow recommendations that switch between Intel and AMD processors (both x86_64). Set to `Yes` to allow cross-manufacturer recommendations; `No` (default) to keep the same CPU manufacturer.
- *Statistic Lookback Period* - How many days back to look at CPU and memory data for instances. Maximum is 90 days (AWS CloudWatch data retention limit).
- *Rightsizing Safety Factor* - A multiplier applied to peak utilization when computing required resources for a rightsized instance. Default is 1.5 (50% headroom). Set higher for more conservative recommendations.
- *Automatic Actions* - When set, the policy will automatically take the selected action(s) without manual approval. Leave blank to require manual approval for all actions.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Resize Instances" action while applying the policy template, all the underutilized instances that received a rightsizing recommendation will be stopped, resized to the recommended instance type, and restarted.

## Policy Actions

- Sends an email notification
- Terminate EC2 instances (if idle) after approval
- Downsize EC2 instances (if underutilized but not idle) after approval

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
  - `ec2:DescribeInstanceStatus`*

  \* Only required for taking action (resize or termination); the policy will still function in a read-only capacity without these permissions.

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
                  "ec2:StartInstances",
                  "ec2:StopInstances",
                  "ec2:TerminateInstances",
                  "ec2:DescribeInstanceStatus"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

### Memory Support

By default, only CPU metrics are available from CloudWatch. To enable support for memory metrics, you must have the CloudWatch Agent installed on your EC2 instance(s) to collect memory metrics. Please reference [AWS Docs > Install CloudWatch Agent on EC2 Instance](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) for more information.

### Windows Support

To enable Windows support, add the following to your Cloudwatch config.json and restart the Cloudwatch agent:

```json
"metrics": {
  "append_dimensions": {
    "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
    "ImageId": "${aws:ImageId}",
    "InstanceId": "${aws:InstanceId}",
    "InstanceType": "${aws:InstanceType}"
  }
}
```

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
