# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#4978](https://github.com/flexera-public/policy_templates/pull/4978): POL-1842 New Marketplace Products: Additional Fields

*Major Update*

#### Description

> Adds additional fields to the incident table for `AWS New Marketplace Products` and `Azure New Marketplace Products` policy templates.
>
> This is a major version change because the new logic to locate the specific date the purchase was made means that there is now a cap of 30 days regarding how far back one can look for new products. This is unlikely to actually affect any users (the default was and remains 10 days) but it is technically a breaking change.
>

#### Metadata

- **Policies**: [AWS New Marketplace Products](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/marketplace_new_products/README.md), [Azure New Marketplace Products](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/marketplace_new_products/README.md)
- **Merged At**: 2026-09-11 15:07:49 UTC

---

### PR [#4974](https://github.com/flexera-public/policy_templates/pull/4974): POL-1841 Content-Type Update

*Unpublished, Minor Update*

#### Description

> Updates all policy templates to use "Content-Type" instead of "content-type" in API request headers. This is to ensure that the policy engine properly masks the default type of "text/plain" when this header is specified explicitly in the policy template; this masking is currently case sensitive.

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4974) for these details.
- **Merged At**: 2026-09-11 13:17:42 UTC

---

### PR [#4970](https://github.com/flexera-public/policy_templates/pull/4970): POL-1836 Currency Conversion Fixes

#### Description

> - Fixed `415 Unsupported Media Type` when applying adjustments - lowercase `content-type` header didn't override the engine's default `text/plain`, so both were sent. Same fix applied to Container Cost Visibility (unverified, but identical code).
> - Fixed incident name showing `<no value>` instead of the currency codes - `summary_template` referenced a datasource via the `parameters` namespace.
> - Fixed incident detail showing `[object Object]` instead of the month - concatenated the month loop variable instead of `date['current']`.
>
> Versions bumped: Currency Conversion 5.1.6, Container Cost Visibility 0.1.6.
>

#### Metadata

- **Policies**: [Container Cost Visibility Setup](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/spot/container_cost_visibility/README.md), [Currency Conversion](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/currency_conversion/README.md)
- **Merged At**: 2026-09-10 14:35:56 UTC

---

### PR [#4966](https://github.com/flexera-public/policy_templates/pull/4966): POL-1835 Meta Parent Frequency Changes

*Minor Update*

#### Description

> Modifies meta parent policy templates so that, if the frequency parameter for child policies is changed, the child policies themselves will be updated accordingly. In doing so, I found and fixed a bug that was preventing similar functionality for when other parameters are changed from working correctly.
>
> Also updates the hand-managed meta parents to include this and other changes made to meta parents so that they are up to date.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4966) for these details.
- **Merged At**: 2026-09-09 12:07:55 UTC

---

### PR [#4957](https://github.com/flexera-public/policy_templates/pull/4957): POL-1831 RBD from CSV Policy Templates: Current Month Support

*Unpublished, Minor Update*

#### Description

> Adds an "Effective Date Mode" parameter to the RBD from CSV policies that functions similarly to the same parameter in the other RBD policies.
>
> Also corrects some bugs related to how datasources were being used as parameters across a handful of policy templates.
>
> Also updates the policy dev agent to be aware of the risks when using datasources as parameters.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4957) for these details.
- **Merged At**: 2026-09-04 14:35:40 UTC

---

### PR [#4953](https://github.com/flexera-public/policy_templates/pull/4953): POL-1833 Savings Plan Policies: Parameter Fix

*Minor Update*

#### Description

> Two policy templates recently had meta parent functionality enabled but were missing the AWS account number parameter. This PR fixes that.
>

#### Metadata

- **Policies**: [AWS Expiring Savings Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/expiration/README.md), [Meta Parent: AWS Expiring Savings Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/expiration/README.md), [AWS Savings Plan Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/utilization/README.md), [Meta Parent: AWS Savings Plan Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/utilization/README.md)
- **Merged At**: 2026-09-03 14:29:22 UTC

---

### PR [#4950](https://github.com/flexera-public/policy_templates/pull/4950): SQ-28381 Policy Sanitization Fix

*Unpublished, Minor Update*

#### Description

> Fixes an issue accidentally introduced with a previous PR in a handful of PRs because datasources can't be referenced directly in a join() statement even if they contain a raw string.
>
> Also updates the policy dev agent to fix this issue going forward with automated changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4950) for these details.
- **Merged At**: 2026-09-03 14:14:48 UTC

---

### PR [#4940](https://github.com/flexera-public/policy_templates/pull/4940): POL-1833 Savings Plan Policies: Meta Parents

*Minor Update*

#### Description

> Adds meta parent support to the `AWS Savings Plan Utilization` and `AWS Expiring Savings Plans` policy templates. This is because the DescribeSavingsPlans API call does not report the entire estate as previously assumed.
>

#### Metadata

- **Policies**: [AWS Expiring Savings Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/expiration/README.md), [Meta Parent: AWS Expiring Savings Plans](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/expiration/README.md), [AWS Savings Plan Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/utilization/README.md), [Meta Parent: AWS Savings Plan Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/savings_plan/utilization/README.md)
- **Merged At**: 2026-09-03 12:00:22 UTC

---

### PR [#4941](https://github.com/flexera-public/policy_templates/pull/4941): POL-1834 AWS Reserved Instances Coverage: Support for Additional Services

*Minor Update*

#### Description

> Adds support for ElastiCache, OpenSearch Service, Redshift, and Relational Database Service to the `AWS Reserved Instances Coverage` policy template. Previously, this policy template only reported on EC2.
>

#### Metadata

- **Policies**: [AWS Reserved Instances Coverage](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/reserved_instances/coverage/README.md)
- **Merged At**: 2026-09-02 19:20:53 UTC

---

### PR [#4891](https://github.com/flexera-public/policy_templates/pull/4891): POL-1832 Policy Template Bug Fix Pass [19]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4891) for these details.
- **Merged At**: 2026-09-02 12:51:47 UTC

---

### PR [#4890](https://github.com/flexera-public/policy_templates/pull/4890): POL-1832 Policy Template Bug Fix Pass [18]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4890) for these details.
- **Merged At**: 2026-09-02 12:32:52 UTC

---

### PR [#4889](https://github.com/flexera-public/policy_templates/pull/4889): POL-1832 Policy Template Bug Fix Pass [17]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4889) for these details.
- **Merged At**: 2026-09-02 12:20:04 UTC

---

### PR [#4888](https://github.com/flexera-public/policy_templates/pull/4888): POL-1832 Policy Template Bug Fix Pass [16]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4888) for these details.
- **Merged At**: 2026-09-02 12:19:14 UTC

---

### PR [#4887](https://github.com/flexera-public/policy_templates/pull/4887): POL-1832 Policy Template Bug Fix Pass [15]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4887) for these details.
- **Merged At**: 2026-09-02 12:18:52 UTC

---

### PR [#4886](https://github.com/flexera-public/policy_templates/pull/4886): POL-1832 Policy Template Bug Fix Pass [14]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4886) for these details.
- **Merged At**: 2026-09-02 12:18:44 UTC

---

### PR [#4882](https://github.com/flexera-public/policy_templates/pull/4882): POL-1832 Policy Template Bug Fix Pass [10]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4882) for these details.
- **Merged At**: 2026-09-01 13:57:10 UTC

---

### PR [#4880](https://github.com/flexera-public/policy_templates/pull/4880): POL-1832 Policy Template Bug Fix Pass [08]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4880) for these details.
- **Merged At**: 2026-09-01 13:57:06 UTC

---

### PR [#4885](https://github.com/flexera-public/policy_templates/pull/4885): POL-1832 Policy Template Bug Fix Pass [13]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4885) for these details.
- **Merged At**: 2026-09-01 12:45:01 UTC

---

### PR [#4884](https://github.com/flexera-public/policy_templates/pull/4884): POL-1832 Policy Template Bug Fix Pass [12]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4884) for these details.
- **Merged At**: 2026-09-01 12:44:53 UTC

---

### PR [#4883](https://github.com/flexera-public/policy_templates/pull/4883): POL-1832 Policy Template Bug Fix Pass [11]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4883) for these details.
- **Merged At**: 2026-09-01 12:02:36 UTC

---

### PR [#4881](https://github.com/flexera-public/policy_templates/pull/4881): POL-1832 Policy Template Bug Fix Pass [09]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4881) for these details.
- **Merged At**: 2026-09-01 12:02:27 UTC

---

### PR [#4879](https://github.com/flexera-public/policy_templates/pull/4879): POL-1832 Policy Template Bug Fix Pass [07]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4879) for these details.
- **Merged At**: 2026-09-01 12:02:19 UTC

---

### PR [#4878](https://github.com/flexera-public/policy_templates/pull/4878): POL-1832 Policy Template Bug Fix Pass [06]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4878) for these details.
- **Merged At**: 2026-09-01 12:02:12 UTC

---

### PR [#4876](https://github.com/flexera-public/policy_templates/pull/4876): POL-1832 Policy Template Bug Fix Pass [04]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4876) for these details.
- **Merged At**: 2026-09-01 07:56:09 UTC

---

### PR [#4877](https://github.com/flexera-public/policy_templates/pull/4877): POL-1832 Policy Template Bug Fix Pass [05]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4877) for these details.
- **Merged At**: 2026-08-31 12:11:14 UTC

---

### PR [#4875](https://github.com/flexera-public/policy_templates/pull/4875): POL-1832 Policy Template Bug Fix Pass [03]

*Unpublished, Minor Update*

#### Description

> Fixes conditional/data-dependent JavaScript bugs found during a repo-wide audit of policy templates. See individual CHANGELOG.md files for user-facing descriptions of each fix.
>
> Split into multiple PRs due to the large number of changes.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4875) for these details.
- **Merged At**: 2026-08-31 12:10:55 UTC

---

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

