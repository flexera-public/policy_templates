# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#2887](https://github.com/flexera-public/policy_templates/pull/2887): FLEX-5165 Add datalake optimization policy template

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

### PR [#2747](https://github.com/flexera-public/policy_templates/pull/2747): POL-1385 - New Template: Billing Centers from Dimensions

#### Description

> This policy generates a billing center structure based on specified dimensions. It allows users to create a hierarchical billing center structure that reflects their organizational needs by using existing dimensions -- including custom Rule-Based Dimensions, Tag Dimensions, or Cloud Bill Dimensions like Vendor, Cloud Vendor Account Name.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1385
>

#### Metadata

- **Policies**: [Flexera Billing Centers from Dimension Values](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/billing_centers_from_dimensions/README.md)
- **Merged At**: 2024-10-24 19:24:41 UTC

---

### PR [#2777](https://github.com/flexera-public/policy_templates/pull/2777): POL-1404 AWS Superseded EBS Volumes - Fix Currency Conversion Message in Policy Incident

#### Description

> <!-- Describe what this change achieves below -->
> This change fixes a bug in the policy incident of the AWS Superseded EBS Volumes policy in a customer's tenant.
>
> This bug occurs when the customer’s native currency in the platform is not USD:
>
> > “Price and savings values are in USD due to a malfunction with Flexera's internal currency conversion API. Please contact Flexera support to report this issue.”
>
> This message is incorrectly showing even though currency conversion was successful.
>
> This change fixes this bug.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Fixes a bug where the Currency Conversion messaging in the policy incident is incorrectly showing.
>

#### Metadata

- **Policies**: [AWS Superseded EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_ebs_volumes/README.md), [Meta Parent: AWS Superseded EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_ebs_volumes/README.md)
- **Merged At**: 2024-10-24 06:58:29 UTC

---

### PR [#2774](https://github.com/flexera-public/policy_templates/pull/2774): POL-1400 Fix Invalid Recommendations: Azure Rightsize SQL Managed Instances

#### Description

> Azure Rightsize SQL Managed Instances would sometimes produce recommendations for invalid sizes. This is because it was using the existing SQL tier sizes list, and SQL Managed Instances are only available for a much smaller subset of these sizes.
>
> This fixes the issue by creating a separate JSON asset specific to SQL Managed Instances with only the sizes used for that product, and a small modification of the policy template to make use of this new asset.

#### Metadata

- **Policies**: [Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md), [Meta Parent: Azure Rightsize SQL Managed Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql/README.md)
- **Merged At**: 2024-10-22 14:45:54 UTC

---

### PR [#2772](https://github.com/flexera-public/policy_templates/pull/2772): POL-1398 Azure Expiring Certificates - fix Days Until Expiration bug

#### Description

> <!-- Describe what this change achieves below -->
> Regardless of the threshold set, the Azure Expiring Certificates policy returns (in the incident) certificate resources that will expire months and years from now. The reason for this is an incorrect calculation which makes the 'Days Until Expiration' a negative number. This is a change to fix this.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> - 'Days Until Expiration' no longer produces a negative value in the policy incident.
> - Certificate resources outside of the threshold set are no longer returned in the policy incident.
>

#### Metadata

- **Policies**: [Azure Expiring Certificates](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/azure_certificates/README.md), [Meta Parent: Azure Expiring Certificates](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/azure_certificates/README.md)
- **Merged At**: 2024-10-22 14:45:40 UTC

---

### PR [#2763](https://github.com/flexera-public/policy_templates/pull/2763): POL-1392 AWS Rightsize RDS Instances: Downsize Multiple Tiers

#### Description

> Adds option to make recommendations to go down multiple sizes in the `AWS Rightsize RDS Instances` Instances policy template.
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md), [Meta Parent: AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2024-10-21 12:15:34 UTC

---

### PR [#2762](https://github.com/flexera-public/policy_templates/pull/2762): POL-1391 Azure Rightsize Compute Instances: Downsize Multiple Tiers

#### Description

> Adds option to make recommendations to go down multiple sizes in the `Azure Rightsize Compute Instances` policy template.
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md), [Meta Parent: Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2024-10-21 12:15:26 UTC

---

### PR [#2756](https://github.com/flexera-public/policy_templates/pull/2756): POL-1387 New Object Storage Lifecycle Policies / Deprecate Object Storage Optimization Policies

#### Description

> This adds two new policy templates, `AWS S3 Buckets Without Lifecycle Configuration` and `Google Cloud Storage Without Lifecycle Configuration`, to the policy catalog. Additionally, it deprecates the `AWS Object Storage Optimization`, `Azure Blob Storage Optimization`, and `Google Object Storage Optimization` policy templates. The READMEs for these policy templates now direct users to the appropriate lifecycle policy templates instead.
>
> Reason: Due to the scale involved, policy templates that attempt to manage individual objects within object storage buckets are not efficient or, in most cases, even able to run without errors on the Flexera platform. It is bad practice to attempt to micromanage individual objects anyway; users should instead be configuring their cloud environment to automate this via the lifecycle tools all three hyperscalers provide for their object storage solutions. The new policy templates ensure that we have a policy template solution available to users interested in enforcing the usage of lifecycle tools.
>
> (Ignore the dead link warnings. Those links won't be dead once this PR is merged)
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2756) for these details.
- **Merged At**: 2024-10-21 12:15:19 UTC

---

### PR [#2759](https://github.com/flexera-public/policy_templates/pull/2759): POL-1390 AWS Rightsize EC2 Instances: Downsize Multiple Tiers

#### Description

> Adds option to make recommendations to go down multiple sizes in the `AWS Rightsize EC2 Instances` policy template.
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md), [Meta Parent: AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md)
- **Merged At**: 2024-10-21 12:04:19 UTC

---

### PR [#2745](https://github.com/flexera-public/policy_templates/pull/2745): POL-1383 New Policy: Google Missing Projects

#### Description

> New policy template, `Google Missing Projects`, that mirrors the `Azure Missing Subscriptions` policy template. From the README:
>
> This policy template checks the stored Flexera CCO billing data for Google from 3 days ago to obtain a list of Google Projects that we have billing data for and compares that to the list of Google Projects returned by the Google Cloud Resource Manager API. An incident is raised and email sent containing any projects present in Flexera CCO but not returned by the Google Cloud Resource Manager API, as well as projects returned by the Google Cloud Resource Manager API but not present in Flexera CCO. The user can select which of those two reports they'd like to produce.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2745) for details about unpublished policies.
- **Merged At**: 2024-10-16 17:15:30 UTC

---

### PR [#2738](https://github.com/flexera-public/policy_templates/pull/2738): POL-1380 Applied Policy Template Errors: Child Policy Support

#### Description

> This adds optional support for reporting child policy errors as a separate incident in the `Applied Policy Template Errors` policy template.
>

#### Metadata

- **Policies**: [Applied Policy Template Errors](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/automation/applied_policy_error_notification/README.md)
- **Merged At**: 2024-10-16 17:04:31 UTC

---

### PR [#2734](https://github.com/flexera-public/policy_templates/pull/2734): POL-1378 Linting Updates: Cost Policies: AWS

#### Description

> Various small changes to Security policies to bring them up to current linting standards. Also removes known bad coding patterns to avoid their reuse.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2734) for these details.
- **Merged At**: 2024-10-16 12:03:43 UTC

---

### PR [#2736](https://github.com/flexera-public/policy_templates/pull/2736): POL-1378 Linting Updates: Cost Policies: Google

#### Description

> Various small changes to Google Cost policies to bring them up to current linting standards. Also removes known bad coding patterns to avoid their reuse.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2736) for these details.
- **Merged At**: 2024-10-16 12:03:35 UTC

---

### PR [#2735](https://github.com/flexera-public/policy_templates/pull/2735): POL-1378 Linting Updates: Cost Policies: Azure

#### Description

> Various small changes to Azure Cost policies to bring them up to current linting standards. Also removes known bad coding patterns to avoid their reuse.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2735) for these details.
- **Merged At**: 2024-10-14 18:04:01 UTC

---

### PR [#2733](https://github.com/flexera-public/policy_templates/pull/2733): POL-1378 Linting Updates: SaaS Policies

#### Description

> <!-- Describe what this change achieves below -->
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2733) for these details.
- **Merged At**: 2024-10-14 17:01:46 UTC

---

### PR [#2732](https://github.com/flexera-public/policy_templates/pull/2732): POL-1378 Linting Updates: Operational Policies

#### Description

> Various small changes to Security policies to bring them up to current linting standards. Also removes known bad coding patterns to avoid their reuse.
>
> Dangerfile error is a false positive and can be ignored. The coding pattern causing it is sufficiently niche to not be worth the effort of coding the Dangerfile test around it.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2732) for these details.
- **Merged At**: 2024-10-14 17:01:39 UTC

---

### PR [#2731](https://github.com/flexera-public/policy_templates/pull/2731): POL-1378 Linting Updates: Compliance Policies

#### Description

> Various small changes to Compliance policies to bring them up to current linting standards. Also removes known bad coding patterns to avoid their reuse.
>
> Small tweak to Dangerfile to avoid a false positive for one of the tests.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2731) for these details.
- **Merged At**: 2024-10-14 17:01:30 UTC

---

### PR [#2730](https://github.com/flexera-public/policy_templates/pull/2730): POL-1378 Linting Updates: Security Policies

#### Description

> Various small changes to Security policies to bring them up to current linting standards. Also removes known bad coding patterns to avoid their reuse.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2730) for these details.
- **Merged At**: 2024-10-14 17:01:21 UTC

---

### PR [#2729](https://github.com/flexera-public/policy_templates/pull/2729): POL-1378 Linting Updates: Automation Policies

#### Description

> Various small updates to policy templates in the `automation` directory to bring them in conformance to current lint tests.
>
> Small tweak to Dangerfile test to avoid false positives for policies that legitimately have no parameters

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2729) for these details.
- **Merged At**: 2024-10-14 14:32:34 UTC

---

### PR [#2616](https://github.com/flexera-public/policy_templates/pull/2616): POL-1330 New Policy: AWS Account Credentials

#### Description

> This adds a new, unpublished policy template along with a custom meta parent. The purpose of this policy template is to test all of the various cross-account roles implied by an AWS credential to see if they were working as expected or not. Please see the README for more details.
>
> (A custom meta parent is used because the policy engine does not allow you to ignore_status on a signing error, so the meta parent will compare the aggregated incident results to the status of the child policies to determine if the API request succeeded or failed.)
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2616) for details about unpublished policies.
- **Merged At**: 2024-10-11 19:31:30 UTC

---

### PR [#2728](https://github.com/flexera-public/policy_templates/pull/2728): POL-1379 Azure SQL MI Storage Pricing Automation

#### Description

> This adds automation to gather Azure SQL MI Storage Pricing and updates the Azure SQL MI Storage policy template to use this pricing data. In most cases, this will not matter (the generic SQL DB storage pricing is the same in most cases), but this ensures that any deviations in storage pricing specific to SQL MI are accounted for.

#### Metadata

- **Policies**: [Azure Rightsize SQL Managed Instance Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql_storage/README.md), [Meta Parent: Azure Rightsize SQL Managed Instance Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql_storage/README.md)
- **Merged At**: 2024-10-11 17:53:41 UTC

---

### PR [#2726](https://github.com/flexera-public/policy_templates/pull/2726): POL-1375 Google Label Cardinality Report: BigQuery Fix

#### Description

> Fixes an issue caused by the BigQuery API returning both the project ID and dataset ID in the "id" field when listing datasets. This caused errors when attempting to use this id to query for BigQuery tables in the dataset.
>

#### Metadata

- **Policies**: [Google Label Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/google/label_cardinality/README.md), [Meta Parent: Google Label Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/google/label_cardinality/README.md)
- **Merged At**: 2024-10-11 17:53:29 UTC

---

### PR [#2743](https://github.com/flexera-public/policy_templates/pull/2743): POL-1382 Currency Conversion: Multiple Dimension Support

#### Description

> Adds support for multiple dimension filters for the `Currency Conversion` policy template.
>

#### Metadata

- **Policies**: [Currency Conversion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/currency_conversion/README.md)
- **Merged At**: 2024-10-11 13:18:16 UTC

---

### PR [#2712](https://github.com/flexera-public/policy_templates/pull/2712): POL-1139 New Policy: AWS S3 Usage Type Rule-Based Dimension

#### Description

> This new unpublished policy template, `AWS S3 Usage Type Rule-Based Dimension`, creates a single rule-based dimension based on the usage_type values for AWS S3. The intent is to provide a more general and human readable alternative to the built-in dimension, whose values tend to be very specific and not very human readable.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2712) for details about unpublished policies.
- **Merged At**: 2024-10-10 18:09:28 UTC

---

### PR [#2702](https://github.com/flexera-public/policy_templates/pull/2702): POL-1355 New Policy: AWS Rightsize ElastiCache

#### Description

> New policy template to produce rightsizing recommendations for AWS ElastiCache clusters. See README for more details.
>

#### Metadata

- **Policies**: [AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md), [Meta Parent: AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md)
- **Merged At**: 2024-10-09 17:11:27 UTC

---

### PR [#2709](https://github.com/flexera-public/policy_templates/pull/2709): POL-1374 Email Cost Optimization Recommendations: Added Policy Support

#### Description

> Updates to Email Cost Optimization Recommendations. From the CHANGELOG:
>
> - Added support for additional recommendation policy templates
> - Changed "Disks" option to "Storage" for `Recommendation List` parameter to better reflect functionality
> - Added "PaaS" option to `Recommendation List` parameter
>

#### Metadata

- **Policies**: [Email Cost Optimization Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/email_recommendations/README.md)
- **Merged At**: 2024-10-09 17:11:10 UTC

---

### PR [#2721](https://github.com/flexera-public/policy_templates/pull/2721): POL-1377 Cloud Bill Processing Error Notification: Fixes/Improvements

#### Description

> Fixes for `Cloud Bill Processing Error Notification`. From the CHANGELOG:
>
> - Updated some API requests to use newer internal Flexera API
> - Fixed error that sometimes caused functioning bill connections to appear in results
> - Fixed error that sometimes caused the policy template to fail
> - Modified incident table to include more useful information
>

#### Metadata

- **Policies**: [Cloud Bill Processing Error Notification](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/bill_processing_errors_notification/README.md)
- **Merged At**: 2024-10-09 17:10:55 UTC

---

### PR [#2708](https://github.com/flexera-public/policy_templates/pull/2708): POL-1373 Update AWS Superseded EBS Volumes - fix incorrect "New Monthly List Price" value

#### Description

> <!-- Describe what this change achieves below -->
> This policy was previously showing incorrect values in the incident for "New Monthly List Price" and "Estimated Monthly Savings".
>
> This change improves the querying of the AWS Price List API to capture all prices associated with GP3 volumes to provide an accurate value for both these fields in the policy incident.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Policy incident now shows accurate values for "New Monthly List Price" and "Estimated Monthly Savings" to the user.
>

#### Metadata

- **Policies**: [AWS Superseded EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_ebs_volumes/README.md), [Meta Parent: AWS Superseded EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_ebs_volumes/README.md)
- **Merged At**: 2024-10-03 17:34:23 UTC

---

### PR [#2713](https://github.com/flexera-public/policy_templates/pull/2713): POL-1329 Fix calculation of IOPS and Bandwith at Azure Rightsize Managed Disk

#### Description

> This addresses the issue when calculating the IOPS and Bandwith of Premium SSD V2 disk recommendations.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1329
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-10-03 15:10:20 UTC

---

### PR [#2668](https://github.com/flexera-public/policy_templates/pull/2668): POL-1354 New Policy: AWS Rightsize Redshift

#### Description

> New policy template to report rightsizing recommendations for AWS Redshift Clusters
>

#### Metadata

- **Policies**: [AWS Rightsize Redshift](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_redshift/README.md), [Meta Parent: AWS Rightsize Redshift](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_redshift/README.md)
- **Merged At**: 2024-10-03 15:09:51 UTC

---

### PR [#2705](https://github.com/flexera-public/policy_templates/pull/2705): POL-1371 Azure Rightsize NetApp Resources Meta Parent Fix

#### Description

> Fixes an issue causing the consolidated incident in the meta parent to be misnamed.

#### Metadata

- **Policies**: [Azure Rightsize NetApp Resources](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp/README.md), [Meta Parent: Azure Rightsize NetApp Resources](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp/README.md)
- **Merged At**: 2024-10-02 12:41:33 UTC

---

### PR [#2649](https://github.com/flexera-public/policy_templates/pull/2649): POL-1361 Azure Rightsize NetApp Files: Add ignore_status / Misc fixes and Improvements

#### Description

> `Azure Rightsize NetApp Files`: Add ignore_status fields to various datasources for parity with other Azure policy templates
>
> Other misc. changes were also made. From the CHANGELOG:
>
> - Renamed policy template to `Azure Rightsize NetApp Resources` to better reflect its functionality
> - Added ability to use regex to filter resources by tag
> - Added `Recommendation` field to incident table for parity with other Azure policy templates
> - Added logic to skip gathering volume-level data if the user selects "Resize Pools"
> - Several policy parameters updated to more clearly describe their function
> - Incident subject now explicitly indicates that the resources found are oversized
> - Fixed issue where policy template would fail to complete if some subscriptions and resources are inaccessible due to credential permissions
> - Fixed issue where tag filtering was not working as intended
>

#### Metadata

- **Policies**: [Azure Rightsize NetApp Resources](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp/README.md), [Meta Parent: Azure Rightsize NetApp Resources](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp/README.md)
- **Merged At**: 2024-10-01 12:29:52 UTC

---

### PR [#2679](https://github.com/flexera-public/policy_templates/pull/2679): POL-1367 New Policy: Azure Rightsize SQL Managed Instance Storage

#### Description

> This is a new policy template: Azure Rightsize SQL Managed Instance Storage. It does what it says on the tin.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Managed Instance Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql_storage/README.md), [Meta Parent: Azure Rightsize SQL Managed Instance Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_sql_storage/README.md)
- **Merged At**: 2024-10-01 12:29:26 UTC

---

### PR [#2645](https://github.com/flexera-public/policy_templates/pull/2645): SQ-9955 Fix Cloud Cost Anomaly Alerts Policy

#### Description

> <!-- Describe what this change achieves below -->
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2024-09-30 18:59:11 UTC

---

### PR [#2685](https://github.com/flexera-public/policy_templates/pull/2685): POL-1347 - fix: meta_parent_policy_compiler.rb no export block

#### Description

> https://github.com/flexera-public/policy_templates/actions/runs/11059501776
> Workflow is currently failing on a PT
>
> ```
> Writing parent policy template: ../../security/azure/sql_auditing_retention/sql_auditing_retention_meta_parent.pt
> meta_parent_policy_compiler.rb:334:in `block in compile_meta_parent_policy': undefined method `scan' for nil (NoMethodError)
>
>     fields = export_block[0].scan(/(^.*field\s+\".*?\".*?end)/m).flatten
>                             ^^^^^
> 	from meta_parent_policy_compiler.rb:314:in `each'
> 	from meta_parent_policy_compiler.rb:314:in `compile_meta_parent_policy'
> 	from meta_parent_policy_compiler.rb:467:in `block in <main>'
> 	from meta_parent_policy_compiler.rb:466:in `each'
> 	from meta_parent_policy_compiler.rb:466:in `<main>'
> ```
> Modified Workflow Run Succesful: https://github.com/flexera-public/policy_templates/actions/runs/11059612277
>
> Which resulted in these changes: https://github.com/flexera-public/policy_templates/pull/2687
>

#### Metadata

- **Policies**: [AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Meta Parent: AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Meta Parent: Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md), [Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md), [Meta Parent: Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2024-09-30 14:42:51 UTC

---

### PR [#2620](https://github.com/flexera-public/policy_templates/pull/2620): POL-1347 - feat: refactor AWS, Azure, and Google Schedule Instance Policy Templates

#### Description

>  - remove next_stop, next_start tag requirements
>  - remove static zone to region mapping
>  - add task_labels and debugging for CWF actions
>  - add error capture, graceful timeout handling
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1347
>

#### Metadata

- **Policies**: [AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md), [Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2024-09-26 19:47:20 UTC

---

### PR [#2644](https://github.com/flexera-public/policy_templates/pull/2644): POL-1359 AWS Reserved Instances Recommendations: DynamoDB Support

#### Description

> This adds support for DynamoDB and MemoryDB to the `AWS Reserved Instances Recommendations` policy template.
>

#### Metadata

- **Policies**: [AWS Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/recommendations/README.md)
- **Merged At**: 2024-09-26 19:45:30 UTC

---

### PR [#2657](https://github.com/flexera-public/policy_templates/pull/2657): POL-1363 AWS EC2 Compute Optimizer Recommendations: Additional Options

#### Description

> From the `AWS EC2 Compute Optimizer Recommendations` CHANGELOG:
>
> - Added option to filter out recommendations for EC2 instances based on OS family
> - Added option to filter out either x86-64 (Intel/AMD) or ARM (Graviton) recommendations
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2657) for details about unpublished policies.
- **Merged At**: 2024-09-26 19:44:47 UTC

---

### PR [#2673](https://github.com/flexera-public/policy_templates/pull/2673): POL-1366 Currency Conversion: Add Arbitrary Dimension Support

#### Description

> This replaces the option to select a cloud provider in the `Currency Conversion` policy template with an option to specify any arbitrary Dimension=Value. The primary use case is to enable users to do per-bill source conversion, but this of course also enables any number of other possibilities while still retaining the original functionality.
>

#### Metadata

- **Policies**: [Currency Conversion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/currency_conversion/README.md)
- **Merged At**: 2024-09-26 19:43:53 UTC

---

### PR [#2139](https://github.com/flexera-public/policy_templates/pull/2139): POL-1218 New Policy: Google Rightsize Cloud SQL Recommender

#### Description

> New policy to produce recommendations for both idle and underutilized Google Cloud SQL recommendations.
>
> Also deprecates the now redundant `Google Idle Cloud SQL Instance Recommender` and `Google Rightsize CloudSQL Instances` policies.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2139) for these details.
- **Merged At**: 2024-09-25 14:06:51 UTC

---

### PR [#2640](https://github.com/flexera-public/policy_templates/pull/2640): POL-1351 Google Unlabeled Resources: Add Project Support

#### Description

> Adds option to report/update Project labels to `Google Unlabeled Resources` policy template
>

#### Metadata

- **Policies**: [Google Unlabeled Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/google/unlabeled_resources/README.md), [Meta Parent: Google Unlabeled Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/google/unlabeled_resources/README.md)
- **Merged At**: 2024-09-25 12:14:33 UTC

---

### PR [#2633](https://github.com/flexera-public/policy_templates/pull/2633): POL-1352 Outdated Applied Policies: Deprecated Policy Support

#### Description

> This updates the `Flexera Automation Outdated Applied Policies` policy template to also, optionally, report on deprecated policy templates. It also allows the user, via parameter, to allow for automated major version upgrades. Documentation has been updated accordingly.
>
> This also makes a very minor tweak to Dangerfile tests to address a false positive.
>

#### Metadata

- **Policies**: [Flexera Automation Outdated Applied Policies](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/outdated_applied_policies/README.md)
- **Merged At**: 2024-09-24 14:04:10 UTC

---

### PR [#2639](https://github.com/flexera-public/policy_templates/pull/2639): POL-1357 Azure Hybrid Use Benefit Policy Actions

#### Description

> This updates the policy actions in two Azure Hybrid Use Benefit policy templates to correctly use task labels to log errors.
>

#### Metadata

- **Policies**: [Azure Hybrid Use Benefit for Windows Server](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit/README.md), [Meta Parent: Azure Hybrid Use Benefit for Windows Server](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit/README.md), [Azure Hybrid Use Benefit for Linux Server](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_linux/README.md), [Meta Parent: Azure Hybrid Use Benefit for Linux Server](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_linux/README.md)
- **Merged At**: 2024-09-24 12:10:41 UTC

---

### PR [#2638](https://github.com/flexera-public/policy_templates/pull/2638): POL-1356 AWS Rightsize EBS Volume: Type Filtering

#### Description

> Adds a parameter to `AWS Rightsize EBS Volume` to enable the user to filter any arbitrary volume type from the results if desired.
>

#### Metadata

- **Policies**: [AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/README.md), [Meta Parent: AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/README.md)
- **Merged At**: 2024-09-24 12:10:33 UTC

---

### PR [#2663](https://github.com/flexera-public/policy_templates/pull/2663): POL-1364 Update Azure Savings Plan Expiration - Fix Policy Set value

#### Description

> <!-- Describe what this change achieves below -->
> The policy_set field in the policy template metadata has been changed from its current value of "Savings Plan" to "Savings Plans" .
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> This does not change the functionality of the policy but it does help us internally with reporting on templates in our repository.
>

#### Metadata

- **Policies**: [Azure Expiring Savings Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/expiration/README.md)
- **Merged At**: 2024-09-23 17:07:43 UTC

---

### PR [#2656](https://github.com/flexera-public/policy_templates/pull/2656): POL-1013 Add Azure Expiring Savings Plans Policy

#### Description

> <!-- Describe what this change achieves below -->
> Pretty self-explanatory. This is a change to add Azure Expiring Savings Plans policy to the Catalog. This policy will be added to remain consistent with its AWS counterpart. This policy will report on Savings Plans that are expired and/or nearing expiration.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Maintains parity between AWS and Azure. Customers can now be alerted via email when Savings Plans are nearing expiration or have expired.
>

#### Metadata

- **Policies**: [Azure Expiring Savings Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/expiration/README.md)
- **Merged At**: 2024-09-23 15:53:39 UTC

---

### PR [#2624](https://github.com/flexera-public/policy_templates/pull/2624): POL-1349 Applied Policy Template Errors Revamp

#### Description

> This is a revamp of the `Applied Policy Error Notification` policy template. From the CHANGELOG:
>
> - Renamed to `Applied Policy Template Errors` to conform to policy template naming conventions
> - Added ability to ignore specific applied policy templates by name or ID
> - Parameters altered to be more descriptive and human-readable
> - Added additional fields to incident table to provide more context
> - Incident table now includes links to the problematic applied policy templates
> - Streamlined code for better readability and faster execution
> - Policy template is now published in the public catalog
>

#### Metadata

- **Policies**: [Applied Policy Template Errors](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/automation/applied_policy_error_notification/README.md)
- **Merged At**: 2024-09-23 15:31:26 UTC

---

### PR [#2621](https://github.com/flexera-public/policy_templates/pull/2621): POL-1345 Azure Untagged Resources: Subscription/Resource Group Support

#### Description

> Adds support for reporting untagged Azure Subscriptions and Resource Groups to the `Azure Untagged Resources` policy template.
>

#### Metadata

- **Policies**: [Azure Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_resources/README.md), [Meta Parent: Azure Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_resources/README.md)
- **Merged At**: 2024-09-20 13:57:01 UTC

---

### PR [#2647](https://github.com/flexera-public/policy_templates/pull/2647): POL-1360 Meta Parent: Fix Deprecation Status

#### Description

> This fixes an issue where the "deprecated" field in the info() blocks of generated meta parent policy templates did not match the child.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2647) for these details.
- **Merged At**: 2024-09-20 12:23:46 UTC

---

### PR [#2610](https://github.com/flexera-public/policy_templates/pull/2610): POL-1338 Validated Permissions

#### Description

> This PR makes several changes related to tracking policy permissions:
>
> - Several policy templates that were missing have been validated and added. Where appropriate, these policy templates and their associated README files were updated.
> - Automation has been added to track every non-deprecated policy template that is not in the validation list. This is to assist in completing this project by getting all of the missing policy templates added.
> - A couple of deprecated policy templates were missing the deprecated: "true" field in the info block. This has been fixed.
> - Minor tweaks made to changed files to pass current Dangerfile tests

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2610) for these details.
- **Merged At**: 2024-09-20 12:03:15 UTC

---

### PR [#2642](https://github.com/flexera-public/policy_templates/pull/2642): POL-1358 AWS Rule-Based Dimension From Account Tags: Tag Casing Fix

#### Description

> This updates the `AWS Rule-Based Dimension From Account Tags` policy template to fix an issue where tag keys were being ignored if they contained upper case letters.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2642) for details about unpublished policies.
- **Merged At**: 2024-09-19 17:53:06 UTC

---

### PR [#2622](https://github.com/flexera-public/policy_templates/pull/2622): POL-1348 Cloud Bill Processing Error Notification: Ignore List

#### Description

> Cloud Bill Processing Error Notification: Added `Bill Connection Ignore List` parameter to allow user to ignore specific bill connections.
>

#### Metadata

- **Policies**: [Cloud Bill Processing Error Notification](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/bill_processing_errors_notification/README.md)
- **Merged At**: 2024-09-19 13:06:52 UTC

---

### PR [#2634](https://github.com/flexera-public/policy_templates/pull/2634): POL-1353 New Policy: Azure Unused Load Balancers

#### Description

> New policy that reports on Azure Unused Load Balancers
>

#### Metadata

- **Policies**: [Azure Unused Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_load_balancers/README.md), [Meta Parent: Azure Unused Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_load_balancers/README.md)
- **Merged At**: 2024-09-17 17:19:02 UTC

---

### PR [#2565](https://github.com/flexera-public/policy_templates/pull/2565): POL-1327 New Policy: AWS Lambda Functions Without Provisioned Concurrency

#### Description

> New template `AWS Lambda Functions Without Provisioned Concurrency` does what it says on the tin.
>

#### Metadata

- **Policies**: [AWS Lambda Functions Without Provisioned Concurrency](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/lambda_provisioned_concurrency/README.md), [Meta Parent: AWS Lambda Functions Without Provisioned Concurrency](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/lambda_provisioned_concurrency/README.md)
- **Merged At**: 2024-09-16 17:17:03 UTC

---

### PR [#2556](https://github.com/flexera-public/policy_templates/pull/2556): POL-793 Azure MySQL Policy Templates

#### Description

> Two new policy templates: `Azure Rightsize MySQL Single Servers` and `Azure Rightsize MySQL Flexible Servers`
>
> Two templates because of substantial differences between API requests and metrics between the two kinds of MySQL instances. Single servers are also an increasingly outdated instance type, so most users can likely just get away with using the latter policy template only.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2556) for these details.
- **Merged At**: 2024-09-16 12:11:48 UTC

---

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

