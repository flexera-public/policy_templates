# AWS Auto Scaling Group Recommendations

## What It Does

This policy template looks at the EC2 Auto Scaling Groups (ASGs) in your AWS accounts and flags ones that don't appear to be scaling. The most common pattern it catches is an ASG that was set up to grow and shrink with demand but, in practice, always runs at the same size — meaning you're paying for fixed capacity without getting any of the elasticity benefits of an ASG.

The policy is **advisory only**. It surfaces findings with the supporting evidence and asks a human to decide what (if anything) to change. It will never raise or lower an ASG's Min, Max, or Desired capacity, and it never takes any other action against AWS. The right Min and Max for a group depend on intent (availability-zone redundancy, burst headroom, latency targets) that isn't visible in the metrics, so the policy deliberately stays out of that decision.

Dollar amounts shown in incidents are **on-demand-equivalent spend**, not savings. They represent what the floor capacity would cost at on-demand rates, before any Savings Plan or Reserved Instance discounts you may already have. If a Savings Plan or RI is already covering that capacity, "removing" it usually saves nothing until the commitment expires — so always net the figure against existing commitments before treating it as money on the table.

The policy raises four distinct findings per ASG:

1. **Fixed-size ASG** — Min, Max, and Desired capacity are all set to the same number. The ASG cannot scale at all. High confidence.
1. **Never moved off floor** — Min is lower than Max (so the ASG *could* scale), but the Desired capacity never actually changed during the lookback window. Either the floor is the real steady-state demand or a scaling policy exists but is never being triggered. High confidence when ASG group metrics are enabled; reduced confidence when the policy has to rely on the scaling-activity history alone.
1. **Over-provisioned floor** — Min is greater than 1, and either the peak number of running instances stayed well below Min for the whole lookback window, or aggregate CPU stayed below the configured threshold. This is a "worth a review" finding, not a definitive call — the floor may be deliberately oversized for AZ spread or burst headroom that the metrics can't see. Medium confidence.
1. **Group metrics collection disabled** — A hygiene finding raised when the ASG isn't emitting its group-level metrics to CloudWatch. Enabling group metrics is free and unblocks higher-confidence evaluation of findings 2 and 3 on the next policy run. This finding is raised independently of the other three.

## How It Works

For each in-scope AWS region, the policy:

- Lists every Auto Scaling Group with the `DescribeAutoScalingGroups` API, capturing Min, Max, Desired, member instances, scaling policies, age, and the list of group metrics the ASG is emitting.
- Pulls recent scaling activity history with `DescribeScalingActivities`. Zero capacity-changing activities over the lookback window is direct evidence that the ASG never scaled.
- Queries CloudWatch in batches via `GetMetricData` for the ASG's group metrics (`GroupInServiceInstances`, `GroupDesiredCapacity`, `GroupTotalInstances`) when collection is enabled, and for aggregate `CPUUtilization` (Average, Maximum, p95) in all cases.
- Looks up the on-demand cost of each ASG's member instances from Flexera Cloud Cost Optimization (CCO) using the `cost_list_price` billing metric, and projects a monthly figure for incident display.

When the inputs needed to confirm a finding are missing (most commonly because group metrics collection is off), the policy lowers the reported confidence and says so in the incident text rather than asserting a finding at full confidence.

**Filtering and exclusions:**

- ASGs younger than the configured **Minimum ASG Age** are skipped because there isn't enough history to make a reliable call.
- ASGs carrying any tag listed in **Exclusion Tags** are skipped for findings 1, 2, and 3. They are *not* skipped for finding 4 — the hygiene check still surfaces.
- ASGs in regions you've excluded via the **Allow/Deny Regions** parameters are skipped entirely.

### Policy Spend Characterization Details

The policy reports a monthly dollar figure for each cost-related finding to give the reviewer a rough sense of scale. It is **not** a savings number and should not be treated as one.

- For the fixed-size and never-moved-off-floor findings, the figure is `MinSize × per-instance daily on-demand list price × 30.44` (30.44 is the average number of days in a month). It represents what the floor capacity costs at on-demand rates.
- For the over-provisioned floor finding, the figure is `(MinSize − peak in-service instance count) × per-instance daily on-demand list price × 30.44`. This is a **theoretical maximum** — it assumes the unused floor capacity could be fully eliminated and ignores any future scale-up needs that the current Min might be sized for.
- Per-instance daily list prices are sourced from Flexera CCO via the `cost_list_price` metric. If an instance can't be matched in CCO (for example, a brand-new instance that hasn't been ingested yet), it contributes 0 to the figure.
- The figures **do not net out existing Savings Plan or Reserved Instance coverage**. If you've already committed to the baseline capacity, removing it during the commitment window typically saves nothing until the commitment expires. Always cross-check the figure against your active commitments before acting on it.
- Figures are reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Allow/Deny Regions* - Whether the regions listed below should be allowed or denied.
- *Allow/Deny Regions List* - A list of AWS regions to either include or exclude (controlled by the parameter above). Leave empty to evaluate all enabled regions.
- *Statistic Lookback Period* - How many days of CloudWatch and scaling-activity history to analyze. Minimum: 1. Maximum: 90 (CloudWatch does not retain metrics longer than 90 days). Default: 30.
- *Metric Aggregation Period (Seconds)* - The CloudWatch aggregation period (seconds per datapoint). Default: 3600 (one datapoint per hour).
- *Floor Headroom Ratio Threshold* - For the over-provisioned floor finding: flag the ASG when (peak in-service instance count ÷ MinSize) is at or below this ratio. For example, 0.5 means "peak utilization of the floor was 50% or less." Default: 0.5.
- *Floor CPU Threshold (%)* - For the over-provisioned floor finding: flag the ASG when aggregate p95 CPU is at or below this percentage. Default: 20.
- *Minimum ASG Age (Days)* - Skip ASGs younger than this many days because their history is too short to assess. Set to 0 to disable the age filter (every ASG is evaluated regardless of how recently it was created). Default: 30, which matches the default lookback window.
- *Findings To Raise* - Which finding types this policy should evaluate and raise as incidents. Deselect a finding to suppress it. All four are selected by default. Allowed values: `Fixed-size ASG`, `Never Moved Off Floor`, `Over-provisioned Floor`, `Group Metrics Collection Disabled`.
- *Exclusion Tags* - Tags used to opt ASGs out of the cost/over-provisioning findings (1, 2, and 3). ASGs carrying any matching tag are skipped. The hygiene finding (4) still fires regardless. Enter a key name on its own to match any ASG that has that key, or `Key==Value` for an exact match. Other operators (`!=`, `=~`, `!~`) and regex are also supported. Example: `finops:ignore-elasticity`.
- *Exclusion Tags: Any / All* - Whether an ASG is excluded if it matches **any** of the exclusion tags, or only if it matches **all** of them.
- *Attach CSV To Incident Email* - Whether to attach a CSV of the incident data to the incident email.
- *Incident Table Rows for Email Body (#)* - Maximum number of rows to include in the incident table embedded in the email body.

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
