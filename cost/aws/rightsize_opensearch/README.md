# AWS Rightsize OpenSearch Service Domains

## What It Does

This policy template identifies AWS OpenSearch Service domains that are idle (receiving little or no traffic) or underutilized (consuming resources well below their provisioned capacity). It produces separate incidents for idle domains and underutilized domains, providing estimated monthly savings for each finding. Idle domains can optionally be deleted after approval.

## How It Works

The policy enumerates all OpenSearch Service domains across configured regions using the `ListDomainNames` API, retrieves full configuration details via the bulk `DescribeDomains` API, fetches resource tags via `ListTags`, and then collects CloudWatch metrics for each domain using batched `GetMetricData` calls (up to 500 metric queries per request). Domain costs are retrieved from Flexera Cloud Cost Optimization (CCO) to calculate estimated savings.

### Idle Detection Logic

A domain is classified as idle when **all three** of the following conditions are true over the full lookback period:

1. The average daily `OpenSearchRequests` metric (or `ElasticsearchRequests` for legacy Elasticsearch domains) is at or below the **Idle Domain Request Threshold** parameter (default: 100 requests/day).
1. The average `SearchRate` is also at or below the threshold (or the metric has no data for the domain).
1. The average `IndexingRate` is also at or below the threshold (or the metric has no data for the domain).

All three signals must indicate inactivity simultaneously to classify a domain as idle, reducing false positives from domains that receive traffic only on some metrics.

### Rightsizing Logic

The policy identifies the smallest instance type in the same family that can handle the domain's observed peak resource usage with the configured safety margin.

For each domain, the policy computes minimum required resources from peak observed metrics:

- **Required vCPU** = peak CPU utilization (p99) × current vCPU count × safety factor
- **Required memory** = peak Java heap memory usage (the higher of `OldGenJVMMemoryPressure` or `JVMMemoryPressure` metrics, p99) × current instance memory × safety factor

The policy then selects the smallest instance type in the same family whose vCPU count and memory both meet or exceed these requirements. If a smaller valid type exists, the domain is flagged as underutilized and that type is recommended. If no smaller type satisfies the requirements, no recommendation is made.

**Domains that are classified as idle are never also reported as underutilized.** The idle check takes precedence: if a domain meets the idle criteria, it appears only in the idle incident, not the rightsizing incident.

Domains that use UltraWarm or Cold tier storage are excluded from instance type downsize recommendations (warm and cold nodes have their own independent sizing considerations that require separate analysis). They may still be classified as idle.

**Scale-up advisory signals** are included in the recommendation details when any of the following are observed (even for underutilized domains), as informational notes to help operators make a fully-informed decision:

- CPU p99 > 80%
- Java heap memory (JVM) p99 > 75%
- Average `ThreadpoolSearchQueue` depth > 0 (sustained search backlog)
- Average `ThreadpoolWriteQueue` depth > 0 (sustained write backlog)

### Risk Flags

Downsize recommendations carry risk flags when applicable. Risk flags are informational — they do not suppress recommendations, but operators should review them before acting.

| Flag | Condition | Recommended Action |
| --- | --- | --- |
| **Disk Risk** | Domain uses instance storage (EBS not enabled) | Verify the target instance type has sufficient local NVMe storage. Smaller instances in the same family may have less NVMe than the current one. |
| **Network Risk** | Current `NetworkTXThroughput` or `NetworkRXThroughput` maximum is ≥ 80% of the documented baseline for the current instance type | Verify the target instance type's network baseline is adequate for the observed throughput. |
| **EBS IOPS Risk** | Actual combined ReadIOPS + WriteIOPS ≥ 80% of the configured EBS volume IOPS limit | Verify EBS IOPS configuration for the target instance type. |
| **EBS Throughput Risk** | Actual combined read + write throughput ≥ 80% of the configured EBS throughput limit | Verify EBS throughput configuration for the target instance type. |
| **Incomplete Data Risk** | Only one utilization metric (CPU or memory) was available during the lookback period | Review whether the missing metric is expected for this domain; verify the unchecked resource dimension manually before rightsizing. |

### Policy Savings Details

The policy includes an estimated monthly savings figure for each finding.

**Idle domains:** The `Estimated Monthly Savings` equals the domain's full monthly amortized cost as reported in Flexera CCO. This represents the total spend that would be eliminated by deleting the domain.

**Underutilized domains:** The `Estimated Monthly Savings` is estimated by multiplying the domain's monthly CCO cost by the fraction of resources saved — the greater of: (1) 1 minus the ratio of the recommended instance type's vCPU count to the current instance type's vCPU count, or (2) 1 minus the ratio of the recommended instance type's memory to the current instance type's memory. Using the larger of the two ratios better reflects savings for memory-optimized instance families. For example, downsizing from an 8-vCPU/64 GiB instance to a 4-vCPU/32 GiB instance yields an estimated 50% savings.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the domain for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the domain cannot be found in Flexera CCO (e.g., billing data has not yet been ingested), the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Domains with estimated savings below this value are not included in incident output.
- *Exclusion Tags* - Cloud native tags to ignore domains that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter domains containing any of the specified tags or only those that contain all of them.
- *Allow/Deny Regions* - Allow or Deny entered regions. See the README for more details.
- *Allow/Deny Regions List* - A list of allowed or denied regions. See the README for more details.
- *Exclude Recommendations with Risk Flags* - Suppress downsize recommendations that carry the selected risk flags. Risk flags highlight areas — such as storage, network, disk I/O, or incomplete utilization data — where shrinking a domain may carry additional risk. Only applies to underutilized domain recommendations; idle domain findings are not affected. Leave blank to include all recommendations regardless of risk flags. See the README for more details.
- *Statistic Lookback Period* - How many days of historical usage data to analyze when assessing domains. This value cannot be set higher than 90 because AWS only retains usage history for up to 90 days.
- *Idle Domain Request Threshold (Requests/Day)* - Average number of search and indexing requests received per day below which a domain is considered idle. When a domain falls below this level across all traffic signals, it is flagged as idle. Set to 0 to disable idle detection.
- *Rightsizing Safety Factor* - A multiplier applied to peak resource usage when computing the minimum resources required for a rightsized instance. For example, a value of 1.5 means the recommended instance type must be able to handle 1.5 times the observed peak usage. Set a higher value for more headroom.
- *Automatic Actions* - When set, the policy will automatically take the selected action(s) without requiring manual approval.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Delete Idle Domains" action while applying the policy template, all the idle OpenSearch domains that didn't satisfy the policy condition will be deleted.

## Policy Actions

- Sends an email notification.
- Deletes idle OpenSearch domains after approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `elasticache:DescribeCacheClusters`
  - `es:ListDomainNames`
  - `es:DescribeDomains`
  - `es:ListTags`
  - `cloudwatch:GetMetricData`
  - `es:DeleteDomain`*

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
                  "elasticache:DescribeCacheClusters",
                  "es:ListDomainNames",
                  "es:DescribeDomains",
                  "es:ListTags",
                  "cloudwatch:GetMetricData",
                  "es:DeleteDomain"
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
