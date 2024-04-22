# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

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

### PR [#1861](https://github.com/flexera-public/policy_templates/pull/1861): POL-1065 Cloud Cost Anomaly Alerts Revamp

#### Description

> This is a revamp of the Cloud Cost Anomaly Alerts policy. From the CHANGELOG:
>
> - Link to Flexera One Cloud Cost Anomalies page now includes filters
> - Incident for invalid dimensions now includes list of valid dimensions
> - Improved text formatting and presentation of incidents
> - Incident now includes currency
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Cloud Cost Anomaly Alerts](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/cloud_cost_anomaly_alerts/README.md)
- **Merged At**: 2024-02-26 17:09:54 UTC

---

### PR [#1842](https://github.com/flexera-public/policy_templates/pull/1842): POL-1018 AWS Policy Regex Support

#### Description

> This adds support for regex tag filtering to several AWS policies.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1842) for these details.
- **Merged At**: 2024-02-26 14:44:21 UTC

---

### PR [#1707](https://github.com/flexera-public/policy_templates/pull/1707): FOPTS-2025 Deployment of Rightsize Azure NetApp Files Policy

#### Description

> Deploy Rightsize NetApp Files Policy
>
> ### Link to applied policy
>
> https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65d5596c2cd37e0001aa6328
>
> You can also watch this GIF:
> ![azure-rightsize-netapp-files-demo](https://github.com/flexera-public/policy_templates/assets/54189123/d820bde3-5810-41bd-a8ae-d7137fc07f89)
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/FOPTS-2025
>

#### Metadata

- **Policies**: [Azure Rightsize NetApp Files](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_netapp_files/README.md)
- **Merged At**: 2024-02-23 17:42:29 UTC

---

### PR [#1841](https://github.com/flexera-public/policy_templates/pull/1841): POL-1017 AWS Old Snapshots Regex Support

#### Description

> This adds regex support to the AWS Old Snapshots policy. This is a breaking change, hence the major version number change, but anyone not currently using the tag filtering functionality should not be impacted by this change.
>

#### Metadata

- **Policies**: [AWS Old Snapshots](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/old_snapshots/README.md)
- **Merged At**: 2024-02-23 13:18:40 UTC

---

### PR [#1840](https://github.com/flexera-public/policy_templates/pull/1840): POL-996 AWS Burstable EC2 Instances Revamp

#### Description

> This is a revamp of the AWS Burstable EC2 Instances policy, including actions. From the CHANGELOG:
>
> - Policy name changed to reference EC2 service directly
> - Policy now consistently gathers correct CloudWatch statistics
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by multiple tag key:value pairs
> - Removed cooldown parameter/functionality and set default policy frequency to "monthly"
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export for added context
> - Policy no longer raises new escalations if tag data has changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Added logic required for "Meta Policy" use-cases
> - Flexera credential now required to facilitate meta policy use cases
>

#### Metadata

- **Policies**: [AWS Burstable EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/burstable_ec2_instances/README.md)
- **Merged At**: 2024-02-23 13:18:28 UTC

---

### PR [#1847](https://github.com/flexera-public/policy_templates/pull/1847): Currency Conversion Fixes

#### Description

> An error was found in the currency conversion implementation in some policies. This is the fix for it.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1847) for these details.
- **Merged At**: 2024-02-22 20:01:27 UTC

---

### PR [#1828](https://github.com/flexera-public/policy_templates/pull/1828): POL-1054 New Policy: Azure Bring-Your-Own-License (BYOL) Report

#### Description

> This new policy analyzes the stored billing data for Microsoft Azure from 2 days ago to a user-specified number of days back and reports on the number of VMs using the Bring-Your-Own-License (BYOL) feature each day. The report includes daily numbers and percentages as well as the peak total BYOL usage and peak percentage BYOL usage and is emailed to a user-specified list of email addresses.
>

#### Metadata

- **Policies**: [Azure Bring-Your-Own-License (BYOL) Report](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/byol_report/README.md)
- **Merged At**: 2024-02-21 13:06:33 UTC

---

### PR [#1829](https://github.com/flexera-public/policy_templates/pull/1829): FOPTS-3031 Update parameters of Azure Rightsize Managed Disk policy

#### Description

> - Updated the descriptions and labels of the IOPS and throughput parameters in the README and policy template files.
> - Updated the short description of the policy.
> - Changed the functionality of `param_min_savings`: Before this version, the `param_min_savings` parameter was used to consider the total savings (the sum of all the savings per resource) and not the savings per resource to decide whether to recommend or not. In this new version, this parameter is used to recommend or not based on the savings of each resource, just as other policies do.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/FOPTS-3170
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-02-16 17:46:03 UTC

---

### PR [#1830](https://github.com/flexera-public/policy_templates/pull/1830): POL-1061 New Policy: Flexera Automation Outdated Applied Policies

#### Description

> This new policy checks all applied policies against the same policy in the catalog to determine if the applied policy is using an outdated version of the catalog policy. An email is sent and an incident is raised with all outdated policies. Optionally, outdated policies can automatically be updated.
>

#### Metadata

- **Policies**: [Flexera Automation Outdated Applied Policies](https://github.com/flexera-public/policy_templates/tree/master/automation/flexera/outdated_applied_policies/README.md)
- **Merged At**: 2024-02-16 13:18:04 UTC

---

### PR [#1817](https://github.com/flexera-public/policy_templates/pull/1817): POL-1004 Azure Schedule Instance Revamp

#### Description

> This is a full revamp of the Azure Schedule Instance policy, including CWF actions. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to specify custom tag keys for tracking instance schedules
> - Added ability to use subscription filter as an allow list or a deny list
> - Added ability to filter resources by multiple tag key:value pairs
> - Added ability to filter resources by region
> - Added ability for user to start and stop instances directly
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export for additional context
> - Streamlined code for better readability and faster execution
> - Policy action error logging modernized and now works as expected in EU/APAC
>

#### Metadata

- **Policies**: [Azure Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/schedule_instance/README.md)
- **Merged At**: 2024-02-13 16:19:13 UTC

---

### PR [#1808](https://github.com/flexera-public/policy_templates/pull/1808): POL-998 AWS Schedule Instance Revamp

#### Description

> This is a full revamp of the AWS Schedule Instance policy, including CWF actions. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to specify custom tag keys for tracking instance schedules
> - Added ability to filter resources by multiple tag key:value pairs
> - Added ability for user to start and stop instances directly
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export for additional context
> - Streamlined code for better readability and faster execution
> - Policy action error logging modernized and now works as expected in EU/APAC
>

#### Metadata

- **Policies**: [AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md)
- **Merged At**: 2024-02-13 13:44:18 UTC

---

### PR [#1819](https://github.com/flexera-public/policy_templates/pull/1819): POL-1005 Google Schedule Instance Revamp

#### Description

> This is a full revamp of the Google Schedule Instance policy, including CWF actions. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to specify custom tag keys for tracking instance schedules
> - Added ability to filter resources by project
> - Added ability to filter resources by region
> - Added ability to filter resources by multiple tag key:value pairs
> - Added ability for user to start and stop instances directly
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export for additional context
> - Streamlined code for better readability and faster execution
> - Policy action error logging modernized and now works as expected in EU/APAC
> - Added logic required for "Meta Policy" use-cases
> - To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential
>

#### Metadata

- **Policies**: [Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2024-02-13 13:09:17 UTC

---

### PR [#1805](https://github.com/flexera-public/policy_templates/pull/1805): POL-1056 New Policy: Azure Missing Subscriptions

#### Description

> This is a net new policy for finding missing subscriptions. For now, this policy is unpublished since the primary user is internal rather than clients directly.
>
> From the README:
>
> This policy checks the stored Flexera CCO billing data for Azure from 3 days ago to obtain a list of Azure Subscriptions that we have billing data for and compares that to the list of Azure Subscriptions returned by the Azure Resource Manager API. An incident is raised and email sent containing any subscriptions present in Flexera CCO but not returned by the Azure Resource Manager API, as well as subscriptions returned by the Azure Resource Manager API but not present in Flexera CCO. The user can select which of those two reports they'd like to produce.
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1805) for details about unpublished policies.
- **Merged At**: 2024-02-08 16:13:44 UTC

---

### PR [#1804](https://github.com/flexera-public/policy_templates/pull/1804): POL-1007 Azure Policies - Add ignore 400 error status

#### Description

> Fixed error in several Azure policies where policy would fail completely when trying to access resources credential does not have access to. Policies will now simply skip these resources.
>
> In many cases, these were regressions caused by copying and pasting from policies that did not have this update done previously. To prevent future regressions, I have gone through all Azure policies to ensure that only the correct datasources with the proper ignore_status functionality will exist in the catalog after this update.
>
> I also did the same with a couple of minor, non-material changes to spacing to ensure consistency. In cases where this was the only change made, I did not bother iterating the version number or updating the changelog because these changes do not affect policy execution whatsoever. These changes are:
>
> query "api-version"," -> query "api-version", " (Added space after comma)
> ignore_status [400,403,404] -> ignore_status [400, 403, 404] (Added space between numbers)
> changelog.md -> CHANGELOG.md (Renamed this file in a couple of places where it was incorrectly in lowercase)
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1804) for these details.
- **Merged At**: 2024-02-08 15:32:23 UTC

---

### PR [#1799](https://github.com/flexera-public/policy_templates/pull/1799): POL-1055 Correct Path for Azure Blob Storage Optimization Policy

#### Description

> The path for this policy is incorrect and, as a result, does not match the link in the policy's description. The path to this policy should be blob_storage_optimization, not object_storage_optimization, to keep it in line with the name of the policy itself as well as Azure’s own terminology.
>
> ### Issues Resolved
>
> Path to this policy is now correct and matches the link within the policy itself as well as the policy name.
>

#### Metadata

- **Policies**: [Azure Blob Storage Optimization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/blob_storage_optimization/README.md)
- **Merged At**: 2024-02-07 15:04:03 UTC

---

### PR [#1786](https://github.com/flexera-public/policy_templates/pull/1786): POL-1053 Custom Dimension Names in RBD Policies

#### Description

> This adds the ability for the user to specify the names of the created dimensions via a parameter in the unpublished RBD creation policies. The new parameter is a list, and if this parameter is left blank, the existing functionality will occur instead.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1786) for these details.
- **Merged At**: 2024-02-05 21:09:40 UTC

---

### PR [#1793](https://github.com/flexera-public/policy_templates/pull/1793): POL-999 Azure Blob Storage Optimization Revamp

#### Description

> This is a revamp of the Azure Blob Storage Optimization that brings its functionality more in line with the equivalent AWS policy while also ensuring that policy actions have been revamped for better error reporting outside of NAM. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to assess blobs in multiple storage accounts
> - Added ability to filter storage accounts by subscription
> - Added ability to filter storage accounts by region
> - Added ability to filter storage accounts by multiple tag key:value pairs
> - Added ability to delete blobs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if tag data changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Policy now correctly requires both Azure Resource Manager and Azure Storage credentials
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1793) for details about unpublished policies.
- **Merged At**: 2024-02-05 21:09:22 UTC

---

### PR [#1750](https://github.com/flexera-public/policy_templates/pull/1750): POL-997 AWS Object Storage Optimization Revamp

#### Description

> This is a revamp of the AWS Object Storage Optimization policy, similar to other similar revamps. Both the core policy and the CWF actions have been revamped. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter objects by multiple tag key:value pairs
> - Added ability to filter objects/buckets by region
> - Added option to automatically delete offending S3 objects
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added additional fields to incident export
> - Policy no longer raises new escalations if object tags changed but nothing else has
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS Object Storage Optimization](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/object_storage_optimization/README.md)
- **Merged At**: 2024-02-05 18:54:59 UTC

---

### PR [#1747](https://github.com/flexera-public/policy_templates/pull/1747): POL-1003 Azure Long Running Instances Action Revamp

#### Description

> This revamps the policy actions to properly log errors in EU/APAC and also normalizes action names. The CWF code was lifted directly from other, already-updated Azure policies. General policy functionality is unchanged.
>
> From the CHANGELOG:
>
> - Added option to either gracefully or forcefully power off instances
> - Renamed policy actions to conform with Azure's own terminology and documentation
> - Policy action error logging modernized and now works as expected in EU/APAC
>

#### Metadata

- **Policies**: [Azure Long Running Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/azure/azure_long_running_instances/README.md)
- **Merged At**: 2024-02-05 13:06:34 UTC

---

### PR [#1677](https://github.com/flexera-public/policy_templates/pull/1677): FOPTS-2607 Deployment of rightsize azure managed disks policy

#### Description

> Deploy first version of Rightsize Azure Managed Disks policy.
>
> ### Issues Resolved
>
> - https://flexera.atlassian.net/browse/FOPTS-2607
>

#### Metadata

- **Policies**: [Azure Rightsize Managed Disks](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_managed_disks/README.md)
- **Merged At**: 2024-02-02 22:31:32 UTC

---

### PR [#1746](https://github.com/flexera-public/policy_templates/pull/1746): POL-1000 AWS Long Running Instances Action Revamp

#### Description

> This revamps the policy actions to properly log errors in EU/APAC. The CWF code was lifted directly from other, already-updated AWS policies. General policy functionality is unchanged.
>

#### Metadata

- **Policies**: [AWS Long Running Instances](https://github.com/flexera-public/policy_templates/tree/master/operational/aws/long_running_instances/README.md)
- **Merged At**: 2024-02-02 15:11:07 UTC

---

### PR [#1737](https://github.com/flexera-public/policy_templates/pull/1737): POL-994 Azure Disallowed Regions Revamp

#### Description

> This is a revamp similar to other revamps we've done. This revamps both the policy itself and the policy actions. It also changes the name of the policy to better conform to standards established elsewhere in the catalog.
>
> From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added more robust ability to filter resources by subscription
> - Added ability to filter resources by tag key:value pairs
> - Added ability to power off instances instead of deleting them
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Azure Disallowed Regions](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_disallowed_regions/README.md)
- **Merged At**: 2024-02-02 13:11:31 UTC

---

### PR [#1743](https://github.com/flexera-public/policy_templates/pull/1743): POL-995 Google Long Stopped Instances Revamp

#### Description

> This is a revamp similar to other revamps we've done. This revamps both the policy itself and the policy actions. It also changes the name of the policy to better conform to standards established elsewhere in the catalog and adds meta policy support.
>
> From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added more robust ability to filter resources by project
> - Added ability to filter resources by region
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Streamlined code for better readability and faster execution
> - Meta policy support added
> - Policy now requires a valid Flexera credential
>

#### Metadata

- **Policies**: [Google Long Stopped VM Instances](https://github.com/flexera-public/policy_templates/tree/master/compliance/google/long_stopped_instances/README.md)
- **Merged At**: 2024-02-02 13:11:19 UTC

---

### PR [#1751](https://github.com/flexera-public/policy_templates/pull/1751): POL-1042 AWS Untagged Resources Revamp

#### Description

> This is a complete revamp and overhaul of the AWS Untagged Resources policy. Both the policy code and actions have been revamped. From the CHANGELOG:
>
> - Added ability to filter resources by tag key, tag key==value, or using regex
> - Added ability to use all filters as an allow list or a deny list
> - Added additional context to incident description
> - Streamlined code for better readability and faster execution
> - Meta policy support added
>

#### Metadata

- **Policies**: [AWS Untagged Resources](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/untagged_resources/README.md)
- **Merged At**: 2024-02-01 11:34:07 UTC

---

### PR [#1748](https://github.com/flexera-public/policy_templates/pull/1748): POL-1047 Azure Reserved Instances Recommendations Scaling Fixes

#### Description

> We were receiving reports of 429 rate limiting errors from the Azure APIs when attempting to use this policy. The following has been done to try to alleviate this issue:
> - A forced 5 second delay between requests to the Microsoft.Consumption/reservationRecommendations API endpoint has been added.
> - Information has been added to the README recommending that the policy be applied once for each resource type for large cloud estates.
> - Meta policy support has been added.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md)
- **Merged At**: 2024-01-17 19:46:17 UTC

---

### PR [#1735](https://github.com/flexera-public/policy_templates/pull/1735): POL-993 Azure Long Stopped Instances Revamp

#### Description

> This is a revamp similar to other revamps we've done. This revamps both the policy itself and the policy actions. It also changes the name of the policy to better conform to standards established elsewhere in the catalog.
>
> From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added more robust ability to filter resources by subscription
> - Added ability to filter resources by region
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Azure Long Stopped Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/compliance/azure/azure_long_stopped_instances/README.md)
- **Merged At**: 2024-01-16 13:37:44 UTC

---

### PR [#1730](https://github.com/flexera-public/policy_templates/pull/1730): POL-992 AWS Long Stopped Instances Revamp

#### Description

> This is a revamp similar to other revamps we've done. This revamps both the policy itself and the policy actions. It also changes the name of the policy to better conform to standards established elsewhere in the catalog.
>
> From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added additional fields to incident export for additional context
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS Long Stopped EC2 Instances](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/long_stopped_instances/README.md)
- **Merged At**: 2024-01-16 13:24:26 UTC

---

### PR [#1738](https://github.com/flexera-public/policy_templates/pull/1738): POL-1045 Azure Reserved Instances Recommendations: Term Parameter Fix

#### Description

> This fixes an issue where the policy was returning all reservation recommendations instead of either 1 year or 3 year based on the parameter.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Recommendations](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/recommendations/README.md)
- **Merged At**: 2024-01-16 10:25:36 UTC

---

### PR [#1736](https://github.com/flexera-public/policy_templates/pull/1736): POL-1043 Update Meta Policies

#### Description

> The script for generating meta policies has been updated. This is just a PR to regenerate some of the meta policies using this script.

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1736) for details about unpublished policies.
- **Merged At**: 2024-01-12 14:28:44 UTC

---

### PR [#1732](https://github.com/flexera-public/policy_templates/pull/1732): POL-1043 Meta Policy Substring Support

#### Description

> This adds support for substrings when filtering dimensions in the parent policies.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1732) for these details.
- **Merged At**: 2024-01-12 13:12:37 UTC

---

### PR [#1731](https://github.com/flexera-public/policy_templates/pull/1731): POL-1015 Meta Policy Escalation Name Fixes

#### Description

> This changes the name of escalation blocks so that the meta policy generator can properly generate meta policies for these policies. I also removed some strange whitespace characters that were in one of the policies for some reason and replaced them with standard spaces.
>
> Meta policies themselves are unchanged since separate work is being done to update the meta policy templates for new functionality, which will in turn automatically update the meta policies.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1731) for these details.
- **Merged At**: 2024-01-11 19:13:28 UTC

---

### PR [#1718](https://github.com/flexera-public/policy_templates/pull/1718): POL-991 AWS Disallowed Regions Revamp

#### Description

> This is a revamp of the AWS Disallowed Regions policy. Both the policy itself and CWF code for actions have been updated. Most of the code was adapted from similar policies that have received similar improvements. From the CHANGELOG:
>
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if tag data has changed for an instance
> - Policy action error logging modernized and now works as expected in EU/APAC
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [AWS Disallowed Regions](https://github.com/flexera-public/policy_templates/tree/master/compliance/aws/disallowed_regions/README.md)
- **Merged At**: 2024-01-10 14:40:43 UTC

---

### PR [#1719](https://github.com/flexera-public/policy_templates/pull/1719): FOPTS-2229 Added a way to url decode the skiptoken

#### Description

> Replaced the jq function used from rt
>
> ### Issues Resolved
>
> [FOPTS-2229](https://flexera.atlassian.net/browse/FOPTS-2229)
>

#### Metadata

- **Policies**: [Schedule ITAM Report](https://github.com/flexera-public/policy_templates/tree/master/operational/flexera/itam/schedule_itam_report/README.md)
- **Merged At**: 2024-01-09 13:36:56 UTC

---

### PR [#1727](https://github.com/flexera-public/policy_templates/pull/1727): POL-958 Add 'Minimum Age' to Azure Rightsize SQL

#### Description

> Added optional `Minimum Age (Days)` parameter to filter results by age. This is for users that want to avoid reporting on freshly created databases that, as a result of their newness, have not had any connections and would therefore be seen as "unused" by the policy.
>
> This is not a breaking change since the default value of this parameter is 0 and this functions just like the policy did without the parameter.
>
> From the README:
>
> - *Minimum Age (Days)* - The minimum age, in days, since a SQL database was created to produce recommendations for it. Set to 0 to ignore age entirely.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2024-01-08 18:05:59 UTC

---

### PR [#1725](https://github.com/flexera-public/policy_templates/pull/1725): feat: add cluster id filtering for databricks PT

#### Description

> - Add `param_databricks_cluster_list` for filtering to a specific Databricks Cluster within a Databricks Workspace
> - Add `p90`,`p95`,`p99` Threshold Statistic choices
> - Fixed subscription ID and Name output in recommendation
>

#### Metadata

- **Policies**: [Azure Databricks Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/databricks/rightsize_compute/README.md)
- **Merged At**: 2024-01-08 13:17:33 UTC

---

### PR [#1716](https://github.com/flexera-public/policy_templates/pull/1716): POL-989 Azure Old Snapshots Policy Action Revamp

#### Description

> This updates the policy actions to follow current conventions and have better error logging outside of NAM. Functionality is unchanged.
>

#### Metadata

- **Policies**: [Azure Old Snapshots](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/old_snapshots/README.md)
- **Merged At**: 2024-01-04 13:10:00 UTC

---

### PR [#1717](https://github.com/flexera-public/policy_templates/pull/1717): POL-990 Azure Rightsize SQL Policy Action Revamp

#### Description

> This updates the policy actions to follow current conventions and have better error logging outside of NAM. Functionality is unchanged.
>

#### Metadata

- **Policies**: [Azure Rightsize SQL Databases](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_sql_instances/README.md)
- **Merged At**: 2024-01-04 13:09:53 UTC

---

### PR [#1720](https://github.com/flexera-public/policy_templates/pull/1720): POL-988 AWS Unused Volumes Policy Action Revamp

#### Description

> This updates the policy actions to follow current conventions and have better error logging outside of NAM. Functionality is unchanged.
>

#### Metadata

- **Policies**: [AWS Unused Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_volumes/README.md)
- **Merged At**: 2024-01-04 13:09:41 UTC

---

### PR [#1678](https://github.com/flexera-public/policy_templates/pull/1678): POL-981 Azure Untagged Resources Revamp / Untagged Virtual Machines

#### Description

> This PR is for several related things:
>
> - `/data/azure/tag-support.csv` has been replaced with `/data/azure/resource_types.json` due to JSON being natively supported by the policy engine. It also contains information unrelated to tag support, so this new naming is more accurate and will allow for the file to be extended with more resource type related metadata if ever needed. The below `Azure Untagged Resources` policy is the only policy currently making use of this file, so this change should have no impact on other policies.
>
> - `Azure Untagged Resources` policy has been completely rebuilt from the ground up. Core functionality is the same, but new filtering features were added. From the CHANGELOG:
>   - Added ability to filter resources by tag key, tag key==value, or using regex
>   - Added ability to filter resources by region
>   - Added ability to filter resources by Azure resource type
>   - Added ability to use all filters as an allow list or a deny list
>   - Added additional context to incident description
>   - Streamlined code for better readability and faster execution
>   - Policy now requires a valid Flexera One credential
>
> - `Azure Untagged Virtual Machines`: This is a new policy that only checks tags for virtual machines, but due to this narrowed focus, has more functionality than the `Azure Untagged Resources` policy. The incident reports on additional VM-specific metadata, and the policy allows for powering off or deleting instances in addition to tagging them.
>
> - The above policies now support a variety of conditionals as well as regex. Note that, while I have intentionally not documented this since it is not "to spec", using a single = will also work in order to account for user error when entering in values. From the READMEs:
>   - *Tags* - The policy will report resources missing the specified tags. The following formats are supported:
>     - `Key` - Find all resources missing the specified tag key.
>     - `Key==Value` - Find all resources missing the specified tag key:value pair and all resources missing the specified tag key.
>     - `Key!=Value` - Find all resources that have the specified tag key:value pair.
>     - `Key=~/Regex/` - Find all resources where the value for the specified key does not match the specified regex string and all resources missing the specified tag key.
>     - `Key!~/Regex/` - Find all resources where the value for the specified key matches the specified regex string.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1678) for these details.
- **Merged At**: 2024-01-03 20:48:02 UTC

---

### PR [#1713](https://github.com/flexera-public/policy_templates/pull/1713): POL-986 AWS Old Snapshots Policy Action Revamp

#### Description

> This non-breaking change updates the policy actions for the AWS Old Snapshots policy. Functionality is identical, but now the error logging is modernized and should work as expected in EU and APAC.
>

#### Metadata

- **Policies**: [AWS Old Snapshots](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/old_snapshots/README.md)
- **Merged At**: 2024-01-02 13:09:45 UTC

---

### PR [#1714](https://github.com/flexera-public/policy_templates/pull/1714): POL-987 AWS Unused IP Policy Action Revamp

#### Description

> This non-breaking change updates the policy actions for the AWS Unused IP policy. Functionality is identical, but now the error logging is modernized and should work as expected in EU and APAC.
>
> The verbiage for a parameter was also updated to be more clear and the parameter in question was added to the README
>

#### Metadata

- **Policies**: [AWS Unused IP Addresses](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/unused_ip_addresses/README.md)
- **Merged At**: 2024-01-02 13:09:34 UTC

---

### PR [#1704](https://github.com/flexera-public/policy_templates/pull/1704): POL-1010 Scheduled Report Policy Revamp

#### Description

> This is a revamp of the Scheduled Report policy that streamlines it and extends functionality. From the CHANGELOG:
>
> - Added ability to specify custom dimensions for the graph in the report
> - Added ability to filter costs in report by any user-specified dimension
> - Improved incident output for readability and removed references to Optima
> - Incident table now shows the raw data used to create the graph in the report
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: [Scheduled Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/scheduled_reports/README.md)
- **Merged At**: 2023-12-29 14:11:13 UTC

---

### PR [#1706](https://github.com/flexera-public/policy_templates/pull/1706): POL-982 Hybrid Use Benefit Policy - currency separator symbol shown as undefined

#### Description

> n the incident of Hybrid Use Benefit Policy, currency separator is shown as undefined:
>
> ### Issues Resolved
>
> [POL-982](https://flexera.atlassian.net/browse/POL-982)
>

#### Metadata

- **Policies**: [Azure Hybrid Use Benefit for Windows Server](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/hybrid_use_benefit/README.md)
- **Merged At**: 2023-12-27 13:30:57 UTC

---

### PR [#1700](https://github.com/flexera-public/policy_templates/pull/1700): FOPTS-2702 Enabling hyperlinks in Turb policies for incidents.

#### Description

> Enabling hyperlinks in Turbonomics policies for incidents.
>
> ### Issues Resolved
>
> [FOPTS-2702](https://flexera.atlassian.net/browse/FOPTS-2702)

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1700) for these details.
- **Merged At**: 2023-12-19 19:46:41 UTC

---

### PR [#1697](https://github.com/flexera-public/policy_templates/pull/1697): POL-1008 Google Idle Persistent Disk Recommender: Add 'Days Unattached' Parameter

#### Description

> This adds the ability to filter the results by how long a disk has been unattached for. GCP produces recommendations based on whether a disk has been detached for 15 days, and this allows the user to filter those results further, going back to 90 days, by using GCP's native event logging.
>
> This is a non-breaking change; the default value for the relevant parameter is 15 days, equivalent to what GCP already checks for, and if the user has not granted their GCP credential the permissions to access the above logs, then the policy will simply report all of the recommendations as it did before rather than fail.
>

#### Metadata

- **Policies**: [Google Idle Persistent Disk Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/idle_persistent_disk_recommendations/README.md)
- **Merged At**: 2023-12-19 15:26:01 UTC

---

### PR [#1701](https://github.com/flexera-public/policy_templates/pull/1701): POL-1012 AWS Rightsize RDS Dash Fix

#### Description

> This fixes an issue where the policy was not correctly identifying unused instances if they had dashes in the name. The policy was incorrectly using the instance id, rather than the instance name, to find the instance in the Cloudwatch data.
>

#### Metadata

- **Policies**: [AWS Rightsize RDS Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_rds_instances/README.md)
- **Merged At**: 2023-12-19 14:42:36 UTC

---

### PR [#1693](https://github.com/flexera-public/policy_templates/pull/1693): feat: improved logging error handling schedule instance PTs

#### Description

> Improved logging and error handling in the Scheduled Instance Policy Templates (AWS, Google)
>

#### Metadata

- **Policies**: [AWS Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/schedule_instance/README.md), [Google Schedule Instance](https://github.com/flexera-public/policy_templates/tree/master/cost/google/schedule_instance/README.md)
- **Merged At**: 2023-12-15 19:00:19 UTC

---

### PR [#1683](https://github.com/flexera-public/policy_templates/pull/1683): POL-566 Policy Update Notification Revamp

#### Description

> This is a revamp of the Policy Update Notification policy. The policy now works in EU and APAC, but this change required removing support for multiple projects within an org. That said, the vast majority of our users do not have multiple projects, so this is unlikely to be a major downside for most users.
>
> From the CHANGELOG:
>
> - Policy now works in all Flexera orgs regardless of zone
> - Policy now requires a valid Flexera One credential
> - Policy no longer makes use of deprecated APIs
> - Policy no longer reports on multiple accounts within a Flexera organization
> - Policy no longer raises new escalations if applied policy name or catalog template version number changed but nothing else has
> - Improved incident export for clarity and detail
> - Streamlined code for better readability and faster execution
>

#### Metadata

- **Policies**: Not displayed due to PR with no published policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/1683) for details about unpublished policies.
- **Merged At**: 2023-12-13 18:39:14 UTC

---

### PR [#1666](https://github.com/flexera-public/policy_templates/pull/1666): POL-971 Azure Reserved Instances Utilization - update to use Modern Azure APIs

#### Description

> <!-- Describe what this change achieves below -->
> We are currently migrating customers' bill configurations to the new Azure method, however this policy still uses legacy EA APIs, which will be deprecated as part of the migration.
>
> This is a change to update the policy to move away from the legacy EA APIs and utilize the modern Azure APIs.
>
> ### Issues Resolved
>
> <!-- List any existing issues this PR resolves below -->
> Moving the modern Azure APIs resolves the issue of having a dependency on the Azure EA Key as an Automation Credential.
>

#### Metadata

- **Policies**: [Azure Reserved Instances Utilization](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/reserved_instances/utilization/README.md)
- **Merged At**: 2023-12-12 15:15:08 UTC

---

### PR [#1681](https://github.com/flexera-public/policy_templates/pull/1681): POL-757 Azure Rightsize Compute Fixes/Improvements

#### Description

> This is intended to fix a couple of issues with this policy, as well as implement some improvements made to other revamped policies to ensure this one is fully up to date. While this policy should continue to function without issue for most customers, a change to the `Automatic Actions` parameter does technically constitute a breaking change, hence the major version number change.
>
> From the CHANGELOG:
>
> - Fixed issue with resource count in incident subject being off by 1
> - Fixed minor grammar issue if results only include 1 item
> - Renamed policy actions to make it clear whether they are for underutilized or idle instances
> - Added ability to filter resources by tag key via wildcard
> - Added option to power off idle instances
> - Added ability to indicate whether to do a graceful or forced shutdown when powering off instances
> - Improved code related to incident export
> - Updated and improved code for policy actions
>

#### Metadata

- **Policies**: [Azure Rightsize Compute Instances](https://github.com/flexera-public/policy_templates/tree/master/cost/azure/rightsize_compute_instances/README.md)
- **Merged At**: 2023-12-11 18:59:28 UTC

---

