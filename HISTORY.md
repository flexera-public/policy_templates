# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#3305](https://github.com/flexera-public/policy_templates/pull/3305): POL-1558 New Unpublished CBI Policy Templates

*Unpublished, New Policy Template*

#### Description

> Adds two new unpublished policy templates for sending CSV files from AWS S3 or Azure Blob Storage to Flexera CBI.
>
> Unpublished because these policy templates require some extra knowhow to use, since they send in CSV files over multiple executions, similar to the Oracle CBI policy template. They should generally only be used as a fallback, with guidance from Flexera, when the published policy templates that work in a much more straight-forward and user-friendly way are not able to be used due to the amount of data being sent to CBI.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3305) for details about unpublished policies.
- **Merged At**: 2025-07-14 14:34:26 UTC

---

### PR [#3314](https://github.com/flexera-public/policy_templates/pull/3314): POL-1559 doc_link Metadata

*Unpublished, Minor Update*

#### Description

> - Adds a new doc_link field to every policy's metadata that contains a link to the policy template in Github. This is to support a future UI enhancement.
> - Adds appropriate changes to the meta parent templates to add doc_links to meta parent policies.
> - Adds Dangerfile tests to check for the presence of a valid doc_link
> - Updates the style guide to include doc_link
>
> NOTE: The various Dangerfile warnings/errors are unrelated to this change. This touches almost every policy template in the catalog.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3314) for these details.
- **Merged At**: 2025-07-14 14:18:53 UTC

---

### PR [#3312](https://github.com/flexera-public/policy_templates/pull/3312): POL-1551 Meta Parent Fix: Actions with Parameters

*Bug Fix*

#### Description

> Fixes issue with meta parent policies where actions would not work if the actions had parameters. The root cause was a typo where a variable "action_options" was incorrectly declared as "actions_options".
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3312) for these details.
- **Merged At**: 2025-07-11 14:46:22 UTC

---

### PR [#3306](https://github.com/flexera-public/policy_templates/pull/3306): FOAA-294 fix: improved savings calculation accuracy for underutilized resources on AWS Rightsize RDS

*Minor Update, Bug Fix*

#### Description

> Improved accuracy of savings calculation for underutilized RDS instances recommending to be resized.  We now consider only the "InstanceUsage" usage type costs when estimating potential savings from resize.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-294
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2025-07-11 12:05:29 UTC

---

### PR [#3210](https://github.com/flexera-public/policy_templates/pull/3210): FOPTS-10413 Add validation for tag tag_azure_databricks_clusterid

*Minor Update*

#### Description

> This PR introduces a validation mechanism in the Azure Databricks Rightsize Compute Instances policy template to ensure accurate cost allocation. Specifically, it verifies the presence of the tag_azure_databricks_clusterid dimension by validating the required tag.
>
> ### Issues Resolved
> * Prevents policies from failing by checking for the required tag in advance.
>
>
>

#### Metadata

- **Policies**: [Azure Databricks Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/databricks/rightsize_compute/README.md)
- **Merged At**: 2025-07-09 17:10:06 UTC

---

### PR [#3296](https://github.com/flexera-public/policy_templates/pull/3296): POL-1557 CBI Policy Daily Granularity Support

*Minor Update*

#### Description

> Updates the "Common Bill Ingestion from AWS S3 Object Storage" and "Common Bill Ingestion from Azure Blob Storage" policy templates to support billing data stored at a daily, rather than a monthly, granularity. From the READMEs:
>
> - *Granularity* - Whether there will be one file per month of billing data, or one file per day of billing data.
>   - If set to "Daily", file names will be expected to end with a full date like "2024-10-03.csv". The policy template will grab all of the files for a given month to upload to Flexera.
>   - If set to "Monthly", file names will be expected to end with a year and month like "2024-10.csv". The policy template will grab one file for the month to upload to Flexera.
>

#### Metadata

- **Policies**: [Common Bill Ingestion from AWS S3 Object Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cbi_ingestion_aws_s3/README.md), [Common Bill Ingestion from Azure Blob Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cbi_ingestion_azure_blob/README.md)
- **Merged At**: 2025-07-09 12:18:25 UTC

---

### PR [#3111](https://github.com/flexera-public/policy_templates/pull/3111): POL-1514 - Add resource utilization charts to Azure + AWS Rightsize Compute PTs

*Minor Update*

#### Description

> Adds resource utilization chart URLs to the resulting incidents for AWS+Azure Rightsize Compute Policy Templates.  This mitigates/prevents need to use cloud vendor console or another observability tool outside Flexera to validate the recommendation is true.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1514
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md), [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2025-07-08 01:20:58 UTC

---

### PR [#3280](https://github.com/flexera-public/policy_templates/pull/3280): SQ-16235 | Bill Processing Errors Notification | Add support for Azure CSP and Azure MCA Enterprise

*Minor Update*

#### Description

> Add support for Azure CSP and Azure MCA Enterprise accounts to Bill Processing Errors Notification policy.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/SQ-16235
>

#### Metadata

- **Policies**: [Cloud Bill Processing Error Notification](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/bill_processing_errors_notification/README.md)
- **Merged At**: 2025-07-07 17:55:14 UTC

---

### PR [#3272](https://github.com/flexera-public/policy_templates/pull/3272): POL-1553 AWS Untagged Resources Resource Type Filtering

*Minor Update*

#### Description

> AWS Untagged Resources
> - New `Resource Types` parameter allows policy template to only report on specific services or resource types.
> - Small code changes made to improve the speed of policy template execution.*
>
> (Basically just amounts to changing IncludeComplianceDetails to false since we don't use this data in the policy template anyway)
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3272) for these details.
- **Merged At**: 2025-07-07 14:04:48 UTC

---

### PR [#3275](https://github.com/flexera-public/policy_templates/pull/3275): POL-1542 feat: Update tag resource action to use Tags API and enable Tag Contributor role

*Minor Update*

#### Description

> Update tag resource action to use Azure Tags API, which enables `Tag Contributor` role to be used for enabling action capabilities with minimum scope.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1542
>

#### Metadata

- **Policies**: [Azure Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_resources/README.md)
- **Merged At**: 2025-07-07 12:31:41 UTC

---

### PR [#3276](https://github.com/flexera-public/policy_templates/pull/3276): SQ-15559 Azure Superseded Compute Instances Reference Error

*Minor Update, Bug Fix*

#### Description

> A ReferenceError is being caused:
>
> ```
> ReferenceError: 'instance_type_price_map' is not defined\nLocation:\n datasource \"ds_superseded_instances\"\n script \"js_superseded_instances\
> ```
>
> This is caused because the variable instance_type_price_map is not always declared, so instead of being undefined it's causing a reference error.
>
> ![image](https://github.com/user-attachments/assets/0de1be8b-9889-4042-b7e4-04f4b8b871e1)
>
> To fix this we declare the variable before accessing it.
>
> ### Issues Resolved
>
> There's a support question related to this PR: https://flexera.atlassian.net/browse/SQ-15559
>

#### Metadata

- **Policies**: [Azure Superseded Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/superseded_instances/README.md), [Meta Parent: Azure Superseded Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/superseded_instances/README.md)
- **Merged At**: 2025-07-04 19:41:59 UTC

---

### PR [#3260](https://github.com/flexera-public/policy_templates/pull/3260): POL-1550 - fix: Flexera Onboarding - handle when no tag dimensions or rbds exist yet

*Bug Fix*

#### Description

> Quick fix on Flexera Onboarding PT
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1550
>

#### Metadata

- **Policies**: [Flexera Onboarding](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/onboarding/README.md)
- **Merged At**: 2025-06-30 18:34:50 UTC

---

### PR [#3255](https://github.com/flexera-public/policy_templates/pull/3255): POL-1544 Azure Hybrid Use Benefit for SQL: Additional Incident Fields

*Minor Update*

#### Description

> Azure Hybrid Use Benefit for SQL:
> - Added `Version` and `Database Format` fields to the incident table.
> - Updated version for various API calls from preview versions to the current stable ones.
>

#### Metadata

- **Policies**: [Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md), [Meta Parent: Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md)
- **Merged At**: 2025-06-17 17:47:41 UTC

---

### PR [#3251](https://github.com/flexera-public/policy_templates/pull/3251): POL-1546 AWS Rightsize RDS Instances Better Savings Calculation

*Minor Update*

#### Description

> The `AWS Rightsize RDS Instances` policy template has been updated to make use of the RDS price list to calculate savings. From the updated README:
>
> - For underutilized resources, the `Estimated Monthly Savings` is calculated based on whether or not the [RDS price sheet](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/data/aws/aws_rds_pricing.json) contains list prices for the instance types.
>   - If it does, the percentage difference between the list prices of the current instance type and the recommended instance type is multiplied by the full actual cost of the resource. This is then subtracted from the current cost of the resource to calculate the savings.
>   - If it does not, the full cost of the resource divided by the number of [NFUs (Normal Form Units)](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-reservation-models/normalization-factor-for-dedicated-ec2-instances.html) for the current resource size, multiplied by the number of NFUs for the recommended resource size, and then subtracted from the current cost of the resource.
>
> The update also corrects some issues that would prevent underutilized resources from appearing in the incident.
>
> ### Issues Resolved
>
> We had reports that the estimated savings being reported by this policy template were not accurate enough. This should help with that.
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md), [Meta Parent: AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2025-06-16 20:12:22 UTC

---

### PR [#3241](https://github.com/flexera-public/policy_templates/pull/3241): POL-1545 Azure Rightsize Managed Disks Fixes

*Minor Update*

#### Description

> Azure Rightsize Managed Disks
> - Policy template no longer raises an incident if user does not set any thresholds for determining underutilization.
> - Defaults changed for `IOPS Threshold (%)` and `Throughput Threshold (%)` parameters to something a typical user would expect.
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2025-06-16 12:19:25 UTC

---

### PR [#3238](https://github.com/flexera-public/policy_templates/pull/3238): POL-1543 Cloud Cost Anomaly Alerts: Filter Improvements

*Minor Update*

#### Description

> This modifies the `Cloud Cost Anomaly Alerts` policy template to add the ability to add negative filters (NOT x=y).
>
> Note: I have verified that the URL for the Cloud Cost Anomaly page in Flexera One has no way to add a NOT filter even though the API supports it. A disclaimer is added to the incident if the customer uses any such filters to let them know this won't be reflected on the link. This disclaimer only appears if the parameter to exclude alerts is actually used.
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2025-06-13 14:08:32 UTC

---

### PR [#3232](https://github.com/flexera-public/policy_templates/pull/3232): POL-1538 Budget Alerts Revamp

*Minor Update*

#### Description

> This revamps the code for the Budget Alerts policy template to conform with current standards. It also modifies the filtering parameters to make it clear that the user cannot filter a Summarized report.
>

#### Metadata

- **Policies**: [Budget Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_report_alerts/README.md)
- **Merged At**: 2025-06-10 18:32:45 UTC

---

### PR [#3219](https://github.com/flexera-public/policy_templates/pull/3219): POL-1537 Scheduled Report: Ignore Current Month

*Major Update*

#### Description

> Scheduled Report policy template:
>
> - Added option to ignore current month when reporting.
> - Added ability to select an arbitrary number of months (up to 12) instead of preselected options.
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2025-06-06 13:59:43 UTC

---

### PR [#2450](https://github.com/flexera-public/policy_templates/pull/2450): POL-1298 - Flexera Onboarding v0.1.0

*New Policy Template*

#### Description

> This policy checks various configurations in your Organization to ensure that it is set up correctly.  The checks and recommendations are opinionated, and align with recommended best practices for onboarding and productionizing your Organization.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1298
>

#### Metadata

- **Policies**: [Flexera Onboarding](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/onboarding/README.md)
- **Merged At**: 2025-06-05 16:48:07 UTC

---

### PR [#3127](https://github.com/flexera-public/policy_templates/pull/3127): Initial revision of custom branding

*New Policy Template*

#### Description

> This Policy allows a customer to brand the FlexeraOne platform quickly and consistently.
>
> ### Issues Resolved
>
> No Jira for now
>

#### Metadata

- **Policies**: [Configure Custom Branding](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/flexeraone/custom_branding/README.md)
- **Merged At**: 2025-05-30 12:14:27 UTC

---

### PR [#3180](https://github.com/flexera-public/policy_templates/pull/3180): POL-1528 DTU support for Azure Rightsize SQL Databases

#### Description

> Azure Rightsize SQL Databases changes:
>
> - Policy template now distinguishes between vCore-model and DTU-model databases and checks CPU and DTU metrics to determine usage for each purchase model respectively.
> - Fixed issue where policy template would report new recommendations if a metric other than cpuAverage had changed for an existing recommendation.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md), [Meta Parent: Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2025-05-23 20:21:42 UTC

---

### PR [#3156](https://github.com/flexera-public/policy_templates/pull/3156): FOPTS-9865 Performance improvement -- migrated to Metrics getBatch API call

#### Description

> Migrated from "Metrics" API to "Metrics getBatch" API, improving policy performance.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-9865
> https://flexera.atlassian.net/browse/SQ-12222
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md), [Meta Parent: Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2025-05-23 13:49:41 UTC

---

### PR [#3174](https://github.com/flexera-public/policy_templates/pull/3174): POL-1527 Azure Rightsize NetApp Resources - Correct Typo in Template Description

#### Description

> <!-- Describe what this change achieves below -->
> Fixes a typo in policy template's Short Description
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> None, less typos = more professional
>

#### Metadata

- **Policies**: [Azure Rightsize NetApp Resources](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp/README.md)
- **Merged At**: 2025-05-21 13:01:40 UTC

---

### PR [#3171](https://github.com/flexera-public/policy_templates/pull/3171): POL-1526 Meta Parent Improvements

#### Description

> - Adds Account ID field to various incidents raised by the meta parent.
> - Converts incidents for policies to be created/updated/deleted to proper incident tables instead of Go templates.
>
> Tested in client environment with success.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3171) for these details.
- **Merged At**: 2025-05-21 12:25:47 UTC

---

### PR [#3168](https://github.com/flexera-public/policy_templates/pull/3168): POL-1521 AWS CloudTrails Without Log File Validation Enabled - Fix Reference Error due to undefined variable

#### Description

> <!-- Describe what this change achieves below -->
> Applied policy fails to run with ReferenceError: 'log_file_validation_enabled' is not defined
>
> This is probably due to the incorrect naming of a variable and/or the code referencing a variable that does not exist.
>
> Link to applied policy where error has been observed - https://app.flexera.com/orgs/39679/automation/applied-policies/projects/141708?policyId=681c8c88d88a69fbd74b297b
>
> This change adds a fix to mitigate the non-instantiated variable
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Fixes an issue where the applied policy fails due to `log_file_validation_enabled` variable not being defined.
>

#### Metadata

- **Policies**: [AWS CloudTrails Without Log File Validation Enabled](https://github.com/flexera-public/policy_templates/tree/master/security/aws/log_file_validation_enabled/README.md)
- **Merged At**: 2025-05-19 13:09:13 UTC

---

### PR [#3110](https://github.com/flexera-public/policy_templates/pull/3110): POL-1509 Meta Policy Update: Usability & Incident for Child Policies in Error State

#### Description

> This makes two significant changes:
>
> #### Usability Improvements
>
> - The list of default policy templates to generate meta parents for is now in a separate `default_template_files.yaml` file rather than contained in the script.
> - The script now has much improved command line functionality to allow the user to generate meta parents from a custom list or individual policy template files, as well as using a custom meta parent template instead of one of the provided ones if desired.
>   - There is also improved error output if the user does not use the script correctly.
> - Added improved error handling/output if child policy template is missing necessary modifications to create a meta parent.
> - README for the script is updated to include info on the above.
>
> #### Error Incident
>
> This adds a new incident to meta parent policies that list child policies that are in an error state, along with the error details.
>
> The user has the option of deleting these child policies from the incident page so that new ones are generated the next time the meta parent executes. This can eliminate the need to completely terminate/reapply the parent policy if an issue external to Flexera (such as credential permissions) is corrected.
>
> NOTE: The primary thing to review are the updated meta generation templates. The policies themselves are all just generated from those templates.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3110) for these details.
- **Merged At**: 2025-05-19 12:09:50 UTC

---

### PR [#3157](https://github.com/flexera-public/policy_templates/pull/3157): POL-1525 Azure Untagged Resources Fix

#### Description

> Two fixes for the `Azure Untagged Resources` policy template:
>
> - Fixed issue where prompt for adding tags incorrectly said to use "key:value" instead of "key=value" format.
> - Fixed issue where tags would fail to apply to Azure subscriptions.
>

#### Metadata

- **Policies**: [Azure Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_resources/README.md), [Meta Parent: Azure Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_resources/README.md)
- **Merged At**: 2025-05-16 19:48:36 UTC

---

### PR [#3154](https://github.com/flexera-public/policy_templates/pull/3154): POL-1524 Currency Conversion Fix

#### Description

> This fixes an issue with the Currency Conversion policy template where execution would fail if the user built off of the adjustment created by this policy template.
>
> The currency conversion adjustment is now always first in the list being sent into the API, ensuring no issues if later adjustment rules build off of it.
>

#### Metadata

- **Policies**: [Currency Conversion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/currency_conversion/README.md)
- **Merged At**: 2025-05-16 13:18:16 UTC

---

### PR [#3138](https://github.com/flexera-public/policy_templates/pull/3138): FOPTS-9680 Correctly handle pagination in Azure Long Stopped Instances policy

#### Description

> 1. Fixed pagination for `datasource ds_azure_instances_with_logs`.
> Previously, pagination would result multiple items for the same ResourceId. This fix ensures that multiple pages for the same ResourceId will be combined into one item.
>
> Also confirmed that pagination will **not** cause error for other datasources in this policy.
>
> 2. Safe guard for `state = powerstate.split('/')[1];`
> `powerstate` is `undefined` sometime, causing JavaScript error
> This error is hard to reproduce, and it is unclear when will it happen.
> Snapshot of the DB document showing the error:
> `"error": "Summary:\n  script execution failed\nDetail:\n  execution failed: TypeError: Cannot access member 'split' of undefined\nLocation:\n  datasource \"ds_azure_incident_results\"\n    script \"js_azure_incident_results\"\n",`
> [policy db 680aa239ce13ed33750fdc2e.json](https://github.com/user-attachments/files/20190083/policy.db.680aa239ce13ed33750fdc2e.json)
> [policy db 680aa60f1344d852b0392969.json](https://github.com/user-attachments/files/20190085/policy.db.680aa60f1344d852b0392969.json)
>
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-14979
> https://flexera.atlassian.net/browse/FOPTS-9680
>

#### Metadata

- **Policies**: [Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md), [Meta Parent: Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md)
- **Merged At**: 2025-05-15 13:17:18 UTC

---

### PR [#3117](https://github.com/flexera-public/policy_templates/pull/3117): FOPTS-9434 Correctly include all RDS snapshots in policy evaluation

#### Description

> This PR addresses an issue in the policy template's RDS snapshot filtering logic that was causing some snapshots to be incorrectly excluded from policy evaluation.
>
>
> The js_describe_db_snapshots script was incorrectly filtering RDS snapshots. It was grouping snapshots by ParentId (the RDS instance identifier), sorting them by StartTime, and then only retaining the most recent snapshot for each ParentId. This meant that older snapshots, even if they met other policy criteria (like age), were being ignored. This behavior could lead to:
>
> * Data Governance Gaps: Older snapshots, which might be needed for compliance or audit purposes, were not being properly managed by the policy.
> * Cost Optimization Inefficiencies: Opportunities to identify and manage older, potentially costly snapshots were being missed.
> * Recovery Risks: In some disaster recovery scenarios, the policy might not be able to identify or take action on older snapshots that could be required.
>
>
>
> ### Issues Resolved
>
> This PR modifies the js_describe_db_snapshots script to correctly include all RDS snapshots in the policy's evaluation. The change involves iterating through all snapshots for each ParentId instead of just selecting the most recent one.
>
> The following code snippet shows the key change in the js_describe_db_snapshots script:
>
> ``` golang
> --- a/path/to/your/policy/template.rb  # Replace with the actual path
> +++ b/path/to/your/policy/template.rb  # Replace with the actual path
> @@ -99,10 +99,12 @@
>      })
>      _.each(_.keys(sorted_by_parent), function(parent) {
>        sorted_parents = _.sortBy(sorted_by_parent[parent], "startTime").reverse()
> -      result.push(sorted_parents[0])
> +      sorted_parents.forEach(function(snapshot) {
> +        result.push(snapshot);
> +      });
>      })
> ```
>

#### Metadata

- **Policies**: [AWS Old Snapshots](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/old_snapshots/README.md)
- **Merged At**: 2025-05-14 17:10:22 UTC

---

### PR [#2954](https://github.com/flexera-public/policy_templates/pull/2954): POL-1446 - New Policy - MSP Usage Audit

*New Policy Template*

#### Description

> This policy generates a comprehensive report on the usage of MSP Customer Organizations. It provides operational capabilities related to managing MSP Customer Organizations, including cost analysis and user activity metrics.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1446
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2954) for details about unpublished policies.
- **Merged At**: 2025-05-13 19:49:15 UTC

---

### PR [#3081](https://github.com/flexera-public/policy_templates/pull/3081): POL-1507 New Policy Template: Rule-Based Dimension From Custom Tags

*New Policy Template*

#### Description

> This unpublished policy template creates and updates custom Rule-Based Dimensions that duplicate Custom Tags that have been configured in the Flexera platform. The user can then add or remove rules above or below the generated rules, either through automation or the Flexera One UI, to further customize the dimension; rules added to these rule-based dimensions manually, or by other policy templates, will not be deleted.
>
> The purpose of this policy template is to enable a user to easily make a Rule-Based Dimension that mirrors a Custom Tag but then add their own additional rules to address various resources, accounts, etc. that aren't tagged or are improperly tagged.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3081) for details about unpublished policies.
- **Merged At**: 2025-05-13 12:09:21 UTC

---

### PR [#3092](https://github.com/flexera-public/policy_templates/pull/3092): POL-1480 AWS instance_types.json Policy Template Updates

#### Description

> The following policy templates have been updated to use the new, generated `aws_ec2_instance_types.json` file instead of the old manually maintained `instance_types.json` file:
>
> - AWS Burstable EC2 Instances
> - AWS Cost Report - EC2 Instance Cost Per Hour
> - AWS Rightsize ElastiCache
> - AWS Rightsize RDS Instances
> - AWS Superseded EC2 Instances
> - AWS Usage Forecast - Instance Time Used
> - AWS Usage Report - Instance Time Used
> - AWS Publicly Accessible RDS Instances
> - AWS Unencrypted RDS Instances
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3092) for these details.
- **Merged At**: 2025-05-13 12:06:59 UTC

---

### PR [#1807](https://github.com/flexera-public/policy_templates/pull/1807): POL-877 New Policy: Alibaba Cloud CBI

*New Policy Template*

#### Description

> Policy for ingesting Alibaba billing data. Also includes minor changes to Dangerfile testing to account for Alibaba policy templates.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1807) for details about unpublished policies.
- **Merged At**: 2025-05-12 15:10:40 UTC

---

### PR [#3128](https://github.com/flexera-public/policy_templates/pull/3128): SQ-14908 Fix the error with Last 30 days parameter

#### Description

> This change fixes the error that costs/select API returns when the parameter date range is set to 30 days.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/SQ-14908
>

#### Metadata

- **Policies**: [Scheduled Report for Unallocated Costs](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_report_unallocated/README.md)
- **Merged At**: 2025-05-08 19:33:15 UTC

---

### PR [#3089](https://github.com/flexera-public/policy_templates/pull/3089): POL-1508 - AWS and Google Scheduled Policy Enhancements

#### Description

> - Remove `next_stop`, `next_start` label requirements
> - Add task labels to improve status updates and debugging for CWF actions
> - Enhanced start/stop functions with retry logic that attempts each operation up to 3 times
> - Added robust state verification to ensure instances reach the desired state
> - Add error capture, graceful timeout handling for triggered actions
> - Added detailed logging for troubleshooting failed operations
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1508
>

#### Metadata

- **Policies**: [AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md), [Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2025-05-01 17:57:11 UTC

---

### PR [#3091](https://github.com/flexera-public/policy_templates/pull/3091): POL-1510 Repository Cleanup

#### Description

> We've started to receive complaints from both internal and external users that the large number of deprecated policy templates in the catalog is causing confusion. Additionally, the repository itself has become a bit cluttered due to old and unused assets.
>
> This PR solves this by making the following changes:
>
> - All policy templates that were both deprecated and unpublished have been deleted. These are almost all very old policy templates that are defunct and not useful. This will have no impact on the catalog itself (since they were unpublished) but will declutter the repository a bit. The repository history can still be used to obtain these files in the unlikely event that they are needed for something.
> - All published deprecated policy templates have been unpublished. This should remove them from the catalog and make it less confusing and cluttered. None of these policy templates were recently deprecated, and the files remain in the repository if a user needs them.
>
> Unfortunately, due to several factors, we do not have a simple way to proactively reach out to users about these changes. That said, none of these files were newly deprecated or newly unpublished (prior to this PR), so users have had in most cases over a year to make any necessary changes. Existing applied policies will be unaffected.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3091) for these details.
- **Merged At**: 2025-04-25 18:33:16 UTC

---

### PR [#3080](https://github.com/flexera-public/policy_templates/pull/3080): POL-1506 Account RBD Policy Updates

#### Description

> This updates the unpublished policy templates for generating RBDs from account tags to play nice with each other. By making use of dummy rules to delineate the beginning and end of the rules generated by the policy templates, they can now be applied simultaneously and will not overwrite each other's work. Additionally, rules manually added in the UI will not be deleted.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3080) for these details.
- **Merged At**: 2025-04-16 20:05:52 UTC

---

### PR [#3071](https://github.com/flexera-public/policy_templates/pull/3071): task: add `publish: "false",`

#### Description

> Adding `publish: "false",` for new PTs merged

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3071) for details about unpublished policies.
- **Merged At**: 2025-04-15 17:26:36 UTC

---

### PR [#2918](https://github.com/flexera-public/policy_templates/pull/2918): POL-1435 POL-1436 POL-1437 - feat: Schedule Instance PT Enhancements

#### Description

> - Added retry mechanism in case of failed actions or timeout waiting for the expected status change
> - Fixed issue preventing schedules being enforced when first action attempt fails
> - Added "Last Stop Status", "Last Stop Time", "Last Start Status", "Last Start Time" details to instance list
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1435
> https://flexera.atlassian.net/browse/POL-1436
> https://flexera.atlassian.net/browse/POL-1437
>

#### Metadata

- **Policies**: [Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md)
- **Merged At**: 2025-04-15 17:19:43 UTC

---

### PR [#2956](https://github.com/flexera-public/policy_templates/pull/2956): POL-1452 - New PT - RBDs from CSV

*New Policy Template*

#### Description

> This policy creates and updates custom Rule-Based Dimensions based on data provided in CSV format. It allows you to create multiple Rule-Based Dimensions at once using data from a CSV file that maps dimension values to other values that should be used as rules.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1452
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2956) for details about unpublished policies.
- **Merged At**: 2025-04-14 19:01:18 UTC

---

### PR [#3032](https://github.com/flexera-public/policy_templates/pull/3032): POL-1136 Automation Credential Policy Templates

#### Description

> Creates two new policy templates to report on disallowed credentials and expiring credentials. Also fixes a minor error in the `Flexera Automation Outdated Applied Policies` policy template.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3032) for these details.
- **Merged At**: 2025-04-14 12:19:28 UTC

---

### PR [#3055](https://github.com/flexera-public/policy_templates/pull/3055): POL-1478 New Policy Template: Spot Eco - Commitment Source Dimension

*New Policy Template*

#### Description

> This policy template creates a rule-based dimension in Flexera Cloud Cost Optimization that reports on whether commitments were purchased by Spot Eco or not. Costs will have one of three values for this dimension:
>
> - "Eco" - The commitment was purchased by Spot Eco.
> - "Non-Eco" - The commitment was not purchased by Spot Eco.
> - "None" - The cost is not a commitment and therefore the commitment source is not applicable.
>
> **NOTE: This policy template should be considered an alpha release and currently only works with a single Spot Eco organization. Support for multiple organizations may be added in a future iteration.**
>

#### Metadata

- **Policies**: [Spot Eco - Commitment Source Dimension](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/spot/commitment_source_rbd/README.md)
- **Merged At**: 2025-04-11 21:27:17 UTC

---

### PR [#2941](https://github.com/flexera-public/policy_templates/pull/2941): POL-1449 - Initial Spot Policy Templates

*New Policy Template*

#### Description

> Adds 3 new policy templates showcasing early integrations between Flexera and Spot after the announcement of [definitive agreement to acquire the Spot by NetApp FinOps business from NetApp®](https://www.flexera.com/about-us/press-center/flexera-to-acquire-finops-business-from-netapp-to-strengthen-portfolio)
>
> **Spot Ocean - Common Bill Ingest**
> Brings cost and usage visibility from Kubernetes Clusters into Flexera.
>
> **Spot Security - Compliance Report**
> Brings misconfigurations and compliance recommendations into Flexera.
>
> **Spot Ocean - Rightsize Recommendations**
> Brings rightsizing recommendations for Kubernetes Containers into Flexera.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2941) for these details.
- **Merged At**: 2025-04-07 19:07:19 UTC

---

### PR [#3038](https://github.com/flexera-public/policy_templates/pull/3038): POL-1477 Update Repository README Automation

#### Description

> This updates and improves the automation for generating the repository's README file. It now makes use of the active policy JSON file.
>
> PR also updates the provider for a couple of Google policies from "GCE" to "Google" for accurate categorization in the README file.
>
> (Ignore linting warnings for FOOTER.md. That file is just used to generate the README.md. As long as the linting warnings don't persist in README.md, they aren't an issue)

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3038) for these details.
- **Merged At**: 2025-04-07 17:04:16 UTC

---

### PR [#2995](https://github.com/flexera-public/policy_templates/pull/2995): POL-1462 Azure Long Stopped Compute Instances: Savings and Disk Support

#### Description

> This is a major update to the Azure Long Stopped Compute Instances policy template. From the CHANGELOG:
>
> - Corrected issue where policy template incorrectly calculated length of time an instance had been stopped for.
> - Added potential savings information to policy output, including potential disk savings.
> - Policy recommendations will now appear in the Optimization dashboard in Flexera One.
> - Changed policy category from "Compliance" to "Cost".
>

#### Metadata

- **Policies**: [Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md), [Meta Parent: Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md)
- **Merged At**: 2025-04-07 12:27:33 UTC

---

### PR [#3029](https://github.com/flexera-public/policy_templates/pull/3029): POL-1473 Schedule ITAM Report: Add Truncated Date Option

#### Description

> Adds an option to truncate dates to just YYYY-MM-DD instead of showing full ISO-8601 format for users that want the emailed report to resemble the report as shown in the Flexera One UI.
>
> From the CHANGELOG:
>
> - Added parameter to normalize dates in report to match Flexera One UI
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3029) for these details.
- **Merged At**: 2025-04-07 12:06:20 UTC

---

### PR [#2994](https://github.com/flexera-public/policy_templates/pull/2994): POL-1461 New Policy: Google Overutilized VM Instances

*New Policy Template*

#### Description

> This adds a new policy template to report on overutilized Google VM instances.
>

#### Metadata

- **Policies**: [Google Overutilized VM Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/google/overutilized_vms/README.md), [Meta Parent: Google Overutilized VM Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/google/overutilized_vms/README.md)
- **Merged At**: 2025-03-31 12:15:40 UTC

---

### PR [#2991](https://github.com/flexera-public/policy_templates/pull/2991): POL-1459 New Policy: AWS Overutilized EC2 Instances

*New Policy Template*

#### Description

> New policy template to report and optionally upsize overutilized oversized AWS EC2 instances.
>
> Also made some minor fixes to the AWS Rightsize EC2 Instances README that I spotted.
>

#### Metadata

- **Policies**: [AWS Overutilized EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/overutilized_ec2_instances/README.md), [Meta Parent: AWS Overutilized EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/overutilized_ec2_instances/README.md)
- **Merged At**: 2025-03-28 13:48:08 UTC

---

### PR [#3017](https://github.com/flexera-public/policy_templates/pull/3017): POL-1469 Dangerfile Fixes/Updates

#### Description

> * Updated Ruby and node packages to update versions and solve potential security vulnerabilities.
>
> * Added CodeQL configuration file so that we can enable CodeQL scanning for additional security on PRs.
>
> * Updated Dangerfile "policy_missing_master_permissions?" test to ignore policy templates with `skip_permissions: "true"` in their info block for policy templates with unusual permissions that won't properly scrape or other extenuating reasons we might not want to scape them for permissions.
>
> * Updated Dangerfile "policy_bad_block_name?" test to work when the block name is in single quotes instead of double quotes. Previously, the test would fail to capture a bad block name in this situation.
>
> * Added new Dangerfile "policy_block_name_single_quotes?" test to check if block names are in single quotes instead of double quotes.
>
> * Added new Dangerfile "policy_defunct_metadata?" test to check if defunct metadata fields such as tenancy are used.
>
> * Added new Dangerfile "policy_abbreviated_info_field?" test to ensure consistent naming of info() fields and to avoid abbreviations like CCO, MSP, etc.
>
> * Added new Dangerfile "policy_missing_info_block?" test to report when the info() block is missing entirely. Stolen shamelessly from Bryan.
>
> * Updated existing policy templates so that they will pass the above tests. Also changed these policy templates to pass existing tests as warnings and errors arose from modifying them.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3017) for these details.
- **Merged At**: 2025-03-28 12:29:47 UTC

---

### PR [#2966](https://github.com/flexera-public/policy_templates/pull/2966): POL-1456 Azure/Google Credential Testing Policy Templates

*New Policy Template*

#### Description

> This adds two new unpublished policy templates to test credentials for Azure and Google. A modified meta parent is used for each to ensure that an incident is still raised even if the credential fails in a way that prevents policy template execution from completing. More detail is in the README and META_README files for each policy template.
>
> Also fixes a minor bug in the AWS policy template and makes some minor changes to the docs for that policy template to conform to the two new policy templates added here.
>
> Note: Dead link warnings can be ignored. Those links won't be dead once this PR is merged.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2966) for these details.
- **Merged At**: 2025-03-27 12:10:18 UTC

---

### PR [#3014](https://github.com/flexera-public/policy_templates/pull/3014): POL-1468  Bug/fixing retired status in results ITAM Expiring Licenses

#### Description

> Fixed issue with retired status not being filtered out of the results
>
> ### Issues Resolved
>
> Fixed issue with retired status not being filtered out of the results
>

#### Metadata

- **Policies**: [ITAM Expiring Licenses](https://github.com/flexera-public/policy_templates/tree/master/compliance/flexera/fnms/fnms_licenses_expiring/README.md)
- **Merged At**: 2025-03-26 17:31:52 UTC

---

### PR [#3005](https://github.com/flexera-public/policy_templates/pull/3005): FOPTS-6901 - Batch Processing Adoption for AWS Rightsize EBS Volumes

#### Description

> <!-- Describe what this change achieves below -->
>
> This represents the last step in enabling Batch Processing for prioritized policies. The selected policies are the ones with the highest overall and cross-organizational usage, as well as those consuming the most memory.
>
> In this PR, AWS Rightsize EBS Volumes has been refactored to leverage Batch Processing. Specifically, the datasource operations that involve large datasets have been optimized to use EFS (Elastic File System) instead of in-memory processing. This change ensures that **memory usage is reduced** while **maintaining** or improving **execution times**
>
> ### Issues Resolved
>
> Please check the policies and applied policy links here:
> https://flexera.atlassian.net/browse/FOPTS-7713?focusedCommentId=2717833
>
> [Grafana link](https://g-1cda041840.grafana-workspace.us-east-1.amazonaws.com/d/6r9N9ysIk/evaluation-service-usage?orgId=1&var-dataSource=Prometheus%20Prod%20US&var-pod=All&viewPanel=2&from=1741647410214&to=1741649609883)
>
> ![image](https://github.com/user-attachments/assets/7903ca7d-6ea5-47ad-9c92-025870a9bebe)
>
>
>
>

#### Metadata

- **Policies**: [AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/README.md), [Meta Parent: AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/README.md)
- **Merged At**: 2025-03-24 16:39:39 UTC

---

### PR [#3006](https://github.com/flexera-public/policy_templates/pull/3006): SQ-12222 Fixed incorrect calculation for "average used memory"

#### Description

> Fixed incorrect calculation for "average used memory".
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-12222
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md), [Meta Parent: Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2025-03-20 18:47:56 UTC

---

### PR [#3003](https://github.com/flexera-public/policy_templates/pull/3003): POL-1464 Meta Policy Fix

#### Description

> This is a fix for the meta policy script that prevents the generated meta policy from containing consolidated incidents out of child policy incidents that don't have an export table. 3 malfunctioning meta policies generated by the old version of the script are also being updated using this fixed version of the script.

#### Metadata

- **Policies**: [Meta Parent: AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Meta Parent: Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md), [Meta Parent: Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2025-03-18 18:57:26 UTC

---

### PR [#2996](https://github.com/flexera-public/policy_templates/pull/2996): FOPTS-8007 Fixed OAuth authentication for `Common Bill Ingestion from Azure Blob Storage` policy

#### Description

> Fixed OAuth2 authentication for `Common Bill Ingestion from Azure Blob Storage` policy.
>
> This is caused by the request missing `x-ms-version` header.
> (See section "**Requests that use an OAuth 2.0 token from Microsoft Entra**" in Microsoft documentation [Versioning for Azure Storage](https://learn.microsoft.com/en-us/rest/api/storageservices/versioning-for-the-azure-storage-services#specify-service-versions-in-requests))
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-8007
> https://flexera.atlassian.net/browse/SQ-13259
>

#### Metadata

- **Policies**: [Common Bill Ingestion from Azure Blob Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cbi_ingestion_azure_blob/README.md)
- **Merged At**: 2025-03-14 22:12:33 UTC

---

### PR [#2990](https://github.com/flexera-public/policy_templates/pull/2990): POL-1460 New Policy: Azure Overutilized Compute Instances

*New Policy Template*

#### Description

> This adds a new policy template to the catalog, Azure Overutilized Compute Instances, that reports instances above a certain threshold of CPU and/or memory usage.
>

#### Metadata

- **Policies**: [Azure Overutilized Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/overutilized_compute_instances/README.md), [Meta Parent: Azure Overutilized Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/overutilized_compute_instances/README.md)
- **Merged At**: 2025-03-13 17:30:30 UTC

---

### PR [#2950](https://github.com/flexera-public/policy_templates/pull/2950): POL-1448 New Policy: FinOps Dashboards

*New Policy Template*

#### Description

> This policy template creates a series of FinOps cloud dashboards within the Flexera organization. Created dashboards are public and can be accessed at the Dashboards -> Cloud page in Flexera One. Optionally, information about the newly created dashboards can be emailed.
>
> Configuration information for these dashboards is stored in separate JSON files located at `data/dashboards/`
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2950) for these details.
- **Merged At**: 2025-03-11 17:09:10 UTC

---

### PR [#2976](https://github.com/flexera-public/policy_templates/pull/2976): FOPTS-7572 Fixed memory stats showing decimal instead of percentage | Policy: Azure Rightsize Compute Instances

#### Description

> Memory stats were showing decimal numbers (such as `0.5` for half), instead of showing percentage (such as `50` for half).
> Showing `50` for half and `100` for all is the expected behavior.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/SQ-12222
> - https://flexera.atlassian.net/browse/FOPTS-7572
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2025-03-06 14:05:52 UTC

---

### PR [#2965](https://github.com/flexera-public/policy_templates/pull/2965): FOPTS-6833 - Batch Processing Adoption for Azure RightSize Policies

#### Description

> This represents the second step in enabling Batch Processing for prioritized policies. The selected policies are the ones with the highest overall and cross-organizational usage, as well as those consuming the most memory.
>
> In this PR, the identified policies have been refactored to leverage Batch Processing. Specifically, the datasource operations that involve large datasets have been optimized to use EFS (Elastic File System) instead of in-memory processing. This change ensures that **memory usage is reduced** while **maintaining** or improving **execution times**
>
> - [x] Azure Rightsize SQL Databases
> - [x] Azure Rightsize Manage Disk
> - [x] Azure Rightsize  Database SQL Storage
> - Note : excluded Azure Rightsize Compute Instance  as the refactored version (enable batch processing) result in considerable increase in execution time)
>
> For each policy these steps got taken :
> -  **Investigate Memory and Time Usage** : Analyze the memory and execution time of data sources in to identify bottlenecks.
> - **Enable Batch Processing**: Refactor the identified data sources to use batch processing.
> - **Test Consistency**: Run both the original and batch-enabled versions on staging data to ensure error-free execution and consistent results across both.
> - **Create Mock Policies**: Generate mock versions of both the original and batch-enabled policies to simulate real-world use cases.
> - **Performance Analysis**: Verified that the changes effectively reduce memory usage without significantly increasing execution time.
>
>
>
> ### Issues Resolved
>
> Please check the policies and applied policy links here:
> https://flexera.atlassian.net/browse/FOPTS-7713?focusedCommentId=2717833
>
> [Grafana link](https://g-1cda041840.grafana-workspace.us-east-1.amazonaws.com/d/6r9N9ysIk/evaluation-service-usage?orgId=1&var-dataSource=Prometheus%20Prod%20US&var-pod=All&viewPanel=2&from=1741647410214&to=1741649609883)
>
> ![image](https://github.com/user-attachments/assets/7903ca7d-6ea5-47ad-9c92-025870a9bebe)
>
>
>
>
> Grafana Reference:
>
> [Azure Rightsize SQL Databases](https://g-1cda041840.grafana-workspace.us-east-1.amazonaws.com/d/6r9N9ysIk/evaluation-service-usage?orgId=1&var-dataSource=Prometheus%20Staging&var-pod=All&viewPanel=2&from=1740429756026&to=1740430085811)
>
> ![image](https://github.com/user-attachments/assets/1d0eb87c-0c0f-4f4f-a42f-c0c73a255c89)
>
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2965) for these details.
- **Merged At**: 2025-03-05 22:22:54 UTC

---

### PR [#2957](https://github.com/flexera-public/policy_templates/pull/2957): FOPTS-7277 Excluded fields to avoid sent email each execution

#### Description

> The client has been receiving error notification emails about invoice processing approximately 3 to 4 times per hour. Additionally, the client mentioned that this issue is impacting their ability to manage invoices efficiently and has requested a solution to reduce the frequency of these error notifications, as they are unnecessary and do not add value to resolving the billing issues.
>
> ### Issues Resolved
>
> We are including 'hash_exclude ` "created_at"`,`"updated_at"` to ensure that changes to these fields do not trigger an email notification unless a significant modification occurs. At the same time, we are adding `result = _.sortBy(result, 'created_at')` to ensure that the collection is ordered by 'created_at'. Without sorting, the collection may arrive in a different order, which could unnecessarily trigger a new email notification even when the "incident" contains the same information but in a different sequence.
>
>

#### Metadata

- **Policies**: [Cloud Bill Processing Error Notification](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/bill_processing_errors_notification/README.md)
- **Merged At**: 2025-03-05 22:21:17 UTC

---

### PR [#2967](https://github.com/flexera-public/policy_templates/pull/2967): FOPTS-7572 Changed the way to calculate used memory | Policy: Azure Rightsize Compute Instances

#### Description

> This PR changed the way to calculate "used memory" for Azure instances.
> Previously the policy is trying to compute "used memory" by substracting "available memory" from "total memory".
> This PR has changed to directly retrieving "available memory" from Azure metrics.
>
> The previous method had flawed if the "total memory" is changed due to instance resizing.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/SQ-12222
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2025-03-04 22:56:01 UTC

---

### PR [#2942](https://github.com/flexera-public/policy_templates/pull/2942): FOPTS-6829 - Batch Proccessing Adoption for AWS Tag Cardinality Report Policy

#### Description

> This PR represents the first step in enabling Batch Processing for prioritized policies—those with the highest overall and cross-organizational usage, as well as those consuming the most memory.
>
> In this update, the `AWS Tag Cardinality Report` policy has been refactored to implement batch processing for data sources that handle large datasets.
>
>
> ### Issues Resolved
>
> Related Task : https://flexera.atlassian.net/browse/FOPTS-6829
> Epic : https://flexera.atlassian.net/browse/FOPTS-6341
>

#### Metadata

- **Policies**: [AWS Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/tag_cardinality/README.md), [Meta Parent: AWS Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/tag_cardinality/README.md)
- **Merged At**: 2025-02-20 20:54:30 UTC

---

### PR [#2955](https://github.com/flexera-public/policy_templates/pull/2955): POL-1451 Add sys- and app- Project Filtering to Google Policy Templates

#### Description

> Adds two new parameters to most Google policy templates to enable easy filtering of sys- and app- projects. This can help in situations where a user has thousands of these projects and no need for them to be checked for recommendations.
>
> - "sys-*" projects generally refer to system-generated projects that are automatically created for internal Google services and management functions in google sheets
>
> - "app-*" projects typically refer to projects associated with Google Apps Script
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2955) for these details.
- **Merged At**: 2025-02-13 13:02:48 UTC

---

### PR [#2932](https://github.com/flexera-public/policy_templates/pull/2932): FOPTS-6822 Enhance "Cloud Bill Processing Error Notification" Policy to Report Connections with Zero Imported Bills

#### Description

> Added a new parameter (disable by default) to report connections with no bills. This is asked by one of the customers (Accenture) as they want to be able to identify misconfigured bill connection.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-12286
>

#### Metadata

- **Policies**: [Cloud Bill Processing Error Notification](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/bill_processing_errors_notification/README.md)
- **Merged At**: 2025-02-03 19:43:17 UTC

---

### PR [#2928](https://github.com/flexera-public/policy_templates/pull/2928): FOPTS-6730 Fix negative memory statistics for recently rightsized resources | Policy: Azure Rightsize Compute Instances

#### Description

> This change skips memory recommendations when data from recently rightsized instances gets mixed with current data making negative values for memory usage.
>
> Here's a much more detailed explanation of the problem: https://flexera.atlassian.net/browse/SQ-12222?focusedCommentId=2672680
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/SQ-12222
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2025-01-27 15:35:43 UTC

---

### PR [#2920](https://github.com/flexera-public/policy_templates/pull/2920): FOPTS-6034 Make Azure New Marketplace Products Policy Support MSP Configurations

#### Description

> We changed the method used to obtain the bill connections, now instead of calling the bill-connects API we fetch cost data and get the bill connections from there, this change is required since MSP customers have a different way of configuring their bill connects, and that method would make the policy fail.
>
> This also adds support for MCA connections.
>
> Code change used here is based on already tested code for policy template **Azure Savings Realized from Reservations**.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/FOPTS-6315 (Refactor  Azure New Marketplace Products policy)
>

#### Metadata

- **Policies**: [Azure New Marketplace Products](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/marketplace_new_products/README.md)
- **Merged At**: 2025-01-27 15:33:40 UTC

---

### PR [#2911](https://github.com/flexera-public/policy_templates/pull/2911): POL-1441 ITAM Reporting Policies

#### Description

> This creates 3 new policy templates for ITAM to report on asset, licenses, and installed applications. All are fairly simple but can serve both as basic reporting policies and as a springboard for more sophisticated ITAM policies down the road.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2911) for these details.
- **Merged At**: 2025-01-23 13:28:22 UTC

---

### PR [#2921](https://github.com/flexera-public/policy_templates/pull/2921): FOPTS-6693 Fix conversion issue that stops policy execution

#### Description

> This fixes a problem when the ds_currency_conversion is an empty list, causing the policy to terminate.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/SQ-12110 (Support Case 02978642 - Issue with Meta Policy - AWS Superseded volumes)
>

#### Metadata

- **Policies**: [AWS Superseded EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_ebs_volumes/README.md)
- **Merged At**: 2025-01-10 21:38:45 UTC

---

### PR [#2916](https://github.com/flexera-public/policy_templates/pull/2916): POL-1443 AWS Rightsize Elasticache - Fix undeclared variable causing policy to fail

#### Description

> <!-- Describe what this change achieves below -->
> This change rearranges the code so that the `savings` variable is no longer being referenced before it is declared/defined, meaning the policy no longer fails when it is run.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Fixed an issue with the `savings` variable causing the policy to fail.
>

#### Metadata

- **Policies**: [AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md), [Meta Parent: AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md)
- **Merged At**: 2025-01-08 14:07:17 UTC

---

### PR [#2892](https://github.com/flexera-public/policy_templates/pull/2892): POL-1433 Use Flexera CCO Costs for Azure Rightsize Managed Disks

#### Description

> This updates the Azure Rightsize Managed Disks policy template to use Flexera CCO to obtain costs for managed disks. Calculations of savings now incorporate this to give more accurate estimates. From the CHANGELOG:
>
> - Savings are now calculated using cost data stored in Flexera Cloud Cost Optimization instead of only via Azure list price.
> - Currency conversion functionality has been removed. It is no longer needed due to actual cost data stored in Flexera Cloud Cost Optimization being used to assess cost and savings.
>
> From the README:
>
> The `Estimated Monthly Savings` is calculated via the following:
>
> - The `monthly list price` of the current disk type obtained via the Azure Pricing API.
> - The `real monthly cost of the disk` is calculated by multiplying the amortized cost of the disk for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
> - The percentage difference between the two is calculated by dividing the `real monthly cost of the disk` by the `monthly list price` of the current disk type.
> - The `monthly list price of the new disk type` is multiplied by the above percentage to get an `estimated real monthly cost of the new disk` type under the assumption that any discounts or other changes from list price that applied to the old disk type will also apply to the new one.
> - The savings is then calculated by subtracting the `estimated real monthly cost of the new disk type` from the `real monthly cost of the disk`.
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2025-01-07 14:35:14 UTC

---

### PR [#2907](https://github.com/flexera-public/policy_templates/pull/2907): POL-1440 Flexera FOCUS Report Bug Fix

#### Description

> This fixes an issue in the `Flexera FOCUS Report` policy template where the policy would fail when reporting unamortized costs.
>

#### Metadata

- **Policies**: [Flexera FOCUS Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/focus_report/README.md)
- **Merged At**: 2025-01-02 13:32:31 UTC

---

### PR [#2896](https://github.com/flexera-public/policy_templates/pull/2896): POL-1434 Scheduled Report for Unallocated Costs "7 Days" Fix

#### Description

> From the `Scheduled Report for Unallocated Costs` CHANGELOG:
> - Fixed issue that would cause policy template to fail when "Last 7 Days" was selected for the "Date Range" parameter.
> - "Dimensions List" parameter now accepts both dimension names and dimension IDs as valid inputs.
> - Markdown tables in incident now uses pretty names for various fields to improve readability.
>

#### Metadata

- **Policies**: [Scheduled Report for Unallocated Costs](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_report_unallocated/README.md)
- **Merged At**: 2025-01-02 13:32:12 UTC

---

### PR [#2887](https://github.com/flexera-public/policy_templates/pull/2887): FLEX-5165 Add datalake optimization policy template

*New Policy Template*

#### Description

> Initial implementation of a Policy (Azure Data Lake Optimization) which enables customers to run efficiently for Azure Data Lake. The policy type is Usage Reduction and provide the recommendations with Potential savings.
>
> ### Issues Resolved
> https://flexera.atlassian.net/browse/FLEX-5165
>

#### Metadata

- **Policies**: [Azure Data Lake Optimization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/data_lake_optimization/README.md), [Meta Parent: Azure Data Lake Optimization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/data_lake_optimization/README.md)
- **Merged At**: 2024-12-23 18:30:07 UTC

---

### PR [#2833](https://github.com/flexera-public/policy_templates/pull/2833): POL-1405 Replace deprecated Kubecost endpoints for Kubecost Cluster Policy

#### Description

> The endpoint we are currently using has been deprecated “/model/savings/clusterSizing"
> It still works but only returns one cluster rather than all clusters.
>
> The new endpoint is returns a different response “/model/savings/clusterSizingETL" and simply adding ETL onto the end of our current end point in the policy returns null values in ds_cluster_sizing
>
> This endpoint returns all cluster recommendations in one response.
>
>
> The `ds_clusters` function has been created  to include two new parameters in the Kubecost API call:
>
> * param_allow_shared_core: This boolean parameter indicates whether shared cores should be allowed in the cluster sizing calculation. By default, Kubecost may not consider the shared cores between pods as part of the cost savings calculations. With this new parameter, the explicit inclusion of shared cores in the calculations can be enabled. This is useful for environments where resources are shared between multiple pods, and a more accurate estimate of potential savings is desired.
>
>
>
> #### Changes Made:
>
> * Updated the function responsible for the API call to /model/savings/clusterSizing
> * Added the param_allow_shared_core to the `ds_clusters` function.
> * Updated the HTTP call to send these parameters in the Request.
> * Set the default values of these parameters to False, meaning shared cores will not be allowed.
>
> > How the response for the new endpoint differs from what we initially wanted: we modified it and added new functions to handle the response and convert it to the expected struct
>
> ### Issues Resolved
>
> - Deprecated endpoint from kubecost was replaced.
> - https://flexera.atlassian.net/browse/POL-1405
>

#### Metadata

- **Policies**: [Kubecost Cluster Rightsizing Recommendation](https://github.com/flexera-public/policy_templates/tree/master/cost/kubecost/cluster/README.md)
- **Merged At**: 2024-12-19 15:58:27 UTC

---

### PR [#2869](https://github.com/flexera-public/policy_templates/pull/2869): POL-1414 Currency Conversion Functionality on Kubecost cluster rightsizing policy

#### Description

> This update introduces functionality to handle automatic currency conversion within Kubecost cluster rightsizing policy, ensuring that incidents reflect values across different currencies.
>
> #### Changes
>
> * Support for multiple currencies has been added to the system.
> * If the kubecost config endpoint returns an empty currency, USD (United States Dollar) will be used as the default currency.
> * A condition has been implemented where, if Kubecost's currency matches Flexera's, no currency conversion will take place.
>
> ### Issues Resolved
>
> Resolves the issue where currency discrepancies occurred between our template and Kubecost when they had different base currencies.
>
>
> https://flexera.atlassian.net/browse/POL-1414
>

#### Metadata

- **Policies**: [Kubecost Cluster Rightsizing Recommendation](https://github.com/flexera-public/policy_templates/tree/master/cost/kubecost/cluster/README.md)
- **Merged At**: 2024-12-16 22:02:52 UTC

---

### PR [#2817](https://github.com/flexera-public/policy_templates/pull/2817): POL-1410 - Improve Scheduled Instance Notifications

#### Description

> Improved notifications related for the 3 Scheduled Instance Policy Templates
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1410
>

#### Metadata

- **Policies**: [AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md), [Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2024-12-11 19:42:39 UTC

---

### PR [#2876](https://github.com/flexera-public/policy_templates/pull/2876): POL-1428 Scheduled Report - fix +Inf issue related to incident creation

#### Description

> <!-- Describe what this change achieves below -->
> This change implements a fix for the Scheduled Report policy incident so that it is successfully created when the `Billing Term` parameter is set to `Week`.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> This PR resolves an issue where the Scheduled Report policy incident failed to generate due to a `+Inf` error.
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2024-12-11 18:02:09 UTC

---

### PR [#2873](https://github.com/flexera-public/policy_templates/pull/2873): POL-1424 New CBI Bill Ingestion Policies

#### Description

> This creates two new policy templates for the catalog: `Common Bill Ingestion from AWS S3 Object Storage` and `Common Bill Ingestion from Azure Blob Storage`. These policies can automate the ingestion of either CBI or FOCUS formatted CSV files into Common Bill Ingestion from S3 Object Storage and Blob Storage respectively.
>
> Additionally, the functionality in the above policies to abort existing bill uploads prior to creating a new one has been added to the `Fixed Cost Common Bill Ingestion` policy template.
>
> Note: Some tweaks were also made to Dangerfile tests to properly account for Azure storage credentials. Some tweaks were also made to a small number of README files to correctly indicate specific permissions for Azure storage credentials.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2873) for these details.
- **Merged At**: 2024-12-11 14:28:50 UTC

---

### PR [#2867](https://github.com/flexera-public/policy_templates/pull/2867): POL-1422 Fix AWS New Marketplace Products

#### Description

> AWS New Marketplace Products has an issue that was introduced during a mass code change that prevents the policy from completing execution. This fixes that issue.
>

#### Metadata

- **Policies**: [AWS New Marketplace Products](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/marketplace_new_products/README.md)
- **Merged At**: 2024-12-02 14:09:36 UTC

---

### PR [#2862](https://github.com/flexera-public/policy_templates/pull/2862): POL-1415 AWS Rightsize RDS Instances: Add Connections to Incident Table

#### Description

> This adds a daily average of connections to the RDS instance, labelled `Connections (Daily)`, to the incident table for both the idle and underutilized incidents.
>
> (This also includes some minor code refactoring to make similar changes in the future easier)
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md), [Meta Parent: AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2024-12-02 13:08:57 UTC

---

### PR [#2859](https://github.com/flexera-public/policy_templates/pull/2859): POL-1419 Bug Fix for Azure Publicly-Accessible Blob Containers 

#### Description

> This fixes a bug in the Azure Publicly-Accessible Blob Containers policy template caused by an incorrectly named variable in a JavaScript block.

#### Metadata

- **Policies**: [Azure Publicly-Accessible Blob Containers](https://github.com/flexera-public/policy_templates/tree/master/security/azure/private_blob_containers/README.md), [Meta Parent: Azure Publicly-Accessible Blob Containers](https://github.com/flexera-public/policy_templates/tree/master/security/azure/private_blob_containers/README.md)
- **Merged At**: 2024-11-26 18:56:50 UTC

---

### PR [#2847](https://github.com/flexera-public/policy_templates/pull/2847): FOPTS-5666 Handle properly null values in Google Rightsize VM Recommender Policy

#### Description

> We had an issue sorting recommendations when cpuAvergae. cpuMinimum or cpuMaximum are nulls.
>
> ### Issues Resolved
>
> [FOPTS-5666](https://flexera.atlassian.net/browse/FOPTS-5666)
> [SQ-10199](https://flexera.atlassian.net/browse/SQ-10199)
>

#### Metadata

- **Policies**: [Google Rightsize VM Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_recommendations/README.md), [Meta Parent: Google Rightsize VM Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_recommendations/README.md)
- **Merged At**: 2024-11-26 15:57:50 UTC

---

### PR [#2837](https://github.com/flexera-public/policy_templates/pull/2837): POL-1417 Azure Savings Realized from Reservations - fix NaN issue related to incident creation

#### Description

> <!-- Describe what this change achieves below -->
> Fixes a bug that produces this error preventing the policy incident from being created for an EU Customer:
> `incident service client: create incident: [Incident create]: failed to encode request body: json: unsupported value: NaN`
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Fixes a bug that produces this error preventing the policy incident from being created for an EU Customer:
> `incident service client: create incident: [Incident create]: failed to encode request body: json: unsupported value: NaN`
>

#### Metadata

- **Policies**: [Azure Savings Realized from Reservations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_realized/README.md)
- **Merged At**: 2024-11-22 13:32:40 UTC

---

### PR [#2841](https://github.com/flexera-public/policy_templates/pull/2841): POL-1416 New Policy: AWS S3 Incomplete Multi-Part Uploads

*New Policy Template*

#### Description

> New policy template `AWS S3 Incomplete Multi-Part Uploads` that reports incomplete S3 multi-part uploads.
>

#### Metadata

- **Policies**: [AWS S3 Incomplete Multi-Part Uploads](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_multipart_uploads/README.md), [Meta Parent: AWS S3 Incomplete Multi-Part Uploads](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_multipart_uploads/README.md)
- **Merged At**: 2024-11-22 13:28:09 UTC

---

### PR [#2722](https://github.com/flexera-public/policy_templates/pull/2722): FOPTS-5124 Added batch processing for some Policies with high memory consumption

#### Description

> Added batch processing in AWS Object Storage Optimization, Azure Databricks Rightsize Compute Instances and Azure Reserved Instance Recommendations Policies
>
>
> Following the release of batch processing for all organizations, it was decided to modify the templates with the highest memory consumption to make use of batch processing. These policies are:
> - Azure Databricks Rightsize Compute Instances
> - Azure Reserved Instance Recommendations
>
> NOTE: For AWS Object Storage Optimization, I think there was a mistake in the parameters to run script
> _$js_aws_s3_objects_with_storage_class_. It was using _$ds_aws_list_s3_objects_ but I think it should use, _$ds_aws_s3_objects_ because it is the data source that has the objects filtered by tags if we use that param, and _$ds_aws_s3_objects_  was not being used by any other datasource. I changed the data source used as input, but let me know if it was correct
>
> ### Issues Resolved
>
> [FOPTS-5124](https://flexera.atlassian.net/browse/FOPTS-5124)
>

#### Metadata

- **Policies**: [Azure Databricks Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/databricks/rightsize_compute/README.md), [Meta Parent: Azure Databricks Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/databricks/rightsize_compute/README.md), [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md), [Meta Parent: Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md)
- **Merged At**: 2024-11-21 17:03:20 UTC

---

### PR [#2830](https://github.com/flexera-public/policy_templates/pull/2830): FOPTS-5507  Added hide_skip_approvals to All Active Policies

#### Description

> This PR marks the last update for the Hide Skip Approval [task](https://flexera.atlassian.net/browse/FLEX-5397).
> ✅ The first phase, updating AWS Right Size policies, is complete in [PR-2799](https://github.com/flexera-public/policy_templates/pull/2799).
> ✅ Additionally, the metaparent policy compiler and Rakefile have been successfully updated : [PR-2813](https://github.com/flexera-public/policy_templates/pull/2813)
>
> Current Phase (Phase 2):
> In this phase, we have added the hide_skip_approvals field to the info section of policy templates that do not use the request approval option in any escalation. This field allows the UI to dynamically show or hide the "Skip Approval" option based on the policy’s configuration. Following the AWS Right Size policy updates, these changes have now been applied to **all remaining active policies.**
>
> More context:[ Seeking Your Input: Proposed Solution for Conditional "Skip Approvals" Visibility](https://teams.microsoft.com/l/message/19:833373548e104af2a20b0216eda1ba7b@thread.skype/1728495063426?tenantId=91034d23-0b63-4943-b138-367d4dfac252&groupId=fb250818-e040-4a26-b207-61c3cd99fd6e&parentMessageId=1728495063426&teamName=Team%20Flexera%20One&channelName=Policy%20Support%20and%20Questions&createdTime=1728495063426)
>
> ### Issues Resolved
>
>
> [FLEX-5397](https://flexera.atlassian.net/browse/FLEX-5397)
>
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2830) for these details.
- **Merged At**: 2024-11-14 19:54:59 UTC

---

### PR [#2829](https://github.com/flexera-public/policy_templates/pull/2829): FOPTS-5505 Fixed consumption calculation for ITAM Overused Licenses

#### Description

> An issue with consumption percentage calculation was fixed.
>
> ### Issues Resolved
>
> [SQ-11024](https://flexera.atlassian.net/browse/SQ-11024)
> [FOPTS-5505](https://flexera.atlassian.net/browse/FOPTS-5505)
>

#### Metadata

- **Policies**: [ITAM Overused Licenses](https://github.com/flexera-public/policy_templates/tree/master/compliance/flexera/fnms/overused_licenses/README.md)
- **Merged At**: 2024-11-14 16:49:56 UTC

---

### PR [#2818](https://github.com/flexera-public/policy_templates/pull/2818): POL-1413 Currency Separator Fix

#### Description

> This fixes the commonly-used formatNumber function present in many policy templates to ensure that it does not end up inserting the text "undefined" where comma separators are supposed to go.
>
> (Warnings/errors are false positives unrelated to the specific change being made with this PR)
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2818) for these details.
- **Merged At**: 2024-11-11 18:09:26 UTC

---

### PR [#2813](https://github.com/flexera-public/policy_templates/pull/2813): FLEX-5397 - Modify Meta Parent Compiler to Conditionally Include `hide_skip_approvals`

#### Description

> This pull request enhances the Meta Parent Policy Template Compiler to conditionally include the hide_skip_approvals field in the generated meta parent policy templates when it exists in the child policy templates.
> It also removes prior manual modifications to meta parent policies : https://github.com/flexera-public/policy_templates/pull/2799
>
> More context:[ Seeking Your Input: Proposed Solution for Conditional "Skip Approvals" Visibility](https://teams.microsoft.com/l/message/19:833373548e104af2a20b0216eda1ba7b@thread.skype/1728495063426?tenantId=91034d23-0b63-4943-b138-367d4dfac252&groupId=fb250818-e040-4a26-b207-61c3cd99fd6e&parentMessageId=1728495063426&teamName=Team%20Flexera%20One&channelName=Policy%20Support%20and%20Questions&createdTime=1728495063426)
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>
> [FLEX-5397](https://flexera.atlassian.net/browse/FLEX-5397)
>
>
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
>

#### Metadata

- **Policies**: [Meta Parent: AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/README.md), [Meta Parent: AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md), [Meta Parent: AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md), [Meta Parent: AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md), [Meta Parent: AWS Rightsize Redshift](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_redshift/README.md)
- **Merged At**: 2024-11-08 19:46:42 UTC

---

### PR [#2808](https://github.com/flexera-public/policy_templates/pull/2808): POL-1402 Azure Rightsizing Compute: Consider Managed Disk

#### Description

> This updates the `Azure Rightsize Compute Instances` policy template so that it never recommends a downsize to a size that wouldn't support the current number of attached disks for an instance.
>
> The [Virtual Machine Sizes - List](https://learn.microsoft.com/en-us/rest/api/compute/virtual-machine-sizes/list?view=rest-compute-2024-07-01&tabs=HTTP) API call is used during policy execution to get a list of resource types and the maximum number of attached disks. The policy template has been given a major version change since the above API call requires an additional permission.
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md), [Meta Parent: Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2024-11-07 13:07:23 UTC

---

### PR [#2799](https://github.com/flexera-public/policy_templates/pull/2799): FOPTS-4819 Added `hide_skip_approvals` to AWS Right Size policies

#### Description

> Adding a new hide_skip_approvals field to the info section of policy templates that do not utilize the request approval option in any escalation. This field enables the UI to dynamically show or hide the "Skip Approval" option based on the policy configuration. Initially, these changes are applied to AWS Right Size policies, with plans to update additional policies in subsequent steps.
>
> More context:[ Seeking Your Input: Proposed Solution for Conditional "Skip Approvals" Visibility](https://teams.microsoft.com/l/message/19:833373548e104af2a20b0216eda1ba7b@thread.skype/1728495063426?tenantId=91034d23-0b63-4943-b138-367d4dfac252&groupId=fb250818-e040-4a26-b207-61c3cd99fd6e&parentMessageId=1728495063426&teamName=Team%20Flexera%20One&channelName=Policy%20Support%20and%20Questions&createdTime=1728495063426)
>
> ### Issues Resolved
>
> [FLEX-5397](https://flexera.atlassian.net/browse/FLEX-5397)
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2799) for these details.
- **Merged At**: 2024-11-05 22:00:13 UTC

---

### PR [#2802](https://github.com/flexera-public/policy_templates/pull/2802): POL-1397 Flexera One API Event Report

#### Description

> This is a new policy template that reports API requests made to the Flexera API with several filtering options.
>

#### Metadata

- **Policies**: [Flexera One API Event Report](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/iam/api_event_report/README.md)
- **Merged At**: 2024-11-04 13:12:12 UTC

---

### PR [#2800](https://github.com/flexera-public/policy_templates/pull/2800): POL-1408 AWS Account Credentials Meta Not Spawning Children

#### Description

> Fixes issue where the meta policy for AWS Account Credentials was not spawning children due to the policy not properly filtering out meta-specific parameters.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2800) for details about unpublished policies.
- **Merged At**: 2024-10-31 17:48:14 UTC

---

### PR [#2737](https://github.com/flexera-public/policy_templates/pull/2737): POL-1378 Linting Updates: Cost Policies: Misc

#### Description

> Various small changes to Cost policies not associated with the big 3 hyperscalers to bring them up to current linting standards. Also removes known bad coding patterns to avoid their reuse.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2737) for these details.
- **Merged At**: 2024-10-30 14:58:32 UTC

---

### PR [#2790](https://github.com/flexera-public/policy_templates/pull/2790): POL-1394 Downsize Multiple Sizes: Azure MySQL

#### Description

> Added support for downsizing multiple sizes where appropriate for the two Azure MySQL policy templates. Enabled via an optional parameter.
>

#### Metadata

- **Policies**: [Azure Rightsize MySQL Flexible Servers](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_mysql_flexible/README.md), [Meta Parent: Azure Rightsize MySQL Flexible Servers](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_mysql_flexible/README.md), [Azure Rightsize MySQL Single Servers](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_mysql_single/README.md), [Meta Parent: Azure Rightsize MySQL Single Servers](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_mysql_single/README.md)
- **Merged At**: 2024-10-30 12:04:39 UTC

---

### PR [#2792](https://github.com/flexera-public/policy_templates/pull/2792): POL-1407 Downsize Multiple Sizes: AWS Rightsize ElastiCache

#### Description

> Added support for downsizing multiple sizes where appropriate. Enabled via an optional parameter.
>

#### Metadata

- **Policies**: [AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md), [Meta Parent: AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md)
- **Merged At**: 2024-10-30 12:04:16 UTC

---

### PR [#2789](https://github.com/flexera-public/policy_templates/pull/2789): POL-1396 Downsize Multiple Sizes: Azure Rightsize SQL Managed Instances

#### Description

> Added support for downsizing multiple sizes where appropriate. Enabled via an optional parameter.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md), [Meta Parent: Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md)
- **Merged At**: 2024-10-29 12:11:49 UTC

---

### PR [#2788](https://github.com/flexera-public/policy_templates/pull/2788): POL-1393 Downsize Multiple Sizes: Azure Rightsize SQL Databases

#### Description

> Added support for downsizing multiple sizes where appropriate. Enabled via an optional parameter.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md), [Meta Parent: Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2024-10-29 12:11:23 UTC

---

### PR [#2787](https://github.com/flexera-public/policy_templates/pull/2787): POL-1406 AWS Rightsize RDS Instances Fix

#### Description

> Fixes issue where policy would fail if a "db.serverless" (or any other instance type not present in the mapping file) instance was found.
>
> Also makes it so that the policy template does not bother to gather metrics for "db.serverless" instances, since we won't be making recommendations for these regardless, as they are not ordinary RDS instances.
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md), [Meta Parent: AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2024-10-29 12:11:04 UTC

---

