# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#3990](https://github.com/flexera-public/policy_templates/pull/3990): Google Meta Parent sys- and app- Project Filtering

*Minor Update*

#### Description

> This change enables the user to ensure that sys- and app- projects are filtered in the child policies by including the relevant parameters in the meta parents and defaulting them to "yes". These projects generally don't produce billable assets and including them in child policy executions can cause timeouts and scaling issues.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3990) for these details.
- **Merged At**: 2026-01-16 13:06:23 UTC

---

### PR [#3989](https://github.com/flexera-public/policy_templates/pull/3989): POL-1718 Scheduled Report: CSV Support

*Minor Update*

#### Description

> From Changelog:
> - Added support for attaching CSV files to incident emails.
> - Fixed issue where incident was missing line breaks.
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2026-01-16 13:06:13 UTC

---

### PR [#3984](https://github.com/flexera-public/policy_templates/pull/3984): POL-1518 Azure Reserved Instances Recommendations Fix

*Minor Update*

#### Description

> Fixes issue with break even calculation in Azure Reserved Instances Recommendations policy template.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md)
- **Merged At**: 2026-01-15 16:44:19 UTC

---

### PR [#3978](https://github.com/flexera-public/policy_templates/pull/3978): POL-1518 Azure Reserved Instances Recommendations: Add Break Even Point

*Minor Update*

#### Description

> Adds the break even point in months to the incident for Azure Reserved Instances Recommendations. This is calculated via the following formula:
>
> (1 - ((costWithNoRI - totalCostWithRI) / costWithNoRI)) * termMonths
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md)
- **Merged At**: 2026-01-15 15:53:54 UTC

---

### PR [#3971](https://github.com/flexera-public/policy_templates/pull/3971): POL-1717 Update AWS Rightsize Redshift - no Policy Incidents fix

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change adds a small fix to the AWS Rightsize Redshift policy template to resolve order of magnitude error when evaluating the CPU Utilization vs the CPU Threshold.
>
> This was previously causing the AWS Rightsize Redshift policy to produce no recommendations for valid Redshift instances/nodes.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Rightsize Redshift](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_redshift/README.md)
- **Merged At**: 2026-01-13 16:32:14 UTC

---

### PR [#3972](https://github.com/flexera-public/policy_templates/pull/3972): POL-1716 Google Project Pagination Update Pt 2

*Minor Update*

#### Description

> This updates several Google policies to use a newer API endpoint for listing Google Projects. This has the benefit of filtering the projects based on parameters during the request itself; this is especially useful for filtering out app- and sys- projects, since it's possible to have so many of those that pagination actually hits Google API limits.
>
> This also updates the meta policy generator script to still work for these policy templates even when "ds_is_deleted" is referenced inside of a JavaScript block.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3972) for these details.
- **Merged At**: 2026-01-13 14:48:05 UTC

---

### PR [#3967](https://github.com/flexera-public/policy_templates/pull/3967): POL-1716 Part 1: Google Project Pagination Update

*Minor Update*

#### Description

> This updates several Google policies to use a newer API endpoint for listing Google Projects. This has the benefit of filtering the projects based on parameters during the request itself; this is especially useful for filtering out app- and sys- projects, since it's possible to have so many of those that pagination actually hits Google API limits.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3967) for these details.
- **Merged At**: 2026-01-12 20:47:53 UTC

---

### PR [#3958](https://github.com/flexera-public/policy_templates/pull/3958): POL-1713 Update AWS Rightsize ElastiCache - no Policy Incidents fix

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> It was observed in a customer org that for the AWS Rightsize ElastiCache policy that even when valid Elasticache instances exist, the policy does not produce an incident and therefore no recommendations.
>
> This is a fix to the `ds_elasticache_clusters_resize_filtered` datasource to ensure datasources are being read and compared correctly when evaluating Elasticache instances.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md)
- **Merged At**: 2026-01-12 15:52:17 UTC

---

### PR [#3948](https://github.com/flexera-public/policy_templates/pull/3948): POL-1709 Fixed Bug onboarding policy ignores google policies

*Minor Update, Bug Fix*

#### Description

> Flexera Onboarding Policy fix issue where all gcp policies were skipped/ignored.
>
> <!-- Describe what this change achieves below -->
>
> ### Issues Resolved
>
> Pol-1709 onboarding policy ignores google policies
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Flexera Onboarding](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/onboarding/README.md)
- **Merged At**: 2026-01-09 14:49:50 UTC

---

### PR [#3944](https://github.com/flexera-public/policy_templates/pull/3944): POL-1649 Update AWS Policies to support Account Name for MSP Child Orgs - Security Policies 5 (IAM 2)

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
>
> - AWS IAM Root User Doing Everyday Tasks
> - AWS IAM User Accounts Without MFA
> - AWS IAM Users With Directly-Attached Policies
> - AWS IAM Users With Multiple Active Access Keys
> - AWS IAM Users With Old Access Keys
> - AWS Regions Without Access Analyzer Enabled
> - AWS Unused IAM Credentials
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3944) for these details.
- **Merged At**: 2026-01-05 16:45:54 UTC

---

### PR [#3943](https://github.com/flexera-public/policy_templates/pull/3943): POL-1648 Update AWS Policies to support Account Name for MSP Child Orgs - Security Policies 4 (IAM 1)

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
>
> - AWS IAM Account Missing Support Role
> - AWS IAM Attached Admin Policies
> - AWS IAM Expired SSL/TLS Certificates
> - AWS IAM Insufficient Required Password Length
> - AWS IAM Password Policy Not Restricting Password Reuse
> - AWS IAM Root Account Access Keys
> - AWS IAM Root User Account Without Hardware MFA
> - AWS IAM Root User Account Without MFA
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3943) for these details.
- **Merged At**: 2026-01-05 16:27:19 UTC

---

### PR [#3938](https://github.com/flexera-public/policy_templates/pull/3938): POL-1647 Update AWS Policies to support Account Name for MSP Child Orgs - Security Policies 3

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
>
> - AWS Open S3 Buckets
> - AWS S3 Buckets Accepting HTTP Requests
> - AWS S3 Buckets Without Default Encryption Configuration
> - AWS S3 Buckets Without MFA Delete Enabled
> - AWS S3 Buckets Without Public Access Blocked
> - AWS S3 Buckets Without Server Access Logging
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3938) for these details.
- **Merged At**: 2026-01-05 13:28:07 UTC

---

### PR [#3927](https://github.com/flexera-public/policy_templates/pull/3927): POL-1646 Update AWS Policies to support Account Name for MSP Child Orgs - Security Policies 2

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
>
> - AWS Regions Without Config Fully Enabled
> - AWS Regions Without Default EBS Encryption
> - AWS Unencrypted EBS Volumes
> - AWS Customer Managed Keys (CMKs) Without Rotation Enabled
> - AWS Elastic Load Balancers With Unencrypted Listeners
> - AWS Internet-Accessible Elastic Load Balancers
> - AWS VPCs Without FlowLogs Enabled
> - AWS Publicly Accessible RDS Instances
> - AWS Unencrypted RDS Instances
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3927) for these details.
- **Merged At**: 2026-01-02 15:23:48 UTC

---

### PR [#3921](https://github.com/flexera-public/policy_templates/pull/3921): POL-1645 Update AWS Policies to support Account Name for MSP Child Orgs - Security Policies 1

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
>
> - AWS CloudTrail Not Enabled In All Regions
> - AWS CloudTrail S3 Buckets Without Access Logging
> - AWS CloudTrails Not Integrated With CloudWatch
> - AWS CloudTrails Without Encrypted Logs
> - AWS CloudTrails Without Log File Validation Enabled
> - AWS CloudTrails Without Object-level Events Logging Enabled
> - AWS Publicly Accessible CloudTrail S3 Buckets
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3921) for these details.
- **Merged At**: 2026-01-02 13:21:19 UTC

---

### PR [#3920](https://github.com/flexera-public/policy_templates/pull/3920): POL-1642 Update AWS Policies to support Account Name for MSP Child Orgs - Cost Policies 2

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
>
> - AWS Oversized S3 Buckets
> - AWS S3 Buckets Without Intelligent Tiering
> - AWS S3 Buckets Without Lifecycle Configuration
> - AWS S3 Incomplete Multi-Part Uploads
> - AWS Schedule Instance
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3920) for these details.
- **Merged At**: 2026-01-02 13:20:20 UTC

---

### PR [#3919](https://github.com/flexera-public/policy_templates/pull/3919): POL-1641 Update AWS Policies to support Account Name for MSP Child Orgs - Cost Policies 1

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
> - AWS Burstable EC2 Instances
> - AWS REC2 Instances Time Stopped Report
> - AWS EKS Cluster Without Spot Instances
> - AWS CloudTrails With Read Logging Enabled
> - ~AWS Expiring Reserved Instances~ - Not applicable: Vendor Account Name appears for Reserved Instances list in Child Orgs
> - ~AWS Expiring Savings Plans~ - Not applicable
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3919) for these details.
- **Merged At**: 2026-01-02 13:19:54 UTC

---

### PR [#3897](https://github.com/flexera-public/policy_templates/pull/3897): FOPTS-18273 Fix possible 'undefined' error for AWS Rightsize EC2 Instances policy

*Bug Fix*

#### Description

> Fix possible 'undefined' error for AWS Rightsize EC2 Instances policy.
> This error only happens when `"Skip Instance Sizes"` is set to `"Yes"`, and only happens for certain AWS instance type (such as `"c5.24xlarge"` or `"c5a.24xlarge"`).
>
> `ds_aws_instance_size_map[instance['newResourceType']]['down']` might error due to `ds_aws_instance_size_map[instance['newResourceType']]` being "null".
> https://github.com/flexera-public/policy_templates/blob/14f8fe295d44df97e42db84aafd4eb8b1916a6a3/cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt#L1599
>
> it could be caused by `instance['resourceType']` equal to `"c5.24xlarge"` or `"c5a.24xlarge"`, as there is no resource type "c18.18xlarge" nor "c18.16xlarge" in "instance_types.json" file.
> https://github.com/flexera-public/policy_templates/blob/14f8fe295d44df97e42db84aafd4eb8b1916a6a3/data/aws/instance_types.json#L311-L320
> https://github.com/flexera-public/policy_templates/blob/14f8fe295d44df97e42db84aafd4eb8b1916a6a3/data/aws/instance_types.json#L400-L409
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-20106
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md), [Meta Parent: AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md)
- **Merged At**: 2026-01-02 13:10:14 UTC

---

### PR [#3916](https://github.com/flexera-public/policy_templates/pull/3916): POL-1712 Google Meta Policy Fixes

*Minor Update*

#### Description

> Fixes issue with two Google policy templates where meta policies were not being properly generated with version updates.
>

#### Metadata

- **Policies**: [Google Rightsize Cloud SQL Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_cloudsql_instances/README.md), [Meta Parent: Google Rightsize Cloud SQL Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_cloudsql_instances/README.md), [Google Unused Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/google/unused_disks/README.md), [Meta Parent: Google Unused Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/google/unused_disks/README.md)
- **Merged At**: 2025-12-31 16:48:36 UTC

---

### PR [#3906](https://github.com/flexera-public/policy_templates/pull/3906): POL-1640 Update AWS Policies to support Account Name for MSP Child Orgs - Compliance Policies 2

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
> - AWS IAM Role Audit (and meta parent)
> - AWS RDS Instances With Unapproved Backup Settings (and meta parent)
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS IAM Role Audit](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/iam_role_audit/README.md), [Meta Parent: AWS IAM Role Audit](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/iam_role_audit/README.md), [AWS RDS Instances With Unapproved Backup Settings](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/rds_backup/README.md), [Meta Parent: AWS RDS Instances With Unapproved Backup Settings](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/rds_backup/README.md)
- **Merged At**: 2025-12-30 19:06:53 UTC

---

### PR [#3905](https://github.com/flexera-public/policy_templates/pull/3905): POL-1639 Update AWS Policies to support Account Name for MSP Child Orgs - Optimization Compliance Policies 1

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
> - AWS Long Stopped EC2 Instances (and meta parent)
> - AWS Unused ECS Clusters(and meta parent)
> - AWS Untagged Resources (and meta parent)
> - AWS Disallowed Regions (and meta parent)
>
> ### Other Notes
> - Includes Cheng's fix in [FOPTS-18276](https://github.com/flexera-public/policy_templates/pull/3898) - cc @jc1203
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3905) for these details.
- **Merged At**: 2025-12-30 19:06:47 UTC

---

### PR [#3907](https://github.com/flexera-public/policy_templates/pull/3907): POL-1711 Google Rightsize VM Meta Issue

*Minor Update*

#### Description

> The meta policy for "Google Rightsize VM Instances" was not being properly generated because it was not listed in the appropriate YAML file. The meta parent code in the child policy was also broken.
>
> This fixes both things.
>

#### Metadata

- **Policies**: [Google Rightsize VM Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_instances/README.md), [Meta Parent: Google Rightsize VM Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_instances/README.md)
- **Merged At**: 2025-12-30 18:20:16 UTC

---

### PR [#3898](https://github.com/flexera-public/policy_templates/pull/3898): FOPTS-18276 Fixed 'undefined' error in POL-1636

*Bug Fix*

#### Description

> Fixing an "undefined" error introduced in POL-1636.
>
> E.g. `result["tags"] = {}` would fail due to `result` is `undefined`
> https://github.com/flexera-public/policy_templates/pull/3884/files#diff-9e47704a4846c077cda93e9dcb2307747be5b1e38584b670213625def1b5248eR406-R412
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-18276
> (no related SQ ticket)
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3898) for these details.
- **Merged At**: 2025-12-30 13:31:24 UTC

---

### PR [#3896](https://github.com/flexera-public/policy_templates/pull/3896): FOAA-810 - Fix JS `TypeError` from else [ ... ] typo

*Unpublished, Bug Fix*

#### Description

> Fixes Javascript TypeError that can arise under certain conditions because of a typo/incorrect `else [ ... ]` statement.
>
> Here is the fix:
> https://github.com/flexera-public/policy_templates/pull/3896/changes#diff-16cc7427fb6b811a00954f15e673c86e82a0c2e723647ec131d11591ed941456L797-R801
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-810
> https://flexera.atlassian.net/browse/SQ-20600
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3896) for details about unpublished policies.
- **Merged At**: 2025-12-30 13:31:14 UTC

---

### PR [#3890](https://github.com/flexera-public/policy_templates/pull/3890): POL-1637 Update AWS Policies to support Account Name for MSP Child Orgs - Optimization Recommendation Policies 2

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
> - AWS Rightsize Elasticache (and meta parent)
> - AWS Rightsize Redshift (and meta parent)
> - AWS Rightsize EBS Volumes (and meta parent)
> - AWS Rightsize RDS Instances (and meta parent)
> - AWS Old Snapshots (and meta parent)
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3890) for these details.
- **Merged At**: 2025-12-29 19:18:29 UTC

---

### PR [#3891](https://github.com/flexera-public/policy_templates/pull/3891): POL-1644 Update AWS Policies to support Account Name for MSP Child Orgs - Operational Policies

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
> - AWS Long Running Instances (and meta parent)
> - AWS Overutilized Instances (and meta parent)
> - AWS Scheduled EC2 Instances (and meta parent)
> - AWS Lambda Functions With High Error Rate (and meta parent)
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3891) for these details.
- **Merged At**: 2025-12-29 19:18:19 UTC

---

### PR [#3892](https://github.com/flexera-public/policy_templates/pull/3892): POL-1638 Update AWS Policies to support Account Name for MSP Child Orgs - Optimization Recommendation Policies 3

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
> - AWS Idle NAT Gateways (and meta parent)
> - AWS Unused Application Load Balancers (and meta parent)
> - AWS Unused Classic Load Balancers (and meta parent)
> - AWS Unused Network Load Balancers (and meta parent)
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3892) for these details.
- **Merged At**: 2025-12-29 19:18:13 UTC

---

### PR [#3884](https://github.com/flexera-public/policy_templates/pull/3884): POL-1636 Update AWS Policies to support Account Name for MSP Child Orgs - Optimization Recommendation Policies 1

#### Description

> <!-- Describe what this change achieves below -->
> This PR adds a fallback mechanism for retrieving AWS account information in multiple AWS policy templates, addressing issues where the Flexera List Cloud Accounts API may not return relevant account details (common in MSP environments). When the primary API fails, policies now fall back to querying aggregated cost data from the Flexera Bill Analysis API to populate account names.
>
> Changes Made:
> - **New Datasources & Scripts**: Added `ds_billing_centers_aws_acc`, `ds_top_level_bcs_aws_acc`, and `ds_cloud_vendor_accounts_fallback` datasources, along with corresponding JS scripts (`js_top_level_bcs_aws_acc`, `js_cloud_vendor_accounts_fallback`) to handle fallback account retrieval.
> - **Updated Logic**: Modified existing scripts (e.g., `js_vendor_account_table`, `js_aws_account`) to check for empty results from the primary API and use the fallback data.
>
> ### Affected Policies
> - AWS Reserved Instance Recommendations
> - AWS Rightsize EC2 Instances (and meta parent)
> - AWS Savings Plan Recommendations
> - AWS Superseded EBS Volumes (and meta parent)
> - AWS Superseded EC2 Instances (and meta parent)
> - AWS Unused IP Addresses (and meta parent)
> - AWS Lambda Functions Without Provisioned Concurrency (and meta parent)
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3884) for these details.
- **Merged At**: 2025-12-29 14:09:08 UTC

---

### PR [#3859](https://github.com/flexera-public/policy_templates/pull/3859): POL-1702 AWS Oversized S3 Buckets - Add Storage Type field to Policy Incident

*Major Update, Minor Update*

#### Description

> <!-- Describe what this change achieves below -->
> The AWS Oversized S3 Buckets Policy Incident output now emits one entry per S3 bucket per storage type (e.g., StandardStorage, StandardIAStorage, StandardIASizeOverhead, GlacierStorage). The incident export and CSV attachment include the new `storageType` and per-class size (GiB).
>
> This change also fixes a typo in the AWS Savings Plan Recommendations policy Changelog.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md)
- **Merged At**: 2025-12-19 14:04:49 UTC

---

### PR [#3853](https://github.com/flexera-public/policy_templates/pull/3853): POL-1703 - fix: Cost Reallocation PT

*Unpublished, Bug Fix*

#### Description

> This is the major change: https://github.com/flexera-public/policy_templates/compare/fix/flexera_cost_reallocation_v0.1.2?expand=1#diff-403d8fbc6343839c275de9201ad525674a422843c45df7bceae06b745fdfec5cR624
>
> Everything else is comments added, fixing logSample() which provide some additional context helpful for next maintainer/operator attempting to debug.
>
> Before the fix, we were seeing the negation line items but not the reallocated line items (sum of reallocated bill source < $0) which is not expected.
>
> With the fix, we see the reallocated line items net to $0 as expected, and the proper lower reallocated granularity line items are being pushed correctly.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1703
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3853) for details about unpublished policies.
- **Merged At**: 2025-12-15 13:50:32 UTC

---

### PR [#3848](https://github.com/flexera-public/policy_templates/pull/3848): POL-1682 New Policy Template: AWS Savings Plan Purchase Analysis

*New Policy Template*

#### Description

> Adds a new policy template `AWS Savings Plan Purchase Analysis`:
>
> This policy template performs a purchase analysis via the [AWS Savings Plans Purchase Analyzer](https://aws.amazon.com/blogs/aws-cloud-financial-management/announcing-savings-plans-purchase-analyzer/) tool included in AWS Cost Explorer and reports the results. Optionally, this report can be emailed.
>

#### Metadata

- **Policies**: [AWS Savings Plan Purchase Analysis](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/purchase_analysis/README.md)
- **Merged At**: 2025-12-12 13:57:18 UTC

---

### PR [#3849](https://github.com/flexera-public/policy_templates/pull/3849): POL-1700 AWS Savings Plan Recommendations - Add Support for Database Savings Plan Type

#### Description

> <!-- Describe what this change achieves below -->
> This change adds support for the new Database Savings Plan Type in AWS - https://aws.amazon.com/blogs/aws/introducing-database-savings-plans-for-aws-databases/
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/recommendations/README.md)
- **Merged At**: 2025-12-09 16:45:09 UTC

---

### PR [#3831](https://github.com/flexera-public/policy_templates/pull/3831): POL-1673 New Policy: Oracle Tag Cardinality 

*New Policy Template*

#### Description

> Adds a new Oracle Tag Cardinality Report policy template that is similar to the ones for other cloud providers.
>

#### Metadata

- **Policies**: [Oracle Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/oracle/tag_cardinality/README.md)
- **Merged At**: 2025-12-03 14:30:12 UTC

---

### PR [#3830](https://github.com/flexera-public/policy_templates/pull/3830): POL-1697 Google Long Running VM Instances Policy

*New Policy Template*

#### Description

> New Policy: Google Long Running VM Instances. Functions similarly to the AWS/Azure counterparts.
>
> Also fixed a minor issue in the Google Long Stopped VM Instances policy and did some work on the Long Running policy READMEs for consistency.
>

#### Metadata

- **Policies**: [Google Long Stopped VM Instances](https://github.com/flexera-public/policy_templates/tree/master/compliance/google/long_stopped_instances/README.md), [Google Long Running VM Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/google/long_running_instances/README.md)
- **Merged At**: 2025-12-03 13:59:42 UTC

---

### PR [#3826](https://github.com/flexera-public/policy_templates/pull/3826): POL-1698 Azure Rightsize NetApp Resources - Undefined variable fix

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> The Azure Rightsize NetApp Resources applied policy fails to run with `ReferenceError: 'endpool' is not defined`
>
> This is due to the incorrect naming of a variable and/or the code referencing a variable that does not exist.
>
> This change adds a fix to mitigate the non-instantiated variable
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Azure Rightsize NetApp Resources](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp/README.md)
- **Merged At**: 2025-12-02 14:00:09 UTC

---

### PR [#3823](https://github.com/flexera-public/policy_templates/pull/3823): POL-1696 Heredoc Improvements

*Unpublished, Minor Update*

#### Description

> Updates all heredocs to use the `<<-'EOS'` format (instead of `<<-EOS` without single quotes) to conform with new Dangerfile testing and code standards.
>
> Dangerfile warnings/errors are false positives that are not related to this change.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3823) for these details.
- **Merged At**: 2025-12-01 21:12:47 UTC

---

### PR [#3806](https://github.com/flexera-public/policy_templates/pull/3806): FOPTS-16932 Fetch only ACTIVE recommendations from Google Recommender API

*Minor Update*

#### Description

> <!-- Describe what this change achieves below -->
>
> Usage of google recommenders API. The Google Recommenders API returns duplicate recommendations for the same resource ID in different states i.e active, claimed, dismissed, succeeded, failed. "ACTIVE" includes recommendations that haven't been claimed, dismissed, succeeded, or failed yet in google cloud.
>
>
> https://[raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/cud_recommendations/google_committed_use_discount_recommendations.pt](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/cud_recommendations/google_committed_use_discount_recommendations.pt)
>
> ### Google Recommenders API Docs
> https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list#query-parameters
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> https://flexera.atlassian.net/browse/FOPTS-16932

#### Metadata

- **Policies**: [Google Committed Use Discount Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cud_recommendations/README.md), [Meta Parent: Google Committed Use Discount Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cud_recommendations/README.md)
- **Merged At**: 2025-12-01 14:04:10 UTC

---

### PR [#3781](https://github.com/flexera-public/policy_templates/pull/3781): POL-1688 AWS Oversized S3 Buckets - Capture Missing Buckets in Incident

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change fixes a gap where bucket size stats data from CloudWatch wasn’t being captured in the policy for many S3 buckets. This fix ensures users now get a more complete picture when reviewing recommendations for oversized S3 buckets.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md)
- **Merged At**: 2025-11-27 09:23:10 UTC

---

### PR [#3808](https://github.com/flexera-public/policy_templates/pull/3808): POL-1693 fix: use separate email escalation for errors identified incident

*Bug Fix*

#### Description

> Updated email escalation declaration for new "Errors Identified" incident to prevent error `failed make a CSV attachment with data: unable to collect csv data from nil export`
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3808) for these details.
- **Merged At**: 2025-11-26 17:43:28 UTC

---

### PR [#3804](https://github.com/flexera-public/policy_templates/pull/3804): POL-1690 Fix Azure Rightsize Managed Disks Meta Parent

#### Description

> This fixes a bug in the Azure Rightsize Managed Disks policy that not only breaks that policy but breaks the meta parent as well.
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2025-11-25 13:54:56 UTC

---

### PR [#3792](https://github.com/flexera-public/policy_templates/pull/3792): FOPTS-16961: Fetch only ACTIVE recommendations by google recommender service

*Minor Update*

#### Description

> Usage of google recommenders API. The Google Recommenders API returns duplicate recommendations for the same resource ID in different states i.e active, claimed, dismissed, succeeded, failed. "ACTIVE" includes recommendations that haven't been claimed, dismissed, succeeded, or failed yet in google cloud.
>
> https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/idle_ip_address_recommendations/google_idle_ip_address_recommendations.pt
>
> <!-- Describe what this change achieves below -->
>
> ### Issues Resolved
>
> ### Google Recommenders API Docs
> https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list#query-parameters
>
> <!-- List any existing issues this PR resolves below -->
>
> https://flexera.atlassian.net/browse/FOPTS-16961
>

#### Metadata

- **Policies**: [Google Idle IP Address Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/idle_ip_address_recommendations/README.md), [Meta Parent: Google Idle IP Address Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/idle_ip_address_recommendations/README.md)
- **Merged At**: 2025-11-25 13:17:09 UTC

---

### PR [#3773](https://github.com/flexera-public/policy_templates/pull/3773): POL-1663 - Prevent Duplicate Policy Creation where the Outdated Policy itself is Outdated

*Minor Update*

#### Description

> - Use 201 Response (created) from the application of a given updated policy to target the older one for deletion https://developer.flexera.com/docs/api/policy/v1#/Applied%20Policy/Applied%20Policy%23create
> - Use function for translation of frequency rrule for minutely interval to 15 minute and capture the whole response in `ds_apllied_policies` rather than split by `=`
>
> ### Issues Resolved
>
> [POL-1663](https://flexera.atlassian.net/browse/POL-1663)
>

#### Metadata

- **Policies**: [Flexera Automation Outdated Applied Policies](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/outdated_applied_policies/README.md)
- **Merged At**: 2025-11-25 13:15:28 UTC

---

### PR [#3346](https://github.com/flexera-public/policy_templates/pull/3346): FOAA-307 - feat: Update AWS S3 Buckets Without Intelligent Tiering policy to include estimated monthly savings

*Minor Update*

#### Description

> - Update `AWS S3 Buckets Without Intelligent Tiering` policy template to include estimated monthly savings
> - Policy now continues execution for accessible regions when some regions return permission errors
> - Added separate incident report to identify regions with access issues and provide remediation guidance
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-307
>

#### Metadata

- **Policies**: [AWS S3 Buckets Without Intelligent Tiering](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_storage_policy/README.md)
- **Merged At**: 2025-11-24 19:48:52 UTC

---

### PR [#3753](https://github.com/flexera-public/policy_templates/pull/3753): FOAA-582 - feat: Graceful error handling for inaccessible regions

*Minor Update*

#### Description

> AWS policy templates can fail completely when encountering HTTP errors (403, 401, etc.) in any region due to permission issues, disabled regions, or SCPs.. This enhancement improves AWS Policy Templates from "all-or-nothing" to "best-effort" execution. This should improve user experience and minimize effort to generate recommendations.
>
> This is the second batch of policies for initial PR here: https://github.com/flexera-public/policy_templates/pull/3630
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-18272
> https://flexera.atlassian.net/browse/FOAA-582
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3753) for these details.
- **Merged At**: 2025-11-24 17:57:15 UTC

---

### PR [#3630](https://github.com/flexera-public/policy_templates/pull/3630): FOAA-582 - Graceful error handling for inaccessible regions

*Minor Update*

#### Description

> AWS policy templates can fail completely when encountering HTTP errors (403, 401, etc.) in any region due to permission issues, disabled regions, or SCPs.. This enhancement improves AWS Policy Templates from "all-or-nothing" to "best-effort" execution.  This should improve user experience and minimize effort to generate recommendations.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-582
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3630) for these details.
- **Merged At**: 2025-11-24 17:57:06 UTC

---

### PR [#2933](https://github.com/flexera-public/policy_templates/pull/2933): POL-1401 - Initial Cost Reallocation Policy Templates

*Unpublished, New Policy Template*

#### Description

> Adds 3 new policy templates for reallocating shared costs using Flexera Automation + Flexera Common Bill Ingest
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/2933) for these details.
- **Merged At**: 2025-11-24 17:11:05 UTC

---

### PR [#3779](https://github.com/flexera-public/policy_templates/pull/3779): FOPTS-16832 Fetch only ACTIVE recommendations by google recommender service

*Minor Update*

#### Description

> <!-- Describe what this change achieves below -->
>
> Usage of google recommenders API. The Google Recommenders API returns duplicate recommendations for the same resource ID in different states i.e active, claimed, dismissed, succeeded, failed. "ACTIVE" includes recommendations that haven't been claimed, dismissed, succeeded, or failed yet in google cloud.
>
>
> https://[raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/rightsize_cloudsql_recommendations/google_rightsize_cloudsql_recommendations.pt](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/rightsize_cloudsql_recommendations/google_rightsize_cloudsql_recommendations.pt)
>
> ### Google Recommenders API Docs
> https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list#query-parameters
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> https://flexera.atlassian.net/browse/FOPTS-16832

#### Metadata

- **Policies**: [Google Rightsize Cloud SQL Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_cloudsql_recommendations/README.md), [Meta Parent: Google Rightsize Cloud SQL Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_cloudsql_recommendations/README.md)
- **Merged At**: 2025-11-21 13:16:06 UTC

---

### PR [#3780](https://github.com/flexera-public/policy_templates/pull/3780): FOPTS-16924: Fetch only ACTIVE recommendations by google recommender service

*Minor Update*

#### Description

> Usage of google recommenders API. The Google Recommenders API returns duplicate recommendations for the same resource ID in different states i.e active, claimed, dismissed, succeeded, failed. "ACTIVE" includes recommendations that haven't been claimed, dismissed, succeeded, or failed yet in google cloud.
>
> https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations.pt
>
> ### Google Recommenders API Docs
> https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list#query-parameters
>
> ### Issues Resolved
> https://flexera.atlassian.net/browse/FOPTS-16924
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Google Idle Persistent Disk Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/idle_persistent_disk_recommendations/README.md), [Meta Parent: Google Idle Persistent Disk Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/idle_persistent_disk_recommendations/README.md)
- **Merged At**: 2025-11-21 13:16:02 UTC

---

### PR [#3765](https://github.com/flexera-public/policy_templates/pull/3765): feat: Add automatic actions parameter to Dynamic Dashboard Policy Template

*Minor Update*

#### Description

> - Added "Automatic Actions" parameter to allow automatic creation/updating of dashboards without manual approval
> - Fixed Widgets Date Granularity to use user-configurable Dashboard setting instead of hardcoded "monthly" value
> - Fixed identification of existing dashboards for Create or Update logic
>

#### Metadata

- **Policies**: [Dynamic Dashboards](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/dynamic_dashboards/README.md)
- **Merged At**: 2025-11-19 15:10:09 UTC

---

### PR [#3737](https://github.com/flexera-public/policy_templates/pull/3737): POL-1683 AWS Oversized S3 Buckets - Datasource Not Defined fix

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> The AWS Oversized S3 Buckets currently fails due to an incorrect datasource reference. This issue was identified during a review of applied policies in Flexera, where the default template failed to execute correctly across multiple customer orgs.
>
> This change updates the policy to fix the datasource reference and prevent widespread failures.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md)
- **Merged At**: 2025-11-18 14:09:18 UTC

---

### PR [#3734](https://github.com/flexera-public/policy_templates/pull/3734): FOPTS-16588: Changes to fetch only ACTIVE recommendations by Google recommender service

*Minor Update*

#### Description

> Usage of google recommenders API. The Google Recommenders API returns duplicate recommendations for the same resource ID in different states i.e active, claimed, dismissed, succeeded, failed. fetching only those in the ACTIVE state is sufficient to resolve the duplicate recommendations.
>
> https://[raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations.pt](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations.pt)
>
> https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list#query-parameters
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-16588
>

#### Metadata

- **Policies**: [Google Rightsize VM Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_recommendations/README.md), [Meta Parent: Google Rightsize VM Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_vm_recommendations/README.md)
- **Merged At**: 2025-11-17 14:55:01 UTC

---

### PR [#3733](https://github.com/flexera-public/policy_templates/pull/3733): FOPTS-16584 Fetch only ACTIVE recommendations by google recommender service

*Minor Update*

#### Description

> <!-- Describe what this change achieves below -->
> Usage of google recommenders API. The Google Recommenders API returns duplicate recommendations for the same resource ID in different states i.e active, claimed, dismissed, succeeded, failed. "ACTIVE" includes recommendations that haven't been claimed, dismissed, succeeded, or failed yet in google cloud.
>
>
> https://[raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/recommender/recommender.pt](https://raw.githubusercontent.com/flexera-public/policy_templates/refs/heads/master/cost/google/recommender/recommender.pt)
>
> [https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list#query-parameters](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list#query-parameters)
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> [FOPTS-16584](https://flexera.atlassian.net/browse/FOPTS-16584)

#### Metadata

- **Policies**: [Google Recommenders](https://github.com/flexera-public/policy_templates/tree/master/cost/google/recommender/README.md), [Meta Parent: Google Recommenders](https://github.com/flexera-public/policy_templates/tree/master/cost/google/recommender/README.md)
- **Merged At**: 2025-11-17 13:49:11 UTC

---

### PR [#3748](https://github.com/flexera-public/policy_templates/pull/3748): Revert "FOAA-582 - Graceful error handling for inaccessible regions"

#### Description

> Reverts flexera-public/policy_templates#3742

#### Metadata

- **Policies**: [AWS Unused ECS Clusters](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/ecs_unused/README.md), [AWS Idle NAT Gateways](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/idle_nat_gateways/README.md), [AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md), [AWS Unused Application Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_albs/README.md), [AWS Unused Network Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_nlbs/README.md)
- **Merged At**: 2025-11-14 15:57:44 UTC

---

### PR [#3742](https://github.com/flexera-public/policy_templates/pull/3742): FOAA-582 - Graceful error handling for inaccessible regions

*Minor Update*

#### Description

> AWS policy templates can fail completely when encountering HTTP errors (403, 401, etc.) in any region due to permission issues, disabled regions, or SCPs.. This enhancement improves AWS Policy Templates from "all-or-nothing" to "best-effort" execution. This should improve user experience and minimize effort to generate recommendations.
>
> This is the second batch of policies for initial PR here: https://github.com/flexera-public/policy_templates/pull/3630
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-18272
> https://flexera.atlassian.net/browse/FOAA-582
>

#### Metadata

- **Policies**: [AWS Unused ECS Clusters](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/ecs_unused/README.md), [AWS Idle NAT Gateways](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/idle_nat_gateways/README.md), [AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md), [AWS Unused Application Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_albs/README.md), [AWS Unused Network Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_nlbs/README.md)
- **Merged At**: 2025-11-14 13:55:13 UTC

---

### PR [#3738](https://github.com/flexera-public/policy_templates/pull/3738): POL-1668 Azure Long Stopped Instances - Fix for currency adjustments 

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> When observing an applied policy for Azure Long Stopped Instances in a customer org, the policy produces savings amounts in DKK, where the expected behaviour is that it should show the savings amounts in EUR (the currency configuration for their Flexera org).
>
> This is a change to implement the fix for this. The savings amount now takes into account adjustments, such as currency conversion, while ignoring any shared cost related adjustments.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md)
- **Merged At**: 2025-11-13 17:07:00 UTC

---

### PR [#3732](https://github.com/flexera-public/policy_templates/pull/3732): POL-1681 Email Cost Optimization Recommendations Update

*Minor Update*

#### Description

> `Email Cost Optimization Recommendations`
> - Added support for Oracle recommendations.
> - Added support for additional recommendations for AWS, Azure, and Google.
>

#### Metadata

- **Policies**: [Email Cost Optimization Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/email_recommendations/README.md)
- **Merged At**: 2025-11-12 18:09:27 UTC

---

### PR [#3727](https://github.com/flexera-public/policy_templates/pull/3727): POL-1679 CSV Update Fixes

*Minor Update*

#### Description

> A handful of policy templates were not updating in the catalog due to minor errors introduced with the recent CSV updates. This is the fix.
>
> Dangerfile warnings can be ignored; they are false positives for things unrelated to this fix.
>

#### Metadata

- **Policies**: [AWS EKS Clusters Without Spot Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/eks_without_spot/README.md), [AWS Resources Under Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/extended_support/README.md), [Azure Hybrid Use Benefit for Linux Server](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_linux/README.md), [Azure Rightsize Synapse SQL Pools](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_synapse_sql_pools/README.md)
- **Merged At**: 2025-11-11 21:25:15 UTC

---

### PR [#3723](https://github.com/flexera-public/policy_templates/pull/3723): POL-1678 AWS Savings Plan Policy Template Fix

*Minor Update*

#### Description

> Fixes issue where policy template would error out instead of completing execution.
>
> Dangerfile warning can be ignored; no need to update README since this is just a bug fix.
>

#### Metadata

- **Policies**: [AWS Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/recommendations/README.md)
- **Merged At**: 2025-11-11 20:50:55 UTC

---

### PR [#3711](https://github.com/flexera-public/policy_templates/pull/3711): POL-1675 Flexera Onboarding Fix 

*Minor Update*

#### Description

> Fixes issue in the `Flexera Onboarding` policy template where policy execution would fail if no bill connects have been configured.
>

#### Metadata

- **Policies**: [Flexera Onboarding](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/onboarding/README.md)
- **Merged At**: 2025-11-10 14:07:24 UTC

---

### PR [#3705](https://github.com/flexera-public/policy_templates/pull/3705): POL-1672 Payment Option for Azure/Google RI/SP Policy Templates

*Minor Update*

#### Description

> This adds a "Payment Option" field to the incidents for the "Azure Reserved Instances Recommendations", "Azure Savings Plan Recommendations", and "Google Committed Use Discount Recommender" policy templates. This is to support upcoming UI functionality that uses this field and to align the policy templates more closely to their AWS counterparts.
>
> - For Azure, the user can select via parameter whether they want recommendations to show "No Upfront" or "All Upfront" for this field. Azure supports both, but because there is no difference in cost, savings, or eligibility based on whether you pay up front, there is no functional distinction between these with regards to recommendations.
> - Google only supports "No Upfront", so the value is always "No Upfront" for the "Google Committed Use Discount Recommender" policy template.
>
> The Dangerfile warning can be ignored. The above change does not require modifying the README for the "Google Committed Use Discount Recommender" policy template.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md), [Azure Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/recommendations/README.md), [Google Committed Use Discount Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cud_recommendations/README.md)
- **Merged At**: 2025-11-07 15:02:58 UTC

---

### PR [#3701](https://github.com/flexera-public/policy_templates/pull/3701): POL-1674 CSV Attachments: Google/Misc Policy Templates

*Unpublished, Minor Update*

#### Description

> Adds support for CSV attachments to Google policies and a handful of cloud-agnostic policies.
>
> Dangerfile warnings/errors are false positives and unrelated to these changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3701) for these details.
- **Merged At**: 2025-11-05 16:06:26 UTC

---

### PR [#3696](https://github.com/flexera-public/policy_templates/pull/3696): POL-1671 CSV Email Support: Azure Policy Templates

*Unpublished, Minor Update*

#### Description

> Updates Azure cost/operational/compliance policy templates to support sending incident tables as CSV files.
>
> Warnings/errors from Dangerfile are false positives unrelated to the above changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3696) for these details.
- **Merged At**: 2025-11-04 21:46:51 UTC

---

### PR [#3687](https://github.com/flexera-public/policy_templates/pull/3687): POL-1670 Deprecated Policy Template Cleanup

#### Description

> This PR removes most deprecated policy templates from the repository to avoid clutter. Most of these have been both deprecated and unpublished for a long time. They can still be retrieved historically in the repo in the very unlikely event that they are needed for something.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3687) for these details.
- **Merged At**: 2025-11-04 13:13:11 UTC

---

### PR [#3686](https://github.com/flexera-public/policy_templates/pull/3686): POL-1665 AWS Policy Templates: CSV Support

*Unpublished, Minor Update*

#### Description

> Adds support for emailing CSVs for various AWS policy templates.
>
> Also updates the meta policy generator to include support for this in meta policies, effectively enabling this feature for all meta policies.
>
> The Dangerfile warnings/errors are unrelated to these changes and can be ignored. They are false positives.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3686) for these details.
- **Merged At**: 2025-11-03 19:48:03 UTC

---

### PR [#3663](https://github.com/flexera-public/policy_templates/pull/3663): FOPTS-15982 Azure Superseded Compute Instances policy will consider data disk count.

*Major Update*

#### Description

> Azure Superseded Compute Instances policy will consider data disk count when recommending to upgrade VMs.
>
> The main logic is copied from Azure Rightsize Compute Instances policy.
> https://github.com/flexera-public/policy_templates/blob/master/cost/azure/rightsize_compute_instances/azure_compute_rightsizing.pt#L1236-L1291
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-19003
> https://flexera.atlassian.net/browse/FOPTS-15982
>

#### Metadata

- **Policies**: [Azure Superseded Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/superseded_instances/README.md), [Meta Parent: Azure Superseded Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/superseded_instances/README.md)
- **Merged At**: 2025-10-31 17:42:37 UTC

---

### PR [#3072](https://github.com/flexera-public/policy_templates/pull/3072): POL-1498 Google Flexera-Produced Recommendations

*Unpublished, New Policy Template, Minor Update*

#### Description

> Notes: Some small Dangerfile fixes were also included. Dead link warnings/errors can be ignored because those links will not be dead once this PR is merged.
>
> #### Google Old Snapshots
>
> This existing policy template has been updated to use Flexera CCO billing data to determine estimated savings instead of relying on list prices produced by the Google Cloud Billing API.
>
> #### Google Rightsize Cloud SQL Instances
>
> This is a new policy template for reporting Google rightsize recommendations for Cloud SQL Instances without using Google Recommender. It takes advantage of the new Google detailed billing functionality to report savings. Functionality includes a new feature that will eventually be implemented for AWS and Azure as well; cross-family recommendations.
>
> Additionally, to avoid confusion for users due to the increasingly large number of deprecated policy templates for Google, all Google Cloud SQL Instance recommendations policies are being unpublished except for this one and the `Google Rightsize Cloud SQL Recommender` policy template. That way, the user has two clear options in the catalog. The README for both this new policy template and `Google Rightsize Cloud SQL Recommender` explains the differences between the two policy templates.
>
> #### Google Rightsize VM Instances
>
> This is a new policy template for reporting Google rightsize recommendations for VMs without using Google Recommender. It takes advantage of the new Google detailed billing functionality to report savings. Functionality includes a new feature that will eventually be implemented for AWS and Azure as well; cross-family recommendations.
>
> Additionally, to avoid confusion for users due to the increasingly large number of deprecated policy templates for Google, all Google VM recommendations policies are being unpublished except for this one and the `Google Rightsize VM Recommender` policy template. That way, the user has two clear options in the catalog. The README for both this new policy template and `Google Rightsize VM Recommender` explains the differences between the two policy templates.
>
> #### Google Unused Disks
>
> This is a new policy template for reporting Google unused persistent disks without using Google Recommender. It takes advantage of the new Google detailed billing functionality to report savings. The README for both this new policy template and `Google Idle Persistent Disk Recommender` explains the differences between the two policy templates.
>
> #### Google Overutilized VM Instances
>
> This policy template was updated because, in building out the `Google Rightsize VM Instances` policy template, I discovered an issue with gathering stats, and that same code was in this policy. This is just me porting the fix over.
>
> #### Why there is no new IP address policy template
>
> After spending some significant time digging, it looks like Google does not log IP address detach events in a way that is straightforward to relate back to the actual IP address that was detached. You essentially have to find the attachment event in the logs and then find the detachment event associated with it, and there are several different ways an IP address can be attached all with different ways of being logged. Additionally, the new Google detailed billing info does *not* contain the resource IDs for IP addresses, making it impossible to provide savings based on actual spend.
>
> The above means that such a policy template would be so ineffectual compared to the one that uses Google's native recommendations as to make it pointless.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3072) for these details.
- **Merged At**: 2025-10-29 18:05:20 UTC

---

### PR [#3669](https://github.com/flexera-public/policy_templates/pull/3669): POL-1669 Repo Cleanup

*Unpublished, Minor Update*

#### Description

> `Style Update`
> - The below changes are to bring policy templates in line with the [Style Guide](https://github.com/flexera-public/policy_templates/blob/master/STYLE_GUIDE.md). Since code is commonly copied and pasted from existing policy templates, noncompliant code has a way of replicating itself if not removed from the repo entirely.
> - References to "policy" have been changed to "policy template" where appropriate throughout the repository. Where this involved updating a policy template itself, the policy template version was incremented and the CHANGELOG.md file was updated.
> - Changed parameters with the label "Email addresses to notify" to have the label "Email Addresses" instead for consistency. Where this involved updating a policy template itself, the policy template version was incremented and the CHANGELOG.md file was updated.
> - Removed defunct `tenancy "single"` line from the tiny number of policy templates that still contained it. All of them were deprecated already.
> - Fixed misc. linting errors in README.md files.
> - Fixed several URLs so that they no longer redirect. This prevents the text linter from believing they are dead URLs.
>
> `Dangerfile Fixes`
> - Dangerfile tests updated to account for the word template in the sentence "Deprecated: This policy template is no longer being updated"
> - Dangerfile tests have been updated to tolerate multiple footnote characters on a single permission in policy template README.md files. For example:   - \`ec2:TerminateInstances\`*‡
> - Dangerfile comma test has been updated to ignore lines containing image charts URL information to prevent false positives.
> - Dangerfile no longer reports a warning for new datasources if the policy template itself is new.
> - Dangerfile now filters textlint output to avoid reporting some common false positives, mainly for example or local URLs in documentation that won't pass as valid links when tested.
> - Dangerfile test for a policy template being unpublished now raises a message instead of a warning since this is rarely unintentional.
> - Dangerfile test for mismatched script/datasource names no longer raises a warning if the script block is called by multiple datasources. This logic was already in place but was not working correctly.
>
> `devcontainer`
> - Fixed outdated reference in devcontainer.json with up to date one.
>
> `Spelling`
> - .spellignore has been updated to ignore "FSx" and "fsx"
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3669) for these details.
- **Merged At**: 2025-10-29 17:20:39 UTC

---

### PR [#3658](https://github.com/flexera-public/policy_templates/pull/3658): POL-1661 AWS Overutilized EC2 Instances  - Capture Missing Memory Stats for Instances in Incident

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change fixes a gap where memory usage data from CloudWatch wasn’t being captured in the policy for many EC2 instances. This fix ensures users now get a more complete picture when reviewing overutilization recommendations for EC2 instances across both CPU and Memory metrics.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Tested this in a customer org.
>

#### Metadata

- **Policies**: [AWS Overutilized EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/overutilized_ec2_instances/README.md)
- **Merged At**: 2025-10-22 13:02:39 UTC

---

### PR [#3648](https://github.com/flexera-public/policy_templates/pull/3648): FOPTS-15895 Fixed Azure Rightsize SQL Databases policy not showing metrics for DTU database.

*Bug Fix*

#### Description

> Fixed Azure Rightsize SQL Databases policy not showing metrics for DTU databases.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-15895
> https://flexera.atlassian.net/browse/SQ-18478
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md), [Meta Parent: Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2025-10-16 17:32:58 UTC

---

### PR [#3641](https://github.com/flexera-public/policy_templates/pull/3641): POL-1664 AWS Rightsize EC2 Instances - Capture Missing Memory Stats for Windows Instances in Incident

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change fixes a gap where memory usage data from CloudWatch wasn’t being captured in the policy for many EC2 instances.
>
> The previous fix seen in https://github.com/flexera-public/policy_templates/pull/3613 fixed the issue for Linux instances, however the problem persisted for Windows instances. This change addresses that.
>
> This fix ensures users now get a more complete picture when reviewing rightsizing recommendations across both CPU and Memory metrics for both Windows and Linux instances.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md)
- **Merged At**: 2025-10-16 12:56:42 UTC

---

### PR [#3634](https://github.com/flexera-public/policy_templates/pull/3634): POL-1653 Spot Ocean Common Bill Ingestion - Add Cloud Vendor Account Name and Service Dimensions

*New Policy Template*

#### Description

> <!-- Describe what this change achieves below -->
> This update improves consistency and data completeness for the Spot Ocean Common Bill Ingestion policy. Specifically:
>
> - Renamed the policy to align with naming conventions used across other Common Bill Ingestion policies.
> - Enhanced the policy to now populate the `Cloud Vendor Account Name` and `Service` dimensions, enabling more accurate reporting and filtering.
>
> These changes support better integration with CCO workflows and improve clarity for downstream users.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Spot Ocean Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/spot/ocean_cbi/README.md)
- **Merged At**: 2025-10-16 12:56:23 UTC

---

### PR [#3636](https://github.com/flexera-public/policy_templates/pull/3636): POL-1598 Azure Rightsize Compute Instances / Long Stopped Compute Instances Better Cost Gathering

*Minor Update*

#### Description

> Improves the `Azure Rightsize Compute Instances` and `Azure Long Stopped Compute Instances` policy templates to use better filters when gathering costs. This should result in more relevant results and reduce the risk of the output exceeding 100,000 responses and resulting in some costs being missed.
>

#### Metadata

- **Policies**: [Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md), [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2025-10-15 19:39:39 UTC

---

### PR [#3629](https://github.com/flexera-public/policy_templates/pull/3629): POL-1658 New Policy Template: Azure Deprecated Storage Accounts

*New Policy Template*

#### Description

> `Azure Deprecated Storage Accounts`
> - This policy template reports any active GPv1 Azure Storage Accounts and, optionally, emails this report. Microsoft has deprecated these Storage Accounts and will be migrating them to GPv2 in October 2026.
>
> Also includes a small Dangerfile test fix to prevent false positives on the deprecated policy tests.
>

#### Metadata

- **Policies**: [Azure Deprecated Storage Accounts](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/deprecated_storage_accounts/README.md), [Meta Parent: Azure Deprecated Storage Accounts](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/deprecated_storage_accounts/README.md)
- **Merged At**: 2025-10-13 19:36:25 UTC

---

### PR [#3619](https://github.com/flexera-public/policy_templates/pull/3619): FOPTS-0000 - Spot Ocean CBI update to daily schedule

*Bug Fix*

#### Description

> Quick fix to update default policy schedule

#### Metadata

- **Policies**: [Spot Ocean Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/spot/ocean_cbi/README.md)
- **Merged At**: 2025-10-13 08:45:57 UTC

---

### PR [#3613](https://github.com/flexera-public/policy_templates/pull/3613): POL-1650 AWS Rightsize EC2 Instances - Capture Missing Memory Stats in Incident

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
>
> ### Issues Resolved
> This change fixes a gap where memory usage data from CloudWatch wasn’t being captured in the policy for many EC2 instances. This fix ensures users now get a more complete picture when reviewing rightsizing recommendations across both CPU and Memory metrics.
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md)
- **Merged At**: 2025-10-09 17:05:21 UTC

---

### PR [#3610](https://github.com/flexera-public/policy_templates/pull/3610): POL-1652 AWS Reserved Instances Recommendations - Update Account Scope Parameter description in README

#### Description

> <!-- Describe what this change achieves below -->
> This change updates the description of the "Account Scope" parameter for greater clarity.
>
> This clarification aligns with AWS's documentation and avoids misinterpretation by users applying the policy.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/recommendations/README.md)
- **Merged At**: 2025-10-09 14:27:05 UTC

---

### PR [#3607](https://github.com/flexera-public/policy_templates/pull/3607): POL-1651 Remove "15 minutes" and "Hourly" child schedule options

*Minor Update*

#### Description

> Removes the "15 minutes" and "Hourly" child schedule options from most meta policies. Adds logic in the meta parent compiler to allow for exceptions if the info() block contains enable_child_schedule_options: "true"

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3607) for these details.
- **Merged At**: 2025-10-07 15:01:14 UTC

---

### PR [#3591](https://github.com/flexera-public/policy_templates/pull/3591): POL-1589 Deprecate AWS Savings Realized From Rate Reduction Purchases Policy Template

*Minor Update*

#### Description

> Deprecates `AWS Savings Realized From Rate Reduction Purchases` in favor of more accurate, native product functionality.
>

#### Metadata

- **Policies**: [AWS Savings Realized From Rate Reduction Purchases](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_realized/README.md)
- **Merged At**: 2025-09-26 14:56:05 UTC

---

### PR [#3587](https://github.com/flexera-public/policy_templates/pull/3587): POL-1631 AWS Load Balancer Savings Fixes

*Minor Update*

#### Description

> `AWS Unused Application Load Balancers`
> - Fixed issue where estimated savings would sometimes be reported as 0 inaccurately.
>
> `AWS Unused Classic Load Balancers`
> - Fixed issue where estimated savings would sometimes be reported as 0 inaccurately.
> - Fixed issue where `Resource ARN` field was malformed.
>
> `AWS Unused Network Load Balancers`
> - Fixed issue where estimated savings would sometimes be reported as 0 inaccurately.
>

#### Metadata

- **Policies**: [AWS Unused Application Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_albs/README.md), [AWS Unused Classic Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_clbs/README.md), [AWS Unused Network Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_nlbs/README.md)
- **Merged At**: 2025-09-26 13:34:46 UTC

---

### PR [#3583](https://github.com/flexera-public/policy_templates/pull/3583): POL-1634 New Policy: Oracle Cloud Advisor: Rightsize Autonomous Database Service

*New Policy Template*

#### Description

> `Oracle Cloud Advisor: Rightsize Autonomous Database Service`
> - New recommendation policy template.
>

#### Metadata

- **Policies**: [Oracle Cloud Advisor: Rightsize Autonomous Database Service](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_rightsize_autodbs/README.md)
- **Merged At**: 2025-09-25 17:03:04 UTC

---

### PR [#3578](https://github.com/flexera-public/policy_templates/pull/3578): POL-1630 New Policy: Oracle Cloud Advisor: Rightsize Load Balancers

*New Policy Template, Minor Update*

#### Description

> `Oracle Cloud Advisor: Rightsize Load Balancers`
> - This policy template reports on any existing underutilized Load Balancer recommendations generated by Oracle Cloud Advisor.
>
> `Oracle Cloud Advisor: Rightsize Virtual Machines`
> - Fixed small grammatical error in README
>
> `Oracle Cloud Advisor: Unattached Volumes`
> - Fixed issue where a DELETE request was incorrectly logged as a PUT request. Functionality unchanged.
>

#### Metadata

- **Policies**: [Oracle Cloud Advisor: Rightsize Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_rightsize_lbs/README.md), [Oracle Cloud Advisor: Unattached Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_unattached_volumes/README.md)
- **Merged At**: 2025-09-24 17:06:58 UTC

---

### PR [#3574](https://github.com/flexera-public/policy_templates/pull/3574): POL-1629 New Policy: Oracle Cloud Advisor: Object Storage Without Lifecycle Management

*New Policy Template*

#### Description

> `Oracle Cloud Advisor: Object Storage Without Lifecycle Management`
> - This policy template reports on any existing Object Storage lifecycle management recommendations generated by Oracle Cloud Advisor.
>

#### Metadata

- **Policies**: [Oracle Cloud Advisor: Object Storage Without Lifecycle Management](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_lifecycle_mgmt/README.md)
- **Merged At**: 2025-09-24 15:14:16 UTC

---

### PR [#3570](https://github.com/flexera-public/policy_templates/pull/3570): POL-1628 New Policy: Oracle Cloud Advisor: Unattached Volumes

*New Policy Template, Minor Update*

#### Description

> `Oracle Cloud Advisor: Unattached Volumes`
> - New policy template
>
> `Oracle Cloud Advisor: Rightsize Virtual Machines`
> - Fixed issue where estimated savings value had all fractional values rounded away
>
> `Oracle Cloud Advisor: Rightsize Base Database Service`
> - Fixed issue where estimated savings value had all fractional values rounded away
>

#### Metadata

- **Policies**: [Oracle Cloud Advisor: Rightsize Base Database Service](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_rightsize_basedbs/README.md), [Oracle Cloud Advisor: Rightsize Virtual Machines](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_rightsize_vms/README.md), [Oracle Cloud Advisor: Unattached Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_unattached_volumes/README.md)
- **Merged At**: 2025-09-23 15:37:12 UTC

---

### PR [#3566](https://github.com/flexera-public/policy_templates/pull/3566): POL-1627 Oracle Cloud Advisor: Rightsize Base Database Service

*New Policy Template, Minor Update*

#### Description

> Oracle Cloud Advisor: Rightsize Base Database Service
> - New policy template to report cloud advisor recommendations for the Oracle Base Database Service
>
> Oracle Cloud Advisor: Rightsize Virtual Machines
> - Fixed issue where estimated savings value would sometimes be incorrectly inflated
>

#### Metadata

- **Policies**: [Oracle Cloud Advisor: Rightsize Base Database Service](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_rightsize_basedbs/README.md), [Oracle Cloud Advisor: Rightsize Virtual Machines](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_rightsize_vms/README.md)
- **Merged At**: 2025-09-22 20:07:14 UTC

---

### PR [#3550](https://github.com/flexera-public/policy_templates/pull/3550): POL-1600 Oracle Rightsizing VMs Improvements

*Major Update, Minor Update*

#### Description

> - Multiple improvements for the `Oracle Cloud Advisor: Rightsize Virtual Machines` policy template based on user feedback.
> - Improvements to the README for the `Oracle Cloud Common Bill Ingestion` policy template.
> - Automation to gather and store Oracle credential permissions has been implemented.
>
> Dead link warnings can be ignored; the links will be valid once this PR is merged.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3550) for these details.
- **Merged At**: 2025-09-22 14:25:38 UTC

---

### PR [#3552](https://github.com/flexera-public/policy_templates/pull/3552): POL-1626 Currency Conversion - Bring Adjustments Forward

*Minor Update*

#### Description

> Added a parameter to bring adjustments forward to the `Currency Conversion` policy template. From the updated README:
>
> - *Bring Adjustments Forward* - Whether to automatically fill months with no adjustments with the adjustments from the previous month.
>   - Example: You run this policy template in June 2025 and you choose to backfill starting in January 2025. You currently only have adjustment rules for January 2025 and March 2025.
>     - With this option enabled, the existing adjustment rules for January 2025 will be carried forward to February, and existing rules for March 2025 will be carried forward to April, May, and June.
>     - With this option disabled, the only adjustment rules for March, April, May, and June will be the currency conversion adjustment created by this policy template. This means, for those months, the rules configured for January 2025 and March 2025 respectively will no longer apply for those months when they did previously.
>
> Also replaced a broken link in the README with a working one.
>
> Also made some small tweaks to the ESLint YAML file so that JavaScript is linted by the same standards we use in policy templates.
>

#### Metadata

- **Policies**: [Currency Conversion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/currency_conversion/README.md)
- **Merged At**: 2025-09-17 20:51:32 UTC

---

### PR [#3540](https://github.com/flexera-public/policy_templates/pull/3540): FOPTS-14803 Fixed Cloud Cost Anomaly Alerts PT Email

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> Resolved an issue causing Anomaly detection incident emails to render as plain text rather than HTML.
> [cloud_cost_anomaly_alerts.pt](https://raw.githubusercontent.com/flexera-public/policy_templates/e1899b3fe33e0cedbbfc1f4072e827eed774ec9b/cost/flexera/cco/cloud_cost_anomaly_alerts/cloud_cost_anomaly_alerts.pt)
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> [https://flexera.atlassian.net/browse/FOPTS-14803](https://flexera.atlassian.net/browse/FOPTS-14803)
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2025-09-12 18:40:43 UTC

---

### PR [#3535](https://github.com/flexera-public/policy_templates/pull/3535): POL-1612 Update AWS policies using GetMetricData API to remove "Action" Query Parameter (POL-1618, POL-1619, POL-1620, POL-1621, POL-1622) 

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change fixes an error related to AWS's GetMetricData API which various AWS policies use to gather resource metrics. As suggested by AWS, this change removes the `Action=GetMetricData` query parameter from the API request.
>
> This specific change covers the fix for the following policies:
>
> - AWS Long Stopped EC2 Instances
> - AWS Oversized S3 Buckets
> - AWS Rightsize Redshift
> - AWS Rightsize Elasticache
> - AWS Burstable EC2 Instances
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Long Stopped EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/long_stopped_instances/README.md), [AWS Burstable EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/burstable_ec2_instances/README.md), [AWS Rightsize ElastiCache](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_elasticache/README.md), [AWS Rightsize Redshift](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_redshift/README.md), [AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md)
- **Merged At**: 2025-09-12 12:43:37 UTC

---

### PR [#3534](https://github.com/flexera-public/policy_templates/pull/3534): POL-1612 Update AWS policies using GetMetricData API to remove "Action" Query Parameter (POL-1614, POL-1615, POL-1616, POL-1617)

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change fixes an error related to AWS's GetMetricData API which various AWS policies use to gather resource metrics. As suggested by AWS, this change removes the `Action=GetMetricData` query parameter from the API request.
>
> This specific change covers the fix for the following policies:
> - AWS Rightsize EC2 Instances
> - AWS Rightsize EBS Volumes
> - AWS Rightsize RDS Instances
> - AWS Overutilized EC2 Instances
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/README.md), [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md), [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md), [AWS Overutilized EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/overutilized_ec2_instances/README.md)
- **Merged At**: 2025-09-12 12:42:29 UTC

---

### PR [#3531](https://github.com/flexera-public/policy_templates/pull/3531): POL-1613 Multiple Key Support for RBD Policies

*Unpublished, Major Update*

#### Description

> This adds the ability to specify multiple keys for a single dimension by using semicolons in order to deal with poor tag hygiene. This is similar to the native Tag Dimension functionality for resource tags.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3531) for these details.
- **Merged At**: 2025-09-11 13:36:23 UTC

---

### PR [#2313](https://github.com/flexera-public/policy_templates/pull/2313): POL-1083 Azure Reserved Instances Utilization Revamp

*Major Update, Minor Update*

#### Description

> This is a revamp of the Azure Reserved Instances Utilization policy. It has been completely retooled to use internal Flexera APIs, similar to the same-named AWS policy. From the CHANGELOG:
>
> - Policy has fundamentally been reworked to use internal Flexera API
> - Azure credential is no longer required
> - Report can now use either maximum or average utilization when assessing reservations
> - Normalized incident output for parity with other policy templates
>
> NOTE: The internal Flexera API for this now fully supports Azure MCA. For this reason, the MCA-specific version of this policy is being deprecated.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/utilization/README.md)
- **Merged At**: 2025-09-09 18:14:01 UTC

---

### PR [#3509](https://github.com/flexera-public/policy_templates/pull/3509): FOPTS-14501 Update last start/stop status to 'No Action' when Flexera has not performed any action

*Minor Update*

#### Description

> `Azure Schedule Instance Policy`
>
> This PR modifies the incident output action table so that the `last_start_status` and `last_stop_status` fields now display `No Action` instead of `Unknown` when Flexera has not executed a start or stop action.
>
> ### Issues Resolved
>
> https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=68bb98241b0befcdc03d2bdc
>
> <img width="1588" height="361" alt="image" src="https://github.com/user-attachments/assets/d7437ad8-bb4b-466d-82de-bf108fad292a" />
>

#### Metadata

- **Policies**: [Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md)
- **Merged At**: 2025-09-09 17:27:00 UTC

---

### PR [#3520](https://github.com/flexera-public/policy_templates/pull/3520): POL-1609 Azure Usage Report - Instance Time Used Fix

*Minor Update*

#### Description

> Fixes issue where Azure Usage Report - Instance Time Used policy incident listed the instance family for all instances as "undefined".
>
> - The root cause is that the CSV containing the instance families is provided by Azure and they started putting double-quotes around the fields in the CSV file. This conforms to the CSV spec but since we didn't account for this in our ad hoc parsing of the CSV file, it broke the policy template.
>
> - To avoid possible issues in the future, a Github workflow now grabs and parses this file using proper CSV parsing tooling native to Python and then stores the result in a JSON file in the repository that the policy template will then use instead.
>
> Also adds an example image to the README. The above issue was actually discovered while trying to get this image.
>

#### Metadata

- **Policies**: [Azure Usage Report - Instance Time Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_usage_report/README.md)
- **Merged At**: 2025-09-08 19:03:04 UTC

---

### PR [#3504](https://github.com/flexera-public/policy_templates/pull/3504): POL-1588 AWS Savings Plan Recommendations: Rename Incident Field

*Minor Update*

#### Description

>  `AWS Savings Plan Recommendations`
> - Changed incident field "Recommendeded Quantity to Purchase" to "Recommended Hourly Commitment" to both correct a spelling error and make the field clearer.
>

#### Metadata

- **Policies**: [AWS Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/recommendations/README.md)
- **Merged At**: 2025-09-05 18:54:18 UTC

---

### PR [#3363](https://github.com/flexera-public/policy_templates/pull/3363): POL-1567 - Removed batch processing for large datasources to improve policy reliability and performance

*Minor Update*

#### Description

> Removed batch processing for large datasources to improve policy reliability and performance
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1567
>

#### Metadata

- **Policies**: [Azure Databricks Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/databricks/rightsize_compute/README.md), [Meta Parent: Azure Databricks Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/databricks/rightsize_compute/README.md)
- **Merged At**: 2025-09-05 17:58:32 UTC

---

### PR [#3474](https://github.com/flexera-public/policy_templates/pull/3474): fix: js_make_terminate_request gracefully handle if policy_id not def…

*Unpublished*

#### Description

> Updates the `js_make_terminate_request` script to gracefully handle when policy_id is not set (i.e. during retrieve_data).  This snippet is used for "Meta" capabilities in the child policy template, and today it causes an error during local development.
>
> This change, combined with https://github.com/flexera-public/policy_sdk/pull/43 should enable most catalog policy templates to run `retrieve_data` without any need to modify the template, which should improve the policy developers QoL.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3474) for these details.
- **Merged At**: 2025-09-04 17:56:41 UTC

---

### PR [#3397](https://github.com/flexera-public/policy_templates/pull/3397): FOAA-307 - New Template Dynamic Dashboards

*New Policy Template, Minor Update*

#### Description

> This policy template creates dynamic dashboards based on cost data aggregated by user-specified dimensions over the previous 12 months. For each unique value of the selected dashboard dimension, the policy creates a dashboard showcasing the top N widget dimension values by cost. This enables automatic creation of focused cost dashboards for different organizational segments (vendors, regions, services, etc.).
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-307
>

#### Metadata

- **Policies**: [Dynamic Dashboards](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/dynamic_dashboards/README.md)
- **Merged At**: 2025-09-04 17:28:27 UTC

---

### PR [#3492](https://github.com/flexera-public/policy_templates/pull/3492): POL-1599 Oracle Cloud Common Bill Ingestion Fix

*Minor Update*

#### Description

> Fixes some incorrectly referenced variables that would cause the policy template to fail.
>

#### Metadata

- **Policies**: [Oracle Cloud Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/oracle_cbi/README.md)
- **Merged At**: 2025-09-04 13:13:12 UTC

---

### PR [#3396](https://github.com/flexera-public/policy_templates/pull/3396): FOAA-307 - New Template: Generic Meta Parent

*New Policy Template, Minor Update*

#### Description

> This generic meta parent policy template dynamically creates and manages child policies based on cost dimensions from the Flexera Bill Analysis API. Unlike traditional meta parent policies that are pre-compiled for specific child policy templates, this policy uses parameters so it is very extendable and can be used for many use-cases.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-307
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3396) for details about unpublished policies.
- **Merged At**: 2025-09-03 20:44:23 UTC

---

### PR [#3487](https://github.com/flexera-public/policy_templates/pull/3487): POL-743 New Policy Template: Oracle Cloud Advisor: Rightsize Virtual Machines

*New Policy Template*

#### Description

> This policy template reports on any existing idle and underutilized virtual machine recommendations generated by Oracle Cloud Advisor. Optionally, this report can be emailed.
>
> This is a functioning first pass. There will undoubtedly be improvements as we get user feedback and a better understanding of how to manipulate Oracle's APIs.
>

#### Metadata

- **Policies**: [Oracle Cloud Advisor: Rightsize Virtual Machines](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/advisor_rightsize_vms/README.md)
- **Merged At**: 2025-09-03 13:14:36 UTC

---

### PR [#3473](https://github.com/flexera-public/policy_templates/pull/3473): FOAA-343 - fix: Azure Tag Cardinality subscription filtering

*Bug Fix*

#### Description

> Fixes subscription filtering in Azure Tag Cardinality PT.  Currently was iterating over all subscriptions to inventory RGs + resources which is not expected.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-342
>

#### Metadata

- **Policies**: [Azure Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/tag_cardinality/README.md)
- **Merged At**: 2025-09-02 13:43:46 UTC

---

