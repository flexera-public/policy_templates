# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

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

- **Policies**: [Azure Web Apps With Unoptimized Scaling](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unoptimized_web_app_scaling/README.md)
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

### PR [#2177](https://github.com/flexera-public/policy_templates/pull/2177): POL-1101 Azure SQL Servers Without Elastic Pools Revamp

#### Description

> This is a revamp of the `Azure SQL Servers Without Elastic Pools` policy. From the CHANGELOG:
>
> - Policy renamed to more accurately indicate that it reports SQL Servers and not SQL Databases
> - Several parameters altered to be more descriptive and human-readable
> - Improved and more robust filtering for subscriptions and tags
> - Added ability to filter resources by region
> - Normalized incident export to be consistent with other policies
> - Policy no longer raises new escalations if tag data has changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>
> Additionally, the policy has been moved from `/operational` to `/cost` in the repository. The policy category was already `Cost` and this makes sense, since the purpose of this policy is to find opportunities to save money via elastic pools.
>
> NOTE: Changelog error can be ignored. It's weirdness caused by the CHANGELOG technically having been moved.
>

#### Metadata

- **Policies**: [Azure SQL Servers Without Elastic Pools](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/sql_servers_without_elastic_pool/README.md)
- **Merged At**: 2024-05-20 12:18:05 UTC

---

### PR [#2193](https://github.com/flexera-public/policy_templates/pull/2193): POL-1093 AWS Scheduled EC2 Events Revamp

#### Description

> This is a revamp of the AWS Scheduled EC2 Events policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to only report specific event types
> - Added ability to filter events by how soon they are scheduled to occur
> - Added more robust tag filtering
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export
> - Policy no longer raises new escalations if incidental metadata about a resource or event has changed
> - Streamlined code for better readability and faster execution
>
> Note: Ignore the CHANGELOG error. It's doing that because the CHANGELOG file changed locations, not because the CHANGELOG has not been updated.
>

#### Metadata

- **Policies**: [AWS Scheduled EC2 Events](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/scheduled_ec2_events/README.md)
- **Merged At**: 2024-05-20 12:17:50 UTC

---

### PR [#2228](https://github.com/flexera-public/policy_templates/pull/2228): POL-1232 New Policy: AWS EC2 Instances Time Stopped Report

#### Description

> This is a new policy that reports on all EC2 instances that are stopped for a user-specified percentage of time. The policy can report instances stopped for less than a certain percentage of time, more than a certain percentage, or both.
>

#### Metadata

- **Policies**: [AWS EC2 Instances Time Stopped Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/ec2_stopped_report/README.md)
- **Merged At**: 2024-05-20 12:17:35 UTC

---

### PR [#2226](https://github.com/flexera-public/policy_templates/pull/2226): POL-1241 - Meta Parent PTs - Add Support Actions with Parameters

#### Description

> Adds support for parameters on actions that have them
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1241
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2226) for these details.
- **Merged At**: 2024-05-17 21:27:53 UTC

---

### PR [#2219](https://github.com/flexera-public/policy_templates/pull/2219): POL-1079 AWS Savings Plan Utilization Revamp

#### Description

> This is a revamp of the AWS Savings Plan Utilization policy. From the CHANGELOG:
>
> - Policy can now be run against an arbitrary number of days in the past
> - Policy can now filter for several Savings Plans at once
> - Improved incident output for better readability
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS Savings Plan Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/utilization/README.md)
- **Merged At**: 2024-05-16 12:42:59 UTC

---

### PR [#2215](https://github.com/flexera-public/policy_templates/pull/2215): POL-1073 AWS Reserved Instances Coverage

#### Description

> This is a revamp of the AWS Reserved Instances Coverage policy. From the CHANGELOG:
>
> - Policy can now be run against an arbitrary number of days in the past
> - Policy incident now presented in a more human-readable fashion
> - Streamlined code for better readability and faster execution
> - Policy now requires valid Flexera credential
>

#### Metadata

- **Policies**: [AWS Reserved Instances Coverage](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/coverage/README.md)
- **Merged At**: 2024-05-16 12:42:45 UTC

---

### PR [#2216](https://github.com/flexera-public/policy_templates/pull/2216): POL-1074 Deprecate Policy: AWS Reserved Instance Report by Billing Center

#### Description

> This is a very old policy that would only work if someone isn't using RBDs for cost allocation and is likely superseded by basic functionality in our platform. For this reason, the policy is being deprecated.

#### Metadata

- **Policies**: [Reserved Instance Report by Billing Center](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/report_by_bc/README.md)
- **Merged At**: 2024-05-14 20:02:26 UTC

---

### PR [#2207](https://github.com/flexera-public/policy_templates/pull/2207): POL-1096 New Policy: AWS Usage Forecast - Instance Time Used

#### Description

> This is a new policy, `AWS Usage Forecast - Instance Time Used`, that replaces the following policies that are being deprecated as part of this same change:
>
> - `AWS Usage Forecast - Number of Instance Hours Used`
> - `AWS Usage Forecast - Number of Instance vCPUs Used`
>
> This was done because these policies were almost identical; as a consequence, it really didn't make sense to maintain 2 separate policies for something that could be a simple user parameter. The READMEs of these policies have been updated to direct users to this policy.
>
> The new policy contains all of the functionality of the above, allowing the user to simply select which unit they want to forecast against. Additionally, the following improvements have been made:
>
> - The user can choose which unit of time to normalize the unit against. Default is `Hours`. Ambiguous units, such as `Months`,  are defined explicitly in the README.
> - The incident output has been cleaned up. Months no longer have unnecessary hours/minutes/seconds attached to them, and the normalized numbers are rounded to the 100th.
> - Code in general has been rewritten and optimized to be more readable, more efficient, and have good comments explaining what is happening within the policy.
>
> Note: Ignore the warnings about the dead URL. That's just because this policy does not exist in the master branch yet. That URL will be valid once this is merged.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2207) for these details.
- **Merged At**: 2024-05-14 14:37:09 UTC

---

### PR [#2202](https://github.com/flexera-public/policy_templates/pull/2202): POL-1097 New Policy: AWS Usage Report - Instance Time Used

#### Description

> This is a new policy, `AWS Usage Report - Instance Time Used`, that replaces the following policies that are being deprecated as part of this same change:
>
> - `AWS Usage Report - Number of Instance Hours Used`
> - `AWS Usage Report - Number of Instance vCPUs Used`
> - `AWS Usage Report - Amount of Instance Memory Used`
>
> This was done because these policies were almost identical; as a consequence, it really didn't make sense to maintain 3 separate policies for something that could be a simple user parameter. The READMEs of these policies have been updated to direct users to this policy.
>
> The new policy contains all of the functionality of the above, allowing the user to simply select which unit they want to report against. Additionally, the following improvements have been made:
>
> - The user can choose which unit of time to normalize the unit against. Default is `Hours`. Ambiguous units, such as `Months`,  are defined explicitly in the README.
> - The user can decide how many months back to generate the report for. Still limited to 12 but can be less than 12 if desired.
> - The incident output has been cleaned up. Months no longer have unnecessary hours/minutes/seconds attached to them, and the normalized numbers are rounded to the 100th.
> - Code in general has been rewritten and optimized to be more readable, more efficient, and have good comments explaining what is happening within the policy.
>
> Note: Ignore the warnings about the dead URL. That's just because this policy does not exist in the master branch yet. That URL will be valid once this is merged.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2202) for these details.
- **Merged At**: 2024-05-14 14:12:53 UTC

---

### PR [#2208](https://github.com/flexera-public/policy_templates/pull/2208): POL-1229 Dangerfile Update: Enforce Directory Structure

#### Description

> This PR adds a Dangerfile test to ensure policies are placed in the correct location within the repository's directory structure. This also moves the `Scheduled Report for Unallocated Costs` policy to conform with this test.

#### Metadata

- **Policies**: [Scheduled Report for Unallocated Costs](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_report_unallocated/README.md)
- **Merged At**: 2024-05-14 13:06:01 UTC

---

### PR [#2187](https://github.com/flexera-public/policy_templates/pull/2187): FOPTS-3939 Update: List of cheaper regions for Azure and AWS vendors

#### Description

> Issue reported in this support question: https://flexera.atlassian.net/browse/SQ-7976 by Albertsons.
> Policy is returning empty results, checking the code it's because some regions for Azure and AWS are outdated, previously we had for example: `US West`, `US West 2`, etc. But now those are named `West US`, `West US 2`, etc. Also few `console.log` statements were removed.
>
> ### Issues Resolved
>
> Policy is returning empty results because of outdated regions for Azure and AWS vendors.
>

#### Metadata

- **Policies**: [Cheaper Regions](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cheaper_regions/README.md)
- **Merged At**: 2024-05-10 17:12:38 UTC

---

### PR [#2194](https://github.com/flexera-public/policy_templates/pull/2194): POL-1224 Azure RightsizeSQL bug fix

#### Description

> Bug was present causing all recommendations to return 0$
>
> ### Issues Resolved
>
> Line 743 changed subscriptionId to subscriptionID
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2024-05-10 15:54:23 UTC

---

### PR [#2195](https://github.com/flexera-public/policy_templates/pull/2195): POL-1228 feat: Unallocated Cost Report enhancements

#### Description

> - Fixed bug that related to Summarized Unallocated amount and Unallocated Percent of Total in report
> - Added filter for excluding rows that are below a certain percent of total costs
> - Added Time Period and Filters to report output
> - Added `unallocated` (bool) and `unallocated_details` (string) columns to report output
> - Report column order will match the order user provided in parameter input
>
>

#### Metadata

- **Policies**: [Scheduled Report for Unallocated Costs](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_report_unallocated/README.md)
- **Merged At**: 2024-05-10 12:36:55 UTC

---

### PR [#2189](https://github.com/flexera-public/policy_templates/pull/2189): POL-1108 Google Expiring Committed Use Discounts (CUD) Revamp

#### Description

> This is a revamp of the Google Expiring Committed Use Discounts (CUD). From the CHANGELOG:
>
> - Added ability to filter recommendations by project
> - Added ability to filter recommendations by region
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>

#### Metadata

- **Policies**: [Google Expiring Committed Use Discounts (CUD)](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cud_expiration/README.md)
- **Merged At**: 2024-05-10 12:28:06 UTC

---

### PR [#2188](https://github.com/flexera-public/policy_templates/pull/2188): POL-1109 Google Committed Use Discount Report Revamp

#### Description

> This is a revamp of the Google Committed Use Discount Report. From the CHANGELOG:
>
> - Added ability to filter report by project
> - Added ability to filter recommendations by region
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>

#### Metadata

- **Policies**: [Google Committed Use Discount Report](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cud_report/README.md)
- **Merged At**: 2024-05-10 12:27:47 UTC

---

### PR [#2184](https://github.com/flexera-public/policy_templates/pull/2184): POL-1226 AWS Untagged Resources Improvements

#### Description

> From the CHANGELOG:
>
> - Added parameter `Include Savings` to optionally allow the user to not report savings
> - Improved logic for finding savings for reported resources
> - Added currency field to incident report
> - Minor code cleanup and optimization
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md)
- **Merged At**: 2024-05-10 12:27:27 UTC

---

### PR [#2175](https://github.com/flexera-public/policy_templates/pull/2175): POL-1112 Google Object Storage Optimization Revamp

#### Description

> This is a revamp of the `Google Object Storage Optimization` policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by project
> - Added ability to use wildcards and regex when filtering resources by label
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera One credential
>

#### Metadata

- **Policies**: [Google Object Storage Optimization](https://github.com/flexera-public/policy_templates/tree/master/cost/google/object_storage_optimization/README.md)
- **Merged At**: 2024-05-09 14:10:32 UTC

---

### PR [#2176](https://github.com/flexera-public/policy_templates/pull/2176): POL-1111 Deprecate Google Inefficient Instance Utilization using StackDriver Policy

#### Description

> This deprecates the already-unpublished `Google Inefficient Instance Utilization using StackDriver` policy. The README directs users to the more modern `Google Rightsize VM Recommender` policy instead.

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2176) for details about unpublished policies.
- **Merged At**: 2024-05-08 16:32:50 UTC

---

### PR [#2183](https://github.com/flexera-public/policy_templates/pull/2183): POL-1092 Update/Deprecate Azure Subscription Access

#### Description

> This is a final update and deprecation of the Azure Subscription Access policy. This policy is not used by our customers and does not provide functionality that dovetails with our product suite.

#### Metadata

- **Policies**: [Azure Subscription Access](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/subscription_access/README.md)
- **Merged At**: 2024-05-08 16:32:27 UTC

---

### PR [#2164](https://github.com/flexera-public/policy_templates/pull/2164): SQ-7228 Incorrect currency code and inflated savings bug

#### Description

> - Adds a new parameter that lets the user decide on the format for the currency shown in the incident's chart: code (e.g. USD) or symbol (e.g. $).
> - Fixes a bug that showed inflated savings on the instances.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-7228
>

#### Metadata

- **Policies**: [Azure Savings Realized from Reservations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_realized/README.md)
- **Merged At**: 2024-05-08 12:18:14 UTC

---

### PR [#2169](https://github.com/flexera-public/policy_templates/pull/2169): POL-1223 New Policy: AWS EKS Clusters Without Spot Instances

#### Description

> *New Policy: AWS EKS Clusters Without Spot Instances*
>
> This Policy finds AWS Elastic Kubernetes Service (EKS) clusters without any node groups that use spot instances and reports them. Optionally, it emails the report to a user-specified set of email addresses.
>
> Note: This policy is only capable of assessing managed node groups within a cluster. Unmanaged node groups will not be considered when determining whether or not the cluster is configured to make use of spot instances.
>

#### Metadata

- **Policies**: [AWS EKS Clusters Without Spot Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/eks_without_spot/README.md)
- **Merged At**: 2024-05-08 12:12:52 UTC

---

### PR [#2173](https://github.com/flexera-public/policy_templates/pull/2173): POL-1225 Azure Rightsize SQL Databases: New Incident Fields

#### Description

> New fields added to incident output: `Last Accessed` and `Status`
>
> Note that this required modifying the policy to list SQL servers and then list SQL databases for each server instead of pulling the latter directly from a more general resource API. This means the policy may take longer to execute than it used to.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2024-05-07 12:15:23 UTC

---

### PR [#2163](https://github.com/flexera-public/policy_templates/pull/2163): POL-1224 Fix Google Recommender/Policy List Generation

#### Description

> Due to how the incident was constructed Google Recommenders policy, the generated meta policy had syntax errors, which in turn were causing the active policy list generation to fail. Multiple changes were made to resolve this:
>
> - The order of fields in the Google Recommenders policy was modified slightly. This enables the meta policy to be correctly generated without syntax errors.
>
> - Dangerfile test was added to test meta policies for syntax errors. If such an error is found, a meta policy-specific error is raised indicating that either the policy or the meta policy automation needs to be fixed. This should hopefully catch such problems before they are merged into the catalog and subsequently break other automation.
>
> Changes to Dangerfile have been tested.

#### Metadata

- **Policies**: [Google Recommenders](https://github.com/flexera-public/policy_templates/tree/master/cost/google/recommender/README.md)
- **Merged At**: 2024-05-06 17:48:38 UTC

---

### PR [#2161](https://github.com/flexera-public/policy_templates/pull/2161): POL-1204 Fix Outdated image-charts.com Links

#### Description

> This updates several policies to use our internal image charts link `api.image-charts-auth.flexeraeng.com` instead of `image-charts.com`. The former uses our paid licensed version which does not include a watermark. Minor changes were also made to the policies to comply with Dangerfile tests.
>
> It also updates Dangerfile to test for this and raise an error if anyone attempts to use this old link in the future, and fixes a bug with the README tests that would sometimes cause false positives for out of order sections.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2161) for these details.
- **Merged At**: 2024-05-03 15:07:40 UTC

---

### PR [#2147](https://github.com/flexera-public/policy_templates/pull/2147): POL-1094 AWS Lambda Functions With High Error Rate Revamp

#### Description

> This is a revamp of the AWS Lambda Functions With High Error Rate policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by multiple tag key:value pairs and using regex
> - Added ability to specify how many hours back to gather error data for
> - Policy now uses more efficient and modern method for gathering error data
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export for added context
> - Policy no longer raises new escalations if inconsequential metadata has changed
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS Lambda Functions With High Error Rate](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/lambda_functions_with_high_error_rate/README.md)
- **Merged At**: 2024-05-02 15:53:13 UTC

---

### PR [#2127](https://github.com/flexera-public/policy_templates/pull/2127): POL-1113 Google Recommenders Revamp

#### Description

> This is a revamp of the Google Recommenders policy. From the CHANGELOG:
>
> - Added support for new recommender: Idle Cloud SQL Instance
> - Added support for new recommender: Overprovisioned Cloud SQL Instance
> - Added support for new recommender: Idle GKE Cluster
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter results by project and by region via an allow list or a deny list
> - Added additional context to incident description
> - Added ability to report on several recommenders at once
> - Policy now reports savings and converts it to local currency when appropriate
> - Several parameters altered to be more descriptive and human-readable
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export for additional context
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Policy now requires a Flexera credential
> - Added logic required for "Meta Policy" use-cases
>
> Additionally, the README has been overhauled and now recommends using other policies for recommenders where supported.
>

#### Metadata

- **Policies**: [Google Recommenders](https://github.com/flexera-public/policy_templates/tree/master/cost/google/recommender/README.md)
- **Merged At**: 2024-05-02 13:14:04 UTC

---

### PR [#2153](https://github.com/flexera-public/policy_templates/pull/2153): POL-1221 Usage Report Policies - Update BC Filter to support Child Billing Centers

#### Description

> <!-- Describe what this change achieves below -->
> Usage Reports for AWS and Azure (e.g., Amount of Instance Memory Used, Number of Instance vCPUs Used, etc.) currently allow the user to define a list of Billing Centers to report on which can either be allowed/filtered in or denied/filtered out.
>
> The current logic only supports filtering on top-level billing centers, which means that child billing centers cannot be specifically reported on.
>
> This is a change to add support for filtering on child billing centers when applying the policy to generate a report.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Fixes issue where only top-level billing centers could be filtered on. Policy now additionally supports filtering on child billing centers.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2153) for these details.
- **Merged At**: 2024-05-02 12:29:40 UTC

---

### PR [#2152](https://github.com/flexera-public/policy_templates/pull/2152): POL-1220 Fix AWS Untagged Resources in EU/AU

#### Description

> This policy had an API request with a hardcoded string pointing specifically to the Optima API host. This host varies based on region, so the policy was failing in EU/AU.
>
> This hardcoded string has been replaced with the `rs_optima_host` keyword that automatically substitutes in the appropriate region-specific host.
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md)
- **Merged At**: 2024-05-02 12:04:34 UTC

---

### PR [#2146](https://github.com/flexera-public/policy_templates/pull/2146): POL-1099 Azure Expiring Certificates Revamp

#### Description

> This is a revamp of the Azure Expiring Certificates policy. From the CHANGELOG:
>
> - Added ability to delete Azure certificates automatically or manually
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to use Subscription filter as an allow or a deny list
> - Added ability to filter resources by multiple tag key:value pairs
> - Added ability to filter resources by region
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if inconsequential metadata like tag values change
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Azure Expiring Certificates](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/azure_certificates/README.md)
- **Merged At**: 2024-05-02 12:04:20 UTC

---

### PR [#2117](https://github.com/flexera-public/policy_templates/pull/2117): POL-1105 Azure VMs Not Using Managed Disks Revamp

#### Description

> This is a revamp of the Azure VMs Not Using Managed Disks policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Improved ability to filter resources by subscription
> - Added ability to filter resources by region
> - Added ability to filter resources by multiple tag key:value pairs
> - Added several fields to incident export to provide additional context
> - Normalized incident export to be consistent with other policies
> - Policy no longer raises new escalations for the same resource if incidental metadata has changed
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Azure VMs Not Using Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/vms_without_managed_disks/README.md)
- **Merged At**: 2024-05-02 12:04:06 UTC

---

### PR [#2112](https://github.com/flexera-public/policy_templates/pull/2112): POL-1090 Azure Regulatory Compliance Revamp

#### Description

> This is a revamp of the AWS IAM Role Audit policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>
> Additionally, the policy now has meta policy support.
>

#### Metadata

- **Policies**: [Azure Regulatory Compliance](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/compliance_score/README.md)
- **Merged At**: 2024-05-02 12:03:30 UTC

---

### PR [#2111](https://github.com/flexera-public/policy_templates/pull/2111): POL-1089 Azure Policy Audit Revamp

#### Description

> This is a revamp of the AWS IAM Role Audit policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>
> Additionally, the policy now has meta policy support.
>

#### Metadata

- **Policies**: [Azure Policy Audit](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_policy_audit/README.md)
- **Merged At**: 2024-05-02 12:03:17 UTC

---

### PR [#2099](https://github.com/flexera-public/policy_templates/pull/2099): POL-1209 Add "newResourceType" field to idle/unused incidents for multi-incident Recommendation policies

#### Description

> Updates to several Recommendations policies with multiple incidents to add a "newResourceType" field to the incident reporting idle/unused resources. This is because, when data is exported from the Optimization dashboard, there is no field indicating which incident (underutilized or idle/unused) a recommendation came from. To make distinguishing recommendations easier, we can simply add a "newResourceType" field with a value like "Delete Instance".
>
> The policies were also updated to pass current linting and adhere to current standards. Additionally, the following updates were made to Dangerfile to address false positives raised by this PR:
> - `policy_run_script_incorrect_order?` test now correctly parses `iter_item` as though it were the same as `val(iter_item, "field")`
> - `policy_ds_js_name_mismatch?` test no longer raises warnings for datasources and scripts with mismatched names when the script is called by multiple datasources.
> - File name in Dangerfile output reduced in size to avoid UI issues with scrolling left/right
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2099) for these details.
- **Merged At**: 2024-05-02 12:02:41 UTC

---

### PR [#2108](https://github.com/flexera-public/policy_templates/pull/2108): POL-1087 AWS IAM Role Audit Revamp

#### Description

> This is a revamp of the AWS IAM Role Audit policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - `IAM Role Name` parameter renamed to `IAM Role Names/IDs/ARNs` and now accepts role IDs and ARNs
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>
> Additionally, the policy now has meta policy support.
>

#### Metadata

- **Policies**: [AWS IAM Role Audit](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/iam_role_audit/README.md)
- **Merged At**: 2024-05-02 12:02:22 UTC

---

### PR [#2118](https://github.com/flexera-public/policy_templates/pull/2118): POL-1106 Google Unlabeled Resources Revamp

#### Description

> This is a revamp of the Google Unlabeled Resources policy. From the CHANGELOG:
>
> - Added ability to filter resources by Google Project
> - Added ability to filter resources by Google resource type
> - Added additional context to incident description
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera One credential
>
> Additionally, some minor tweaks to Dangerfile testing to avoid false positives
>

#### Metadata

- **Policies**: [Google Unlabeled Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/google/unlabeled_resources/README.md)
- **Merged At**: 2024-05-01 15:43:31 UTC

---

### PR [#2123](https://github.com/flexera-public/policy_templates/pull/2123): POL-1213 Google Old Snapshots: Add Savings

#### Description

> This adds savings information to the Google Old Snapshots policy using list prices from the Google Cloud Billing API. From the CHANGELOG:
>
> - Added estimated savings based on Google's Cloud Billing API
> - Added `Minimum Savings Threshold` parameter to filter results
> - Added support for automatic currency conversion for savings
> - To facilitate the above, policy template now requires additional permissions
>

#### Metadata

- **Policies**: [Google Old Snapshots](https://github.com/flexera-public/policy_templates/tree/master/cost/google/old_snapshots/README.md)
- **Merged At**: 2024-04-30 16:26:22 UTC

---

### PR [#2138](https://github.com/flexera-public/policy_templates/pull/2138): POL-1219 Update policies referencing Microsoft ISF Ratio CSV

#### Description

> <!-- Describe what this change achieves below -->
> Microsoft provides a CSV file which has a mapping of instance types, their respective Instance Families, and their respective normalization factor unit.
>
> The CSV is available via a URL, however the current URL (https://isfratio.blob.core.windows.net/isfratio/ISFRatio.csv) no longer works and has been replaced with a new URL (https://aka.ms/isf)
>
> This is causing several policies to fail.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> This is a change to update the URL for all policies referencing this CSV file, thereby fixing the policies.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/utilization/README.md), [Azure Usage Report - Number of Instance Hours Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_hours/README.md), [Azure Usage Report - Amount of Instance Memory Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_memory/README.md), [Azure Usage Report - Number of Instance vCPUs Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_vcpus/README.md)
- **Merged At**: 2024-04-30 15:38:57 UTC

---

### PR [#2137](https://github.com/flexera-public/policy_templates/pull/2137): POL-1217 Email Cost Optimization Recommendations: Always Send Incident

#### Description

> Added the following parameter to the `Email Cost Optimization Recommendations` policy:
>
> - *Always Email Incident* - Whether or not to always email the incident even if no new items were added to the recommendations since the policy's last execution.
>
> This works by adding a new incident field that is set to an empty string if this parameter is set to "No" and is set to the current date and time if the parameter is set to "Yes". Since the current date and time of policy execution will always be a unique value, this should have the desired effect.
>
> Also added support for some newer recommendations policies that didn't exist when this policy was last updated.
>

#### Metadata

- **Policies**: [Email Cost Optimization Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/email_recommendations/README.md)
- **Merged At**: 2024-04-30 14:09:25 UTC

---

### PR [#2132](https://github.com/flexera-public/policy_templates/pull/2132): POL-1216 New Policy: Azure Unused Firewalls

#### Description

> This is a new recommendation policy that reports on any unused Azure Firewalls. An Azure Firewall is considered unused if it has received no incoming connections for a user-specified number of days. More details are in the README.
>

#### Metadata

- **Policies**: [Azure Unused Firewalls](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_firewalls/README.md)
- **Merged At**: 2024-04-30 14:09:12 UTC

---

### PR [#2128](https://github.com/flexera-public/policy_templates/pull/2128): POL-1214 - fix: error for tag_dimension_tag_keys not defined

#### Description

> Fixes error `ReferenceError: 'tag_dimension_tag_keys' is not defined`
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1214
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md)
- **Merged At**: 2024-04-26 12:06:36 UTC

---

### PR [#2124](https://github.com/flexera-public/policy_templates/pull/2124): POL-1114 Google Policy Deprecations

#### Description

> This deprecates 4 policies that have more modern equivalents. The READMEs have been updated to direct users to the proper policy.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2124) for these details.
- **Merged At**: 2024-04-24 19:23:05 UTC

---

### PR [#1668](https://github.com/flexera-public/policy_templates/pull/1668): feat: add `Scheduled Report for Unallocated Costs`

#### Description

> Commits PT for `Scheduled Report for Unallocated Costs` -- this is not going to be published to catalog initially
>

#### Metadata

- **Policies**: [Scheduled Report for Unallocated Costs](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_report_unallocated/README.md)
- **Merged At**: 2024-04-24 13:55:38 UTC

---

### PR [#2113](https://github.com/flexera-public/policy_templates/pull/2113): POL-1100 Policy Deprecations

#### Description

> This deprecates several policies that have not been updated in years and likely no longer work. In some cases, the policy is also obsolete due to platform improvements.
>
> This also updates Dangerfile testing to automatically skip deprecated policies.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2113) for these details.
- **Merged At**: 2024-04-22 20:35:58 UTC

---

### PR [#2098](https://github.com/flexera-public/policy_templates/pull/2098): POL-1207 Azure Rightsize Compute Fixes/Enhancements

#### Description

> Several changes to the Azure Rightsize Compute policy based on customer feedback:
>
> - New `Exclude Stopped Virtual Machines` parameter to filter stopped virtual machines from results
> - New `Exclude Databricks` parameter to filter Azure Databricks virtual machines from results
> - `Power State` field added to results to indicate whether a virtual machine is running or stopped
> - Fields related to the image the virtual machine was created with added to results
> - Idle Virtual Machines incident now includes a `Recommended Instance Size` field with a value of `Delete Virtual Machine` for ease of analyzing recommendations from the Flexera Optimization dashboard
> - Added warning about invalid Databricks recommendations to incident description if `Exclude Databricks` parameter is set to `No`
> - Fixed issue that would cause downsize actions to fail
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2024-04-22 14:50:00 UTC

---

### PR [#2097](https://github.com/flexera-public/policy_templates/pull/2097): POL-1208 AWS Unused IP Address Cost Fix

#### Description

> It was discovered that the AWS Unused IP Address policy now sometimes fails on execution. Further digging revealed that the AWS Price List API no longer provides pricing for unattached IP addresses, which breaks the datasource and script that retrieve this pricing. This is likely because AWS now charges for all IP addresses, not just unattached ones. I also discovered the following:
>
> - Pricing for attached IPs is consistent regardless of region in the results; all IPv4 addresses cost $0.005 USD/hour. This aligns with AWS's own documentation, which cites a single universal price for IPv4 addresses rather than one that is contextualized by region or other variables.
> - The Price List API does not bother to return pricing results for a majority of AWS regions even for attached IP addresses.
>
> The short version is that the AWS Price List API doesn't really bother to provide granular IP address pricing information anymore. Because of this, and because AWS's own docs specifically outline a single consistent price, the price is now hardcoded into the policy rather than retrieved from an API.
>
> This does mean that, if the price model changes, the policy itself will need to be updated, but that would be true regardless, since that would likely also mean that the Price List API's output would change as well. This seems to be the least bad solution until and unless AWS provides a means via API to get region-specific pricing for unattached IP addresses.
>

#### Metadata

- **Policies**: [AWS Unused IP Addresses](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_ip_addresses/README.md)
- **Merged At**: 2024-04-22 14:01:04 UTC

---

### PR [#2073](https://github.com/flexera-public/policy_templates/pull/2073): POL-1086 AWS Unused ECS Clusters Revamp

#### Description

> This is a revamp of the AWS Unused ECS Clusters policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by multiple tag key:value pairs and with regex
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>

#### Metadata

- **Policies**: [AWS Unused ECS Clusters](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/ecs_unused/README.md)
- **Merged At**: 2024-04-22 13:02:52 UTC

---

### PR [#2100](https://github.com/flexera-public/policy_templates/pull/2100): POL-1210 AWS Missing Regions Meta Policy Fix

#### Description

> Meta policy wasn't working because the account number parameter was missing. This fixes that.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2100) for details about unpublished policies.
- **Merged At**: 2024-04-19 20:56:22 UTC

---

### PR [#2080](https://github.com/flexera-public/policy_templates/pull/2080): fix: add default values for parameters that do not require user input

#### Description

> - Adds default values for parameters that are do not require user input.  This will be helpful for deploy applied policies at scale by minimizing/preventing the user to provide parameter values.  Some PTs will still require user input (i.e. ITAM Scheduled Report) and those have had the appropriate comment added to declare that.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2080) for these details.
- **Merged At**: 2024-04-18 19:08:59 UTC

---

### PR [#2082](https://github.com/flexera-public/policy_templates/pull/2082): FOPTS-3836 Fix: cloud_cost_anomaly_alerts.pt incident link

#### Description

> Currently when we click on the incident link of `cloud_cost_anomaly_alerts.pt` in mail, we get this error in the dashboard:
>
> `Load Anomalies failed at this time`
>
> The issue is happening because the link is including `)**` at the end of the url, once it's removed it returns the proper result to page.
>
> ### Issues Resolved
>
> Incident URL in mail.
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2024-04-18 14:48:21 UTC

---

### PR [#2060](https://github.com/flexera-public/policy_templates/pull/2060): POL-1196 Update AWS Usage Report policies to include BC Filter and Region Filter

#### Description

> <!-- Describe what this change achieves below -->
> This is a change to add parameters which allow the user to filter (Allow or Deny) for a list of Billing Centers and a list of Regions to report on. This parameter will be added to the following Usage Report policies:
>
> - AWS Usage Report - Number of Instance Hours Used
> - AWS Usage Report - Number of Instance vCPUs Used
> - AWS Usage Report - Amount of Instance Memory Used
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> - Adds functionality to make the policy more valuable to customers who may want to produce a Usage Report for specific Billing Centers and/or Regions.
> - Brings these policies in line with their Azure counterparts.
> - Resolves inaccuracies in the policy template Readme files regarding the listed input parameters.
>

#### Metadata

- **Policies**: [AWS Usage Report - Number of Instance Hours Used](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/total_instance_hours/README.md), [AWS Usage Report - Amount of Instance Memory Used](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/total_instance_memory/README.md), [AWS Usage Report - Number of Instance vCPUs Used](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/total_instance_vcpus/README.md)
- **Merged At**: 2024-04-18 14:25:49 UTC

---

### PR [#2055](https://github.com/flexera-public/policy_templates/pull/2055): POL-1194 Update Azure Usage Report policies to include BC Filter

#### Description

> <!-- Describe what this change achieves below -->
> This is a change to add a parameter which allows the user to filter (Allow or Deny) for a list of Billing Centers to report on. This parameter will be added to the following Usage Report policies:
>
> - Azure Usage Report - Number of Instance Hours Used
> - Azure Usage Report - Number of Instance vCPUs Used
> - Azure Usage Report - Amount of Instance Memory Used
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> - Adds functionality to make the policy more valuable to customers who may want to produce a Usage Report for specific Billing Centers.
> - Resolves inaccuracies in the policy template Readme files regarding the listed input parameters.
>

#### Metadata

- **Policies**: [Azure Usage Report - Number of Instance Hours Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_hours/README.md), [Azure Usage Report - Amount of Instance Memory Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_memory/README.md), [Azure Usage Report - Number of Instance vCPUs Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_vcpus/README.md)
- **Merged At**: 2024-04-18 14:07:37 UTC

---

### PR [#2079](https://github.com/flexera-public/policy_templates/pull/2079): POL-1202 Currency Conversion Fix

#### Description

> - New Functionality: Policy can now automatically set the organization's currency to match the `Currency To` parameter. This setting defaults to being disabled to maintain parity with previous versions.
> - Fixes issue where policy would fail if the org had adjustment rules set for future months. Payload is now intentionally sorted by month first to ensure that this doesn't cause issues.
> - Removed the Email Addresses parameter because it's not actually used by the policy. Updated the major version number since this is technically a breaking change.
> - Made the JSON stringified version of the payload for the adjustments API a separate datasource to assist in debugging when errors occur, but this has no impact on functionality from a user standpoint.
> - Various tweaks were made to pass linting tests.
>

#### Metadata

- **Policies**: [Currency Conversion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/currency_conversion/README.md)
- **Merged At**: 2024-04-18 13:51:11 UTC

---

### PR [#2062](https://github.com/flexera-public/policy_templates/pull/2062): POL-1198 Fix Scheduled Report Filtering

#### Description

> Fixed issue in `Scheduled Report` policy where filter would not work correctly if `Month` was selected for the `Billing Term` parameter.
>
> Also made some minor edits to pass the new linting tests.
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2024-04-18 13:39:48 UTC

---

### PR [#2075](https://github.com/flexera-public/policy_templates/pull/2075): POL-1201 Convert "AWS Resources Under Extended Support" into Savings Policy

#### Description

> Changes to `AWS Resources Under Extended Support` policy:
>
> - Modified policy to correctly report cost as potential savings
> - Added `Minimum Savings Threshold` parameter to filter out recommendations with low savings potential
> - Added total `Potential Monthly Savings` to incident description
> - Extended policy to include resources outside of RDS and EKS where applicable
>
> Warning is due to missing fields that can't really be added or contain no useful information when pulling data directly from CCO. It can be ignored.
>

#### Metadata

- **Policies**: [AWS Resources Under Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/extended_support/README.md)
- **Merged At**: 2024-04-17 12:07:41 UTC

---

### PR [#2061](https://github.com/flexera-public/policy_templates/pull/2061): POL-1195 New Policy: AWS Resources Under Extended Support

#### Description

> This is a new policy to report on AWS RDS and EKS resources that are under "extended support". AWS is likely to start increasing the prices on these resources to encourage users to migrate/upgrade.
>
> The policy pulls resource-level billing data from the Flexera CCO platform from 3 days ago. This data is filtered to just those resources with a Service of AmazonRDS or AmazonEKS and a Usage Type that contains the string ExtendedSupport. Data from 3 days ago is used to ensure that we have available, processed billing data to search through.
>

#### Metadata

- **Policies**: [AWS Resources Under Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/extended_support/README.md)
- **Merged At**: 2024-04-16 13:54:32 UTC

---

### PR [#2018](https://github.com/flexera-public/policy_templates/pull/2018): FOPTS-3624 Add support for MCA accounts

#### Description

> - The current policy does not support MCA accounts, with this change supporting MCA CBI accounts is implemented.
> - The currency code that this policy shows is always USD, despite the org using EUR or other currency, this PR fixes that.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/SQ-7053
> - https://flexera.atlassian.net/browse/SQ-7228
>

#### Metadata

- **Policies**: [Azure Savings Realized from Reservations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_realized/README.md)
- **Merged At**: 2024-04-15 23:18:08 UTC

---

### PR [#2037](https://github.com/flexera-public/policy_templates/pull/2037): feat: add savings, param consider tag dimensions to AWS Untagged Resources PT

#### Description

> - Added parameter for *Consider Tag Dimensions* to help mitigate/prevent seeing results for resources which have the tag key/tag value through a normalized Tag Dimension
> - Added Estimated Savings mappings for each resource
>
>   For example,
>    - A resource tagged `app=prod-cluster`
>    - A Tag Dimension named "Application" (tag_application) which normalizes tag resource tag keys `app`, `Application`, `App`, `application`, etc...
>
>   If *Consider Tag Dimensions* is enabled and `Tags=["Application"]` the example resource would be considered to **not** be missing the `Application` tag, because it has the `app` tag which is normalized under the "Application" tag dimension
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md)
- **Merged At**: 2024-04-15 20:39:22 UTC

---

### PR [#2045](https://github.com/flexera-public/policy_templates/pull/2045): POL-1085 Azure Storage Accounts without Lifecycle Management Policies Revamp

#### Description

> This is a revamp of the Azure Storage Accounts without Lifecycle Management Policies policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Removed `Azure API Wait Time` parameter
> - Added ability to filter results by subscription, region, or tag
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Azure Storage Accounts without Lifecycle Management Policies](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/storage_account_lifecycle_management/README.md)
- **Merged At**: 2024-04-15 14:07:22 UTC

---

### PR [#2040](https://github.com/flexera-public/policy_templates/pull/2040): POL-1077 AWS S3 Intelligent Tiering Policy Revamp

#### Description

> This is a revamp of the AWS S3 Buckets Without Intelligent Tiering policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter buckets by region and tags
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS S3 Buckets Without Intelligent Tiering](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_storage_policy/README.md)
- **Merged At**: 2024-04-15 14:07:10 UTC

---

### PR [#2036](https://github.com/flexera-public/policy_templates/pull/2036): POL-1193 New Policy: Flexera FOCUS Report

#### Description

> This is a new policy that produces an aggregated billing report for a month that aligns with the FinOps FOCUS framework.
>

#### Metadata

- **Policies**: [Flexera FOCUS Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/focus_report/README.md)
- **Merged At**: 2024-04-11 10:11:12 UTC

---

### PR [#2012](https://github.com/flexera-public/policy_templates/pull/2012): POL-1184 Add AWS Usage Report - Amount of Instance Memory Used

#### Description

> <!-- Describe what this change achieves below -->
>
> - Adds AWS Usage Report showing the amount of instance memory in GiB used over a historical 12 month period.
> - Also updates the READMEs and policy template file names of the following existing policies:
>   - AWS Usage Report - Number of Instance Hours Used
>   - AWS Usage Report - Number of Instance vCPUs Used
>   - AWS Usage Forecast - Number of Instance Hours Used
>   - AWS Usage Forecast - Number of Instance vCPUs Used
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Adds another variation of existing usage reports tracking Instance Hours Used and Instance vCPUs used.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2012) for these details.
- **Merged At**: 2024-04-11 08:29:46 UTC

---

### PR [#1970](https://github.com/flexera-public/policy_templates/pull/1970): POL-1179 Add Azure Usage Report - Amount of Instance Memory Used

#### Description

> <!-- Describe what this change achieves below -->
> Adds Azure Usage Report showing the amount of instance memory in GiB used over a historical 12 month period.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Adds another variation of existing usage reports tracking Instance Hours Used and Instance vCPUs used.
>

#### Metadata

- **Policies**: [Azure Usage Report - Amount of Instance Memory Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_memory/README.md)
- **Merged At**: 2024-04-10 15:56:27 UTC

---

### PR [#2033](https://github.com/flexera-public/policy_templates/pull/2033): POL-1076 AWS Bucket Size Revamp

#### Description

> This is a revamp of the AWS Bucket Size policy. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - `Size Threshold (GiB)` parameter no longer expects user to specify size in bytes
> - Added ability to filter buckets by region and tags
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
>
> Additionally, the policy now has meta policy support.
>

#### Metadata

- **Policies**: [AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md)
- **Merged At**: 2024-04-10 13:13:30 UTC

---

### PR [#1969](https://github.com/flexera-public/policy_templates/pull/1969): POL-600 Add Azure Usage Report - Number of Instance vCPUs Used

#### Description

> <!-- Describe what this change achieves below -->
> Adds Azure Usage Report showing the number of instance vCPUs used over a historical 12 month period.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Resolves cadence between AWS and Azure (AWS version of this policy already exists in the Catalog)
>

#### Metadata

- **Policies**: [Azure Usage Report - Number of Instance vCPUs Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_vcpus/README.md)
- **Merged At**: 2024-04-10 08:39:34 UTC

---

### PR [#1961](https://github.com/flexera-public/policy_templates/pull/1961): POL-599 Add Azure Usage Report - Number of Instance Hours Used

#### Description

> <!-- Describe what this change achieves below -->
> Adds Azure Usage Report showing the number of instance hours used over a historical 12 month period.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Resolves cadence between AWS and Azure (AWS version of this policy already exists in the Catalog)
>

#### Metadata

- **Policies**: [Azure Usage Report - Number of Instance Hours Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_hours/README.md)
- **Merged At**: 2024-04-09 14:16:40 UTC

---

### PR [#2022](https://github.com/flexera-public/policy_templates/pull/2022): POL-1192 Policy Metadata Fixes

#### Description

> This corrects metadata in a large number of policies to align them with our general categorization schema. This should result in a cleaner list of policies in the global README. A lot of very minor stylistic changes (spacing, ordering of parameters, etc.) were also made to some of the affected policies based on feedback from the Dangerfile linter.
>
> The Dangerfile was also updated to avoid some false positives, particularly around the SaaS Manager policies.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2022) for these details.
- **Merged At**: 2024-04-08 12:24:02 UTC

---

### PR [#2020](https://github.com/flexera-public/policy_templates/pull/2020): POL-1191 Azure Hybrid Use Benefit Policy for SQL Revamp

#### Description

> This is a revamp of the Azure Hybrid Use Benefit Policy for SQL. From the CHANGELOG:
>
> - Fixed bug where databases ineligible for AHUB would appear in incident
> - Added support for Elastic Pool recommendations, including automated actions
> - Several parameters altered to be more descriptive and human-readable
> - Added improved subscription, region, and tag filtering for results
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Streamlined code for better readability and faster execution
>
> I also made a minor tweak to the Dangerfile's comma-separation test based on a false positive generated by this policy.
>

#### Metadata

- **Policies**: [Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md)
- **Merged At**: 2024-04-05 13:35:00 UTC

---

### PR [#1958](https://github.com/flexera-public/policy_templates/pull/1958): feat: Add params for github repo for Policy Sync PT

#### Description

> Added parameters for the Policy Template Github Repo to enable this to be used for other repos without modifying Policy Template
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1958) for details about unpublished policies.
- **Merged At**: 2024-04-04 12:08:05 UTC

---

### PR [#1960](https://github.com/flexera-public/policy_templates/pull/1960): SQ-7195 Spelling errors within 'ignored_recent_inventory_dates' policy template

#### Description

> There are spelling typos in our policy template that has been found by a customer.
>
> ### Issues Resolved
>
> Corrected typos in policy short description and parameter description
>

#### Metadata

- **Policies**: [ITAM Ignored Recent Inventory Dates](https://github.com/flexera-public/policy_templates/tree/master/compliance/flexera/fnms/ignored_recent_inventory_dates/README.md)
- **Merged At**: 2024-04-02 17:59:01 UTC

---

### PR [#1997](https://github.com/flexera-public/policy_templates/pull/1997): POL-1159 Update Flexera Policy Metadata

#### Description

> This updates the metadata for all of the dedicated Flexera policies to more clearly indicate what Flexera service they are for, and to consistently flag them as "Flexera" for the `provider` field. This also removes references to dated terminology for products/services in this metadata, such as RISC and Optima.
>
> Note: There are a large number of warnings/errors due to the large number of policies touched, but it is not feasible to update every policy to pass the modernized linting. Those policies can be updated as they get touched organically for other reasons.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1997) for these details.
- **Merged At**: 2024-04-02 15:37:07 UTC

---

### PR [#1999](https://github.com/flexera-public/policy_templates/pull/1999): POL-1157 Add Region Filtering to AWS/Azure Tag Cardinality Policies

#### Description

> This adds region filtering to the AWS and Azure Tag Cardinality policy. The main impetus for this change is to ensure the policy can work as expected for AWS estates with SCP protections enabled. Azure policy was updated to ensure both policies have parity in terms of their functionality.
>

#### Metadata

- **Policies**: [AWS Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/tag_cardinality/README.md), [Azure Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/tag_cardinality/README.md)
- **Merged At**: 2024-04-01 17:13:44 UTC

---

### PR [#1968](https://github.com/flexera-public/policy_templates/pull/1968): POL-1183 AWS Old Snapshots RDS Duplicate Fix

#### Description

> The AWS API endpoint for gathering RDS snapshots will return a value for each instance of an iterative snapshot of a single RDS resource. This means a snapshot for a single RDS resource that only appears in the bill once would be returned by the API several times, even though each instance returned by the API was just a version of a single snapshot.
>
> This fix adds new logic to account for this. When these iterative snapshots are found, only the most recent one is considered during the analysis instead of all of them. As a result, if someone has a daily backup of an RDS instance, the same instance with the same dollar value in the bill doesn't appear several times in the results, greatly inflating them. This also means that such snapshots will not be reported erroneously simply because their oldest iteration is > 30 days.
>

#### Metadata

- **Policies**: [AWS Old Snapshots](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/old_snapshots/README.md)
- **Merged At**: 2024-03-29 19:27:52 UTC

---

### PR [#1967](https://github.com/flexera-public/policy_templates/pull/1967): POL-1182 New Policy: AWS Missing Regions

#### Description

> This adds a new unpublished policy to test for AWS regions that are returned as enabled by the AWS API but that we can't actually make requests to.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1967) for details about unpublished policies.
- **Merged At**: 2024-03-27 19:23:22 UTC

---

### PR [#1954](https://github.com/flexera-public/policy_templates/pull/1954): POL-1171 AWS Rightsize RDS Instances APAC Fix

#### Description

> This fixes an issue with the policy referencing an invalid API endpoint for the APAC shard. This was fixed in other policies already but somehow this specific policy slipped through the cracks.
>
> Some other very minor tweaks around block names and ordering of fields were also made for the sake of conformity to other policies and to pass the new lint tests.
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2024-03-27 12:26:28 UTC

---

### PR [#1949](https://github.com/flexera-public/policy_templates/pull/1949): POL-1161 Move currency_reference.json

#### Description

> - currency_reference.json has been copied to `data/currency/currency_reference.json`
> - File also remains in `cost/scheduled_reports` with a README.md file explaining why it is there and indicating not to use that location going forward
> - Policies have been updated to point to the new location at `data/currency/currency_reference.json`

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1949) for these details.
- **Merged At**: 2024-03-22 14:36:00 UTC

---

### PR [#1937](https://github.com/flexera-public/policy_templates/pull/1937): POL-1158 Policy Catalog Reorganization

#### Description

> This PR evolved into a behemoth due to changes requiring further changes to facilitate them. This PR does the following:
>
> ### Billing Center Access Report Policy Revamp
>
> From the CHANGELOG:
>
> - Billing Center filter condensed to a single parameter and now supports both names and IDs
> - Incident summary is now derived from the name of the applied policy
> - Streamlined code for better readability and faster execution
>
> Example Applied Policy: https://app.flexera.com/orgs/28010/automation/applied-policies/projects/123559?policyId=65fb2c113ad5094c4696143c
>
> ### Dangerfile short_description Link Test
>
> The Dangerfile now checks for invalid URLs in the `short_description` of a policy and raises an error if the link doesn't match the location of the file.
>
> ### Invalid short_description Link Fixes
>
> By running a local version of the above test, I found several existing policies with bad URLs in their `short_description`. These have been fixed.
>
> ### Github Repository Reorganization
>
> The repository has been reorganized so that Flexera policies are in their own subdirectories based on the specific product they apply to. For example, `compliance/flexera/automation`, `cost/flexera/cco`, `operational/flexera/cmp`, etc. This makes the repository much less cluttered and much easier to find things in. MSP policies also have been moved accordingly into the appropriate `flexera/msp` directories.
>
> The meta policy and permissions generator files have been updated to account for the new file paths.
>
> ### Explicit Publish False
>
> All policies that are currently unpublished due to special rules in the Rakefile have been updated to contain an explicit `publish: false` in their metadata. This means we can get rid of these special rules and have a consistent implementation.
>
> ### Rakefile Update: `updated_at` and `recommendation_type` fields added
>
> The Rakefile used for generating the active policy list has been updated to include two new fields. `updated_at` is an ISO-8601 datetime string indicating when the policy was last modified in the catalog. `recommendation_type` is the requivalent field from the policy's info metadata block if such a value is specified.
>
> The Rakefile also no longer ignores policies based on location or metadata other than the `publish` field in the info block. Policies should always have this field set to false if we don't want them to be published, and this same PR updates the relevant policies to ensure that this is the case.
>
> ### Gemfile Update: octokit
>
> `Gemfile` and `Gemfile.lock` have been updated to include the octokit gem. This is what enables the Rakefile to obtain metadata from Github, such as when a policy was last updated.
>
> ### Manual Workflow Updates
>
> The `Test Policies` and `Update Active Policy List` workflows have been updated to allow for manual execution to assist in testing changes.
>
> ### Defunct File Removal
>
> A handful of ancient defunct files from the RightScale days have been removed.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1937) for these details.
- **Merged At**: 2024-03-21 20:02:47 UTC

---

### PR [#1930](https://github.com/flexera-public/policy_templates/pull/1930): FOPTS-3569 Fix: empty bill_source_expressions

#### Description

> Currently when `bill_source_expressions` is empty it creates an `or` condition with empty expressions, it causes that policy breaks in runtime, specifically with this error message:
>
> `Invalid filter: invalid #4 AND expression: attribute 'expressions' must contain at least one expression for type \\\"or\\\": invalid argument\`
>
> So we added a condition to validate if `bill_source_expressions` is empty, if so get rid to create that `or` condition.
>
> SQ link: https://flexera.atlassian.net/browse/SQ-7053
> CLONE link: https://flexera.atlassian.net/browse/FOPTS-3569
>
> ### Issues Resolved
>
> - Bug on empty `bill_source_expressions`.
>

#### Metadata

- **Policies**: [Azure Savings Realized from Reservations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_realized/README.md)
- **Merged At**: 2024-03-21 18:17:18 UTC

---

### PR [#1931](https://github.com/flexera-public/policy_templates/pull/1931): POL-1156 Deprecate "Policy Update Notification" Policy

#### Description

> This deprecates the Policy Update Notification policy and directs users to the more up to date and functional Flexera Automation Outdated Applied Policies policy.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1931) for details about unpublished policies.
- **Merged At**: 2024-03-20 17:50:31 UTC

---

### PR [#1920](https://github.com/flexera-public/policy_templates/pull/1920): FOPTS-3519 Fix work with unbudgeted spend for new API

#### Description

> New Budget API v1 not returning budgeted values for some budgets
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-3519
>

#### Metadata

- **Policies**: [Budget vs Actual Spend Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_v_actual_spend_report/README.md)
- **Merged At**: 2024-03-19 22:26:39 UTC

---

### PR [#1916](https://github.com/flexera-public/policy_templates/pull/1916): SQ-6941 Sort the dimensions shown in the report

#### Description

> Fixed bug where incident showed dimensions from column `Grouping Dimensions` in random order.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-6941
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2024-03-13 16:24:33 UTC

---

### PR [#1818](https://github.com/flexera-public/policy_templates/pull/1818): feat: initial revision for Google Cloud Run Anomaly Detection PT

#### Description

> New Policy Template from PoC - `Google Cloud Run Anomaly Detection`.
>
> <img width="1500" alt="image" src="https://github.com/flexera-public/policy_templates/assets/1490015/800b8c04-eed2-4d92-969f-18e2f3c7e245">
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1818) for details about unpublished policies.
- **Merged At**: 2024-03-06 13:18:15 UTC

---

### PR [#1909](https://github.com/flexera-public/policy_templates/pull/1909): Add links to documentation in the policy short description

#### Description

> Add links to documentation in the "Budget vs Actual Spend Report" policy short description
>

#### Metadata

- **Policies**: [Budget vs Actual Spend Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_v_actual_spend_report/README.md)
- **Merged At**: 2024-03-04 19:58:45 UTC

---

### PR [#1882](https://github.com/flexera-public/policy_templates/pull/1882): POL-1118 Flexera CCO Delete All Billing Centers Policy

#### Description

> This policy deletes all Billing Centers in the Flexera organization it is executed within. The policy will automatically self-terminate the second time it runs to avoid accidental future deletion of Billing Centers.
>
> This policy is unpublished and primarily intended for internal use.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1882) for details about unpublished policies.
- **Merged At**: 2024-03-04 13:41:58 UTC

---

### PR [#1881](https://github.com/flexera-public/policy_templates/pull/1881): POL-1117 Azure Bring-Your-Own-License (BYOL) Report Improvements

#### Description

> - Refactored to no longer require Azure credential
> - Removed parameter for Azure API endpoint since it is no longer needed
>

#### Metadata

- **Policies**: [Azure Bring-Your-Own-License (BYOL) Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/byol_report/README.md)
- **Merged At**: 2024-03-04 13:38:49 UTC

---

### PR [#1893](https://github.com/flexera-public/policy_templates/pull/1893): POL-979 AWS Policies: Improve Pricing API Endpoint Parameter

#### Description

> This updates the Pricing API parameter in the `AWS Unused IP Addresses` and `AWS Rightsize EBS Volumes` policies to be more user friendly, and provides better README documentation for the parameter and what it does.
>

#### Metadata

- **Policies**: [AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/README.md), [AWS Unused IP Addresses](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_ip_addresses/README.md)
- **Merged At**: 2024-03-04 13:17:47 UTC

---

### PR [#1778](https://github.com/flexera-public/policy_templates/pull/1778): FOPTS-3024 - New Budget vs Actual Spend report policy

#### Description

> Email a report of budget vs actual spend so the customer doesn't need to login to Flexera One
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FLEX-204
>

#### Metadata

- **Policies**: [Budget vs Actual Spend Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_v_actual_spend_report/README.md)
- **Merged At**: 2024-03-01 21:36:24 UTC

---

### PR [#1892](https://github.com/flexera-public/policy_templates/pull/1892): POL-1127 Meta Policy Duplicate Incidents Fix

#### Description

> Meta policies were sometimes returning duplicate results in the consolidated incident if they terminated a child policy and then replaced it with a new one, because both the old and new incident were being scraped.
>
> This changes the meta policy template (and meta policies) to filter the child incidents so that only active incidents are considered.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1892) for these details.
- **Merged At**: 2024-02-29 20:01:42 UTC

---

### PR [#1867](https://github.com/flexera-public/policy_templates/pull/1867): POL-1046 Google Open Buckets Revamp

#### Description

> This is a revamp of the Google Open Buckets policy that also fixes a known bug with the policy. From the CHANGELOG:
>
> - Fixed issue where some open buckets were not being reported on
> - Added ability to filter resources by project
> - Added ability to filter resources by region
> - Added ability to filter resources by label
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
> - Added logic required for "Meta Policy" use-cases
> - Flexera credential now required to facilitate meta policy use cases.
>

#### Metadata

- **Policies**: [Google Open Buckets](https://github.com/flexera-public/policy_templates/tree/master/security/google/public_buckets/README.md)
- **Merged At**: 2024-02-29 13:45:21 UTC

---

### PR [#1875](https://github.com/flexera-public/policy_templates/pull/1875): POL-1071 Merge 'AWS RDS Instances' policy into 'AWS Rightsize RDS Instances'

#### Description

> This modifies the AWS Rightsize RDS Instances policy to include Availability Zone, License Model, and vCPUs in the incident output, rendering the AWS RDS Instances policy obsolete.
>
> Additionally, the AWS RDS Instances policy is flagged as deprecated, and users are directed to the AWS Rightsize RDS Instances policy in the README.
>

#### Metadata

- **Policies**: [AWS RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rds_instance_license_info/README.md), [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2024-02-29 13:04:22 UTC

---

### PR [#1873](https://github.com/flexera-public/policy_templates/pull/1873): POL-973 Azure Unused IPs Better Filtering

#### Description

> This adds more filtering options to the policy:
>
> - Added IP allocation type (Dynamic or Static) to incident output
> - Added ability to filter results by allocation type via parameter
> - Added ability to filter results by minimum savings via parameter
>

#### Metadata

- **Policies**: [Azure Unused IP Addresses](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_ip_addresses/README.md)
- **Merged At**: 2024-02-29 10:28:28 UTC

---

### PR [#1870](https://github.com/flexera-public/policy_templates/pull/1870): FOPTS-3238 Update `short_description` of the policy Azure Rightsize NetApp Files

#### Description

> The short description of the policy Azure Rightsize NetApp Files was in sync with the Flexera documentation, this change updated the `short_description` of the policy so both descriptions match.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/FOPTS-3238
>

#### Metadata

- **Policies**: [Azure Rightsize NetApp Files](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp_files/README.md)
- **Merged At**: 2024-02-27 21:44:12 UTC

---

### PR [#1874](https://github.com/flexera-public/policy_templates/pull/1874): POL-1070 Deprecate AWS Inefficient Instance Utilization using CloudWatch

#### Description

> The AWS Inefficient Instance Utilization using CloudWatch policy does basically the same thing as the existing Rightsize EC2 policy, so it is being deprecated.

#### Metadata

- **Policies**: [AWS Inefficient Instance Utilization using CloudWatch](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/instance_cloudwatch_utilization/README.md)
- **Merged At**: 2024-02-27 21:41:58 UTC

---

### PR [#1833](https://github.com/flexera-public/policy_templates/pull/1833): POL-1062 Deprecate CMP Policies

#### Description

> This pull request deprecates the 4 remaining CMP policies that have not yet been deprecated.
>
> No testing was done since no changes were made to anything that would impact policy execution.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1833) for these details.
- **Merged At**: 2024-02-27 16:43:33 UTC

---

### PR [#1846](https://github.com/flexera-public/policy_templates/pull/1846): POL-1035 Google Policy Regex Support

#### Description

> This adds support for regex tag filtering to several Google policies.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1846) for these details.
- **Merged At**: 2024-02-27 13:35:39 UTC

---

### PR [#1845](https://github.com/flexera-public/policy_templates/pull/1845): POL-1025 Azure Policy Regex Support

#### Description

> This adds support for regex tag filtering to several Azure policies. Additionally, it includes revamps of the two AKS Node Pools policies to help facilitate this update.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1845) for these details.
- **Merged At**: 2024-02-27 13:04:09 UTC

---

### PR [#1864](https://github.com/flexera-public/policy_templates/pull/1864): POL-1068 Cloud Cost Anomaly Alerts Link Fix

#### Description

> This fixes a bug where the link would render incorrectly if spaces were present. Spaces are now appropriately replaced with %20 in the link.
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2024-02-26 20:25:42 UTC

---

