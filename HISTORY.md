# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#4253](https://github.com/flexera-public/policy_templates/pull/4253): POL-1743 Misc. Policy Template instance_types.json Update

*Minor Update*

#### Description

> - `AWS RDS Instances With Unapproved Backup Settings`: Updated to use `aws_ec2_instance_types.json`
> - `Azure Databricks Rightsize Compute Instances`: Updated to use `azure_compute_instance_types` and to make proper use of hash_exclude.
> - `Google Overutilized VM Instances`: Updated to use `google_compute_instance_types.json`
> - `google_compute_instance_types.py`: Updated to pull in superseded instance data from `instance_types.json`
> - `instance_types.json (AWS/Azure/Google)`: Updated to have up to date instance information. This is primarily to support users using old versions of policy templates.
> - Additionally, automated instance type JSONs for each cloud provider have been updated.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4253) for these details.
- **Merged At**: 2026-04-03 14:34:39 UTC

---

### PR [#4245](https://github.com/flexera-public/policy_templates/pull/4245): POL-1482 AWS Policy Templates: aws_ec2_instance_types.json

*Minor Update*

#### Description

> Updates 2 AWS policy templates to now use the aws_ec2_instance_types.json file, which is generated from automation, instead of the manually maintained instance_types.json file.
>
> - AWS Rightsize EC2 Instances
> - AWS Overutilized EC2 Instances
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md), [AWS Overutilized EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/overutilized_ec2_instances/README.md)
- **Merged At**: 2026-04-03 12:57:14 UTC

---

### PR [#4244](https://github.com/flexera-public/policy_templates/pull/4244): POL-1492 Azure Policy Templates: azure_compute_instance_types.json

*Minor Update*

#### Description

> Updates 3 Azure policy templates to now use the `azure_compute_instance_types.json` file, which is generated from automation, instead of the manually maintained `instance_types.json` file.
>
> - Azure Rightsize Compute Instances
> - Azure Overutilized Compute Instances
> - Azure Usage Report - Instance Time Used (Also includes a bug fix)
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md), [Azure Overutilized Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/overutilized_compute_instances/README.md), [Azure Usage Report - Instance Time Used](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/total_instance_usage_report/README.md)
- **Merged At**: 2026-04-03 12:55:28 UTC

---

### PR [#4155](https://github.com/flexera-public/policy_templates/pull/4155): POL-1707 AWS Reserved Instances Recommendations Fix

*Minor Update*

#### Description

> `AWS Reserved Instances Recommendations`
> - Fixed issue where policy execution would sometimes fail if "Everything" was selected for the `Payment Option` parameter.
>

#### Metadata

- **Policies**: [AWS Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/recommendations/README.md)
- **Merged At**: 2026-04-02 20:58:34 UTC

---

### PR [#4223](https://github.com/flexera-public/policy_templates/pull/4223): POL-0000 - fix: remove suffix from service account to better support policy manager

*Minor Update*

#### Description

> Removes suffix from Credential Name to better support new Policy Manager use-cases
>

#### Metadata

- **Policies**: [Flexera Onboarding](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/onboarding/README.md)
- **Merged At**: 2026-04-02 20:20:06 UTC

---

### PR [#4224](https://github.com/flexera-public/policy_templates/pull/4224): POL-1741 Azure Rightsize Compute Instances: Local Disk Support

*Minor Update*

#### Description

> `Azure Rightsize Compute Instances`
> - Added `Current Instance Local Disk` and `Recommended Instance Local Disk` fields to incident export to inform users whether local disk support will change as a result of the recommended action.
> - Added `Filter Recommendations That Change Local Disk` parameter to allow users to exclude downsize recommendations where the recommended instance type has a different local disk configuration than the current instance type.
>
> `azure_compute_instance_types.py`
> - Now includes a field, `localDisk`, that indicates whether or not the instance type has a local disk.
> - Improved filtering removes a handful of non-compute SKUs from erroneously appearing in the results.
>
> `Dangerfile`
> - Fixed issue where hash_exclude test was ignoring the path field in export blocks.
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2026-04-02 19:43:28 UTC

---

### PR [#4118](https://github.com/flexera-public/policy_templates/pull/4118): POL-1729 README Permissions Audit

*Minor Update*

#### Description

> #### Primary Changes
> - This PR updates the READMEs of various policy templates to correct the permissions required. This involves adding missing permissions, removing unneeded permissions, and correcting invalid permissions. Additionally, READMEs that had incorrect descriptions of the policy template's functionality were fixed.
> - This also updates the Policy API script to be more robust and to store permissions for AWS, Azure, and Google API calls. This is coupled with a Dangerfile test to check whether a policy template's README matches the output of this script. These are raised as warnings because false positives will occur in a handful of edge cases.
>   - False positives are inevitable as it is non-trivial to accurately parse every API call from policy templates given that they support legitimate programming languages (JavaScript, CWF) that utilize variables. I've gotten it very close though.
>   - A handful of these false positives will show up as warnings on this PR. The READMEs are correct though.
>
> #### Other
> - This PR also adds a Dangerfile text to make sure policy templates in the compliance, cost, operational, saas, and security directories have a matching Category field in the template itself. 8 issues were found with existing policy templates; 7 had their category updated, and one was moved to the correct directory.
> - This PR updates the Dangerfile test for bad URLs so that it doesn't incorrectly parse Markdown URLs by assuming the trailing `)` is part of the URL. This was happening in edge cases where the markdown was immediately followed by punctuation, such as a period.
> - This PR turns off (maybe temporarily) dead link testing in the textlinter. It keeps reporting valid links for a number of domains (not just Flexera) as dead. I suspect there may be some internet-wide blocking of Github requests for URLs going on that is causing this to not work as expected.
>
> Dangerfile errors and warnings are false positives. The errors in particular are unrelated to changes made by this PR.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4118) for these details.
- **Merged At**: 2026-04-01 20:31:25 UTC

---

### PR [#4208](https://github.com/flexera-public/policy_templates/pull/4208): POL-1737 - Graceful error handling for inaccessible AWS regions, Batch 2

*Minor Update*

#### Description

> In [POL-1684](https://flexera.atlassian.net/browse/POL-1684) we improved a majority of AWS Policy Templates in the Catalog for FinOps/Optimization outcomes to gracefully handle errors as it collects data.  This story is to finish the rest of the PTs in Catalog so users generally will not run into fatal errors for AWS PTs due to regional issues/blocks.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1737
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md), [AWS EC2 Compute Optimizer Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/ec2_compute_optimizer/README.md), [AWS Rightsize Redshift](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_redshift/README.md), [AWS Unused Classic Load Balancers](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_clbs/README.md), [AWS Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/tag_cardinality/README.md)
- **Merged At**: 2026-04-01 18:11:54 UTC

---

### PR [#4201](https://github.com/flexera-public/policy_templates/pull/4201): POL-1735 Budget Alerts / Budget vs Actual Spend Report BC Name Fix

*Minor Update*

#### Description

> The `Budget Alerts` and `Budget vs Actual Spend Report` policy templates now show the full billing center name instead of billing center ID when costs are grouped by billing center dimensions.
>

#### Metadata

- **Policies**: [Budget Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_report_alerts/README.md), [Budget vs Actual Spend Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_v_actual_spend_report/README.md)
- **Merged At**: 2026-03-31 19:06:16 UTC

---

### PR [#4197](https://github.com/flexera-public/policy_templates/pull/4197): FOPTS-21273: Added upper limit for 'Days of Usage' parameter for 'Low Usage Report' policy.

*Bug Fix*

#### Description

> Added upper limit for 'Days of Usage' parameter for 'Low Usage Report' policy.
>
> The Flexera billing API "/bill-analysis/orgs/{orgId}/costs/aggregated" supports a maximum of 31 days billing data.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/SQ-23457
> https://flexera.atlassian.net/browse/FOPTS-18576
>

#### Metadata

- **Policies**: [Low Usage Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/low_usage/README.md)
- **Merged At**: 2026-03-31 15:36:41 UTC

---

### PR [#4191](https://github.com/flexera-public/policy_templates/pull/4191): POL-1734 Azure End-of-Life Resources Meta Parent Fix

*Minor Update*

#### Description

> Fixed issue preventing meta parent policy template from being generated for the `Azure End-of-Life Resources` policy template. Also updated the policy-dev copilot agent to reduce the likelihood of this issue happening in the future.
>

#### Metadata

- **Policies**: [Meta Parent: Google Rightsize Persistent Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/google/rightsize_persistent_disks/README.md), [Meta Parent: Google Unused Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/google/unused_disks/README.md), [Azure End-of-Life Resources](https://github.com/flexera-public/policy_templates/tree/master/security/azure/eol_resources/README.md), [Meta Parent: Azure End-of-Life Resources](https://github.com/flexera-public/policy_templates/tree/master/security/azure/eol_resources/README.md)
- **Merged At**: 2026-03-30 20:32:37 UTC

---

### PR [#4185](https://github.com/flexera-public/policy_templates/pull/4185): POL-1138 New Policy Template: Google Rightsize Persistent Disks

*New Policy Template*

#### Description

>  `Google Rightsize Persistent Disks`
> - Added a new policy template, `Google Rightsize Persistent Disks`, that reports both idle and underutilized Google persistent disks.
>
>  `Google Unused Disks`
> - Deprecated. README now directs user to above policy template instead.
>
> `Google Idle Persistent Disk Recommender`
> - README updated to direct people to Google Rightsize Persistent Disks instead of Google Unused Disks.
>
> `policy-dev.agent`
> - Added dedicated information on FinOps as a practice and links to appropriate web resources.
> - Improvements to the policy development Copilot agent to more correctly handle deprecation and versioning.
> - Refactoring to streamline it and make it more readable for Claude.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4185) for these details.
- **Merged At**: 2026-03-30 19:27:10 UTC

---

### PR [#4170](https://github.com/flexera-public/policy_templates/pull/4170): POL-1733 New Policy Template: Azure End-of-Life Resources

*New Policy Template*

#### Description

> - Adds a new policy template `Azure End-of-Life Resources` to report Azure resources that are either EOL or under extended support.
> - Adds new data file, `data/azure/azure_esu_os_versions.json`, to support the above. This will enable us to update the list over time without requiring users to update their applied policies.
> - Improvements to policy development copilot agent.
> - Improvements to Flexera Policy Template VSCode extension to expand functionality and fix issues.
> - Improvements to some Dangerfile tests to eliminate false positives.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4170) for these details.
- **Merged At**: 2026-03-27 18:55:51 UTC

---

### PR [#4164](https://github.com/flexera-public/policy_templates/pull/4164): POL-1732 Meta Policy Generator Fix

#### Description

> Fixes issue where meta policies generated are malformed under certain conditions. The bug was triggered by the child policy containing the line `export "instances" do` and was caused by a regex issue in the generator script.
>

#### Metadata

- **Policies**: [Meta Parent: AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Meta Parent: Azure Data Lake Optimization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/data_lake_optimization/README.md), [Meta Parent: Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md), [Meta Parent: Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2026-03-27 12:40:44 UTC

---

### PR [#4156](https://github.com/flexera-public/policy_templates/pull/4156): POL-1585 Meta Parent Updates

#### Description

> This PR makes several adjustments to meta parent policy templates:
> - All requests to deprecated API endpoints have been replaced with modern counterparts.
> - Policy code was rearranged to be more readable and more closely align to what we expect in other policy templates.
> - Cloud workflow for creating, deleting, and updating policy templates was refactored for better error reporting and handling.
> - Other small misc. improvements made.
>
> Note: Review can mostly just ignore the newly generated meta parents and focus on the 3 templates in the tools/ directory, since these are what are used to generate the meta parents.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4156) for these details.
- **Merged At**: 2026-03-27 11:05:31 UTC

---

### PR [#4160](https://github.com/flexera-public/policy_templates/pull/4160): POL-1731 Copilot Agent & AWS Idle Lambda Functions

*New Policy Template*

#### Description

> This adds a copilot agent, `.github/agents/policy-dev.agent.md`, for using Copilot CLI to develop policy templates. This agent was developed via a combination of manual work and use of Copilot CLI itself to expand and optimize its contents. It seems to work *very* well.
>
> This also adds a new policy template, `AWS Idle Lambda Functions`, generated entirely by Copilot CLI. It was reviewed thoroughly and tested, and small errors (mostly in formatting rather than ones that would meaningfully affect execution) were also corrected via Copilot along with instructions to modify the above `.github/agents/policy-dev.agent.md` file to prevent similar errors in the future.
>
> Some small Dangerfile changes were also made:
>
> - Spell check and outdated terminology checks were disabled explicitly for Copilot Agent files, since they may need to contain instructions that would violate these rules.
> - This PR updates the Dangerfile test for bad URLs so that it doesn't incorrectly parse Markdown URLs by assuming the trailing ) is part of the URL. This was happening in edge cases where the markdown was immediately followed by punctuation, such as a period.
> - This PR turns off (maybe temporarily) dead link testing in the textlinter. It keeps reporting valid links for a number of domains (not just Flexera) as dead. I suspect there may be some internet-wide blocking of Github requests for URLs going on that is causing this to not work as expected.
>

#### Metadata

- **Policies**: [AWS Idle Lambda Functions](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/idle_lambda_functions/README.md)
- **Merged At**: 2026-03-27 11:05:24 UTC

---

### PR [#4150](https://github.com/flexera-public/policy_templates/pull/4150): POL-1730 Azure Savings Plan Recommendations: API Version Update

*Minor Update*

#### Description

> Updates the `Azure Savings Plan Recommendations` policy template to use the latest version, "2025-03-01", for the Azure "Microsoft.CostManagement/benefitRecommendations" API endpoint. This is to ensure that all recommendations currently produced by Azure and made available by this endpoint are captured and reported.
>

#### Metadata

- **Policies**: [Azure Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/recommendations/README.md)
- **Merged At**: 2026-03-23 12:52:23 UTC

---

### PR [#4139](https://github.com/flexera-public/policy_templates/pull/4139): POL-1725 CSV Support for Security & ITAM/FNMS Policy Templates

*Minor Update*

#### Description

> Adds support for CSV incidents for Security & ITAM/FNMS policy templates
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4139) for these details.
- **Merged At**: 2026-03-20 20:52:16 UTC

---

### PR [#4126](https://github.com/flexera-public/policy_templates/pull/4126): FOAA-913 - New PTs RBDs from AWS Accounts (Organization API) and Sync RBD to Customer Orgs

*Unpublished, New Policy Template*

#### Description

> New Policy Templates to support new use-cases from some of our Partner customers.
>
> - Sync RBD rules from AWS Account Tags sourced from AWS Organizations API (instead of Flexera Account Tag Inventory)
> - Sync RBD rules from MSP Organization to Customer Organizations for accounts that are allocated to Customer Orgs
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-913
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4126) for details about unpublished policies.
- **Merged At**: 2026-03-17 18:48:46 UTC

---

### PR [#4002](https://github.com/flexera-public/policy_templates/pull/4002): FOAA-878 - MSP Invoiceable Spend Report

*New Policy Template*

#### Description

> - Introduces the initial release of the MSP Invoiceable Spend Report policy template.
> - Updates Danger README tests to support new Flexera Docs URLs
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-878
>

#### Metadata

- **Policies**: [MSP Invoiceable Spend Report](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/msp/msp_invoiceable_spend_report/README.md)
- **Merged At**: 2026-03-17 17:01:49 UTC

---

### PR [#4078](https://github.com/flexera-public/policy_templates/pull/4078): FOAA-905 - Fix Kubernetes Rightsizing Recomendations PT - No Recs for Azure Clusters

*Minor Update*

#### Description

> - Improved incident report formatting to use currency from Flexera Org
> - Improved formatting and context in the "Recommendation Details" for each recommendation
> - Added Minimum Savings Threshold input parameter to filter out recommendations below the specified estimated monthly savings
> - Fixed bug preventing Azure recommendations from being pulled
> - Estimated Savings is being provided by Recommendations Spot API instead of calculated from aggregated costs
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-905
>

#### Metadata

- **Policies**: [Kubernetes - Rightsizing Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/spot/ocean_recommendations/README.md)
- **Merged At**: 2026-03-17 17:01:01 UTC

---

### PR [#4108](https://github.com/flexera-public/policy_templates/pull/4108): POL-1728 AWS EC2 Compute Optimizer - Add GPU Filtering

*Unpublished, New Policy Template, Minor Update*

#### Description

> Makes multiple changes to the `AWS EC2 Compute Optimizer` policy template to better accommodate recommendations for GPU instances:
> - Adds an option to the `AWS EC2 Compute Optimizer` policy template to filter resources based on presence or absence of a GPU.
> - Adds GPU metrics returned by the Compute Optimizer tool to the incident.
> - Publishes the policy template so that it is available in the catalog.
> - Updated README to contain specific instructions on how to use this alongside the `AWS Rightsize EC2 Instances` policy template as a GPU-only supplement to it.
>

#### Metadata

- **Policies**: [AWS EC2 Compute Optimizer Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/ec2_compute_optimizer/README.md)
- **Merged At**: 2026-03-12 12:55:42 UTC

---

### PR [#4101](https://github.com/flexera-public/policy_templates/pull/4101): FOAA-909 - New PT: Flexera User Groups from Billing Centers

*New Policy Template*

#### Description

> Automatically creates and manages Flexera IAM User Groups based on the Billing Centers in the organization. For each Billing Center, a corresponding User Group is created and granted a configurable role (`billing_center_viewer` or `billing_center_admin`) scoped to that Billing Center.
>
> Mitigates/prevents the need for a FinOps persona to create/manage User Groups and grants to Billing Centers.
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/FOAA-909
>

#### Metadata

- **Policies**: [Flexera User Groups from Billing Centers](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/iam/user_groups_from_billing_centers/README.md)
- **Merged At**: 2026-03-10 20:32:47 UTC

---

### PR [#4090](https://github.com/flexera-public/policy_templates/pull/4090): POL-1726 Update URLs in READMEs/Templates

*Unpublished, Minor Update*

#### Description

> Updates policy templates and READMEs to use newer, more up to date URLs to Flexera documentation. The old URLs still work (for now) but redirect to these new ones anyway.
>
> Also, some Dangerfile updates to help with this; in particular, the text linting now explicitly lets you know that a URL redirect will come up as a dead link and to update the URL with wherever it redirects to.
>
> Note: Dangerfile warnings/errors are false positives unrelated to any changes made by this PR. Also, for some reason a handful of URLs are being treated as dead links by textlint even though the URLs work fine.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4090) for these details.
- **Merged At**: 2026-03-10 12:29:22 UTC

---

### PR [#4085](https://github.com/flexera-public/policy_templates/pull/4085): POL-1685 Add "Exclude GPU Instances" Parameter to AWS Rightsize EC2 Instances

*Minor Update*

#### Description

> Adds a parameter to AWS Rightsize EC2 Instances to exclude GPU instances from the results.
>
> This also updates the Dangerfile tests to use updated URLs. This is because our docs have been rearranged and the old URLs now redirect to newer ones.
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md)
- **Merged At**: 2026-03-09 14:48:19 UTC

---

### PR [#4047](https://github.com/flexera-public/policy_templates/pull/4047): POL-1710 AWS Lambda Functions With High Error Rate Fix

#### Description

> `AWS Lambda Functions With High Error RateAWS Lambda Functions With High Error Rate`
> - Fixed issue with `GetMetricData` API request when gathering CloudWatch metrics. Functionality unchanged.
>

#### Metadata

- **Policies**: [AWS Lambda Functions With High Error Rate](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/lambda_functions_with_high_error_rate/README.md)
- **Merged At**: 2026-02-19 13:05:39 UTC

---

### PR [#4046](https://github.com/flexera-public/policy_templates/pull/4046): POL-1695 Azure Long Stopped Compute Instances Fix

#### Description

> Fixes issue with the `Azure Long Stopped Compute Instances` policy template where resources in a state of "starting" were reported as stopped.
>

#### Metadata

- **Policies**: [Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md)
- **Merged At**: 2026-02-19 13:05:31 UTC

---

### PR [#4023](https://github.com/flexera-public/policy_templates/pull/4023): POL-1720 Meta Policy Fix

*New Policy Template*

#### Description

> Fixes issue where meta parents aren't being generated due to non-existent policy templates being listed in the YAML file.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4023) for these details.
- **Merged At**: 2026-02-05 14:51:16 UTC

---

### PR [#4018](https://github.com/flexera-public/policy_templates/pull/4018): POL-1708 Azure Long Stopped Compute Instances - Fix for "Start time cannot be more than 90 days in the past" error

*Bug Fix*

#### Description

> <!-- Describe what this change achieves below -->
> This change prevents intermittent failures when querying Azure Activity Logs caused by `start_date` exceeding Azure's strict 90-day limit.
>
> The fix removes timestamp rounding and adds a small safety buffer (+5 minutes) after subtracting 90 days, ensuring all iterative API calls stay within the allowed window.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
>

#### Metadata

- **Policies**: [Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/long_stopped_instances/README.md)
- **Merged At**: 2026-02-05 14:17:00 UTC

---

### PR [#3670](https://github.com/flexera-public/policy_templates/pull/3670): POL-1666 New Policy: AWS Idle FSx File Systems

*New Policy Template*

#### Description

> New policy template to detect and report on AWS FSx File Systems that are idle (no read/write operations).
>

#### Metadata

- **Policies**: [AWS Idle FSx File Systems](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/idle_fsx/README.md)
- **Merged At**: 2026-02-04 21:42:54 UTC

---

### PR [#4017](https://github.com/flexera-public/policy_templates/pull/4017): FOPTS-19145 Fixed Account Scope description for AWS savings plan recs policy

#### Description

> This PR updates the account_scope description in the AWS Savings Plan Recommendations Policy to align with AWS documentation.
>
> Reference - [AWS GetSavingsPlansPurchaseRecommendation API Specification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html#API_GetSavingsPlansPurchaseRecommendation_RequestParameters)
>
> ### Issues Resolved
>

#### Metadata

- **Policies**: [AWS Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/recommendations/README.md)
- **Merged At**: 2026-02-04 20:16:29 UTC

---

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

