# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

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

- **Policies**: [Azure Reserved Instances Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/utilization/README.md), [Azure Reserved Instances Utilization MCA](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/utilization_mca/README.md)
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

### PR [#3475](https://github.com/flexera-public/policy_templates/pull/3475): POL-1582 - fix: superseded_nfu lookup

*Bug Fix*

#### Description

> Fixed lookup when using NFU comparison for estimated savings.  This was causing estimated savings to be $0 for a lot of instances when NFU comparison method was used.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1582
>

#### Metadata

- **Policies**: [Azure Superseded Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/superseded_instances/README.md)
- **Merged At**: 2025-09-02 13:43:22 UTC

---

### PR [#3446](https://github.com/flexera-public/policy_templates/pull/3446): FOPTS-12555 Use actual cost to calculate savings for AWS superseded instance policy

*Major Update*

#### Description

> Similar to #3393, but this PR is for AWS.
>
> Changed how savings is calculated.
> Savings will be calculated using actual cost, multiplied by the percentage difference between the "list price" (or "NFU" if "list price" does not exists) of the current instance type and the recommended instance type.
>
> This new calculation method aligns with [AWS Rightsize RDS](https://github.com/flexera-public/policy_templates/blob/master/cost/aws/rightsize_rds_instances/README.md#policy-savings-details).
>
> ----
>
> Also fixed a bug related to "fallback instance type".
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-12555
> https://flexera.atlassian.net/browse/SQ-16042
>

#### Metadata

- **Policies**: [AWS Superseded EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_instances/README.md), [Meta Parent: AWS Superseded EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_instances/README.md)
- **Merged At**: 2025-08-21 16:10:01 UTC

---

### PR [#3452](https://github.com/flexera-public/policy_templates/pull/3452): FOAA-327 - Spot Ocean Recommendations - Add support for collecting Azure and GCP cluster rightsizing recommendations

*Minor Update*

#### Description

> ## Description
>
> Adds support for Azure Kubernetes Service (AKS) and Google Kubernetes Engine (GKE) cluster rightsizing recommendations (previously AWS EKS only).
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-327
>

#### Metadata

- **Policies**: [Kubernetes - Rightsizing Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/spot/ocean_recommendations/README.md)
- **Merged At**: 2025-08-21 15:57:46 UTC

---

### PR [#3451](https://github.com/flexera-public/policy_templates/pull/3451): FOAA-327 - Spot Ocean CBI - Add support for collecting Azure and GCP cluster cost data

*Minor Update*

#### Description

> Adds support for AKS and GKE (previously AWS EKS only)
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-327
>

#### Metadata

- **Policies**: [Spot Ocean Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/spot/ocean_cbi/README.md)
- **Merged At**: 2025-08-21 15:39:43 UTC

---

### PR [#3453](https://github.com/flexera-public/policy_templates/pull/3453): POL-1575 New Policy: Percentage Cost Common Bill Ingestion

*New Policy Template*

#### Description

> New policy template `Percentage Cost Common Bill Ingestion`. Similar to the `Fixed Cost Common Bill Ingestion` policy template, except it calculates the cost as a percentage of total cloud spend, with optional filtering.
>

#### Metadata

- **Policies**: [Percentage Cost Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/percentage_cost_cbi/README.md)
- **Merged At**: 2025-08-20 20:49:38 UTC

---

### PR [#3445](https://github.com/flexera-public/policy_templates/pull/3445): POL-1586 Fixed Cost Common Bill Ingestion Improvements

*Minor Update*

#### Description

> `Fixed Cost Common Bill Ingestion`.
> - Adds the option to do the fixed cost as a lump sum on the 1st of the month instead of amortizing it.
> - Regex for "CBI (Common Bill Ingestion) Endpoint ID" parameter now allows names to contain additional `-` and `_` characters.
> - Increased the precision of the amortization calculation by a couple of decimal places to reduce the risk of rounding errors e.g. $500 showing up as $499.99 when looking at monthly costs.
>

#### Metadata

- **Policies**: [Fixed Cost Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/fixed_cost_cbi/README.md)
- **Merged At**: 2025-08-19 18:28:32 UTC

---

### PR [#3442](https://github.com/flexera-public/policy_templates/pull/3442): POL-1584 Orgs and Clouds Vendor Accounts Deprecation

*Unpublished, Minor Update*

#### Description

> Due to its reliance on unofficial APIs and the fact that there are zero instances of this policy template actually being used, the `Orgs and Clouds Vendor Accounts` policy template is being deprecated.
>
> The template remains in the repository in case someone does actually need it; this PR does not delete it. The only real change is that users (if they ever exist) will be informed that this policy template is deprecated before use.

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3442) for details about unpublished policies.
- **Merged At**: 2025-08-18 20:38:22 UTC

---

### PR [#3438](https://github.com/flexera-public/policy_templates/pull/3438): POL-1583 AWS S3 Usage Type Rule-Based Dimension API Update

*Unpublished, Minor Update*

#### Description

> Updates the `AWS S3 Usage Type Rule-Based Dimension` policy template to use newer Flexera APIs.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3438) for details about unpublished policies.
- **Merged At**: 2025-08-18 17:39:32 UTC

---

### PR [#3393](https://github.com/flexera-public/policy_templates/pull/3393): FOPTS-12555 Use actual cost to calculate savings for superseded instances.

*Major Update*

#### Description

> Changed how savings is calculated.
> Savings will be calculated using actual cost, multiplied by the percentage difference between the "list price" (or "NFU" if "list price" does not exists) of the current instance type and the recommended instance type.
>
> This new calculation method aligns with [AWS Rightsize RDS](https://github.com/flexera-public/policy_templates/blob/master/cost/aws/rightsize_rds_instances/README.md#policy-savings-details).
>
> ----
> Also switched from `data/azure/instance_types.json` to `data/azure/azure_compute_instance_types.json`.
>
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOPTS-12555
> https://flexera.atlassian.net/browse/SQ-16042
>

#### Metadata

- **Policies**: [Azure Superseded Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/superseded_instances/README.md), [Meta Parent: Azure Superseded Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/superseded_instances/README.md)
- **Merged At**: 2025-08-18 17:19:04 UTC

---

### PR [#3398](https://github.com/flexera-public/policy_templates/pull/3398): FOAA-307 - Cloud Cost Anomaly Alerts - Improved anomaly filtering and sorting logic, improved report formatting

*Major Update*

#### Description

> Improved anomaly filtering and sorting logic, improved report formatting
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-307
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2025-08-18 15:18:48 UTC

---

### PR [#3426](https://github.com/flexera-public/policy_templates/pull/3426): POL-1581 Meta Child API Update

*Unpublished, Minor Update*

#### Description

> This PR updates the code for child policies to use the new APIs, and updates meta policy documentation accordingly.
>
> This also updates some policy templates to use the new API endpoint for getting policy information about themselves that were missed in the first pass.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3426) for these details.
- **Merged At**: 2025-08-15 20:18:43 UTC

---

### PR [#3423](https://github.com/flexera-public/policy_templates/pull/3423): POL-1580 Policy API Updates

*Minor Update*

#### Description

> This updates the following policy templates to use the newer api.flexera.com APIs where applicable. Functionality is unchanged.
>
> * Automation Reports
> * Applied Policy Template Errors
> * Flexera Automation Outdated Applied Policies
>

#### Metadata

- **Policies**: [Flexera Automation Outdated Applied Policies](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/outdated_applied_policies/README.md), [Applied Policy Template Errors](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/automation/applied_policy_error_notification/README.md), [Automation Reports](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/automation/automation_reports/README.md)
- **Merged At**: 2025-08-15 14:13:18 UTC

---

### PR [#3418](https://github.com/flexera-public/policy_templates/pull/3418): SQ-17255 - fix: mapping in ds_flexera_api_hosts

*Minor Update, Bug Fix*

#### Description

> - Fixes mapping in datasource `ds_flexera_api_hosts` which as causing error during evaluation: "invalid request host", "host must be a string" for the Scheduled Instance Policy Templates
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-17255
>

#### Metadata

- **Policies**: [AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md), [Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2025-08-14 23:56:10 UTC

---

### PR [#3410](https://github.com/flexera-public/policy_templates/pull/3410): POL-1577 - fix: max/min selection method

*Minor Update, Bug Fix*

#### Description

> Fixes issue that was causing incorrect Max or minimum values to get selected
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1577
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2025-08-14 23:55:00 UTC

---

### PR [#3395](https://github.com/flexera-public/policy_templates/pull/3395): POL-1573 API Update

*Unpublished, Minor Update*

#### Description

> Updates most policy templates to get metadata about themselves using the newer APIs at flexera.com instead of the governance APIs.
>
> This does not update meta parent policies or update other API calls to the governance APIs. This is part 1 in a larger piece of work.
>
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=6895fc931b706bb1b63f0ed8
>
> The Dangerfile errors/warnings are for stuff that already exists in these policy templates that are not relevant to this change.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3395) for these details.
- **Merged At**: 2025-08-13 18:26:14 UTC

---

### PR [#3394](https://github.com/flexera-public/policy_templates/pull/3394): FOAA-307 - Scheduled Report fix issue with ignore current mont and month granularity

*Minor Update, Bug Fix*

#### Description

> Fixes issue with ignore current month and month granularity with the expected outcome that the result would show 1 month in the chart and it would be the previous month.  Currently it's showing 2 months (current and previous)
>
> ### Issues Resolved
>
> Identified during work related to https://flexera.atlassian.net/browse/FOAA-307
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2025-08-11 16:13:00 UTC

---

### PR [#3399](https://github.com/flexera-public/policy_templates/pull/3399): POL-1576 Flexera Billing Centers from Dimension Values Fix

*Minor Update*

#### Description

> Flexera Billing Centers from Dimension Values: Fixed bug where billing center hierarchy would be incorrectly implemented due to the order of dimensions changing during execution.
>

#### Metadata

- **Policies**: [Flexera Billing Centers from Dimension Values](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/billing_centers_from_dimensions/README.md)
- **Merged At**: 2025-08-08 16:08:55 UTC

---

### PR [#3388](https://github.com/flexera-public/policy_templates/pull/3388): POL-1548 Azure Unused Storage Accounts

*New Policy Template*

#### Description

> New policy template `Azure Unused Storage Accounts`. From the README:
>
> This policy template reports Azure Storage Accounts that have had fewer than a user-specified number of transactions over a user specified number of days and, optionally, deletes them. A transaction is any API operation or action that interacts with the storage service, including reading, writing, or deleting data, as well as metadata operations.
>

#### Metadata

- **Policies**: [Azure Unused Storage Accounts](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_storage_accounts/README.md)
- **Merged At**: 2025-08-05 16:21:38 UTC

---

### PR [#3375](https://github.com/flexera-public/policy_templates/pull/3375): POL-1572 Automation Reports

*New Policy Template*

#### Description

> New policy template `Automation Reports`. From the README:
>
> This policy template generates reports on various aspects of automation within the Flexera One platform. The user can select to generate reports on applied policies, policy templates, and incidents. Optionally, these reports can be emailed.
>
> Note: Dangerfile warning is false positive. This is a brand new policy template.
>

#### Metadata

- **Policies**: [Automation Reports](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/automation/automation_reports/README.md)
- **Merged At**: 2025-08-04 12:13:52 UTC

---

### PR [#3372](https://github.com/flexera-public/policy_templates/pull/3372): POL-1571 AWS S3 Buckets Accepting HTTP Requests - fix 'cannot access member' error

*Minor Update, Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change updates fixes an issue where applied policies fail due to an undefined field in some scenarios. It also fixes an issue where false positive recommendations are produced in policy incidents.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [AWS S3 Buckets Accepting HTTP Requests](https://github.com/flexera-public/policy_templates/tree/master/security/aws/s3_buckets_deny_http/README.md), [Meta Parent: AWS S3 Buckets Accepting HTTP Requests](https://github.com/flexera-public/policy_templates/tree/master/security/aws/s3_buckets_deny_http/README.md)
- **Merged At**: 2025-08-01 17:37:35 UTC

---

### PR [#3368](https://github.com/flexera-public/policy_templates/pull/3368): POL-1569 Flexera Billing Centers from Dimension Values Improvement

*Minor Update*

#### Description

> `Flexera Billing Centers from Dimension Values` policy template will now create the rbd_bc dimension if it doesn't already exist. The README has also been updated to clean things up a bit and fix some Markdown errors.
>
> From the CHANGELOG:
> - Policy execution will no longer fail if the "rbd_bc" Rule-Based Dimension doesn't already exist.
> - Minor tweaks to bring policy template in compliance with best practices.
>

#### Metadata

- **Policies**: [Flexera Billing Centers from Dimension Values](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/billing_centers_from_dimensions/README.md)
- **Merged At**: 2025-07-30 19:10:01 UTC

---

### PR [#3350](https://github.com/flexera-public/policy_templates/pull/3350): POL-1566 Oracle Cloud Common Bill Ingestion: Custom Bucket Support

*Minor Update*

#### Description

> Oracle Cloud Common Bill Ingestion
> - Added additional parameters to allow user to gather cost reports from custom buckets.
>

#### Metadata

- **Policies**: [Oracle Cloud Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/oracle/oracle_cbi/README.md)
- **Merged At**: 2025-07-28 12:46:46 UTC

---

### PR [#3353](https://github.com/flexera-public/policy_templates/pull/3353): POL-1568 Deprecate Azure China Common Bill Ingestion

*Minor Update*

#### Description

> The Azure China Common Bill Ingestion policy template is being deprecated. The README now directs the user to our documentation on configuring an Azure China bill connection.
>

#### Metadata

- **Policies**: [Azure China Common Bill Ingestion](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/azure_china_cbi/README.md)
- **Merged At**: 2025-07-24 17:40:20 UTC

---

### PR [#3331](https://github.com/flexera-public/policy_templates/pull/3331): SQ-16516 Removed "ITAM VMs Missing Host ID" policy

*Unpublished*

#### Description

> This PR removes the policy "ITAM VMs Missing Host ID".
> As confirmed by Tim Johnson, this policy is fundamentally incorrect.
>
> This policy relies on the `hostId` field in the API response to determine which VM does not have host.
> However, the `hostId` field in the API response does **not** represent the "Host of a VM".
>
> The "Host of a VM" can only be obtained through a custom report.
>
> The correct way of listing all VMs without a host would be:
> 1. Create a custom report, and have the report filter on host
> 2. Get this report using another existing policy (https://github.com/flexera-public/policy_templates/blob/master/operational/flexera/itam/schedule_itam_report/README.md OR https://github.com/flexera-public/policy_templates/blob/master/operational/flexera/fnms/schedule_fnms_reports/README.md)
>
> Team's chat link from Tim Johnson:
> https://teams.microsoft.com/l/message/19:833373548e104af2a20b0216eda1ba7b@thread.skype/1752692023347?tenantId=91034d23-0b63-4943-b138-367d4dfac252&groupId=fb250818-e040-4a26-b207-61c3cd99fd6e&parentMessageId=1752690636142&teamName=Team%20Flexera%20One&channelName=Policy%20Support%20and%20Questions&createdTime=1752692023347
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-16516
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/3331) for details about unpublished policies.
- **Merged At**: 2025-07-21 14:11:31 UTC

---

### PR [#3339](https://github.com/flexera-public/policy_templates/pull/3339): POL-1562 AWS Old Snapshots: RDS Fix

*Minor Update*

#### Description

> RDS snapshots are incremental; for this reason, the `AWS Old Snapshots` policy template has been modified to only report the most recent RDS snapshot. A disclaimer has also been added to both the incident page and the README explaining why this is done.
>
> This is because we don't have a straightforward way to assign a savings value to incremental snapshots; deleting one will only save you the amount of space freed up from removing that particular version.
>

#### Metadata

- **Policies**: [AWS Old Snapshots](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/old_snapshots/README.md)
- **Merged At**: 2025-07-21 13:16:41 UTC

---

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

