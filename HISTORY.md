# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#4874](https://github.com/flexera-public/policy_templates/pull/4874): POL-1832 Policy Template Bug Fix Pass [02]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4874) for these details.
- **Merged At**: 2026-08-28 12:07:14 UTC

---

### PR [#4873](https://github.com/flexera-public/policy_templates/pull/4873): POL-1832 Policy Template Bug Fix Pass [01]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4873) for these details.
- **Merged At**: 2026-08-28 12:07:09 UTC

---

### PR [#4871](https://github.com/flexera-public/policy_templates/pull/4871): POL-1828 AWS S3 Buckets Without Lifecycle Configuration: Bug Fix

*Minor Update*

#### Description

> AWS S3 Buckets Without Lifecycle Configuration - Fixed bug where the policy would fail with a `'resource' is not defined` error whenever the `Exclusion Tags` parameter was used.
>
> Also fixed bugs in this and two other policy templates related to the tag filtering not working correctly.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4871) for these details.
- **Merged At**: 2026-08-28 08:29:08 UTC

---

### PR [#4872](https://github.com/flexera-public/policy_templates/pull/4872): POL-1832 Policy Template Bug Fix Pass [00]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4872) for these details.
- **Merged At**: 2026-08-27 18:45:45 UTC

---

### PR [#4867](https://github.com/flexera-public/policy_templates/pull/4867): POL-1829 AWS EC2 Compute Optimizer: Bug Fix

*Minor Update*

#### Description

> AWS EC2 Compute Optimizer - Fixed an issue where the policy would fail to run if AWS Compute Optimizer did not return an estimated savings amount for a recommendation.
>

#### Metadata

- **Policies**: [AWS EC2 Compute Optimizer Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/ec2_compute_optimizer/README.md), [Meta Parent: AWS EC2 Compute Optimizer Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/ec2_compute_optimizer/README.md)
- **Merged At**: 2026-08-26 18:27:10 UTC

---

### PR [#4856](https://github.com/flexera-public/policy_templates/pull/4856): POL-1830 Budget Alerts: Currency Fixes

*Minor Update*

#### Description

> `Budget Alerts`
> - Fixed the Data Table in the incident detail to consistently round currency values to two decimal places and format them using the org currency's thousands separator (e.g. `$10,345,123.33` instead of `$10345123.33456`). Negative amounts (e.g. an over-budget Remaining Amount) now display correctly (e.g. `-$500.26` instead of `$-,500.26`).
> - Fixed currency formatting in the Data Table for currencies whose thousands separator is a period (e.g. Brazilian Real) so the decimal point now correctly switches to a comma (e.g. `R$10.345.123,33` instead of the ambiguous `R$10.345.123.33`).
> - Fixed the Projected (prorated) Spend value to always be rounded to two decimal places.
> - Fixed erroneous "\n" string that would sometimes appear in incident description.
>

#### Metadata

- **Policies**: [Budget Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/budget_report_alerts/README.md)
- **Merged At**: 2026-08-20 20:19:19 UTC

---

### PR [#4810](https://github.com/flexera-public/policy_templates/pull/4810): FOPTS-28887 Fixed various issues for AWS S3 oversized bucket policy

*Bug Fix*

#### Description

> #### 1. Fixed how the bucket name is being handled.
> When calling CloudWatch API, the `Id` field is changed from `{bucketName}_{storageType}` to `id_{i}_{bucketName}_{storageType}`
>
> This is to satisfy two constraints for sending request to CloudWatch:
> 1. `Id` field must match with `^[a-z][a-zA-Z0-9_]*$`
> 2. `Id` field must be unique
>
> Also fixed various other issues related to bucket names.
>
> #### 2. Added a missing pagination
>
> #### 3. Fixed the "Exclusion Tags" filter
>

#### Metadata

- **Policies**: [AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md), [Meta Parent: AWS Oversized S3 Buckets](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/s3_bucket_size/README.md)
- **Merged At**: 2026-08-20 17:09:34 UTC

---

### PR [#4843](https://github.com/flexera-public/policy_templates/pull/4843): POL-1826 Parameter Sanitization: Policy Templates #18

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4843) for these details.
- **Merged At**: 2026-08-20 17:02:11 UTC

---

### PR [#4842](https://github.com/flexera-public/policy_templates/pull/4842): POL-1826 Parameter Sanitization: Policy Templates #17

*Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4842) for these details.
- **Merged At**: 2026-08-20 17:02:03 UTC

---

### PR [#4841](https://github.com/flexera-public/policy_templates/pull/4841): POL-1826 Parameter Sanitization: Policy Templates #16

*Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4841) for these details.
- **Merged At**: 2026-08-20 17:01:55 UTC

---

### PR [#4840](https://github.com/flexera-public/policy_templates/pull/4840): POL-1826 Parameter Sanitization: Policy Templates #15

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4840) for these details.
- **Merged At**: 2026-08-20 17:01:47 UTC

---

### PR [#4839](https://github.com/flexera-public/policy_templates/pull/4839): POL-1826 Parameter Sanitization: Policy Templates #14

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4839) for these details.
- **Merged At**: 2026-08-20 16:59:37 UTC

---

### PR [#4838](https://github.com/flexera-public/policy_templates/pull/4838): POL-1826 Parameter Sanitization: Policy Templates #13

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4838) for these details.
- **Merged At**: 2026-08-20 16:59:29 UTC

---

### PR [#4831](https://github.com/flexera-public/policy_templates/pull/4831): POL-1826 Parameter Sanitization: Policy Templates #12

*Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4831) for these details.
- **Merged At**: 2026-08-20 16:35:01 UTC

---

### PR [#4830](https://github.com/flexera-public/policy_templates/pull/4830): POL-1826 Parameter Sanitization: Policy Templates #11

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4830) for these details.
- **Merged At**: 2026-08-20 16:34:52 UTC

---

### PR [#4829](https://github.com/flexera-public/policy_templates/pull/4829): POL-1826 Parameter Sanitization: Policy Templates #10

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4829) for these details.
- **Merged At**: 2026-08-20 16:34:46 UTC

---

### PR [#4828](https://github.com/flexera-public/policy_templates/pull/4828): POL-1826 Parameter Sanitization: Policy Templates #9

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4828) for these details.
- **Merged At**: 2026-08-20 16:34:41 UTC

---

### PR [#4827](https://github.com/flexera-public/policy_templates/pull/4827): POL-1826 Parameter Sanitization: Policy Templates #8

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>
> Also updates some Dangerfile testing to avoid false positives.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4827) for these details.
- **Merged At**: 2026-08-20 16:34:31 UTC

---

### PR [#4826](https://github.com/flexera-public/policy_templates/pull/4826): POL-1826 Parameter Sanitization: Policy Templates #7

*Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4826) for these details.
- **Merged At**: 2026-08-20 16:34:24 UTC

---

### PR [#4825](https://github.com/flexera-public/policy_templates/pull/4825): POL-1826 Parameter Sanitization: Policy Templates #6

*Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4825) for these details.
- **Merged At**: 2026-08-20 16:34:20 UTC

---

### PR [#4819](https://github.com/flexera-public/policy_templates/pull/4819): POL-1826 Parameter Sanitization: Policy Templates #5

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4819) for these details.
- **Merged At**: 2026-08-20 13:49:17 UTC

---

### PR [#4818](https://github.com/flexera-public/policy_templates/pull/4818): POL-1826 Parameter Sanitization: Policy Templates #4

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4818) for these details.
- **Merged At**: 2026-08-20 13:49:10 UTC

---

### PR [#4817](https://github.com/flexera-public/policy_templates/pull/4817): POL-1826 Parameter Sanitization: Policy Templates #3

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4817) for these details.
- **Merged At**: 2026-08-20 13:49:02 UTC

---

### PR [#4816](https://github.com/flexera-public/policy_templates/pull/4816): POL-1826 Parameter Sanitization: Policy Templates #2

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4816) for these details.
- **Merged At**: 2026-08-20 13:48:54 UTC

---

### PR [#4813](https://github.com/flexera-public/policy_templates/pull/4813): POL-1826 Parameter Sanitization: Policy Templates #1

*Unpublished, Minor Update*

#### Description

> One of several PRs focused on sanitizing inputs for PT parameters. This is to prevent users from breaking policy template execution because they entered a parameter incorrectly, such as putting whitespace at the beginning or end of the value.
>
> Also corrects some Dangerfile-reported issues with the touched PTs.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4813) for these details.
- **Merged At**: 2026-08-20 13:48:49 UTC

---

### PR [#4798](https://github.com/flexera-public/policy_templates/pull/4798): POL-1825 Azure Rightsize Managed Disks Refactor

*Major Update*

#### Description

> Refactors the code in `Azure Rightsize Managed Disks` to be better aligned with other recommendation policy templates and best practices. Full changelog:
>
> - Added a `Recommendation` field to the incident export, describing the recommended disk downgrade action for each resource
> - Results are now sorted by descending estimated monthly savings
> - Added a summary line to the incident message reporting how many disks were analyzed and how many were recommended for a downgrade
> - Fixed a bug where the incident detail's `Potential Monthly Savings` value displayed an incorrect currency format for non-USD organizations
> - Fixed a bug where incident deduplication would sometimes not occur, causing the same resource to appear as different incidents if raised during multiple executions
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md), [Meta Parent: Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2026-08-18 13:20:13 UTC

---

### PR [#4799](https://github.com/flexera-public/policy_templates/pull/4799): POL-1821 Azure Unused Volumes - Fix "Delete Volumes" action fails with slice boundary error

*Minor Update*

#### Description

> <!-- Describe what this change achieves below -->
> - Fixes bug where the `Delete Volumes` action would fail if the volume had already been deleted. The action now treats a volume that no longer exists as a successful deletion.
> - Fixes bug where unexpected responses from the Azure API during volume deletion raised an internal Cloud Workflow error instead of reporting the actual API response.
>

#### Metadata

- **Policies**: [Azure Unused Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/unused_volumes/README.md)
- **Merged At**: 2026-08-18 13:08:17 UTC

---

### PR [#4797](https://github.com/flexera-public/policy_templates/pull/4797): POL-1824 Minimum Savings Set to 1

*Unpublished, Minor Update*

#### Description

> Updates the default value of the Minimum Savings Threshold parameter from 0 to 1 in all relevant policy templates.
>
> (Dangerfile issues unrelated to this change)

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4797) for these details.
- **Merged At**: 2026-08-18 12:28:35 UTC

---

### PR [#4783](https://github.com/flexera-public/policy_templates/pull/4783): POL-1820 General Policy/Repo Cleanup

*Unpublished, Minor Update*

#### Description

> Several broad changes made to clean things up:
> - Bug fixes and improvements to the `AWS Auto Scaling Group Recommendation` policy template.
> - Non-ASCII characters that do not render correctly in the Flexera One UI have been removed from PTs and md files.
> - AWS region error reporting added to several policy templates that were missing the functionality.
> - Meta parent generation enabled for several policy templates where meta parents existed but were not being updated. Manually maintained meta parents had their version numbers updated to match their associated child policies.
> - `hash_exclude` added to several policy incidents to avoid raising multiple incidents for the same resource/problem
> - Various typos and small errors fixed in README files.
> - Dangerfile warnings fixed in various policy templates.
> - Dangerfile policy code block test fixed to show actual line numbers as intended.
>
> All remaining Dangerfile warnings are false positives or not concerning.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4783) for these details.
- **Merged At**: 2026-08-13 14:03:23 UTC

---

### PR [#4779](https://github.com/flexera-public/policy_templates/pull/4779): POL-1819 Code Normalization

*Unpublished, Minor Update*

#### Description

> - Moves canonical code examples from `.github/agents/policy-dev.agent.md` to a new file `data/agent/code_examples.txt` that the agent is instead instructed to reference.
> - Expanded the canonical code examples.
> - Updated several policy templates to use the canonical version of the relevant code.
>   - Fixed a few minor bugs and Dangerfile issues with some of the touched policy templates along the way.
> - Updated Dangerfile tests to trigger fewer false positives

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4779) for these details.
- **Merged At**: 2026-08-11 19:39:58 UTC

---

### PR [#4767](https://github.com/flexera-public/policy_templates/pull/4767): POL-1812 Region Check Fix

*Minor Update*

#### Description

> Fixes issue in several AWS policy templates where the region check would cause policy execution to fail if a 400 response is returned by AWS.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4767) for these details.
- **Merged At**: 2026-08-10 12:06:55 UTC

---

### PR [#4764](https://github.com/flexera-public/policy_templates/pull/4764): POL-1811 Flexera Test Support

*Unpublished, Minor Update*

#### Description

> Adds support for flexeratest.com API endpoints and domains to all relevant policy templates.
>
> Also makes some very minor fixes to a handful of modified policies and their READMEs to fix Dangerfile issues, and makes some improvements to Dangerfile and the Policy API script to avoid false positives.
>
> All remaining Dangerfile errors/warnings are false positives that should be ignored.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4764) for these details.
- **Merged At**: 2026-08-06 19:37:42 UTC

---

### PR [#4761](https://github.com/flexera-public/policy_templates/pull/4761): POL-1808 Azure Meta Parent Fix

#### Description

> Fixes a couple of issues with the unpublished Azure resource group-based meta parent policies that prevented them from working.
> - The parameter for disabling consolidated incidents now exists and works properly.
> - Blank resource group values returned by the Cost API are now ignored.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4761) for these details.
- **Merged At**: 2026-08-04 19:18:49 UTC

---

### PR [#4755](https://github.com/flexera-public/policy_templates/pull/4755): POL-1810 Azure Rightsize SQL Databases: vCore/DTU Disclaimer

*Minor Update*

#### Description

> `Azure Rightsize SQL Databases`: Adds a more elaborate disclaimer about the distinction between vCore and DTU models to the incident.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md), [Meta Parent: Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2026-08-03 15:37:36 UTC

---

### PR [#4744](https://github.com/flexera-public/policy_templates/pull/4744): FOPTS-27963 Fix overlapping X-axis date labels in scheduled report chart

*Minor Update*

#### Description

> Fixes SQ-26519: X-axis date labels in the scheduled reports spending chart were rendering as an overlapping, unreadable block for customers over multi-month date ranges. The chxs axis style parameter only configured the Y-axis (currency formatting), the X-axis had no label-skipping or rotation, so every daily label was drawn with no thinning.
>
> Added opt_skip_labels (s) to the X-axis entry in chxs, so Image-Charts automatically thins out labels when there are too many for the available width, instead of rendering all of them.
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2026-07-29 21:33:46 UTC

---

### PR [#4741](https://github.com/flexera-public/policy_templates/pull/4741): POL-1807 Meta Parent CWF Logging Fix

#### Description

> Fixes logging issue in meta parent policies where a POST request was incorrectly logged as DELETE. Actual functionality itself works correctly.
>
> (Also used Copilot to do a quick pass for similar logging issues in CWF for non-meta parents but nothing was found)

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4741) for these details.
- **Merged At**: 2026-07-29 12:52:14 UTC

---

### PR [#4738](https://github.com/flexera-public/policy_templates/pull/4738): POL-1797 New Policy Template: Azure Rule-Based Dimension For Tenant ID

*Unpublished, New Policy Template*

#### Description

> Azure Rule-Based Dimension For Tenant ID - This policy template creates and maintains a Rule-Based Dimension in Flexera Cloud Cost Optimization that shows the Azure tenant ID associated with each Azure subscription.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4738) for details about unpublished policies.
- **Merged At**: 2026-07-28 14:41:42 UTC

---

### PR [#4724](https://github.com/flexera-public/policy_templates/pull/4724): POL-1806 Markdown Table Option

*Minor Update*

#### Description

> Adds an option to render the data table as a nicely formatted markdown table in a handful of policy templates. This is primarily useful for making the table look nice in emails compared to a traditional export table.
>
> Also adds CSV support to some of these policy templates so that the email won't contain redundant tables if desired by the end user.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4724) for these details.
- **Merged At**: 2026-07-24 14:17:08 UTC

---

### PR [#4706](https://github.com/flexera-public/policy_templates/pull/4706): POL-1801 Email Cost Optimization Recommendations: K8s Support

*Minor Update*

#### Description

> `Email Cost Optimization Recommendations`
> - Added support for AWS and Azure cross-family compute recommendations.
> - Added support for Kubernetes recommendations.
>

#### Metadata

- **Policies**: [Email Cost Optimization Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/email_recommendations/README.md)
- **Merged At**: 2026-07-23 15:15:49 UTC

---

### PR [#4714](https://github.com/flexera-public/policy_templates/pull/4714): POL-1804 New Policy Template: Flexera Billing Center Report

*New Policy Template*

#### Description

> New policy template that simply lists the details for all Billing Centers in the org and allows actions to be taken against them.
>

#### Metadata

- **Policies**: [Flexera Billing Center Report](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/bc_report/README.md)
- **Merged At**: 2026-07-22 19:40:34 UTC

---

### PR [#4710](https://github.com/flexera-public/policy_templates/pull/4710): POL-1802 RBD Effective Date Feature

*Unpublished, Minor Update*

#### Description

> Updates the various RBD generating policy templates to include an option to use the current month as the effective date instead of using a static value.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4710) for these details.
- **Merged At**: 2026-07-21 18:56:52 UTC

---

### PR [#4703](https://github.com/flexera-public/policy_templates/pull/4703): POL-1800 AWS Resources Under or Approaching Extended Support Fixes

*Minor Update*

#### Description

> `AWS Resources Under or Approaching Extended Support`
> - Updated cost estimation to reflect AWS's tiered Extended Support pricing: a lower rate for years 1-2 and a higher rate starting in year 3, selected automatically based on the current date.
> - Estimated savings for Multi-AZ RDS instances now account for both the primary and standby instance vCPUs, since AWS bills extended support for both.
> - Added a `Rate Tier` field to the incident export showing which pricing tier applies to each resource.
> - ElastiCache Extended Support is now correctly modeled as a percentage premium on the node's on-demand rate rather than a flat node-hour fee.
> - MariaDB instances are no longer reported by this policy; they are not eligible for AWS RDS Extended Support.
>
> README also now documents the sources of truth for the information used in determining the extended support status of various resource types.
>

#### Metadata

- **Policies**: [AWS Resources Under or Approaching Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/extended_support/README.md), [Meta Parent: AWS Resources Under or Approaching Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/extended_support/README.md)
- **Merged At**: 2026-07-21 13:59:36 UTC

---

### PR [#4692](https://github.com/flexera-public/policy_templates/pull/4692): POL-1778 Container Cost Visibility Setup: Syntax Error Fix

*Minor Update*

#### Description

> Fixes a syntax error in the Container Cost Visibility Setup policy template.
>

#### Metadata

- **Policies**: [Container Cost Visibility Setup](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/spot/container_cost_visibility/README.md)
- **Merged At**: 2026-07-14 17:57:24 UTC

---

### PR [#4678](https://github.com/flexera-public/policy_templates/pull/4678): POL-1796 Untagged Resources: Improved Filtering

*Major Update*

#### Description

> Updates the 3 Untagged Resources policy templates to allow the user to select various resource types (Account, Resource, Subscription, etc.) from a list. This allows the user to report only Subscriptions, only Resources, etc. as desired.
>
> Also fixes a Dangerfile issue where a change to a policy template's MAJOR version would trigger an error if the MINOR UPDATE label wasn't applied to the PR, and adds "labelable" to the .spellignore since [this is a valid English word](https://en.wiktionary.org/wiki/labelable).
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4678) for these details.
- **Merged At**: 2026-07-08 13:16:57 UTC

---

### PR [#4675](https://github.com/flexera-public/policy_templates/pull/4675): POL-1795 New Policy Template: Flexera Create Service Account

*Unpublished, New Policy Template*

#### Description

> `Flexera Create Service Account`
>
> This policy template creates a Flexera service account via the IAM API, assigns the specified org-level roles to it, generates a client secret, and then registers an OAuth2 credential in Flexera Automation using that client ID and secret. If all steps succeed, an incident is raised containing the credential details and confirmation of role assignments.
>
> Template is unpublished because it is more intended for internal Flexera use. A Flexeran can add their own token to a new org as a credential, run this to quickly create a service account, and then delete their credential from the Flexera Org, leaving behind a functioning service account that does not require that the client maintain a token associated with someone at their organization to execute policy templates.
>
> (Ignore the dangerfile warning. This is a special case where readability requires something off-spec)
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4675) for details about unpublished policies.
- **Merged At**: 2026-07-07 13:53:00 UTC

---

### PR [#4659](https://github.com/flexera-public/policy_templates/pull/4659): POL-1788 AWS Tag Cardinality: API Update

*Minor Update*

#### Description

> Removes the "status" field from the API call to list AWS accounts. This field is changing on the AWS side to "state" and is not actually used at all during policy execution.
>

#### Metadata

- **Policies**: [AWS Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/tag_cardinality/README.md)
- **Merged At**: 2026-07-02 14:44:19 UTC

---

### PR [#4660](https://github.com/flexera-public/policy_templates/pull/4660): POL-1794 Google Cloud Resources Under or Approaching Extended Support: sys- and app- Project Filtering

*Minor Update*

#### Description

> Adds the following parameters to the `Google Cloud Resources Under or Approaching Extended Support` policy template:
>
> - *Ignore System Projects* - Whether or not to automatically ignore system projects (projects whose ID begins with `sys-`).
> - *Ignore Google Apps Script Projects* - Whether or not to automatically ignore Google Apps Script projects (projects whose ID begins with `app-`).
>

#### Metadata

- **Policies**: [Google Cloud Resources Under or Approaching Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/google/extended_support/README.md), [Meta Parent: Google Cloud Resources Under or Approaching Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/google/extended_support/README.md)
- **Merged At**: 2026-07-01 17:37:34 UTC

---

### PR [#4656](https://github.com/flexera-public/policy_templates/pull/4656): POL-1792 RBD from CSV Efficiency Improvements

*Minor Update*

#### Description

> Updates the RBD from CSV policy templates to be more efficient, reducing the risk of timeouts or memory issues.
>
> Additionally, makes a small README correction and fixes a false positive produced by the Policy API script.
>

#### Metadata

- **Policies**: [Rule-Based Dimensions from CSV - AWS S3](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/rbd_from_csv_aws_s3/README.md), [Rule-Based Dimensions from CSV - Azure Storage](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/rbd_from_csv_azure_storage/README.md), [Rule-Based Dimensions from CSV - Google Cloud Storage](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/rbd_from_csv_google_storage/README.md), [Rule-Based Dimensions from CSV - Microsoft Graph](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/rbd_from_csv_microsoft_graph/README.md)
- **Merged At**: 2026-07-01 13:27:25 UTC

---

### PR [#4648](https://github.com/flexera-public/policy_templates/pull/4648): POL-1793 AWS Rightsize RDS Instances Updates

*Minor Update*

#### Description

> `AWS Rightsize RDS Instances`
> - Changed Available Memory fields to report memory utilization as a percentage instead of available memory. This aligns the incident with the other usage recommendation policy templates.
> - Fixed issue where valid recommendations were sometimes filtered from the results.
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2026-06-29 19:23:51 UTC

---

### PR [#4612](https://github.com/flexera-public/policy_templates/pull/4612): POL-1790 New Policy Templates: Azure PostgreSQL

*New Policy Template*

#### Description

> Two new policy tempates, `Azure Rightsize PostgreSQL Flexible Servers` and `Azure Rightsize PostgreSQL Single Servers`
>
> Also corrects some issues in the README files for a handful of other Azure DB policy templates.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4612) for these details.
- **Merged At**: 2026-06-29 14:45:55 UTC

---

### PR [#4611](https://github.com/flexera-public/policy_templates/pull/4611): POL-1789 Email Cost Optimization Recommendations: Improvements

*Minor Update*

#### Description

> Email Cost Optimization Recommendations improvements:
> - New `Dimension List` parameter allows filtering recommendations by Rule-Based Dimensions and Tag Dimensions.
> - `Billing Center List` parameter now supports all Billing Centers instead of just top-level ones.
> - Incident table now shows both top-level and bottom-level Billing Center for each recommendation.
>
> Also removes random py file added by mistake in a previous PR.
>

#### Metadata

- **Policies**: [Email Cost Optimization Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/email_recommendations/README.md)
- **Merged At**: 2026-06-29 12:07:15 UTC

---

### PR [#4614](https://github.com/flexera-public/policy_templates/pull/4614): POL-1791 New Policy: Google Cloud Resources Under or Approaching Extended Support

*New Policy Template*

#### Description

> This policy template identifies Google Kubernetes Engine (GKE) clusters and Cloud SQL instances that are currently under extended support or will enter extended support within a configurable number of days. Extended support is a paid tier that allows customers to continue using a software version beyond its standard end-of-life date, incurring additional hourly charges. The policy reports affected resources alongside an estimated monthly extended-support surcharge for each resource.
>
> This also updates Google READMEs across the board to always include information on which APIs need to be enabled.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4614) for these details.
- **Merged At**: 2026-06-26 13:28:28 UTC

---

### PR [#4490](https://github.com/flexera-public/policy_templates/pull/4490): POL-1769 New Policy: Google Idle Vertex AI Online Prediction Endpoints

*New Policy Template*

#### Description

> `Google Idle Vertex AI Online Prediction Endpoints`
>
> This policy template identifies Google Cloud Vertex AI online prediction endpoints that have dedicated compute resources but have received little or no prediction traffic over a configurable lookback window. Only endpoints with at least one deployed model using `dedicatedResources` are evaluated; endpoints configured with `automaticResources` scale to zero and incur no continuous compute cost. Idle endpoints are reported to the user via an incident and can optionally be deleted automatically or after manual approval.
>
> `Policy Agent Fixes`
>
> Updates the agent to avoid using em dashes and similar exotic characters; they do not render correctly in the Flexera One UI.
>

#### Metadata

- **Policies**: [Google Idle Vertex AI Online Prediction Endpoints](https://github.com/flexera-public/policy_templates/tree/master/cost/google/idle_vertex_ai_endpoints/README.md)
- **Merged At**: 2026-06-26 12:07:31 UTC

---

### PR [#4480](https://github.com/flexera-public/policy_templates/pull/4480): POL-1767 New Policy: Azure Idle ML Online Endpoints

*New Policy Template*

#### Description

> `Azure Idle ML Online Endpoints`
> This policy template finds Azure Machine Learning managed online endpoints that are provisioned and running but receiving little or no inference traffic over a user-specified lookback window, then raises an incident with a list of those endpoints. Optionally, it deletes them. Idle managed online endpoints consume VM compute continuously regardless of actual usage, making them a significant source of avoidable cloud spend. For low-frequency or batch-oriented inference workloads, batch endpoints or on-demand invocation patterns are far more cost-effective alternatives.
>

#### Metadata

- **Policies**: [Azure Idle ML Online Endpoints](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/idle_ml_online_endpoints/README.md), [Meta Parent: Azure Idle ML Online Endpoints](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/idle_ml_online_endpoints/README.md)
- **Merged At**: 2026-06-26 12:07:18 UTC

---

### PR [#4613](https://github.com/flexera-public/policy_templates/pull/4613): SQ-23518 Azure Storage Accounts Allowing Default Network Access Improvement

*Minor Update*

#### Description

> `Azure Storage Accounts Allowing Default Network Access`
> - Added "Treat Disabled Public Network Access as Compliant" parameter to optionally exclude storage accounts with public network access disabled from results. Default value preserves existing behavior.
>

#### Metadata

- **Policies**: [Azure Storage Accounts Allowing Default Network Access](https://github.com/flexera-public/policy_templates/tree/master/security/azure/storage_network_deny/README.md)
- **Merged At**: 2026-06-25 19:01:27 UTC

---

### PR [#4478](https://github.com/flexera-public/policy_templates/pull/4478): POL-1765 New Policy: AWS Idle SageMaker Endpoints

*New Policy Template*

#### Description

> - New policy template `AWS Idle SageMaker Endpoints`
> - New script/Github workflow for retrieving and storing SageMaker pricing.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4478) for these details.
- **Merged At**: 2026-06-22 17:16:20 UTC

---

### PR [#4565](https://github.com/flexera-public/policy_templates/pull/4565): POL-1784 - Align region values to API identifier used in other AWS Policy Sets

*Minor Update*

#### Description

> We noticed that the AWS Resources Under Extended Support recommendations are using display names, instead of the identifier used when interacting with APIs. This release updates the region values to use the API identifier, which aligns with other AWS Policy Sets.
>

#### Metadata

- **Policies**: [AWS Resources Under or Approaching Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/extended_support/README.md)
- **Merged At**: 2026-06-18 17:41:30 UTC

---

### PR [#4580](https://github.com/flexera-public/policy_templates/pull/4580): POL-1787 New Policy Template: Google Rule-Based Dimension From Project Tags

*Unpublished, New Policy Template*

#### Description

> `Google Rule-Based Dimension From Project Tags`: This policy template creates and updates custom Rule-Based Dimensions that surface the specified Google Cloud resource manager tag key short names in the Flexera One platform. This allows costs to be sliced by the values of the tag keys in question.
>
> (Warnings are not relevant to this policy template)
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4580) for details about unpublished policies.
- **Merged At**: 2026-06-17 18:30:21 UTC

---

### PR [#4573](https://github.com/flexera-public/policy_templates/pull/4573): POL-1786 New Policy Template: AWS Auto Scaling Group Recommendations

*New Policy Template*

#### Description

> New Policy Template: AWS Auto Scaling Group Recommendations
>
> This policy template looks at the EC2 Auto Scaling Groups (ASGs) in your AWS accounts and flags ones that don't appear to be scaling. The most common pattern it catches is an ASG that was set up to grow and shrink with demand but, in practice, always runs at the same size — meaning you're paying for fixed capacity without getting any of the elasticity benefits of an ASG.
>
> The policy raises four distinct findings per ASG:
>
> 1. **Fixed-size ASG** — Min, Max, and Desired capacity are all set to the same number. The ASG cannot scale at all. High confidence.
> 1. **Never moved off floor** — Min is lower than Max (so the ASG *could* scale), but the Desired capacity never actually changed during the lookback window. Either the floor is the real steady-state demand or a scaling policy exists but is never being triggered. High confidence when ASG group metrics are enabled; reduced confidence when the policy has to rely on the scaling-activity history alone.
> 1. **Over-provisioned floor** — Min is greater than 1, and either the peak number of running instances stayed well below Min for the whole lookback window, or aggregate CPU stayed below the configured threshold. This is a "worth a review" finding, not a definitive call — the floor may be deliberately oversized for AZ spread or burst headroom that the metrics can't see. Medium confidence.
> 1. **Group metrics collection disabled** — A hygiene finding raised when the ASG isn't emitting its group-level metrics to CloudWatch. Enabling group metrics is free and unblocks higher-confidence evaluation of findings 2 and 3 on the next policy run. This finding is raised independently of the other three.
>

#### Metadata

- **Policies**: [AWS Auto Scaling Group Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/asg_recommendations/README.md), [Meta Parent: AWS Auto Scaling Group Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/asg_recommendations/README.md)
- **Merged At**: 2026-06-17 13:08:09 UTC

---

### PR [#4558](https://github.com/flexera-public/policy_templates/pull/4558): POL-1785 Untagged Resources Bug Fix

*Minor Update*

#### Description

> Fixed bug in the various "Untagged Resources" policy templates where resources whose missing tags were fully covered by Tag Dimension equivalents were still included in the incident with a blank `Missing Tags` field instead of being correctly excluded.
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md), [Azure Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_resources/README.md), [Azure Untagged Virtual Machines](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_untagged_vms/README.md), [Google Unlabeled Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/google/unlabeled_resources/README.md)
- **Merged At**: 2026-06-11 18:31:14 UTC

---

### PR [#4554](https://github.com/flexera-public/policy_templates/pull/4554): POL-1782 AWS Savings Plan Purchase Analysis: Coverage Target Support

*Minor Update*

#### Description

> `AWS Savings Plan Purchase Analysis`
> - Added `Automatic (Linked Account Credentials)` option to `Account Scope` parameter to infer scope instead of specifying it
> - Added `Analysis Type` parameter to support both `Custom Commitment` and `Target Average Coverage` analysis types
> - Updated `Hourly Purchase Commitment` parameter description to clarify it is only applicable for the `Custom Commitment` analysis type
> - Added `Target Coverage Percentage` parameter to support `SavingsPlansTargetCoverage` when Analysis Type is set to `Target Average Coverage`
> - Added `Target Coverage Percentage` field to incident report output
> - Added `Analysis Type` field to incident report output
>

#### Metadata

- **Policies**: [AWS Savings Plan Purchase Analysis](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/purchase_analysis/README.md)
- **Merged At**: 2026-06-10 19:37:35 UTC

---

### PR [#4542](https://github.com/flexera-public/policy_templates/pull/4542): POL-1781 Fix Tag Filtering Logic

*Unpublished, Minor Update*

#### Description

> Fixed bug in many policy templates where the `!~` exclusion tag operator incorrectly excluded resources whose tag value matched the regex instead of excluding those that did not match
>
> (Dangerfile warnings/errors not related to the above change)

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4542) for these details.
- **Merged At**: 2026-06-09 14:06:49 UTC

---

### PR [#4535](https://github.com/flexera-public/policy_templates/pull/4535): POL-1777 Azure Sentinel Commitment Tier Recommendations Fix

*Minor Update*

#### Description

> `Azure Sentinel Commitment Tier Recommendations`
> - Fixed bug where workspaces using Azure Sentinel Simplified pricing (unified SKU) received no recommendations or incorrect savings estimates. The policy now detects the pricing scheme per workspace via the OperationsManagement Solutions API and applies the correct rate model: Simplified workspaces use the all-inclusive Sentinel unified rate; Classic workspaces continue to use the sum of Log Analytics and Sentinel component rates.
> - Added `Pricing Scheme` field to the incident table, indicating whether each recommendation was generated using Classic or Simplified pricing.
> - Added downgrade and PAYG switch recommendations: the policy now evaluates all commitment tiers in both directions and checks whether switching to Pay-As-You-Go pricing would be cheaper than a workspace's current commitment tier.
>
> Also fixes a bug in the Policy API script that was generating a false positive for this policy template.
>

#### Metadata

- **Policies**: [Azure Sentinel Commitment Tier Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/sentinel_commitment_tiers/README.md)
- **Merged At**: 2026-06-09 13:24:03 UTC

---

### PR [#4536](https://github.com/flexera-public/policy_templates/pull/4536): POL-1779 Untagged Resources: Tag Dimension Support

*Major Update, Minor Update*

#### Description

> Adds functionality to the Azure/Google Untagged policy templates to support Tag Dimensions, similar to the AWS policy template. Also corrects a bug in the AWS policy template.
>
> Additionally, improves the Policy API script to avoid some false positives caused by the Google Unlabeled Resources policy.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4536) for these details.
- **Merged At**: 2026-06-08 19:40:28 UTC

---

### PR [#4510](https://github.com/flexera-public/policy_templates/pull/4510): POL-1776 Google Committed Use Discount Recommender: "Any" Option

*Minor Update*

#### Description

> Adds an 'Any' option to the term parameter for `Google Committed Use Discount Recommender` to enable reporting of both 1 Year and 3 Year commitments.
>
> Also updates the Policy API script to solve some false positives associated with this policy template.
>

#### Metadata

- **Policies**: [Google Committed Use Discount Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cud_recommendations/README.md)
- **Merged At**: 2026-06-05 14:13:38 UTC

---

### PR [#4508](https://github.com/flexera-public/policy_templates/pull/4508): POL-1775 Azure RI/SP - Fixes for Multiple Options

*Minor Update*

#### Description

> Updates the `Azure Reserved Instances Recommendations` and `Azure Savings Plan Recommendations` policy templates so that, when I user selects multiple terms or payment types, multiple API calls are made and the results genuinely contain all of the recommendations.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md), [Azure Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/savings_plan/recommendations/README.md)
- **Merged At**: 2026-06-05 12:59:01 UTC

---

### PR [#4491](https://github.com/flexera-public/policy_templates/pull/4491): POL-1770 Fix Calculation: Azure Sentinel Commitment Tier Recommendations

*Minor Update*

#### Description

> `Azure Sentinel Commitment Tier Recommendations`
> - Fixed incorrect overage billing calculation: usage exceeding a commitment tier's daily GB level is now billed at the tier's effective per-GB rate (`Tier Daily Rate / Tier GB Level`) rather than the Pay-As-You-Go rate, consistent with Microsoft Sentinel pricing.
>
> `tools/policy_api_list_generation/policy_api_list_generator.py`
> - Fixed issue causing false positives with Microsoft.Sentinel API calls.
>

#### Metadata

- **Policies**: [Azure Sentinel Commitment Tier Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/sentinel_commitment_tiers/README.md), [Meta Parent: Azure Sentinel Commitment Tier Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/sentinel_commitment_tiers/README.md)
- **Merged At**: 2026-06-04 16:48:26 UTC

---

### PR [#4501](https://github.com/flexera-public/policy_templates/pull/4501): POL-1774 AWS RI/SP - Fixes for Multiple Options

*Major Update, Minor Update*

#### Description

> Updates the `AWS Reserved Instances Recommendations` policy template so that, when a user selects multiple terms or payment types, multiple API calls are made and the results genuinely contain all of the recommendations. This functionality has also been added to the `AWS Savings Plan Recommendations` policy template.
>

#### Metadata

- **Policies**: [AWS Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/recommendations/README.md), [AWS Savings Plan Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/recommendations/README.md)
- **Merged At**: 2026-06-04 13:39:12 UTC

---

### PR [#4477](https://github.com/flexera-public/policy_templates/pull/4477): POL-1564 Resource Group Filtering / Metas

*Unpublished, Minor Update*

#### Description

> This makes two changes to Azure policy templates throughout the catalog:
> - Adds Resource Group level filtering, similar to the existing Subscription filtering parameters.
> - Adds *unpublished* meta policies that create a child policy per Resource Group instead of Subscription. This is intended for rare situations where even individual Subscriptions have too many resources for the policy engine to handle but likely has its own downsides. Should be used with caution and only with guidance from someone at Flexera.
>
> It also makes some tweaks to the Dangerfile to avoid false positives. Remaining Dangerfile warnings are false positives unrelated to the above changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4477) for these details.
- **Merged At**: 2026-06-03 12:43:54 UTC

---

### PR [#4493](https://github.com/flexera-public/policy_templates/pull/4493): POL-1772 Update "Flexera One User Access Report" Policy Template to use api.flexera.com

*Minor Update*

#### Description

> Updates "Flexera One User Access Report" Policy Template to use api.flexera.com when listing groups. The GRS API currently used is being deprecated and was only used at the time because api.flexera.com did not yet support listing groups or their membership.
>

#### Metadata

- **Policies**: [Flexera One User Access Report](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/iam/iam_user_report/README.md)
- **Merged At**: 2026-06-02 18:08:26 UTC

---

### PR [#4481](https://github.com/flexera-public/policy_templates/pull/4481): POL-1768 Meta Policies: New Option To Skip Consolidated Incidents

#### Description

> This adds a new parameter to meta policies to allow the user to opt out of consolidated incidents. This can be useful in situations where the consolidated incident would exceed the 64MB limit, causing the meta policy to fail. Recommendations for the Optimization dashboard are scraped from the child policies regardless.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4481) for these details.
- **Merged At**: 2026-05-22 17:27:21 UTC

---

### PR [#4459](https://github.com/flexera-public/policy_templates/pull/4459): POL-849 Google Committed Use Discount Recommender: Billing Account Support

*Minor Update*

#### Description

> Adds support for Billing Account-level recommendations for the `Google Committed Use Discount Recommender` policy template.
>
> (Dangerfile warning is a false positive)
>

#### Metadata

- **Policies**: [Google Committed Use Discount Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/cud_recommendations/README.md)
- **Merged At**: 2026-05-18 15:19:54 UTC

---

### PR [#4404](https://github.com/flexera-public/policy_templates/pull/4404): POL-1756 - Fix "Allow/Deny" param and add graceful error detection to Kubernetes Rightsizing Recommendations

*Bug Fix*

#### Description

> - Added error detection for Ocean clusters that fail to return rightsizing recommendations, with a separate incident that includes the specific error code, affected cluster details, troubleshooting steps, and links to Spot documentation
> - Fixed Allow/Deny Spot Accounts filter so that the "Deny" option correctly excludes the listed accounts
>

#### Metadata

- **Policies**: [Kubernetes - Rightsizing Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/spot/ocean_recommendations/README.md)
- **Merged At**: 2026-05-14 19:27:40 UTC

---

### PR [#4454](https://github.com/flexera-public/policy_templates/pull/4454): POL-0000 - fix: flexeraOrganizationId from string to int

*Bug Fix*

#### Description

> Hotfix to fix curl/powershell output
>

#### Metadata

- **Policies**: [Container Cost Visibility Setup](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/spot/container_cost_visibility/README.md)
- **Merged At**: 2026-05-14 19:27:01 UTC

---

### PR [#4449](https://github.com/flexera-public/policy_templates/pull/4449): POL-1763 - Additional Dimensions Object Storage

*Minor Update*

#### Description

> Adds multi-cloud rules for Object Storage dimensions
>
>
> Cloud | Rules | Category Values | Key Patterns
> -- | -- | -- | --
> AWS | 7 (unchanged) | Storage, Requests, Data Transfer, Data Retrieval, Management & Analytics, Replication, Other Fees | usage_type patterns
> Azure | 8 (new) | Same categories + Early Deletion Penalty | usage_type: "Data Stored", "Operations", "Data Transfer", "Geo-Replication", "Early Delete", etc.
> GCP | 7 (new) | Same categories + Early Deletion Penalty | resource_type: "Storage <location>", "Class A/B Operations", "Transfer/Download", "Retrieval", "Early Delete"
>
>
>

#### Metadata

- **Policies**: [Flexera CCO Additional Dimensions](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/additional_dimensions/README.md)
- **Merged At**: 2026-05-14 19:26:43 UTC

---

### PR [#4385](https://github.com/flexera-public/policy_templates/pull/4385): FOAA-987 - New PT "Container Cost Visibility Setup"

*New Policy Template*

#### Description

> Tool to help users easily complete setup of Container Cost Visibility
>
> - Create cbi-oi-ocean [Bill Connect](https://app.flexera.com/orgs/36084/optima/cloud-settings/billing-config/cbi-oi-ocean-org-606079870754), "[Kubernetes ..." Tag Dimensions](https://app.flexera.com/orgs/36084/optima/cloud-settings/tag-dimensions), and minimal instructions/command to complete final flexeraCcoIntegration step (Step [5. Spot CCO Export ...](https://app.flexera.com/orgs/36084/automation/incidents/projects/138037?incidentId=69ea8f92c38ccc253645dcc2)). All resources required for CCV costs integration from Spot into Flexera via CBI. Manual steps for flexeraCcoIntegration b/c required Flexera RefreshToken value (sensitive, can't be parameter input)
> - Create [Container Cost Visibility Dashboard](https://app.flexera.com/orgs/36084/optima/dashboards?costType=cost_amortized_unblended_adj&dashboardID=LUKKQKFR0AY_1e-l8wY_iQ&endDate=2026-05-01&granularity=Monthly&startDate=2026-04-01&valueFormat=%7B%22c5ddbd5d-7f39-4d61-9fec-90016a1758a0%22%3A%22currency%22%2C%22502c4858-8abb-4e21-8ba5-ceeabbd0388b%22%3A%22currency%22%2C%221685697700043%22%3A%22currency%22%7D) (aligns with show/will keep in demo orgs). Gives a starting point for visibility into container usage/spend.  Proportionality within the cluster(s), and trends over time as data accumulates.
> - [Kubernetes Rightsizing Recommendations](https://app.flexera.com/orgs/36084/automation/incidents/projects/138037?incidentId=69ea85a592f193f0cdb8dfbe) Applied Policy
> - Optional: [Adjustment Rules to Hide CCV Costs](https://app.flexera.com/orgs/36084/optima/adjustments?datedAdjustment=2026-04) generally (i.e. to prevent these "estimated" costs from showing up in real chargeback/showback report)
>

#### Metadata

- **Policies**: [Container Cost Visibility Setup](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/spot/container_cost_visibility/README.md)
- **Merged At**: 2026-05-14 16:17:35 UTC

---

### PR [#4445](https://github.com/flexera-public/policy_templates/pull/4445): POL-1763 New Policy Template: Flexera CCO Additional Dimensions

*Unpublished, New Policy Template, Minor Update*

#### Description

> New policy template `Flexera CCO Additional Dimensions` that creates additional RBDs from pre-created JSON files stored in the `data/custom_dimensions` directory. Currently includes some useful AI dimensions as well as dimensions specific to AWS S3 usage. Also allows the user to specify an external JSON file for custom RBDs.
>
> Also deprecates the unpublished `AWS S3 Usage Type Rule-Based Dimension` policy template and directs users via its README to this policy template instead.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4445) for these details.
- **Merged At**: 2026-05-13 17:33:15 UTC

---

### PR [#4441](https://github.com/flexera-public/policy_templates/pull/4441): POL-1762 FinOps Dashboards Fix

*Minor Update*

#### Description

> Removes "AI/ML Views" dashboard from the default dashboards applied by this policy template. Also adds some additional information in the README about requirements for this dashboard.
>

#### Metadata

- **Policies**: [FinOps Dashboards](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/finops_dashboards/README.md)
- **Merged At**: 2026-05-12 18:51:06 UTC

---

### PR [#4437](https://github.com/flexera-public/policy_templates/pull/4437): POL-1762 FinOps Dashboards: Add AI/ML Dashboard

*Minor Update*

#### Description

> Fixes bugs and adds an AI/ML dashboard to the `FinOps Dashboards` policy template. Also fixes a bug in the Dangerfile that triggered false positives for URLs that would become valid once the PR is merged.
>

#### Metadata

- **Policies**: [FinOps Dashboards](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/finops_dashboards/README.md)
- **Merged At**: 2026-05-12 13:35:38 UTC

---

### PR [#4419](https://github.com/flexera-public/policy_templates/pull/4419): POL-1761 AWS Superseded EBS Volumes: Fix Savings Calculation

*Minor Update*

#### Description

> `AWS Superseded EBS Volumes`
> - Updated savings calculation to use the percentage difference between GP2 and GP3 list prices applied to the actual cost of the resource in Flexera CCO, rather than the raw list price difference. This ensures that savings estimates reflect Flexera adjustment rules and cloud provider discounts.
> - Fixed bug where the `Resource ID` export field had an incorrect path alias, causing the column to be blank in incident exports.
> - Fixed bug where the `Resource Name` export field had an incorrect path alias, causing the column to be blank in incident exports.
> - Fixed incorrect description for the `AWS Regional Pricing API` parameter, which incorrectly referred to "unused IP addresses" instead of EBS volumes.
> - Fixed potential "NaN%" display in the incident message when no GP2 volumes are found in the account.
> - Fixed upstream list price filter to use strict greater-than (`savings > 0`) instead of greater-than-or-equal, excluding volumes where GP2 and GP3 list prices are identical and no savings opportunity exists.
> - Incident will no longer re-trigger if `Estimated Monthly Cost` changes but the actual recommendation is the same.
>

#### Metadata

- **Policies**: [AWS Superseded EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_ebs_volumes/README.md), [Meta Parent: AWS Superseded EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_ebs_volumes/README.md)
- **Merged At**: 2026-05-11 12:03:24 UTC

---

### PR [#4416](https://github.com/flexera-public/policy_templates/pull/4416): POL-1758 New Policy Template: AWS Rightsize EC2 Instances (Cross-Family)

*New Policy Template*

#### Description

> Adds a new policy template, `AWS Rightsize EC2 Instances (Cross-Family)`, that provides cross-family recommendations and can be used as an alternative to the `AWS Rightsize EC2 Instances` policy template. Enough had to fundamentally change to make this work to make it a new policy template.
>
> Also updates the AWS EC2 pricing script/data to be more accurate, since this policy template relies on list pricing to make sure it's finding the cheapest possible size that fits the workload.
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances (Cross-Family)](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances_cross_family/README.md), [Meta Parent: AWS Rightsize EC2 Instances (Cross-Family)](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances_cross_family/README.md)
- **Merged At**: 2026-05-08 18:44:19 UTC

---

### PR [#4418](https://github.com/flexera-public/policy_templates/pull/4418): POL-1760 New Policy Template: Azure Rightsize Compute Instances (Cross-Family)

*New Policy Template*

#### Description

> Adds a new policy template, `Azure Rightsize Compute Instances (Cross-Family)`, that provides cross-family recommendations and can be used as an alternative to the `Azure Rightsize Compute Instances` policy template. Enough had to fundamentally change to make this work to make it a new policy template.
>
> Also adds some missing regions to the Azure `regions.json` file and makes a minor fix to our policy testing Github Workflow to prevent future issues.
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances (Cross-Family)](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances_cross_family/README.md), [Meta Parent: Azure Rightsize Compute Instances (Cross-Family)](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances_cross_family/README.md)
- **Merged At**: 2026-05-08 18:37:10 UTC

---

### PR [#4390](https://github.com/flexera-public/policy_templates/pull/4390): POL-1423 Azure Hybrid Use Benefit Policies: Ignore "Azure Plan for DevTest" Subscriptions

*Minor Update*

#### Description

> This updates the `Azure Hybrid Use Benefit for Windows Server` and `Azure Hybrid Use Benefit for SQL
> ` policy templates to ignore subscriptions with the "Azure Plan for DevTest" plan, since these plans already include free licenses and VMs running in them do not benefit from AHUB. For the latter, only SQL VMs have this change implemented, since the other AHUB recommendations still apply.
>

#### Metadata

- **Policies**: [Azure Hybrid Use Benefit for Windows Server](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit/README.md), [Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md)
- **Merged At**: 2026-04-24 18:58:38 UTC

---

### PR [#4386](https://github.com/flexera-public/policy_templates/pull/4386): POL-763 Instance Cost Per Hour policy Templates

*New Policy Template, Minor Update*

#### Description

> Adds new Instance Cost Per Hour policy templates for Azure and GCP. Also makes some minor improvements to the AWS policy template and publishes it in the catalog.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4386) for these details.
- **Merged At**: 2026-04-24 15:48:44 UTC

---

### PR [#4384](https://github.com/flexera-public/policy_templates/pull/4384): POL-1307 Tag Cardinality Meta Policy Fix

*Minor Update*

#### Description

> This replaces the meta parents for the AWS, Azure, and Google tag cardinality policies with custom, non-generated ones that correctly combine the child incidents. They have been removed from the YAML file so they will not be overwritten. A new META_README.md for each one contains the details.
>

#### Metadata

- **Policies**: [Meta Parent: AWS Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/tag_cardinality/README.md), [Meta Parent: Azure Tag Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/tag_cardinality/README.md), [Meta Parent: Google Label Cardinality Report](https://github.com/flexera-public/policy_templates/tree/master/operational/google/label_cardinality/README.md)
- **Merged At**: 2026-04-24 15:48:34 UTC

---

### PR [#4379](https://github.com/flexera-public/policy_templates/pull/4379): POL-1705 Azure Subscription Error Incidents

*Unpublished, Minor Update*

#### Description

> Adds a new error incident to most Azure policy templates to report when the Azure API doesn't return any subscriptions so that the user knows there is likely a credential issue.
>
> Also fixes a few misc. Dangerfile issues in a handful of policy templates.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4379) for these details.
- **Merged At**: 2026-04-23 15:07:16 UTC

---

### PR [#4375](https://github.com/flexera-public/policy_templates/pull/4375): POL-1705 Google Project Error Incidents

*Unpublished, Minor Update*

#### Description

> Adds a new error incident to all relevant Google policy templates to report if the credential is not able to access any Google Projects. This way, the lack of results in this scenario is not incorrectly interpreted as a legitimate lack of optimization opportunities.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4375) for these details.
- **Merged At**: 2026-04-22 14:58:25 UTC

---

### PR [#4369](https://github.com/flexera-public/policy_templates/pull/4369): POL-1755 New Policy Template: Azure Sentinel Commitment Tier Recommendations

*New Policy Template*

#### Description

> New rate reduction policy template `Azure Sentinel Commitment Tier Recommendations`:
>
> This policy template identifies Azure Log Analytics workspaces with [Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/) enabled where purchasing or upgrading a daily ingestion Commitment Tier would reduce costs compared to the current pricing tier. It queries each workspace's actual ingestion data over the user-specified lookback period and compares the cost of the current pricing tier (Pay-As-You-Go or an existing commitment level) against each available higher commitment tier using real-time pricing data from the Azure Retail Prices API. When a higher commitment tier is found to produce lower overall monthly costs, an incident is raised with a recommendation to upgrade.
>

#### Metadata

- **Policies**: [Azure Sentinel Commitment Tier Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/sentinel_commitment_tiers/README.md), [Meta Parent: Azure Sentinel Commitment Tier Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/sentinel_commitment_tiers/README.md)
- **Merged At**: 2026-04-21 20:12:12 UTC

---

### PR [#4361](https://github.com/flexera-public/policy_templates/pull/4361): POL-1376 New Policy Template: AWS Superseded RDS Instances

*New Policy Template*

#### Description

> New policy template for reporting on RDS instances that have been superseded. Also updates the instance type JSON files and scripts to include information specific to RDS.
>

#### Metadata

- **Policies**: [AWS Superseded RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_rds_instances/README.md), [Meta Parent: AWS Superseded RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/superseded_rds_instances/README.md)
- **Merged At**: 2026-04-21 13:29:44 UTC

---

### PR [#4356](https://github.com/flexera-public/policy_templates/pull/4356): POL-1176 Azure Hybrid Use Benefit for SQL: Added Estimated Savings

*Minor Update*

#### Description

> Adds estimated savings to the `Azure Hybrid Use Benefit for SQL` policy template, along with a Github workflow and script for gathering licensing pricing information to support this policy template.
>

#### Metadata

- **Policies**: [Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md), [Meta Parent: Azure Hybrid Use Benefit for SQL](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit_sql/README.md)
- **Merged At**: 2026-04-20 15:37:32 UTC

---

### PR [#4341](https://github.com/flexera-public/policy_templates/pull/4341): POL-1177 Add Savings to Azure AHUB Linux Policy Template

*Minor Update*

#### Description

> - `Azure Hybrid Use Benefit for Linux Server`
>   - Added `Estimated Monthly Savings` to incident output based on Azure Linux license pricing data from the Azure Retail Prices API
>   - Added `Minimum Savings Threshold` parameter to filter out low-value recommendations
>   - Incident results are now sorted by estimated savings in descending order
> - Adds a Github Workflow and script to generate and store license pricing data for the above
> - Updates the READMEs for all of the subdirectories in `data/` to provide much more detailed information
> - Updates the Github copilot agent to update the above READMEs when adding to or changing the JSON files in `data/`
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4341) for these details.
- **Merged At**: 2026-04-20 12:55:29 UTC

---

### PR [#4310](https://github.com/flexera-public/policy_templates/pull/4310): POL-1752 New Policy: Common Bill Ingestion from Google Cloud Storage

*Unpublished, New Policy Template*

#### Description

> Adds two new policy templates for ingesting CBI files from Google Cloud Storage. Functionally identical to the existing policy templates that do the same for AWS and Azure.
>

#### Metadata

- **Policies**: [Common Bill Ingestion from Google Cloud Storage](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cbi_ingestion_google_gcs/README.md)
- **Merged At**: 2026-04-20 12:12:22 UTC

---

### PR [#4335](https://github.com/flexera-public/policy_templates/pull/4335): FOPTS-22112 Fixed a string concatenation bug in Dynamic Dashboards Policy.

*Bug Fix*

#### Description

> Fixed a string concatenation bug in Dynamic Dashboards Policy.
>
> The error raises because `$dashboard["verb"]` results to `null`, and `+` operator does not support "string" plus "null".
> > "+ operator cannot be applied between a string and a null"
>
> 1. Removed `$dashboard["verb"]`. `verb` is not exported by the Policy, and thus `$dashboard` does not contain field `verb`.
> 2. The addition of `to_s()` is redundant but just to be safe.
>

#### Metadata

- **Policies**: [Dynamic Dashboards](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/cco/dynamic_dashboards/README.md)
- **Merged At**: 2026-04-17 18:41:49 UTC

---

### PR [#4202](https://github.com/flexera-public/policy_templates/pull/4202): POL-1736 - New PTs: RBD from CSV in Azure, AWS, Google, Microsoft OneDrive/Sharepoint

*New Policy Template*

#### Description

> Mostly shared/common logic between Policy Templates, differentiator is the credentials and getting the CSV from storage.
>
> - Uses “divider” column to identify “rule columns” from “rbd columns” to enable using RBDs as rule conditions
> - Improved CSV parsing, escape and special character handling
> - Normalized logic from other RBD from PT (create rbd if not exist, start/end delimiter rules to allow parallel “RBD from …” applied policies)
>
> ### Issues Resolved
>
> https://flexera.atlassian.net/browse/POL-1736
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4202) for these details.
- **Merged At**: 2026-04-17 18:30:53 UTC

---

### PR [#4318](https://github.com/flexera-public/policy_templates/pull/4318): POL-000 - Fix AWS Rightsize EC2 to use deep clone instead of shallow clone for timeseries queries

*Minor Update, Bug Fix*

#### Description

> Fixed bug which would cause policy to use utilization metrics from the last 1d period instead of the correct full lookback period
>

#### Metadata

- **Policies**: [AWS Rightsize EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ec2_instances/README.md)
- **Merged At**: 2026-04-17 13:59:37 UTC

---

### PR [#4317](https://github.com/flexera-public/policy_templates/pull/4317): POL-1753 "message" Fix

*Unpublished, Minor Update*

#### Description

> This fixes an issue introduced when bulk modifying policy templates to add CSV support. Inadvertently, "message" and "total_savings" were added to the export block, which isn't logical since this will cause policy execution to fail due to neither of them being in the export block.
>
> This also fixes a small issue with a Dangerfile test, and adds some necessary entries to hash_exclude for a few policy templates that were missing them.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4317) for these details.
- **Merged At**: 2026-04-17 13:00:23 UTC

---

### PR [#4279](https://github.com/flexera-public/policy_templates/pull/4279): POL-1739 AWS Resources Under Extended Support Refactor

*Major Update*

#### Description

> This updates the `AWS Resources Under Extended Support` policy template to provide the option of reporting resources that are going to be under extended support in the near future. This involved major changes to the policy template, such as requiring an AWS credential. From the CHANGELOG:
>
> - Policy template is now named `AWS Resources Under or Approaching Extended Support`.
> - Policy template now required an AWS credential and has a meta parent for use with multiple AWS accounts.
> - Added `Days Until Extended Support` parameter to report resources approaching extended support within a user-specified number of days.
> - Added `Resource Type`, `Engine Version`, `Status`, `Extended Support Start Date`, `Extended Support End Date`, and `Days Until Extended Support` fields to the incident export.
>
> This PR also makes a couple of misc. changes:
>
> - Updated the Dangerfile test expecting the NEW POLICY TEMPLATE tag to account for renamed policy templates.
> - Updated the copilot policy agent with some improvements.
>

#### Metadata

- **Policies**: [AWS Resources Under or Approaching Extended Support](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/extended_support/README.md)
- **Merged At**: 2026-04-15 12:03:48 UTC

---

### PR [#4284](https://github.com/flexera-public/policy_templates/pull/4284): POL-1748 CSV Support to More Policy Templates

*Unpublished, Minor Update*

#### Description

> Adds CSV support to most of the remaining policy templates that didn't have it.
>
> Also fixes an issue with the recent workflow update where Python pip packages were not being installed properly.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4284) for these details.
- **Merged At**: 2026-04-13 13:56:12 UTC

---

### PR [#4289](https://github.com/flexera-public/policy_templates/pull/4289): POL-1749 - Add cluster/workload table to Kubernetes Rightsizing Recommendation Report

*Minor Update*

#### Description

> Enhances Kubernetes Rightsizing Recommendation Policy Template to include a table for each cluster, with the net of workload changes (similar to how these recommendations are presented in another view in the platform)
>

#### Metadata

- **Policies**: [Kubernetes - Rightsizing Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/spot/ocean_recommendations/README.md)
- **Merged At**: 2026-04-10 14:20:23 UTC

---

### PR [#4288](https://github.com/flexera-public/policy_templates/pull/4288): POL-1265 Cheaper Regions Update

*Minor Update*

#### Description

> - Updates `regions.json` for each cloud provider to indicate the ratio of price difference between each region and the recommended cheaper region to assist in calculate savings.
> - Adds Github workflows/scripts to automate updating the above for AWS and Azure.
> - Updates the three `Cheaper Regions` policy templates to provide an estimated savings based on the above.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4288) for these details.
- **Merged At**: 2026-04-08 18:31:56 UTC

---

