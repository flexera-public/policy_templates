# AWS Auto Scaling Group Recommendations

## What It Does

This policy template detects non-elastic and over-provisioned EC2 Auto Scaling Groups (ASGs) and surfaces them as **advisory** incidents with supporting evidence for a human owner to review. It is an evidence-first, human-in-the-loop policy. It does **not** prescribe specific Min/Max values, does **not** report a "savings" figure, and does **not** take any automated remediation action. Dollar figures are characterized as on-demand-equivalent spend (pre-commitment), not as savings — they ignore existing Savings Plan / Reserved Instance coverage.

The policy raises four distinct findings per ASG:

1. **Fixed-size ASG** — `MinSize == MaxSize == DesiredCapacity` (definitively static; high confidence)
1. **Never moved off floor** — `MinSize < MaxSize` but Desired never moved over the lookback window (high confidence when group metrics are on; reduced when relying on scaling-activity history only)
1. **Over-provisioned floor** — `MinSize > 1` and either peak in-service / Min ratio is at or below the configured threshold, or aggregate p95 CPU is at or below the configured threshold (medium-confidence "review" finding)
1. **Group metrics collection disabled** — hygiene finding raised independently of the others; enabling group metrics is free and unblocks findings 2 and 3 on the next run

## How It Works

- The policy enumerates Auto Scaling Groups in each in-scope region via `DescribeAutoScalingGroups`, retrieves scaling policy types via `DescribePolicies`, retrieves recent scaling activities via `DescribeScalingActivities`, and queries CloudWatch via `GetMetricData` (batched) for group metrics (`GroupInServiceInstances`, `GroupDesiredCapacity`, `GroupTotalInstances`) and aggregate `CPUUtilization` (Average, Maximum, p95) dimensioned by `AutoScalingGroupName`.
- Group metrics are only queried for ASGs whose `EnabledMetrics` indicates collection is on; otherwise the policy falls back to `DescribeScalingActivities` and aggregate CPU as the elasticity signal and reduces confidence accordingly.
- Per-instance on-demand-equivalent rates are derived from Flexera Cloud Cost Optimization (CCO) `cost_list_price` for matched ASG member instances, then projected: `floor_monthly_on_demand_equiv = MinSize × per_instance_daily_list_price × 30.44`.
- Confidence is reported per finding. When inputs needed to confirm a finding are absent, confidence is downgraded and the gap is stated in the incident text rather than asserted.
- Cross-cutting rules: ASGs younger than the effective minimum age are skipped (history is too short to assess). The exclusion-tag filter applies to findings 1, 2, and 3 (cost/over-provisioning) but not to finding 4 (hygiene).

### Policy Spend Characterization Details

The policy reports monthly on-demand-equivalent spend for each finding, **not** savings.

- The `Monthly On-Demand Equivalent Spend (Pre-Commitment)` is calculated as `MinSize × per-instance daily list price × 30.44` (the average number of days in a month). The per-instance daily list price is sourced from Flexera CCO using the `cost_list_price` metric.
- For the over-provisioned floor finding, the figure is `(MinSize − peak_in_service) × per-instance daily list price × 30.44` — a **theoretical maximum** that assumes the unused floor capacity is fully eliminated and ignores any future scale-up needs.
- These figures **do not net out existing Savings Plan or Reserved Instance coverage**. Removing committed-rate baseline usage inside an active commitment window often yields no actual savings until the commitment expires. Always net against existing commitments before believing the dollar figure.
- If a member instance cannot be matched in Flexera CCO (e.g., new instance not yet ingested), its contribution to the spend figure is 0.
- Spend figures are reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Statistic Lookback Period* - How many days back to look at CloudWatch and scaling-activity data. Minimum: 1, Maximum: 90 (CloudWatch retention ceiling). Default: 30.
- *Metric Aggregation Period (Seconds)* - CloudWatch GetMetricData aggregation period. Default: 3600 (hourly).
- *Floor Headroom Ratio Threshold* - Trigger the over-provisioned floor finding when peak in-service instance count / MinSize is at or below this ratio. Default: 0.5.
- *Floor CPU Threshold (%)* - Trigger the over-provisioned floor finding when aggregate p95 CPU is at or below this percentage. Default: 20.
- *Minimum ASG Age (Days)* - Skip ASGs younger than this many days because their history is too short to assess. Set to 0 to disable the age filter (every ASG is evaluated regardless of how recently it was created). Defaults to 30 to match the default lookback window.
- *Findings To Raise* - Which finding types this policy should evaluate and raise as incidents. Deselect a finding to suppress it. All four are selected by default. Allowed values: `Fixed-size ASG`, `Never moved off floor`, `Over-provisioned floor`, `Group metrics collection disabled`.
- *Exclusion Tags* - Cloud native tags to skip ASGs from the cost/over-provisioning findings. The hygiene finding is still raised. Enter a Key name to filter ASGs with that key regardless of value, or `Key==Value` for exact matching. Other operators (`!=`, `=~`, `!~`) and regex are supported. Example: `finops:ignore-elasticity`.
- *Exclusion Tags: Any / All* - Whether to skip ASGs containing any of the specified tags or only those that contain all of them.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

## Policy Actions

- Send an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `sts:GetCallerIdentity`
  - `autoscaling:DescribeAutoScalingGroups`
  - `autoscaling:DescribePolicies`
  - `autoscaling:DescribeScalingActivities`
  - `cloudwatch:GetMetricData`

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
                  "autoscaling:DescribeAutoScalingGroups",
                  "autoscaling:DescribePolicies",
                  "autoscaling:DescribeScalingActivities",
                  "cloudwatch:GetMetricData"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
