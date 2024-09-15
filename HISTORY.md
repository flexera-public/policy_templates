# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#2617](https://github.com/flexera-public/policy_templates/pull/2617): POL-1344 Account Support for AWS Untagged Resources Policy Template

#### Description

> `AWS Untagged Resources`: This adds the option to include the AWS account itself in the results and adds the necessary cloud workflow logic to enable accounts to be tagged.
>
> Should natively work as expected with the meta parent, since each child incident would include one account, and the consolidated incident would include all of them.
>
> Additionally, significant modifications were made to speed up policy execution when the savings option is enabled. The previous method took a very long time due to inefficient searching techniques.
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md), [Meta Parent: AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md)
- **Merged At**: 2024-09-12 12:21:20 UTC

---

### PR [#2576](https://github.com/flexera-public/policy_templates/pull/2576): POL-1331 New Policy: Azure Advisor Carbon Reduction Recommendations

#### Description

> This is a new policy to report all CO2 emissions reduction opportunities reported by Azure Advisor.
>
> ### Issues Resolved
>
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=66ce16f9a79b5457a281dbba
>

#### Metadata

- **Policies**: [Azure Advisor Carbon Reduction Recommendations](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/advisor_carbon/README.md), [Meta Parent: Azure Advisor Carbon Reduction Recommendations](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/advisor_carbon/README.md)
- **Merged At**: 2024-09-04 12:07:47 UTC

---

### PR [#2560](https://github.com/flexera-public/policy_templates/pull/2560): POL-411 Low Usage: Added Resource List

#### Description

> This adds a link to the Resource Analyzer Dashboard with the appropriate settings to the incident table to make it easy for the user to see the specific resources that exist in the dimension value with low usage.
>

#### Metadata

- **Policies**: [Low Usage Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/low_usage/README.md)
- **Merged At**: 2024-09-03 20:17:23 UTC

---

### PR [#2601](https://github.com/flexera-public/policy_templates/pull/2601): POL-1252 Cloud Cost Anomaly Alerts: Additional Parameters

#### Description

> New functionality added to `Cloud Cost Anomaly Alerts` policy template. From the CHANGELOG:
>
> - Added `Minimum Period Spend Variance` parameter to optionally limit results based on amount of variance
> - Added `Anomalies To Report` parameter to optionally limit results based on whether the anomaly is upward or downward
> - Added `Variance From Average` field to incident table containing the difference (absolute value) between the total cost and the moving average
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2024-09-03 20:08:10 UTC

---

### PR [#2596](https://github.com/flexera-public/policy_templates/pull/2596): POL-1334 Meta Parent Fix: Empty Policy Responses

#### Description

> This is a fix for an issue with Meta Parents where the policy template would fail if no applied policies exist. To fix this issue, the jq statements that were causing the issue have been replaced with standard jmes_path statements, and any additional filtering has been moved to separate javascript blocks.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2596) for these details.
- **Merged At**: 2024-09-03 18:11:14 UTC

---

### PR [#2597](https://github.com/flexera-public/policy_templates/pull/2597): POL-1336 AWS Savings Plan Recommendations: Remove "Any" Option From Savings Plan Term Parameter

#### Description

> Removes invalid "Any" option from the `Savings Plan Term` parameter in the `AWS Savings Plan Recommendations` policy template. The only valid values for this parameter are 1 year and 3 year.
>
> A handful of other small changes were made to bring policy template into compliance with current Dangerfile tests.
>

#### Metadata

- **Policies**: [AWS Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/recommendations/README.md)
- **Merged At**: 2024-09-03 18:06:30 UTC

---

### PR [#2584](https://github.com/flexera-public/policy_templates/pull/2584): POL-1335 Add ARN to AWS Recommendation Policy Template Incident Tables

#### Description

> This adds a resource ARN field to the incidents of all existing AWS recommendations policy templates. This is because the ARN is a useful value for other functionality that might build off of the incident or recommendations table, such as using the AWS tagging API to tag resources.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2584) for these details.
- **Merged At**: 2024-09-03 13:10:25 UTC

---

### PR [#2544](https://github.com/flexera-public/policy_templates/pull/2544): POL-802 New Policy: Azure Unused Virtual Network Gateways

#### Description

> This is a new policy template to report on unused Azure Virtual Network Gateways.
>
> Currently, savings is not reported because Azure billing data stored in Flexera does not appear to contain Virtual Network Gateway costs at the resource level. This may be added with a later update if a solution is found.
>

#### Metadata

- **Policies**: [Azure Unused Virtual Network Gateways](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_vngs/README.md), [Meta Parent: Azure Unused Virtual Network Gateways](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_vngs/README.md)
- **Merged At**: 2024-08-30 15:52:31 UTC

---

### PR [#2543](https://github.com/flexera-public/policy_templates/pull/2543): POL-803 New Policy: Azure Unused App Service Plans

#### Description

> This is a new policy template to report on unused App Service Plans in Azure.
>

#### Metadata

- **Policies**: [Azure Unused App Service Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_app_service_plans/README.md), [Meta Parent: Azure Unused App Service Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_app_service_plans/README.md)
- **Merged At**: 2024-08-30 12:05:05 UTC

---

### PR [#1917](https://github.com/flexera-public/policy_templates/pull/1917): POL-727 Azure Savings Plan Utilization v0.1.0

#### Description

> Adds Azure Savings Plan Utilization Report to bring parity with what we have for AWS
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-727
>

#### Metadata

- **Policies**: [Azure Savings Plan Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/utilization/README.md)
- **Merged At**: 2024-08-27 13:30:34 UTC

---

### PR [#2567](https://github.com/flexera-public/policy_templates/pull/2567): POL-1325 AWS Oversized S3 Buckets: Switch to GetMetricData

#### Description

> This updates the `AWS Oversized S3 Buckets` policy template to use batched GetMetricData requests to gather metrics in order to speed up execution.
>
> Various small tweaks were also made to bring it in compliance with current Dangerfile tests.
>

#### Metadata

- **Policies**: [AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md), [Meta Parent: AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md)
- **Merged At**: 2024-08-22 18:51:35 UTC

---

### PR [#2566](https://github.com/flexera-public/policy_templates/pull/2566): POL-1324 AWS Burstable EC2 Instances: Switch to GetMetricData

#### Description

> This updates the `AWS Burstable EC2 Instances` policy template to use batched GetMetricData requests to gather metrics in order to speed up execution.
>
> Various small tweaks were also made to bring it in compliance with current Dangerfile tests.
>

#### Metadata

- **Policies**: [AWS Burstable EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/burstable_ec2_instances/README.md), [Meta Parent: AWS Burstable EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/burstable_ec2_instances/README.md)
- **Merged At**: 2024-08-22 18:51:26 UTC

---

### PR [#2557](https://github.com/flexera-public/policy_templates/pull/2557): POL-1323 - fix: AWS Rightsize EC2 get memory metrics for Autoscaling groups

#### Description

> Fix bug preventing Memory metrics from being included in result for some EC2 Instances created by Autoscaling Group
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1323
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md)
- **Merged At**: 2024-08-20 13:21:54 UTC

---

### PR [#2531](https://github.com/flexera-public/policy_templates/pull/2531): POL-980 New AWS Load Balancer Policy Templates

#### Description

> This PR adds two new policy templates, `AWS Unused Application Load Balancers` and `AWS Unused Network Load Balancers`. It also modifies the existing `AWS Unused Classic Load Balancers` policy template to bring it more in alignment with the new policy templates.
>
> I opted for 3 separate templates because there are enough differences between the three, especially when it comes to Classic vs App/Network, that a single policy template for all of them would be complex and cumbersome to maintain. The simplest way to offer users an intuitive experience while making the templates themselves maintainable was to simply have a separate policy template for each.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2531) for these details.
- **Merged At**: 2024-08-19 18:05:12 UTC

---

### PR [#2547](https://github.com/flexera-public/policy_templates/pull/2547): POL-1322 New Policy: Google Label Cardinality Report

#### Description

> This is a new policy that reports on Google Label Cardinality. This template has an important caveat that is unique to Google. From the README:
>
> __NOTE: Google Cloud does not offer a straight-forward way to list all resources in a given Project along with their labels. This report should not be considered complete and should be used for general guidance. A list of supported resources is provided below.__
>
> - Compute
>   - Disks
>   - Images
>   - IP Addresses
>   - Snapshots
>   - Storage Pools
>   - VPN Gateways
>   - VPN Tunnels
>   - Virtual Machines
> - Database
>   - BigQuery Datasets
>   - BigQuery Tables
>   - Cloud SQL for MySQL Instances
> - Storage
>   - Object Storage Buckets
>

#### Metadata

- **Policies**: [Google Label Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/google/label_cardinality/README.md), [Meta Parent: Google Label Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/google/label_cardinality/README.md)
- **Merged At**: 2024-08-16 20:22:13 UTC

---

### PR [#2521](https://github.com/flexera-public/policy_templates/pull/2521): POL-1318 New Policy: AWS CloudTrails With Read Logging Enabled

#### Description

> New policy template that reports CloudTrails with read logging enabled, with the option of disabling read logging.
>

#### Metadata

- **Policies**: [AWS CloudTrails With Read Logging Enabled](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/cloudtrail_read_logging/README.md), [Meta Parent: AWS CloudTrails With Read Logging Enabled](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/cloudtrail_read_logging/README.md)
- **Merged At**: 2024-08-16 13:06:21 UTC

---

### PR [#2485](https://github.com/flexera-public/policy_templates/pull/2485): POL-1262 - feat: scheduled report percent change, alert threshold

#### Description

> Adds percent change field to report fields (additional inform) and capabilities for sending this when a threshold is crossed (alerting use-case)
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1262
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2024-08-14 14:33:46 UTC

---

### PR [#2511](https://github.com/flexera-public/policy_templates/pull/2511): POL-1308 New Policy: Flexera One User Access Report

#### Description

> New policy that produces a list of users and the various roles they have assigned to them in order to assist with auditing users in a Flexera org.
>

#### Metadata

- **Policies**: [Flexera One User Access Report](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/iam/iam_user_report/README.md)
- **Merged At**: 2024-08-14 13:09:41 UTC

---

### PR [#2533](https://github.com/flexera-public/policy_templates/pull/2533): POL-1321 Meta Policy Unpublish Fix

#### Description

> This adds publish to the info block of meta parent policies that corresponds to the child policy. This is to prevent meta parent policies for unpublished child policies from themselves being published by mistake.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2533) for these details.
- **Merged At**: 2024-08-13 19:13:27 UTC

---

### PR [#2534](https://github.com/flexera-public/policy_templates/pull/2534): POL-1294 RBD Policy Logic Fix

#### Description

> Modified logic in unpublished RBD policies to reduce risk of policy failure due to an account having no tags

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2534) for details about unpublished policies.
- **Merged At**: 2024-08-13 18:55:54 UTC

---

### PR [#2496](https://github.com/flexera-public/policy_templates/pull/2496): POL-1311 New Policy: Azure Advisor Compute Instances Recommendations

#### Description

> This is a new policy template that reports virtual machine resizing recommendations from the Azure Advisor tool. See the README for more details.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2496) for details about unpublished policies.
- **Merged At**: 2024-08-13 12:04:51 UTC

---

### PR [#2494](https://github.com/flexera-public/policy_templates/pull/2494): POL-1310 New Policy: AWS EC2 Compute Optimizer Recommendations

#### Description

> This is a new policy template that reports EC2 resizing recommendations from AWS Compute Optimizer tool. See the README for more details.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2494) for details about unpublished policies.
- **Merged At**: 2024-08-13 12:04:43 UTC

---

### PR [#2529](https://github.com/flexera-public/policy_templates/pull/2529): POL-1320 Azure RI/SP Policy API Update

#### Description

> Updates the API versions for various API calls for the `Azure Reserved Instances Recommendations` and `Azure Savings Plan Recommendations` policy templates. This is mainly to fix an issue where the old API versions did not produce results that match the Azure console, causing user confusion and concern.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md), [Meta Parent: Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md), [Azure Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/recommendations/README.md), [Meta Parent: Azure Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/recommendations/README.md)
- **Merged At**: 2024-08-12 16:02:52 UTC

---

### PR [#2527](https://github.com/flexera-public/policy_templates/pull/2527): POL-1319: Fix Spelling Issue In Description: AWS Unused Classic Load Balancers

#### Description

> Fixed minor spelling issue in policy template description

#### Metadata

- **Policies**: [AWS Unused Classic Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_clbs/README.md), [Meta Parent: AWS Unused Classic Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_clbs/README.md)
- **Merged At**: 2024-08-12 13:09:37 UTC

---

### PR [#2505](https://github.com/flexera-public/policy_templates/pull/2505): POL-1315 AWS Rightsize RDS Instances: Additional Metrics

#### Description

> This adds memory and network metrics to the incident output for underutilized instances. These metrics are not used for producing recommendations and are merely for added context to assist the user in making decisions.
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md), [Meta Parent: AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2024-08-12 12:28:34 UTC

---

### PR [#2506](https://github.com/flexera-public/policy_templates/pull/2506): POL-1317 AWS Superseded EC2 Instances Fix/Improvement

#### Description

> Improvements to `AWS Superseded EC2 Instances`. From the CHANGELOG:
>
> - Fixed bug where invalid recommendations with no new resource type would sometimes be included in results
> - Added `Fallback Instance Type Category` parameter to provide alternate recommendations when the selected category is not available
>
> This also updates the local Gemfile to use the current version of Danger
>

#### Metadata

- **Policies**: [AWS Superseded EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_instances/README.md), [Meta Parent: AWS Superseded EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_instances/README.md)
- **Merged At**: 2024-08-12 12:27:51 UTC

---

### PR [#2472](https://github.com/flexera-public/policy_templates/pull/2472): POL-1297 Azure Security Policy Revamps: Part 4

#### Description

> This is a revamp of several Azure Security policy templates. Please see their respective CHANGELOGs and READMEs for details.
>
> Additionally, the `Azure Storage Accounts Without HTTPs Enforced` policy template is being deprecated because it is redundant.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2472) for these details.
- **Merged At**: 2024-08-09 15:01:45 UTC

---

### PR [#2474](https://github.com/flexera-public/policy_templates/pull/2474): POL-1302 New Usage Revamp

#### Description

> This is a revamp of the `New Service Usage` policy template, which has been renamed to `New Usage`. From the CHANGELOG:
>
> - Policy template renamed to `New Usage` to better reflect its functionality
> - Added ability to report new usage for any cost dimension
> - Added ability to specify a cost metric and look back period
> - Added ability to filter results by estimated monthly cost
> - Improved Billing Center filtering options
> - Added additional fields and text to incident output for added context
> - Streamlined code for better readability and faster execution
>
> Note: Ignore the "run_script statements" error. The same script is invoked twice; once with a hard value, and once with a parameter value, so there's not a way to place them in the correct order in both situations without needlessly making two identical scripts.
>

#### Metadata

- **Policies**: [New Usage](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/new_usage/README.md)
- **Merged At**: 2024-08-09 13:13:00 UTC

---

### PR [#2503](https://github.com/flexera-public/policy_templates/pull/2503): POL-1313 SaaS Policy Revamps

#### Description

> These are revamps of the following policy templates:
>
> #### Office 365 Security Alerts
> - Modified credential to correctly match Microsoft Graph credentials in the Flexera platform
> - Several parameters altered to be more descriptive and human-readable
> - Removed unused `Azure AD Tenant ID` parameter
> - Updated Microsoft Graph API call to use production `/v1.0/security/alerts_v2` endpoint
> - Fixed issue where policy template would report alerts unrelated to Office 365
> - Streamlined code for better readability and faster execution
>
> #### Okta Inactive Users
> - Several parameters altered to be more descriptive and human-readable
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
>
> #### ServiceNow Inactive Approvers
> - Several parameters altered to be more descriptive and human-readable
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2503) for these details.
- **Merged At**: 2024-08-09 13:12:36 UTC

---

### PR [#2504](https://github.com/flexera-public/policy_templates/pull/2504): POL-1314 Deprecate Budget Alerts by Cloud Account Policy Template

#### Description

> The `Budget Alerts by Cloud Account` policy template is being deprecated because its functionality can be entirely replicated in the `Budget Alerts` policy template, making it redundant.

#### Metadata

- **Policies**: [Budget Alerts by Cloud Account](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_alerts_by_account/README.md)
- **Merged At**: 2024-08-09 12:13:43 UTC

---

### PR [#2508](https://github.com/flexera-public/policy_templates/pull/2508): fix: minor wording fix on incident detail template

#### Description

> Updated incident message to be more relative for this policy template
>

#### Metadata

- **Policies**: [Flexera Automation Outdated Applied Policies](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/outdated_applied_policies/README.md)
- **Merged At**: 2024-08-08 17:02:13 UTC

---

### PR [#2501](https://github.com/flexera-public/policy_templates/pull/2501): POL-1309 Vendor Spend Commitment Forecast Revamp

#### Description

> This is a revamp of the Vendor Commitment Forecast policy template. From the CHANGELOG:
>
> - Renamed policy template to `Vendor Spend Commitment Forecast` to avoid confusion with policy templates for RIs/SPs
> - Added ability to specify a cost metric to use when gathering spend data
> - Several parameters altered to be more descriptive and human-readable
> - Additional fields added to incident table for context
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Vendor Spend Commitment Forecast](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/forecasting/commitment_forecast/README.md)
- **Merged At**: 2024-08-08 13:06:26 UTC

---

### PR [#2468](https://github.com/flexera-public/policy_templates/pull/2468): POL-1297 Azure Security Policy Revamps: Part 3

#### Description

> This is a revamp of several Azure Security policies. Please see their respective CHANGELOGs and READMEs for details.
>
> This also fixes a small issue in the Azure Rightsize SQL policy with how actions are logged.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2468) for these details.
- **Merged At**: 2024-08-01 12:23:52 UTC

---

### PR [#2471](https://github.com/flexera-public/policy_templates/pull/2471): POL-1301 Add Case Sensitivity Option to RBD Policy Templates

#### Description

> This adds the option to retain the casing of tag values when creating RBDs instead of normalizing them to lowercase. Default is still normalizing them to ensure consistency with previous versions and to reduce the risk of the policy template failing due to duplicate values with different casings.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2471) for these details.
- **Merged At**: 2024-08-01 12:21:31 UTC

---

### PR [#2475](https://github.com/flexera-public/policy_templates/pull/2475): POL-1303 Kubecost Policy Template Revamps

#### Description

> This is a revamp of the 2 Kubecost policy templates. From their CHANGELOGs:
>
> #### Kubecost Cluster Rightsizing Recommendation
>
> - Policy template renamed to `Kubecost Cluster Rightsizing Recommendation` to better reflect its functionality
> - Kubecost API requests now use HTTPS for added security
> - Policy template now falls back to Flexera-configured currency if Kubecost does not report a currency
> - Added additional context to incident
> - Renamed some incident fields to conform with other recommendations policy templates
> - Streamlined code for better readability and faster execution
> - Policy template now requires a valid Flexera credential
>
> #### Kubecost Request Rightsizing Recommendations
>
> - Policy template renamed to `Kubecost Container Request Rightsizing Recommendations` to better reflect its functionality
> - Kubecost API requests now use HTTPS for added security
> - Policy template now falls back to Flexera-configured currency if Kubecost does not report a currency
> - Added additional context to incident
> - Renamed some incident fields to conform with other recommendations policy templates
> - Streamlined code for better readability and faster execution
> - Policy template now requires a valid Flexera credential
>

#### Metadata

- **Policies**: [Kubecost Cluster Rightsizing Recommendation](https://github.com/flexera-public/policy_templates/tree/master/cost/kubecost/cluster/README.md), [Kubecost Container Request Rightsizing Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/kubecost/sizing/README.md)
- **Merged At**: 2024-07-31 20:58:49 UTC

---

### PR [#2478](https://github.com/flexera-public/policy_templates/pull/2478): POL-1306 Add Hourly Cost to AHUB Policy Templates

#### Description

> This adds Hourly Cost and Currency as fields in the incident output for the three Azure AHUB policy templates.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2478) for these details.
- **Merged At**: 2024-07-31 20:58:20 UTC

---

### PR [#2477](https://github.com/flexera-public/policy_templates/pull/2477): POL-1305 Azure Rightsize SQL Managed Instances 2-Core Recommendation Fix

#### Description

> SQL instance sizes with only 2 cores are not available in most circumstances for SQL Managed Instances. This fix ensures that these invalid recommendations do not appear in the results by throwing out any downsizing recommendations that are for fewer than 4 cores.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md), [Meta Parent: Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md)
- **Merged At**: 2024-07-31 12:41:36 UTC

---

### PR [#2476](https://github.com/flexera-public/policy_templates/pull/2476): POL-1304 Add Hourly Cost to Time Stopped Policy Templates

#### Description

> Update to the `AWS EC2 Instances Time Stopped Report` and `Azure Compute Instances Time Powered Off Report` policy templates.
>
> This adds `Estimated Hourly Cost` and `Currency` fields to the incident to help users assess potential impact of terminating instances.
>

#### Metadata

- **Policies**: [AWS EC2 Instances Time Stopped Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/ec2_stopped_report/README.md), [Meta Parent: AWS EC2 Instances Time Stopped Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/ec2_stopped_report/README.md), [Azure Compute Instances Time Powered Off Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/compute_poweredoff_report/README.md), [Meta Parent: Azure Compute Instances Time Powered Off Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/compute_poweredoff_report/README.md)
- **Merged At**: 2024-07-31 12:07:05 UTC

---

### PR [#2452](https://github.com/flexera-public/policy_templates/pull/2452): POL-1297 Azure Security Policy Revamps: Part 2

#### Description

> This is a revamp of several Azure Security policies. Please see their respective CHANGELOGs and READMEs for details.
>
> This also deprecates `Azure Resources with public IP address` due to this policy not really being necessary for CIS compliance and not providing complete or particularly useful functionality.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2452) for these details.
- **Merged At**: 2024-07-31 12:06:47 UTC

---

### PR [#2460](https://github.com/flexera-public/policy_templates/pull/2460): POL-1288 Azure Reserved Instance/Savings Plans Updates

#### Description

> This updates the `Azure Reserved Instances Recommendations` and `Azure Savings Plan Recommendations` policy templates to add Resource Group scope support. Additionally, `Azure Savings Plan Recommendations` now has a meta policy and has had some improvements to reduce execution time.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2460) for these details.
- **Merged At**: 2024-07-29 15:07:49 UTC

---

### PR [#2451](https://github.com/flexera-public/policy_templates/pull/2451): POL-1297 Azure Security Policy Revamps: Part 1

#### Description

> This is a revamp of several Azure Security policies. See their respective CHANGELOGS and READMEs for more details.
>
> This also includes two small Dangerfile tweaks around Graph API credentials.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2451) for these details.
- **Merged At**: 2024-07-26 12:08:05 UTC

---

### PR [#2459](https://github.com/flexera-public/policy_templates/pull/2459): POL-1169 P90, P95 and P99 for Azure Rightsize Managed Disks

#### Description

> I implemented the statistics P90, P95 and P99 for the parameters:
> - IOPS Threshold Statistic
> - Throughput Threshold Statistic
>
> ### Issues Resolved
>
> - https://flexera.attlassian.com/browse/POL-1169
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-07-25 18:21:28 UTC

---

### PR [#2453](https://github.com/flexera-public/policy_templates/pull/2453): POL-1300 - fix: use `PaginationToken` for paginating tagging API

#### Description

> Fixes an issue discovered when troubleshooting the `AWS Untagged Resources` Policy Template
>
>  - Use [`PaginationToken`](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html#API_GetResources_RequestSyntax) for paginating tagging API
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md), [AWS Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/tag_cardinality/README.md)
- **Merged At**: 2024-07-24 17:21:06 UTC

---

### PR [#2447](https://github.com/flexera-public/policy_templates/pull/2447): POL-1281 AWS Security Policy Revamps: Part 6

#### Description

> This is a revamp of the last set of AWS Security policies. See their respective CHANGELOGs and READMEs for more details.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2447) for these details.
- **Merged At**: 2024-07-24 17:19:57 UTC

---

### PR [#2429](https://github.com/flexera-public/policy_templates/pull/2429): POL-1281 AWS Security Policy Revamps: Part 5

#### Description

> This is a revamp of two RDS Security policies:
>
> **AWS Publicly Accessible RDS Instances**
> - Policy template renamed to `AWS Publicly Accessible RDS Instances` to better reflect its functionality
> - Added more robust tag filtering options
> - Added option to automatically terminate offending instances
> - Added additional fields to incident table for added context
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>
> **AWS Unencrypted RDS Instances**
> - Added more robust tag filtering options
> - Added additional fields to incident table for added context
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2429) for these details.
- **Merged At**: 2024-07-22 15:36:24 UTC

---

### PR [#2425](https://github.com/flexera-public/policy_templates/pull/2425): POL-1281 AWS Security Policy Revamps: Part 4

#### Description

> This is a revamp for all of the Security policy templates focused on AWS CloudTrail logs. See the individual CHANGELOGs for information on the changes in each template.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2425) for these details.
- **Merged At**: 2024-07-22 12:23:58 UTC

---

### PR [#2424](https://github.com/flexera-public/policy_templates/pull/2424): FOPTS-4349 Display recommendation in the local currency.

#### Description

> Implemented automatic currency detection and conversion, ensuring recommendations are displayed in the currency configured in the user's settings.
>
> ### Issues Resolved
> https://flexera.atlassian.net/browse/SQ-9018
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-07-19 20:48:06 UTC

---

### PR [#2414](https://github.com/flexera-public/policy_templates/pull/2414): POL-1281 AWS Security Policy Revamps: Part 3

#### Description

> This is a revamp of two policy templates:
>
> #### AWS Customer Managed Keys (CMKs) Without Rotation Enabled
> - Policy template renamed to `AWS Customer Managed Keys (CMKs) Without Rotation Enabled` to better reflect its functionality
> - Added option to filter results by region
> - Added additional fields to incident table for added context
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>
> #### AWS Internet-Accessible Elastic Load Balancers
> - Policy template renamed to `AWS Internet-Accessible Elastic Load Balancers` to better reflect its functionality
> - Added more robust tag-filtering options
> - Added additional fields to incident table for added context
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2414) for these details.
- **Merged At**: 2024-07-19 14:28:24 UTC

---

### PR [#2428](https://github.com/flexera-public/policy_templates/pull/2428): POL-1295 Azure Reserved Instances Recommendation: Shared Fix

#### Description

> This is an update to the Azure Reserved Instances Recommendation policy to make it so that, like the equivalent Savings Plan policy, it reports "All" for the Subscription Name, and nothing for the Subscription ID, when producing Shared recommendations.
>
> Additionally, some small cosmetic changes were made to bring the policy in alignment with current Dangerfile tests.
>
> Finally, the Dangerfile tests for recommendation policy incident fields has been updated to properly account for the differences between Usage Reduction and Rate Reduction policies.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md), [Meta Parent: Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md)
- **Merged At**: 2024-07-19 12:39:44 UTC

---

### PR [#2411](https://github.com/flexera-public/policy_templates/pull/2411): POL-1281 AWS Security Policy Revamps: Part 2

#### Description

> This is a revamp for all of the Security policy templates focused on AWS IAM. See the individual CHANGELOGs for information on the changes in each template.
>
> Also includes a minor Dangerfile test fix so that, in the README, AWS permissions with a `-` character are correctly interpreted.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2411) for these details.
- **Merged At**: 2024-07-19 12:39:30 UTC

---

### PR [#2396](https://github.com/flexera-public/policy_templates/pull/2396): POL-1287 RBD Policy API Update

#### Description

> This updates the unpublished RBD policies to use [the newer APIs documented here](https://developer.flexera.com/docs/api/finops-customizations/v1). Functionality is otherwise unchanged.
>
> Additionally, some minor updates were made to the policies and the READMEs to conform to current standards/tests.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2396) for these details.
- **Merged At**: 2024-07-17 13:32:10 UTC

---

### PR [#2389](https://github.com/flexera-public/policy_templates/pull/2389): POL-1281 AWS Security Policy Revamps: Part 1

#### Description

> This is a revamp for the following policy templates:
>
> - AWS Regions Without Config Fully Enabled
> - AWS Regions Without Default EBS Encryption
> - AWS Unencrypted EBS Volumes
> - AWS Elastic Load Balancers With Unencrypted Listeners
>
> Additionally, the `AWS Unencrypted ELB Listeners (CLB)` policy template has been deprecated because its functionality has been folded into `AWS Elastic Load Balancers With Unencrypted Listeners`
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2389) for these details.
- **Merged At**: 2024-07-17 13:16:10 UTC

---

### PR [#1630](https://github.com/flexera-public/policy_templates/pull/1630): POL-745 SaaS Manager - SaaS App User Report by Category Revamp/Unpublish

#### Description

> This is part of a broader initiative to update our SaaS Manager FSM policies to use the correct API endpoints for APAC. The policy itself has also been revamped along similar lines to other policies.
>
> Note: This policy still uses the now-deprecated internal SaaS Manager API. This is because the new API does not yet support the requests this policy needs to make to function. **The policy is being unpublished for now until this support is added.**
>
> From the CHANGELOG:
> - Added support for APAC API endpoint
> - Policy now uses and requires a general Flexera One credential
> - Incident summary now includes applied policy name
> - General code cleanup and normalization
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1630) for details about unpublished policies.
- **Merged At**: 2024-07-16 12:12:16 UTC

---

### PR [#2404](https://github.com/flexera-public/policy_templates/pull/2404): POL-1271 Add parameter to decide recommending HDD or not

#### Description

> Users wanted a parameter to enable or disable recommendations that suggested switching disk tier to Standard HDD.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/POL-1271
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-07-15 20:14:37 UTC

---

### PR [#2394](https://github.com/flexera-public/policy_templates/pull/2394):  Fix syntax erros from the meta parent policy of Azure Synapse

#### Description

>  Fix syntax errors from the meta parent policy of Azure Synapse
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/POL-1282
>

#### Metadata

- **Policies**: [Azure Rightsize Synapse SQL Pools](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_synapse_sql_pools/README.md), [Meta Parent: Azure Rightsize Synapse SQL Pools](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_synapse_sql_pools/README.md)
- **Merged At**: 2024-07-15 19:49:21 UTC

---

### PR [#2376](https://github.com/flexera-public/policy_templates/pull/2376): POL-1279 AWS RDS Instances With Unapproved Backup Settings Revamp

#### Description

> This is a revamp of the `AWS RDS Backup Settings` policy template, which has been renamed to `AWS RDS Instances With Unapproved Backup Settings` to better indicate what it does. From the CHANGELOG:
>
> - Policy template category changed to `Compliance`
> - Resources can be filtered via region using either an allow or deny list
> - Resources can now be filtered by tag
> - Resources can now be tested for backup window or retention period in isolation
> - Added additional incident fields to add context
> - Normalized incident export to be consistent with other policies
> - Policy template no longer raises new escalations if tag data changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Policy template now requires a valid Flexera credential
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2376) for these details.
- **Merged At**: 2024-07-15 17:50:39 UTC

---

### PR [#2388](https://github.com/flexera-public/policy_templates/pull/2388): POL-1237 Azure Hybrid Use Benefit for SQL Improvements

#### Description

> This is a small improvement to the `Azure Hybrid Use Benefit for SQL` policy template. From the CHANGELOG:
>
> - Added ability to filter results by SQL resource type via `SQL Resource Types` parameter
> - Added ability to filter results by SQL Virtual Machine image SKU via `SQL Virtual Machine Image SKUs` parameter
> - Fixed bug where Elastic Pool recommendations were not properly reported in incident
>

#### Metadata

- **Policies**: [Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md), [Meta Parent: Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md)
- **Merged At**: 2024-07-15 12:28:58 UTC

---

### PR [#2382](https://github.com/flexera-public/policy_templates/pull/2382): POL-1280 Flexera Users With Explicit Roles Revamp

#### Description

> This is a revamp of the `Flexera Users With Explicit Roles` policy template. From the CHANGELOG:
>
> - Specific roles can now be ignored via the `Role Ignore List` parameter
> - Policy template renamed to `Flexera Users With Explicit Roles` to better reflect its functionality
> - Policy template now uses newer [Flexera IAM APIs](https://developer.flexera.com/docs/api/iam/v1)
> - Incident table now includes additional fields for added context
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Flexera Users With Explicit Roles](https://github.com/flexera-public/policy_templates/tree/master/compliance/flexera/iam/iam_explicit_user_roles/README.md)
- **Merged At**: 2024-07-09 20:14:36 UTC

---

### PR [#2393](https://github.com/flexera-public/policy_templates/pull/2393): POL-1285 Powered Off Report Math Fix

#### Description

> This fixes a bug in the `AWS EC2 Instances Time Stopped Report` and `Azure Compute Instances Time Powered Off Report` policy templates where discrepancies in the data returned by Flexera CCO would sometimes cause tiny negative values for the amount of time an instance has been powered off. This would result in these instances appearing in the results erroneously, because negative numbers are less than 0. Also, an instance being powered off for a negative amount of time makes no sense, at least in the context of classical physics.
>
> The fix simply checks if the calculated hours powered off is < 0, and if so, sets it to 0 before any further calculations or results are produced.
>

#### Metadata

- **Policies**: [AWS EC2 Instances Time Stopped Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/ec2_stopped_report/README.md), [Meta Parent: AWS EC2 Instances Time Stopped Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/ec2_stopped_report/README.md), [Azure Compute Instances Time Powered Off Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/compute_poweredoff_report/README.md), [Meta Parent: Azure Compute Instances Time Powered Off Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/compute_poweredoff_report/README.md)
- **Merged At**: 2024-07-09 20:04:03 UTC

---

### PR [#2395](https://github.com/flexera-public/policy_templates/pull/2395): POL-1286 New Policy: Azure Rightsize SQL Managed Instances

#### Description

> This is a new policy to produce rightsize recommendations for Azure SQL Managed Instances. There are enough differences from other SQL offerings at Azure to warrant a distinct policy:
>
> - Many informational fields exist for Azure SQL Servers/Databases that don't exist for Azure SQL Managed Instances and vice versa.
> - Number of connections is not a valid metric for Azure SQL Managed Instances. For this reason, this policy only produces downsize recommendations, though delete actions are still available as an option.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md), [Meta Parent: Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md)
- **Merged At**: 2024-07-09 20:03:32 UTC

---

### PR [#2375](https://github.com/flexera-public/policy_templates/pull/2375): POL-1278 Deprecate/Unpublish Azure Tag Resources with Resource Group Name Policy

#### Description

> This both deprecates and unpublishes the `Azure Tag Resources with Resource Group Name` policy. This policy does one strange, highly specific thing that doesn't need to be in the catalog; it adds a tag containing the name of the resource group to Azure resources.

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2375) for details about unpublished policies.
- **Merged At**: 2024-07-09 12:03:39 UTC

---

### PR [#2360](https://github.com/flexera-public/policy_templates/pull/2360): POL-1167 p90/95/99 Support for Azure Rightsize Compute/SQL Policies

#### Description

> This adds support for p90/p95/p99 metrics to the `Azure Rightsize Compute Instances` and `Azure Rightsize SQL Databases` policy templates as well as some other changes outlined below:
>
> Azure Rightsize Compute Instances Changelog:
> - Added support for p90, p95, and p99 metrics for both CPU and memory.
> - Improved calculations for `Minimum` and `Maximum` for both CPU and memory.*
>
> Azure Rightsize SQL Databases Changelog:
> - Added `Threshold Statistic` parameter to assess utilization based on various CPU metrics
> - Added CPU minimum, maximum, p90, p95, and p99 metrics to incident table
>
> \* Previously, the policy was actually reporting the daily average minimum and maximum CPU usage, since it was averaging the daily metrics returned by the Azure API. It now reports the lowest minimum value and the highest maximum value from those data sets instead, which is more accurate and looks less strange next to the relevant p90/p95/p99 metrics.
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md), [Meta Parent: Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md), [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md), [Meta Parent: Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2024-07-02 19:13:24 UTC

---

### PR [#2374](https://github.com/flexera-public/policy_templates/pull/2374): POL-1277 Cheaper Regions Revamp

#### Description

> This deprecates the `Cheaper Regions` policy template and replaces it with three new cloud-specific policy templates. This is more in keeping with how other similar policies work, and will make it easier to extend these policy templates with cloud-specific functionality in the future.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2374) for these details.
- **Merged At**: 2024-07-02 14:45:36 UTC

---

### PR [#2361](https://github.com/flexera-public/policy_templates/pull/2361): POL-1275 Low Account Usage Revamp

#### Description

> This is a revamp of the `Low Account Usage` policy. From the CHANGELOG:
>
> - Policy template renamed to `Low Usage Report`
> - Costs can now be sliced against any cost dimension rather than just vendor account
> - Costs can now be assessed based on various cost metrics
> - Costs are gathered for a user-specified number of days rather than across the current month
> - Costs can be filtered by Billing Center as either an allow list or a deny list
> - Incident table now provides additional contextual data
> - Streamlined code for better readability and faster execution
>
> Additionally, this is a deprecation of the `Low Service Usage` policy. Its functionality is now rolled into this one.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2361) for these details.
- **Merged At**: 2024-07-02 14:35:36 UTC

---

### PR [#2371](https://github.com/flexera-public/policy_templates/pull/2371): POL-1276 New Policy: Fixed Cost Common Bill Ingestion

#### Description

> This is a new policy template, `Fixed Cost Common Bill Ingestion`, that inserts fixed costs into Flexera CCO via CBI. It will automatically create the necessary CBI endpoint, if it does not already exist, generate the CSV, and upload it to the endpoint.
>
> This PR also includes a small tweak to the Dangerfile to avoid false positives for comma separation when a comma is being referenced inside of a replace statement, such as "/,/"
>

#### Metadata

- **Policies**: [Fixed Cost Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/fixed_cost_cbi/README.md)
- **Merged At**: 2024-07-01 15:07:25 UTC

---

### PR [#2355](https://github.com/flexera-public/policy_templates/pull/2355): POL-1271 Azure Rightsize Managed Disks: SKU Filtering

#### Description

> This update to the `Azure Rightsize Managed Disks` policy adds support for filtering by disk SKU so that certain disks, such as HDDs, can be omitted from the results.
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-07-01 12:35:05 UTC

---

### PR [#2261](https://github.com/flexera-public/policy_templates/pull/2261): FOPTS-3684 Azure Synapse SQL Pools

#### Description

> Policy to get optimization recommendations for Azure Synapse service to realize more savings.
>
> ### Issues Resolved
>
> Policy can recommend rightsizing dedicated pool compute resources or recommend to pause them to result in substantial potential savings.
>

#### Metadata

- **Policies**: [Azure Rightsize Synapse SQL Pools](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_synapse_sql_pools/README.md), [Meta Parent: Azure Rightsize Synapse SQL Pools](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_synapse_sql_pools/README.md)
- **Merged At**: 2024-06-27 22:32:04 UTC

---

### PR [#2354](https://github.com/flexera-public/policy_templates/pull/2354): POL-1270 GitHub Policy Revamps

#### Description

> This is a revamp of all of the GitHub policy templates. Additionally, the policy master permission automation has been updated to handle GitHub.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2354) for these details.
- **Merged At**: 2024-06-27 12:05:44 UTC

---

### PR [#2345](https://github.com/flexera-public/policy_templates/pull/2345): POL-1260 Cloud Spend Forecast - Straight-Line Revamp

#### Description

> NOTE: Errors are false positives from files being moved around.
>
> This is a revamp of the `Cloud Spend Forecast - Straight-Line` policy template. From the CHANGELOG:
>
> - Fixed issue where graph would not render if dimension name contains an ampersand
> - Several parameters altered to be more descriptive and human-readable
> - Added support for both simple and linear regression models via parameter
> - Added support for splitting cost by any arbitrary dimension
> - Added ability to filter by Billing Center via an allow or deny list
> - Streamlined code for better readability and faster execution
>
> Additionally, the `Cloud Spend Forecast - Straight-Line (Simple Model)` policy template has been deprecated. Its functionality has been folded into this policy template instead.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2345) for these details.
- **Merged At**: 2024-06-26 15:17:34 UTC

---

### PR [#2336](https://github.com/flexera-public/policy_templates/pull/2336): POL-1259 Cloud Spend Moving Average Report Revamp

#### Description

> This is a revamp of the previously-named `Cloud Spend Forecast - Moving Average` policy template. It is now named `Cloud Spend Moving Average Report`. I did a fair bit of investigating into the history of this policy, and from what I can tell, it has never been a forecasting policy template, and a moving average is not a formula one can meaningfully use to forecast future cost. The policy template was originally named `Moving Average` and did not claim to provide a forecast, but this was changed at some point without any forecasting functionality being added to the policy template.
>
> From the CHANGELOG:
>
> - Renamed policy template and updated description to better reflect functionality
> - Added ability to filter by Billing Center as an allow list or a deny list
> - Added logic to ensure redundant Billing Centers don't skew results
> - Improvements made to moving average calculation for better accuracy
> - Incident table now used to display the moving average data used in the chart
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Cloud Spend Moving Average Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/moving_average/README.md)
- **Merged At**: 2024-06-26 12:08:07 UTC

---

### PR [#2339](https://github.com/flexera-public/policy_templates/pull/2339): POL-1269 Publish Meta Parent Policies

#### Description

> This makes several changes to add meta parent policies to the catalog:
>
> - Removes the `publish: false` flag from meta parent policies.
> - Changes their names to start with "Meta Parent: " to reduce risk of confusion with regular policies.
> - Changes their category to "Meta" to reduce risk of confusion with regular policies.
> - Policy description now contains information about meta policies and directs user to the meta policy README.
> - The meta policy README has been updated to better guide users on the functionality.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2339) for these details.
- **Merged At**: 2024-06-25 20:58:16 UTC

---

### PR [#2334](https://github.com/flexera-public/policy_templates/pull/2334): POL-1267 AWS Accounts Missing Service Control Policies Revamp

#### Description

> This is a revamp of the `AWS Accounts Missing Service Control Policies` policy. From the CHANGELOG:
>
> - Changed policy template name to `AWS Accounts Missing Service Control Policies` to better reflect its functionality
> - Added ability to audit for multiple Service Control Policies in a single execution
> - Streamlined code for better readability and faster execution
> - Policy template now requires a valid Flexera credential
>

#### Metadata

- **Policies**: [AWS Accounts Missing Service Control Policies](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/missing_scps/README.md)
- **Merged At**: 2024-06-24 17:13:54 UTC

---

### PR [#2335](https://github.com/flexera-public/policy_templates/pull/2335): POL-1268 AWS/Azure Expiring Reserved Instances Revamp

#### Description

> This is a revamp of the AWS/Azure Expiring Reserved Instances policies. From the CHANGELOGs:
>
> - Policy is no longer deprecated
> - Added ability to filter results by Billing Center
> - Additional fields added to incident to provide more context
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS Expiring Reserved Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/expiration/README.md), [Azure Expiring Reserved Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/expiration/README.md)
- **Merged At**: 2024-06-21 12:13:03 UTC

---

### PR [#2317](https://github.com/flexera-public/policy_templates/pull/2317): POL-1255 Cloud Bill Processing Error Notification Revamp

#### Description

> This is a revamp of the `Bill Processing Error Notification` policy. From the CHANGELOG:
>
> - Renamed to `Cloud Bill Processing Error Notification` to better indicate that it is specific to Cloud Cost Optimization
> - Parameters altered to be more descriptive and human-readable
> - Added additional fields to incident table to provide more context
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Cloud Bill Processing Error Notification](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/bill_processing_errors_notification/README.md)
- **Merged At**: 2024-06-17 12:05:27 UTC

---

### PR [#2312](https://github.com/flexera-public/policy_templates/pull/2312): POL-1080 AWS Savings Realized From Rate Reduction Purchases Revamp

#### Description

> This is a revamp of the AWS Savings Realized From Rate Reduction Purchases policy. From the CHANGELOG:
>
> - Policy template renamed to `AWS Savings Realized From Rate Reduction Purchases` to better indicate that it is not specific to reservations
> - Several parameters altered to be more descriptive and human-readable
> - Policy now builds report based on a user-specified number of months back rather than the user specifying a specific start and end date
> - Fixed issue with invalid results if user specifies both a parent and child billing center for the `Allow/Deny Billing Center List` parameter
> - Streamlined code for better readability and faster execution
>
> I also made a slight tweak to a Dangerfile test; the policy name change test no longer mentions manually removing the old policy from the catalog since this should no longer be necessary due to improved policy catalog automation.
>

#### Metadata

- **Policies**: [AWS Savings Realized From Rate Reduction Purchases](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_realized/README.md)
- **Merged At**: 2024-06-14 14:17:10 UTC

---

### PR [#2308](https://github.com/flexera-public/policy_templates/pull/2308): POL-1078 AWS Expiring Savings Plans Revamp

#### Description

> This is a revamp of the AWS Expiring Savings Plans Revamp policy. From the CHANGELOG:
>
> - Added more fields to incident table to provide more context
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>

#### Metadata

- **Policies**: [AWS Expiring Savings Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/expiration/README.md)
- **Merged At**: 2024-06-14 13:03:29 UTC

---

### PR [#2306](https://github.com/flexera-public/policy_templates/pull/2306): POL-1239 New Policy: Azure Rightsize SQL Database Storage

#### Description

> This is a new policy, `Azure Rightsize SQL Database Storage`. From the README:
>
> > This policy checks the storage usage for all the Azure SQL database instances purchased using the vCore purchasing model and determines if a smaller maximum storage space would be viable. A report is created with these recommendations that can optionally be emailed.
> >
> > Only vCore purchases are supported because DTU-purchased databases cannot have their maximum storage space changed independently without changing the entire SKU, including CPU and memory usage. Automatic actions are not supported because a SQL database cannot have its maximum storage space reduced; a new smaller database would need to be provisioned and data would need to be migrated to it.
>
> Additionally, this adds a new JSON asset for Azure database storage pricing along with Github workflow automation to periodically update that asset.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2306) for these details.
- **Merged At**: 2024-06-13 13:21:15 UTC

---

### PR [#2320](https://github.com/flexera-public/policy_templates/pull/2320): POL-1263 AWS Cost Report - EC2 Instance Cost Per Hour

#### Description

> This is a new, currently unpublished policy for reporting Instance Cost Per Hour for EC2 instances.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2320) for details about unpublished policies.
- **Merged At**: 2024-06-12 18:50:24 UTC

---

### PR [#2314](https://github.com/flexera-public/policy_templates/pull/2314): POL-1081 Azure China Common Bill Ingestion Revamp

#### Description

> This is a revamp of the Azure China Common Bill Ingestion policy. From the CHANGELOG:
>
> - Policy now supports `Previous Month` for `Month To Ingest` parameter
> - Reworked parameters to be more clear and consistent with other policy templates
> - Streamlined code for better readability and faster execution
>
> Some Dangerfile tests were also updated to not treat Azure China stuff as though it were normal Azure to avoid false errors/warnings. The policy permissions generation automation was also updated for the same reason.
>

#### Metadata

- **Policies**: [Azure China Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/azure_china_cbi/README.md)
- **Merged At**: 2024-06-12 18:48:08 UTC

---

### PR [#2294](https://github.com/flexera-public/policy_templates/pull/2294):  FOPTS-3682 Refactor Turbonomic Authentication: cookies to token-base

#### Description

> Address [FOPTS-3682](https://flexera.atlassian.net/browse/FOPTS-3682)
>
> List of changes :
>
> 1. **Add Turbonomic Credentials:** Integrate basic Turbonomic credentials to obtain an access token.
> 2. **Replace Authentication Method:** Transition all cookie-based authentication to token-based authentication.
> 3. **Align PT Codes with GitHub Tests:** Update PT codes to match GitHub tests, including reordering parameters and fields in DS and JS codes, adding necessary fields and comments to parameters, and renaming the Pagination variable.
> 4. **Update PT Validation:** Add Turbonomic credential and list PTs to `validated_policy_templates.yaml` and update the `generate_policy_master_permissions.rb` file to include Turbonomic credential.
> 5. **Revise Documentation:** Update the README and Changelog files to reflect the changes, including detailed descriptions of modifications and any new requirements necessary to pass GitHub tests.
> 6. **Deprecate the auth cookie refresh policy :** Update the PT, README and Changelog files to deprecated.
>
>
> ### Issues Resolved
>
> IBM/Turbonomic APIs were updated to support bearer token based authentication. CCO/Turbonomic integration needs to be updated accordingly to move from cookie-based to token-based authentication.
> Documents: https://www.ibm.com/docs/en/tarm/8.12.4?topic=cookbook-authenticating-oauth-20-clients-api
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2294) for these details.
- **Merged At**: 2024-06-11 16:15:44 UTC

---

### PR [#2307](https://github.com/flexera-public/policy_templates/pull/2307): FOPTS-4199 Fixing calculation of the Premium SSD price

#### Description

> Fixed premium ssd price calculation
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-8064
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-06-10 23:17:48 UTC

---

### PR [#2227](https://github.com/flexera-public/policy_templates/pull/2227): POL-1240 - Rename `AWS Superseded EBS Volumes` and Introduce new `AWS Rightsize EBS Volumes` Policy Templates

#### Description

> A request from customer – provided AWS EBS Provisioned IOPS Rightsizing Recommendations.. after talking with Shawn and looking at what we currently have in the Catalog this snowballed into a larger story to provide this capability:
>
> Included in this PR:
>  - Currently implemented "EBS Rightsize" PT is renamed to AWS Superseded EBS Volumes
>  - Unused Volumes PT is deprecated
>  - New PT with "EBS Rightsize" name that identifies both "idle" (unattached, or attached and zero read/write ops) and "underutilized" (~low used capacity~, low used provisioned iops)
>
> Underutilized Storage Capacity was not implemented due to reasons that will be outlined in the README
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1240
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2227) for these details.
- **Merged At**: 2024-06-05 18:39:34 UTC

---

### PR [#2292](https://github.com/flexera-public/policy_templates/pull/2292): POL-1251 Unpublish Unused Deprecated Policies

#### Description

> The following deprecated policies are not in use in any customer environment across all 3 shards. As such, they are being unpublished:
>
> AWS Usage Report - Amount of Instance Memory Used
> Application Migration Recommendations
> Azure Migrate Integration
> NetFlow Top Talkers
> SaaS Manager - User Status Change

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2292) for details about unpublished policies.
- **Merged At**: 2024-06-05 15:29:07 UTC

---

### PR [#2295](https://github.com/flexera-public/policy_templates/pull/2295): Fixing issue with disk name calculation

#### Description

> This PR fixes an issue with the disk name calculation. In case of error, we'd want to log the disk details and continue processing
>
> ### Issues Resolved
>
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-06-04 21:36:34 UTC

---

### PR [#2291](https://github.com/flexera-public/policy_templates/pull/2291): POL-1250 Meta Policy Incident Table

#### Description

> When meta policies were originally created, we did not have the ability to put hyperlinks within the incident table. For this reason, the incident that showed a full list of child policies rendered this table via markdown in the detail_template. This causes major issues with slowdown, sometimes causing the incident page to not load at all, when there are a large number of child poliices.
>
> Hyperlink support now exists for incident tables, so this updates the meta policies to use the actual incident table instead. Additionally, this table includes fields for a 2nd incident for policies that raise multiple incidents; these fields are simply blank unless a child policy has raised 2 distinct incidents.
>
> The hyperlinks are in the `Applied Policy Name` and `Incident Summary` fields, linking to the applied child policy and child policy incident respectively.
>
> These changes are non-breaking for existing policies. That said, anyone that wants this new functionality will need to upload and apply the updated meta policy template after this change is merged.
>
> NOTE: The meta policies were all generated with the script. When reviewing this PR, the focus should be on the 3 files in the `tools/meta_parent_policy_compiler/` directory.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2291) for these details.
- **Merged At**: 2024-06-04 16:22:17 UTC

---

### PR [#2221](https://github.com/flexera-public/policy_templates/pull/2221): POL-1230 Policy Template Synchronization Revamp

#### Description

> This is a revamp of the `Policy Template Synchronization` policy. All code was rewritten from scratch to follow current best practices. From the CHANGELOG:
>
> - Policy now raises two incidents: new/updated policies and defunct policies
> - Added support for deleting defunct policies
> - Reworked policy parameters to be more clear and specific
> - Improved logic for determining if a policy needs to be added/updated in the catalog
>   - Policy now checks the catalog directly, rather than just whether a template exists in the org, and uses the newly added "updated_at" field in the active policy JSON to determine if a policy has been updated or not.
> - Streamlined code for better readability and faster execution
>
> __Note:__ Automatically publishing and automatically deleting policies are separate automatic actions. We can have a conversation around whether to actually use the automatic deletion or just have someone look through that incident and manually trigger actions. Either way, the functionality of the old version of the policy is achievable simply by only selecting the "Publish Policy Templates" value for the Automatic Actions parameter.
>
> Additionally, this adds a new policy named `Hidden Policy Templates` whose purpose is to unhide or delete hidden policies in the catalog. This is to resolve the issue of policy publication failing if a policy already exists in the catalog but has its status set to "hidden". The intent is that both policies would be applied in the catalog organizations.
>
> **NOTE:** Dangerfile errors are false positives caused by files being moved around and the README's containing URIs that will be valid once this change is merged.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2221) for these details.
- **Merged At**: 2024-06-04 13:33:46 UTC

---

### PR [#2279](https://github.com/flexera-public/policy_templates/pull/2279): POL-1234 New Policy: AWS Idle NAT Gateways

#### Description

> This new policy template finds and reports on AWS NAT Gateways in the given account which have hourly costs but no network costs; in such cases, it is presumed that the NAT Gateway is idle and not in actual use. Optionally, this report can be emailed and the user can delete the reported NAT Gateways.
>

#### Metadata

- **Policies**: [AWS Idle NAT Gateways](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/idle_nat_gateways/README.md), [Meta Parent: AWS Idle NAT Gateways](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/idle_nat_gateways/README.md)
- **Merged At**: 2024-06-04 13:33:11 UTC

---

### PR [#2288](https://github.com/flexera-public/policy_templates/pull/2288): POL-1249 fix: AWS/Azure Usage Reports - fix chart not rendering in email for Memory Used

#### Description

> <!-- Describe what this change achieves below -->
> When creating a report for Instance Time Used it should render in emails. It works for Normalized Units/Instances and vCPUs, however it does not render correctly for Memory Used.
>
> This is likely being caused by the Chart Title, which in the case of Memory Used, contains parentheses. These parentheses are not being URL encoded.
>
> This is a change to implement a fix.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> - Fixes issue where parentheses are not encoded correctly in the image-charts URL
>

#### Metadata

- **Policies**: [AWS Usage Forecast - Instance Time Used](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/total_instance_usage_forecast/README.md), [AWS Usage Report - Instance Time Used](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/total_instance_usage_report/README.md), [Azure Usage Report - Instance Time Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_usage_report/README.md)
- **Merged At**: 2024-06-03 14:20:03 UTC

---

### PR [#2278](https://github.com/flexera-public/policy_templates/pull/2278): POL-1248 Deprecation Info Field

#### Description

> This adds the following field to the info() block of all deprecated policies: `deprecated: "true"`
>
> Additionally, this adds Dangerfile tests to report errors if this field is missing when the short_description contains the word "deprecated", and when this field is set to true but the short_description does *not* contain the word "deprecated"
>
> Also, a small number of Dangerfile tests will now run even if a policy is deprecated. These tests focus on things that should be checked even for deprecated policies, such as version numbers matching between the policy and the CHANGELOG.
>
> Finally, the active policy automation has been modified to add a "deprecated" field to the active policy list. This field is set to true if the policy is deprecated, and false if it is not.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2278) for these details.
- **Merged At**: 2024-06-03 13:05:27 UTC

---

### PR [#2243](https://github.com/flexera-public/policy_templates/pull/2243): POL-1075 AWS Reserved Instances Utilization Revamp

#### Description

> This is a revamp of the AWS Reserved Instances Utilization policy. From the CHANGELOG:
>
> - Billing Center list can now be used as an allow list or a deny list
> - Added logic to prevent duplicate results due to overlapping child/parent billing centers
> - Added additional fields and context to incident output
> - Normalized incident output for parity with other policy templates
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS Reserved Instances Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/utilization/README.md)
- **Merged At**: 2024-06-03 12:05:10 UTC

---

### PR [#2248](https://github.com/flexera-public/policy_templates/pull/2248): POL-1247 fix: Add default value for `IAM Role Names/IDs/ARNs` param

#### Description

> Add default value for `IAM Role Names/IDs/ARNs` param
>
> This is helpful so we can deploy using the Meta Parent Policy Template and no required user input parameters.
>
> Value is the name of the role created by the recommended Cloud Formation Template
>

#### Metadata

- **Policies**: [AWS IAM Role Audit](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/iam_role_audit/README.md)
- **Merged At**: 2024-05-30 18:26:29 UTC

---

### PR [#2258](https://github.com/flexera-public/policy_templates/pull/2258): POL-1246 AWS/Azure Usage Reports - fix BC Allow/Deny Filter

#### Description

> <!-- Describe what this change achieves below -->
> Current AWS and Azure Usage Report - Instance Time Used policies will fail when a user specifies a list of Billing Centers to Allow or Deny. This is a change to fix this issue.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> - Fixed issue with Billing Center filter so users can now successfully allow/deny Billing Centers from the Usage Report.
>

#### Metadata

- **Policies**: [AWS Usage Report - Instance Time Used](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/total_instance_usage_report/README.md), [Azure Usage Report - Instance Time Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_usage_report/README.md)
- **Merged At**: 2024-05-30 08:13:31 UTC

---

### PR [#2253](https://github.com/flexera-public/policy_templates/pull/2253): FOPTS-4039 Bug fix for unitofMeasure for ultra sized disk

#### Description

> Updated /corrected for Ultra pricing
>
> There is a bug in calculation of the Ultra Price as logic errors out at the unitOfMeasure calculation. This PR fixes the bug
>
> <!-- Describe what this change achieves below -->
>
> ### Issues Resolved
> Issue with unitOfMeasure calculation and errors indicator by the static checks
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-05-29 20:31:07 UTC

---

### PR [#2237](https://github.com/flexera-public/policy_templates/pull/2237): POL-1243 New Policy: Azure Compute Instances Time Powered Off Report

#### Description

> This is a new policy that reports on all Azure VMs that are powered off for a user-specified percentage of time. The policy can report instances powered off for less than a certain percentage of time, more than a certain percentage, or both.
>
> This PR also includes a couple of very small fixes for the equivalent AWS policy that I spotted while building out the Azure equivalent.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2237) for these details.
- **Merged At**: 2024-05-29 12:26:53 UTC

---

### PR [#2246](https://github.com/flexera-public/policy_templates/pull/2246): POL-1244 Update 'resourceType' Incident Fields

#### Description

> This removes the `resourceType` field from policies where this field does not indicate a discrete instance size/capacity/etc. In most cases, it was renamed to the `type` field. This is to prevent issues with how scaped data is presented in the Optimization dashboard.
>
> Additionally, other minor changes were made to bring affected files into compliance with Dangerfile tests.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2246) for these details.
- **Merged At**: 2024-05-28 13:30:34 UTC

---

### PR [#2249](https://github.com/flexera-public/policy_templates/pull/2249): FOPTS-4009 add cumulative report option

#### Description

> This change address the request at [SQ-8125](https://flexera.atlassian.net/browse/SQ-8125)
>
> ### Issues Resolved
>
> - Added Cumulative report option
> - Cumulative chart should show cumulative monthly data
> - Cumulative table should show cumulative based on groups
> - For cumulative report shows a note to indicate that budget, Spend, OverSpend columns shows cumulative data
> - Exclude future data in charts
> - Not include currency sign in the table
> - Chart axis shows accurate currency sign
>
> The history of request changes and also proof of test could be found in the task : [FOPTS-4009](https://flexera.atlassian.net/jira/software/c/projects/FOPTS/boards/398?assignee=712020%3A90605881-06e4-4701-9150-efda16878a29&selectedIssue=FOPTS-4009)
>

#### Metadata

- **Policies**: [Budget vs Actual Spend Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_v_actual_spend_report/README.md)
- **Merged At**: 2024-05-27 17:23:34 UTC

---

### PR [#2247](https://github.com/flexera-public/policy_templates/pull/2247): fix: Meta Parent template `$action_options` check type is array

#### Description

> Fixes issue where $action_options is null instead of a list, which results in an error

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2247) for these details.
- **Merged At**: 2024-05-23 18:30:43 UTC

---

### PR [#2136](https://github.com/flexera-public/policy_templates/pull/2136): POL-1215 Azure Web Apps With Unoptimized Scaling

#### Description

> This is a new policy to find Azure Web Apps that either don't have autoscaling configured or have poor autoscaling settings that are likely to provision excessive resources.
>

#### Metadata

- **Policies**: [Azure Web Apps With Unoptimized Scaling](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unoptimized_web_app_scaling/README.md), [Meta Parent: Azure Web Apps With Unoptimized Scaling](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unoptimized_web_app_scaling/README.md)
- **Merged At**: 2024-05-22 14:08:06 UTC

---

### PR [#2225](https://github.com/flexera-public/policy_templates/pull/2225): POL-1231 New Policy: Azure Usage Report - Instance Time Used

#### Description

> <!-- Describe what this change achieves below -->
> This is a new policy, `Azure Usage Report - Instance Time Used`, that replaces the following policies that are being deprecated as part of this same change:
>
> - `Azure Usage Report - Number of Instance Hours Used`
> - `Azure Usage Report - Number of Instance vCPUs Used`
> - `Azure Usage Report - Amount of Instance Memory Used`
>
> This was done because these policies were almost identical; as a consequence, it really didn't make sense to maintain 3 separate policies for something that could be a simple user parameter. The READMEs of these policies have been updated to direct users to this policy.
>
> The new policy contains all of the functionality of the above, allowing the user to simply select which unit they want to report against. Additionally, the following improvements have been made:
>
> The user can choose which unit of time to normalize the unit against. Default is Hours. Ambiguous units, such as Months, are defined explicitly in the README.
> The user can decide how many months back to generate the report for. Still limited to 12 but can be less than 12 if desired.
> The incident output has been cleaned up. Months no longer have unnecessary hours/minutes/seconds attached to them, and the normalized numbers are rounded to the 100th.
> Code in general has been rewritten and optimized to be more readable, more efficient, and have good comments explaining what is happening within the policy.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2225) for these details.
- **Merged At**: 2024-05-21 12:33:46 UTC

---

### PR [#2238](https://github.com/flexera-public/policy_templates/pull/2238): fix: Meta Parent Consolidated Incidents Only "state=triggered" filter

#### Description

> Fixes an issue that is causing results from non-current incidents to appear in the Consolidated Incident.. which then reflects an inaccurate resource count.
>
> This fixes an issue with the datasource that gets the incidents for the meta parent policy

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2238) for these details.
- **Merged At**: 2024-05-20 17:12:07 UTC

---

