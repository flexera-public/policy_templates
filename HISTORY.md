# flexera-public/policy_templates Change History

## Description

This document contains the last 100 policy template merges for the flexera-public/policy_templates repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

### PR [#1967](): POL-1182 New Policy: AWS Missing Regions

#### Description

> ### Description
> 
> This adds a new unpublished policy to test for AWS regions that are returned as enabled by the AWS API but that we can't actually make requests to.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=660466f37566c288f2dac3f7
> 
> (No incident because our test account has access to everything enabled.)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, New Policy
- **Created At**: 2024-03-27 18:39:18 UTC
- **Merged At**: 2024-03-27 19:23:22 UTC
- **Modified Policies**: aws_missing_regions.pt, aws_missing_regions_meta_parent.pt

### PR [#1954](): POL-1171 AWS Rightsize RDS Instances APAC Fix

#### Description

> ### Description
> 
> This fixes an issue with the policy referencing an invalid API endpoint for the APAC shard. This was fixed in other policies already but somehow this specific policy slipped through the cracks.
> 
> Some other very minor tweaks around block names and ordering of fields were also made for the sake of conformity to other policies and to pass the new lint tests.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-03-25 14:49:22 UTC
- **Merged At**: 2024-03-27 12:26:28 UTC
- **Modified Policies**: aws_rightsize_rds_instances.pt, aws_rightsize_rds_instances_meta_parent.pt

### PR [#1949](): POL-1161 Move currency_reference.json

#### Description

> ### Description
> 
> - currency_reference.json has been copied to `data/currency/currency_reference.json`
> - File also remains in `cost/scheduled_reports` with a README.md file explaining why it is there and indicating not to use that location going forward
> - Policies have been updated to point to the new location at `data/currency/currency_reference.json`
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-03-22 12:32:23 UTC
- **Merged At**: 2024-03-22 14:36:00 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1937](): POL-1158 Policy Catalog Reorganization

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

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-03-21 18:09:03 UTC
- **Merged At**: 2024-03-21 20:02:47 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1930](): FOPTS-3569 Fix: empty bill_source_expressions

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> [Previous version](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65f9bf71d8f0b2e49c9c96f6)
> [With error](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65f9bf02d8f0b2e49c9c96f5)
> [New version](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65f9bc241909b512219a67ff)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: bug, READY-FOR-REVIEW
- **Created At**: 2024-03-19 17:06:45 UTC
- **Merged At**: 2024-03-21 18:17:18 UTC
- **Modified Policies**: azure_savings_realized.pt

### PR [#1931](): POL-1156 Deprecate "Policy Update Notification" Policy

#### Description

> ### Description
> 
> This deprecates the Policy Update Notification policy and directs users to the more up to date and functional Flexera Automation Outdated Applied Policies policy.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-03-19 17:54:47 UTC
- **Merged At**: 2024-03-20 17:50:31 UTC
- **Modified Policies**: policy_update_notification.pt

### PR [#1920](): FOPTS-3519 Fix work with unbudgeted spend for new API

#### Description

> ### Description
> 
> New Budget API v1 not returning budgeted values for some budgets
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/FOPTS-3519
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/28010/automation/applied-policies/projects/123559?policyId=65f0a8cc3ad5094c469602f8
> 
> ### Contribution Check List
> 
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: bug, READY-FOR-REVIEW
- **Created At**: 2024-03-12 19:22:51 UTC
- **Merged At**: 2024-03-19 22:26:39 UTC
- **Modified Policies**: budget_v_actual_spend_report.pt

### PR [#1916](): SQ-6941 Sort the dimensions shown in the report

#### Description

> ### Description
> 
> Fixed bug where incident showed dimensions from column `Grouping Dimensions` in random order.
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/SQ-6941
> 
> ### Link to Example Applied Policy
> 
> Latest version 3.1:
> ![image](https://github.com/flexera-public/policy_templates/assets/54189123/81d0c76b-c412-4d19-b0bf-dd909f36db75)
> As you can see sometimes Azure appears at the beginning and sometimes at the middle
> 
> 
> Incoming version 3.2:
> ![image](https://github.com/flexera-public/policy_templates/assets/54189123/6b606d9d-8e00-4591-a435-fb8c49457fbc)
> Now they appear in the order specified by user.
> https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65efef161909b512219a676e
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL, small fixes
- **Created At**: 2024-03-06 22:53:11 UTC
- **Merged At**: 2024-03-13 16:24:33 UTC
- **Modified Policies**: cloud_cost_anomaly_alerts.pt

### PR [#1818](): feat: initial revision for Google Cloud Run Anomaly Detection PT

#### Description

> ### Description
> 
> New Policy Template from PoC - `Google Cloud Run Anomaly Detection`.  
> 
> <img width="1500" alt="image" src="https://github.com/flexera-public/policy_templates/assets/1490015/800b8c04-eed2-4d92-969f-18e2f3c7e245">
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/incidents/projects/7954?incidentId=65df790199c5e400013ae04b
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: New Policy
- **Created At**: 2024-02-12 19:13:58 UTC
- **Merged At**: 2024-03-06 13:18:15 UTC
- **Modified Policies**: google_cloud_run_anomaly_detection.pt

### PR [#1909](): Add links to documentation in the policy short description

#### Description

> ### Description
> 
> Add links to documentation in the "Budget vs Actual Spend Report" policy short description
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: changelog, documentation
- **Created At**: 2024-03-04 19:04:39 UTC
- **Merged At**: 2024-03-04 19:58:45 UTC
- **Modified Policies**: budget_v_actual_spend_report.pt

### PR [#1882](): POL-1118 Flexera CCO Delete All Billing Centers Policy

#### Description

> ### Description
> 
> This policy deletes all Billing Centers in the Flexera organization it is executed within. The policy will automatically self-terminate the second time it runs to avoid accidental future deletion of Billing Centers.
> 
> This policy is unpublished and primarily intended for internal use.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/projects/7954/policy-templates/65df998bdc59260001cddad8
> 
> The policy has been tested, but the nature of this policy means it can't be left applied to demonstrate that it works. To test it, create some billing centers in org 6 and then apply the policy.
> - The first time the policy executes, it should delete all of the billing centers.
> - The second time the policy executes, it should self-terminate.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, New Policy
- **Created At**: 2024-02-28 21:34:56 UTC
- **Merged At**: 2024-03-04 13:41:58 UTC
- **Modified Policies**: delete_all_billing_centers.pt

### PR [#1881](): POL-1117 Azure Bring-Your-Own-License (BYOL) Report Improvements

#### Description

> ### Description
> 
> - Refactored to no longer require Azure credential
> - Removed parameter for Azure API endpoint since it is no longer needed
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65df663930ca310001db0cb5
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-28 18:09:23 UTC
- **Merged At**: 2024-03-04 13:38:49 UTC
- **Modified Policies**: azure_byol_report.pt

### PR [#1893](): POL-979 AWS Policies: Improve Pricing API Endpoint Parameter

#### Description

> ### Description
> 
> This updates the Pricing API parameter in the `AWS Unused IP Addresses` and `AWS Rightsize EBS Volumes` policies to be more user friendly, and provides better README documentation for the parameter and what it does.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65e0e95ee8a2500001366419
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65e0e98abf861d0001a2abea
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-29 20:34:13 UTC
- **Merged At**: 2024-03-04 13:17:47 UTC
- **Modified Policies**: aws_volumes_rightsizing.pt, aws_volumes_rightsizing_meta_parent.pt, aws_unused_ip_addresses.pt, aws_unused_ip_addresses_meta_parent.pt

### PR [#1778](): FOPTS-3024 - New Budget vs Actual Spend report policy

#### Description

> ### Description
> 
> Email a report of budget vs actual spend so the customer doesn't need to login to Flexera One
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/FLEX-204
> 
> ### Link to Example Applied Policy
> 
> Full budget report:
> https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65e0c8b01b78750001a4d4ab
> 
> With filtered dimensions:
> https://app.flexera.com/orgs/1105/automation/incidents/projects/60073?incidentId=65e21c3d99c5e4000120eb4e
> 
> [Budget used (to compare data and chart)](https://app.flexera.com/orgs/1105/optima/budgets/1ef4c91?budgetName=FinOps%202023%202&endDate=2023-12&startDate=2023-01) 
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, New Policy
- **Created At**: 2024-01-31 16:13:51 UTC
- **Merged At**: 2024-03-01 21:36:24 UTC
- **Modified Policies**: monthly_budget_v_actual.pt, budget_v_actual_spend_report.pt

### PR [#1892](): POL-1127 Meta Policy Duplicate Incidents Fix

#### Description

> ### Description
> 
> Meta policies were sometimes returning duplicate results in the consolidated incident if they terminated a child policy and then replaced it with a new one, because both the old and new incident were being scraped.
> 
> This changes the meta policy template (and meta policies) to filter the child incidents so that only active incidents are considered.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65e0ddf9e8a2500001366412
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [ ] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-29 19:47:41 UTC
- **Merged At**: 2024-02-29 20:01:42 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1867](): POL-1046 Google Open Buckets Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65dcfdb51b78750001a4ceaa
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-26 21:16:47 UTC
- **Merged At**: 2024-02-29 13:45:21 UTC
- **Modified Policies**: google_public_buckets.pt, google_public_buckets_meta_parent.pt

### PR [#1875](): POL-1071 Merge 'AWS RDS Instances' policy into 'AWS Rightsize RDS Instances'

#### Description

> ### Description
> 
> This modifies the AWS Rightsize RDS Instances policy to include Availability Zone, License Model, and vCPUs in the incident output, rendering the AWS RDS Instances policy obsolete.
> 
> Additionally, the AWS RDS Instances policy is flagged as deprecated, and users are directed to the AWS Rightsize RDS Instances policy in the README.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65de53f71b78750001a4d0b1
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-27 21:32:04 UTC
- **Merged At**: 2024-02-29 13:04:22 UTC
- **Modified Policies**: rds_instance_license_info.pt, rds_instance_license_info_meta_parent.pt, aws_rightsize_rds_instances.pt, aws_rightsize_rds_instances_meta_parent.pt

### PR [#1873](): POL-973 Azure Unused IPs Better Filtering

#### Description

> ### Description
> 
> This adds more filtering options to the policy:
> 
> - Added IP allocation type (Dynamic or Static) to incident output
> - Added ability to filter results by allocation type via parameter
> - Added ability to filter results by minimum savings via parameter
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65de3a061b78750001a4d094
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2024-02-27 19:43:32 UTC
- **Merged At**: 2024-02-29 10:28:28 UTC
- **Modified Policies**: azure_unused_ip_addresses.pt, azure_unused_ip_addresses_meta_parent.pt

### PR [#1879](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/8071749355)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-27 21:44:42 UTC
- **Merged At**: 2024-02-27 21:48:08 UTC
- **Modified Policies**: azure_rightsize_netapp_files_meta_parent.pt

### PR [#1870](): FOPTS-3238 Update `short_description` of the policy Azure Rightsize NetApp Files

#### Description

> ### Description
> 
> The short description of the policy Azure Rightsize NetApp Files was in sync with the Flexera documentation, this change updated the `short_description` of the policy so both descriptions match.
> 
> ### Issues Resolved
> 
> - https://flexera.atlassian.net/browse/FOPTS-3238
> 
> ### Link to Example Applied Policy
> 
> This did not updated any part of the code, only the short description, despite this I still applied the policy just in case:
> https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65ddfce1f73314000135e2c4
> 
> It uploaded correctly, that means the code is fine. I attach this GIF if you are not able to log in Flexera test:
> ![azure-rightsize-netapp-files-v1 1](https://github.com/flexera-public/policy_templates/assets/54189123/729082fd-4ca2-4741-b026-c3b89754d3e8)
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL, small fixes, documentation
- **Created At**: 2024-02-27 15:21:13 UTC
- **Merged At**: 2024-02-27 21:44:12 UTC
- **Modified Policies**: azure_rightsize_netapp_files.pt

### PR [#1874](): POL-1070 Deprecate AWS Inefficient Instance Utilization using CloudWatch

#### Description

> ### Description
> 
> The AWS Inefficient Instance Utilization using CloudWatch policy does basically the same thing as the existing Rightsize EC2 policy, so it is being deprecated.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-27 20:40:44 UTC
- **Merged At**: 2024-02-27 21:41:58 UTC
- **Modified Policies**: aws_instance_cloudwatch_utilization.pt

### PR [#1833](): POL-1062 Deprecate CMP Policies

#### Description

> ### Description
> 
> This pull request deprecates the 4 remaining CMP policies that have not yet been deprecated.
> 
> No testing was done since no changes were made to anything that would impact policy execution.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-16 15:11:22 UTC
- **Merged At**: 2024-02-27 16:43:33 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1846](): POL-1035 Google Policy Regex Support

#### Description

> ### Description
> 
> This adds support for regex tag filtering to several Google policies.
> 
> ### Link to Example Applied Policies
> 
> Google Long Stopped VM Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6523d72834a00010ab2f6
> Google Idle Cloud SQL Instance Recommender: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6527660a6a60001794f0d
> Google Idle IP Address Recommender: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6529972834a00010ab2f7
> Google Idle Persistent Disk Recommender: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d652d360a6a60001794f14
> Google Old Snapshots: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6530372834a00010ab2fb
> Google Rightsize VM Recommender: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6533f72834a00010ab2fe
> Google Schedule Instance: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6536e72834a00010ab302
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-21 19:34:43 UTC
- **Merged At**: 2024-02-27 13:35:39 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1845](): POL-1025 Azure Policy Regex Support

#### Description

> ### Description
> 
> This adds support for regex tag filtering to several Azure policies. Additionally, it includes revamps of the two AKS Node Pools policies to help facilitate this update.
> 
> ### Link to Example Applied Policies
> 
> Azure AHUB Utilization with Manual Entry: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6297272834a00010ab067
> Azure Long Stopped Compute Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d62a1172834a00010ab073
> Azure Hybrid Use Benefit for Windows Server: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d62ab272834a00010ab084
> Azure Hybrid Use Benefit for Linux Server: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d62ac272834a00010ab087
> Azure Old Snapshots: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d62b1760a6a60001794c69
> Azure Rightsize Compute Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d62b5260a6a60001794c71
> Azure Rightsize Managed Disks: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d62bc272834a00010ab094
> Azure Rightsize SQL Databases: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d62bf360a6a60001794c84
> Azure Schedule Instance: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6444e60a6a60001794e80
> Azure Superseded Compute Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6446f60a6a60001794e83
> Azure Unused IP Addresses: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6448e72834a00010ab260
> Azure Unused Volumes: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d644b960a6a60001794e8a
> Azure Long Running Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6456372834a00010ab27f
> AKS Node Pools Without Autoscaling: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6463260a6a60001794ea6
> AKS Node Pools Without Zero Autoscaling: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d6466d72834a00010ab299
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-21 15:00:11 UTC
- **Merged At**: 2024-02-27 13:04:09 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1864](): POL-1068 Cloud Cost Anomaly Alerts Link Fix

#### Description

> ### Description
> 
> This fixes a bug where the link would render incorrectly if spaces were present. Spaces are now appropriately replaced with %20 in the link.
> 
> ### Link to Example Applied Policy
> 
> The change was tested in a customized version of this same policy. It also works in node:
> 
> ❯ node
> > filter = {'id': 'some stuff with spaces', 'value': 'even more spaces omg'}
> { id: 'some stuff with spaces', value: 'even more spaces omg' }
> > value = "&filterBy=anomaly." + filter['id'] + "." + filter['value']
> '&filterBy=anomaly.some stuff with spaces.even more spaces omg'
> > while (value.split(' ')[1] != undefined) { value = value.replace(' ', '%20') }
> '&filterBy=anomaly.some%20stuff%20with%20spaces.even%20more%20spaces%20omg'
> >
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-26 20:12:15 UTC
- **Merged At**: 2024-02-26 20:25:42 UTC
- **Modified Policies**: cloud_cost_anomaly_alerts.pt

### PR [#1861](): POL-1065 Cloud Cost Anomaly Alerts Revamp

#### Description

> ### Description
> 
> This is a revamp of the Cloud Cost Anomaly Alerts policy. From the CHANGELOG:
> 
> - Link to Flexera One Cloud Cost Anomalies page now includes filters
> - Incident for invalid dimensions now includes list of valid dimensions
> - Improved text formatting and presentation of incidents
> - Incident now includes currency
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65dcac3a8a230500018b4adb
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-26 15:52:25 UTC
- **Merged At**: 2024-02-26 17:09:54 UTC
- **Modified Policies**: cloud_cost_anomaly_alerts.pt

### PR [#1842](): POL-1018 AWS Policy Regex Support

#### Description

> ### Description
> 
> This adds support for regex tag filtering to several AWS policies.
> 
> ### Link to Example Applied Policies
> 
> - AWS Rightsize EBS Volumes: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d5090a60a6a6000179488e
> - AWS Rightsize EC2 Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d5093e72834a00010aaca1
> - AWS Rightsize RDS Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d50c5160a6a60001794898
> - AWS Superseded EC2 Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d50f0672834a00010aacb2
> - AWS Unused Classic Load Balancers: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d50f7560a6a6000179489a
> - AWS Unused IP Addresses: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d50ff260a6a6000179489b
> - AWS Unused Volumes: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d5127072834a00010aacbb
> - AWS Long Running Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d51e1c72834a00010aaccf
> - AWS Long Stopped EC2 Instances: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d51fad72834a00010aacd0
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-20 19:26:24 UTC
- **Merged At**: 2024-02-26 14:44:21 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1707](): FOPTS-2025 Deployment of Rightsize Azure NetApp Files Policy

#### Description

> ### Description
> 
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
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: New Policy
- **Created At**: 2023-12-21 17:53:13 UTC
- **Merged At**: 2024-02-23 17:42:29 UTC
- **Modified Policies**: azure_rightsize_netapp_files.pt, azure_rightsize_netapp_files_meta_parent.pt

### PR [#1841](): POL-1017 AWS Old Snapshots Regex Support

#### Description

> ### Description
> 
> This adds regex support to the AWS Old Snapshots policy. This is a breaking change, hence the major version number change, but anyone not currently using the tag filtering functionality should not be impacted by this change.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65d4d67160a6a60001794820
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-20 16:45:35 UTC
- **Merged At**: 2024-02-23 13:18:40 UTC
- **Modified Policies**: aws_delete_old_snapshots.pt, aws_delete_old_snapshots_meta_parent.pt

### PR [#1840](): POL-996 AWS Burstable EC2 Instances Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65cfcbb560a6a6000179410c
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-16 21:07:16 UTC
- **Merged At**: 2024-02-23 13:18:28 UTC
- **Modified Policies**: aws_burstable_ec2_instances.pt, aws_burstable_ec2_instances_meta_parent.pt, aws_burstable_instance_cloudwatch_credit_utilization.pt

### PR [#1848](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/8010285881)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-22 20:02:00 UTC
- **Merged At**: 2024-02-22 20:02:39 UTC
- **Modified Policies**: aws_volumes_rightsizing_meta_parent.pt, aws_superseded_instances_meta_parent.pt, aws_unused_ip_addresses_meta_parent.pt, azure_hybrid_use_benefit_meta_parent.pt, azure_superseded_instances_meta_parent.pt, google_sql_idle_instance_recommendations_meta_parent.pt, google_committed_use_discount_recommendations_meta_parent.pt, google_idle_ip_address_recommendations_meta_parent.pt, google_idle_persistent_disk_recommendations_meta_parent.pt, google_rightsize_vm_recommendations_meta_parent.pt

### PR [#1847](): Currency Conversion Fixes

#### Description

> ### Description
> 
> An error was found in the currency conversion implementation in some policies. This is the fix for it.
> 
> ### Link to Example Applied Policy
> 
> Code was tested in AHUB policy and is identical in the other modified policies.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-22 19:28:32 UTC
- **Merged At**: 2024-02-22 20:01:27 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1828](): POL-1054 New Policy: Azure Bring-Your-Own-License (BYOL) Report

#### Description

> ### Description
> 
> This new policy analyzes the stored billing data for Microsoft Azure from 2 days ago to a user-specified number of days back and reports on the number of VMs using the Bring-Your-Own-License (BYOL) feature each day. The report includes daily numbers and percentages as well as the peak total BYOL usage and peak percentage BYOL usage and is emailed to a user-specified list of email addresses.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65ce1249f69cf3000129e410
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, New Policy
- **Created At**: 2024-02-15 13:33:54 UTC
- **Merged At**: 2024-02-21 13:06:33 UTC
- **Modified Policies**: azure_byol_report.pt

### PR [#1837](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7934272061)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-16 17:46:32 UTC
- **Merged At**: 2024-02-16 18:04:53 UTC
- **Modified Policies**: azure_rightsize_managed_disks_meta_parent.pt

### PR [#1829](): FOPTS-3031 Update parameters of Azure Rightsize Managed Disk policy

#### Description

> ### Description
> 
> - Updated the descriptions and labels of the IOPS and throughput parameters in the README and policy template files.
> - Updated the short description of the policy.
> - Changed the functionality of `param_min_savings`: Before this version, the `param_min_savings` parameter was used to consider the total savings (the sum of all the savings per resource) and not the savings per resource to decide whether to recommend or not. In this new version, this parameter is used to recommend or not based on the savings of each resource, just as other policies do.
> 
> ### Issues Resolved
> 
> - https://flexera.atlassian.net/browse/FOPTS-3170
> 
> ### Link to Example Applied Policy
> 
> You can find the link to the applied policy in the following comment at Jira:
> https://flexera.atlassian.net/browse/FOPTS-3170?focusedCommentId=2248041
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW, READY FOR APPROVAL, small fixes
- **Created At**: 2024-02-15 19:01:58 UTC
- **Merged At**: 2024-02-16 17:46:03 UTC
- **Modified Policies**: azure_rightsize_managed_disks.pt

### PR [#1830](): POL-1061 New Policy: Flexera Automation Outdated Applied Policies

#### Description

> ### Description
> 
> This new policy checks all applied policies against the same policy in the catalog to determine if the applied policy is using an outdated version of the catalog policy. An email is sent and an incident is raised with all outdated policies. Optionally, outdated policies can automatically be updated.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65ce7e2672834a00010aa3e7
> 
> Note: The above version has been tweaked from the version in this PR to include policies that are up to date in the results. This is so the policy will actually report results in the incident and so the policy's actions could be tested.
> 
> This is because it's not possible to apply a policy from the catalog and have it be out of date without waiting for that policy to be updated in the catalog after applying it.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-15 21:17:39 UTC
- **Merged At**: 2024-02-16 13:18:04 UTC
- **Modified Policies**: outdated_applied_policies.pt

### PR [#1817](): POL-1004 Azure Schedule Instance Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65ca36f0b7ceed00016c5552
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-12 15:30:25 UTC
- **Merged At**: 2024-02-13 16:19:13 UTC
- **Modified Policies**: azure_schedule_instance.pt, azure_schedule_instance_meta_parent.pt

### PR [#1808](): POL-998 AWS Schedule Instance Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65c62f838e86c40001ae4df9
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-09 17:00:32 UTC
- **Merged At**: 2024-02-13 13:44:18 UTC
- **Modified Policies**: aws_schedule_instance.pt, aws_schedule_instance_meta_parent.pt

### PR [#1819](): POL-1005 Google Schedule Instance Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65ca7f458e86c40001ae5b84
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-12 20:37:54 UTC
- **Merged At**: 2024-02-13 13:09:17 UTC
- **Modified Policies**: google_schedule_instance.pt, google_schedule_instance_meta_parent.pt

### PR [#1805](): POL-1056 New Policy: Azure Missing Subscriptions

#### Description

> ### Description
> 
> This is a net new policy for finding missing subscriptions. For now, this policy is unpublished since the primary user is internal rather than clients directly.
> 
> From the README:
> 
> This policy checks the stored Flexera CCO billing data for Azure from 3 days ago to obtain a list of Azure Subscriptions that we have billing data for and compares that to the list of Azure Subscriptions returned by the Azure Resource Manager API. An incident is raised and email sent containing any subscriptions present in Flexera CCO but not returned by the Azure Resource Manager API, as well as subscriptions returned by the Azure Resource Manager API but not present in Flexera CCO. The user can select which of those two reports they'd like to produce.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/incidents/projects/116186?incidentId=65c4faa1a14f000001019b36
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65c4fae2b7ceed00016c4175
> 
> (Top one shows subs missing in the Azure API, bottom one shows subs missing in CCO)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-07 20:03:23 UTC
- **Merged At**: 2024-02-08 16:13:44 UTC
- **Modified Policies**: azure_missing_subscriptions.pt

### PR [#1804](): POL-1007 Azure Policies - Add ignore 400 error status

#### Description

> ### Description
> 
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
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-07 16:59:11 UTC
- **Merged At**: 2024-02-08 15:32:23 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1800](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7816819227)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-07 15:04:32 UTC
- **Merged At**: 2024-02-07 15:16:56 UTC
- **Modified Policies**: azure_blob_storage_optimization_meta_parent.pt

### PR [#1799](): POL-1055 Correct Path for Azure Blob Storage Optimization Policy

#### Description

> ### Description
> 
> The path for this policy is incorrect and, as a result, does not match the link in the policy's description. The path to this policy should be blob_storage_optimization, not object_storage_optimization, to keep it in line with the name of the policy itself as well as Azure’s own terminology.
> 
> ### Issues Resolved
> 
> Path to this policy is now correct and matches the link within the policy itself as well as the policy name.
> 
> ### Link to Example Applied Policy
> 
> N/A. No changes are made to the policy itself.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [ ] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-07 14:49:44 UTC
- **Merged At**: 2024-02-07 15:04:03 UTC
- **Modified Policies**: azure_blob_storage_optimization.pt, azure_blob_storage_optimization_meta_parent.pt

### PR [#1786](): POL-1053 Custom Dimension Names in RBD Policies

#### Description

> ### Description
> 
> This adds the ability for the user to specify the names of the created dimensions via a parameter in the unpublished RBD creation policies. The new parameter is a list, and if this parameter is left blank, the existing functionality will occur instead.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65bcf831874bcc00017b8709
> 
> (Note: The change is small and identical across all of the affected policies)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-02 14:26:16 UTC
- **Merged At**: 2024-02-05 21:09:40 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1793](): POL-999 Azure Blob Storage Optimization Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> Note: Due to the nature of the credential and what this policy tests for, it is difficult to test it in our test environments. I have confirmed it works as expected in a client environment.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-05 14:12:34 UTC
- **Merged At**: 2024-02-05 21:09:22 UTC
- **Modified Policies**: azure_object_storage_optimization.pt, azure_object_storage_optimization_meta_parent.pt

### PR [#1750](): POL-997 AWS Object Storage Optimization Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65a93b07246c29000155a797
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-18 15:01:55 UTC
- **Merged At**: 2024-02-05 18:54:59 UTC
- **Modified Policies**: aws_object_storage_optimization.pt, aws_object_storage_optimization_meta_parent.pt

### PR [#1747](): POL-1003 Azure Long Running Instances Action Revamp

#### Description

> ### Description
> 
> This revamps the policy actions to properly log errors in EU/APAC and also normalizes action names. The CWF code was lifted directly from other, already-updated Azure policies. General policy functionality is unchanged.
> 
> From the CHANGELOG:
> 
> - Added option to either gracefully or forcefully power off instances
> - Renamed policy actions to conform with Azure's own terminology and documentation
> - Policy action error logging modernized and now works as expected in EU/APAC
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65a6927767c7960001288333
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-16 14:30:43 UTC
- **Merged At**: 2024-02-05 13:06:34 UTC
- **Modified Policies**: azure_long_running_instances.pt, azure_long_running_instances_meta_parent.pt

### PR [#1789](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7782044712)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-02 22:32:03 UTC
- **Merged At**: 2024-02-05 09:10:27 UTC
- **Modified Policies**: azure_rightsize_managed_disks_meta_parent.pt

### PR [#1677](): FOPTS-2607 Deployment of rightsize azure managed disks policy

#### Description

> ### Description
> 
> Deploy first version of Rightsize Azure Managed Disks policy.
> 
> ### Issues Resolved
> 
> - https://flexera.atlassian.net/browse/FOPTS-2607
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, New Policy
- **Created At**: 2023-12-07 18:14:05 UTC
- **Merged At**: 2024-02-02 22:31:32 UTC
- **Modified Policies**: azure_rightsize_managed_disks.pt, azure_rightsize_managed_disks_meta_parent.pt

### PR [#1746](): POL-1000 AWS Long Running Instances Action Revamp

#### Description

> ### Description
> 
> This revamps the policy actions to properly log errors in EU/APAC. The CWF code was lifted directly from other, already-updated AWS policies. General policy functionality is unchanged.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65a68d0167c796000128832d
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-16 14:05:58 UTC
- **Merged At**: 2024-02-02 15:11:07 UTC
- **Modified Policies**: long_running_instances.pt, long_running_instances_meta_parent.pt

### PR [#1737](): POL-994 Azure Disallowed Regions Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65a148b5246c29000155904f
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-12 14:19:10 UTC
- **Merged At**: 2024-02-02 13:11:31 UTC
- **Modified Policies**: azure_disallowed_regions.pt, azure_disallowed_regions_meta_parent.pt

### PR [#1743](): POL-995 Google Long Stopped Instances Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65a6860567c7960001288302
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-16 13:37:26 UTC
- **Merged At**: 2024-02-02 13:11:19 UTC
- **Modified Policies**: google_long_stopped_instances.pt, google_long_stopped_instances_meta_parent.pt

### PR [#1751](): POL-1042 AWS Untagged Resources Revamp

#### Description

> ### Description
> 
> This is a complete revamp and overhaul of the AWS Untagged Resources policy. Both the policy code and actions have been revamped. From the CHANGELOG:
> 
> - Added ability to filter resources by tag key, tag key==value, or using regex
> - Added ability to use all filters as an allow list or a deny list
> - Added additional context to incident description
> - Streamlined code for better readability and faster execution
> - Meta policy support added
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65aae340246c29000155c2c8
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-19 21:19:56 UTC
- **Merged At**: 2024-02-01 11:34:07 UTC
- **Modified Policies**: aws_untagged_resources.pt, aws_untagged_resources_meta_parent.pt

### PR [#1748](): POL-1047 Azure Reserved Instances Recommendations Scaling Fixes

#### Description

> ### Description
> 
> We were receiving reports of 429 rate limiting errors from the Azure APIs when attempting to use this policy. The following has been done to try to alleviate this issue:
> - A forced 5 second delay between requests to the Microsoft.Consumption/reservationRecommendations API endpoint has been added.
> - Information has been added to the README recommending that the policy be applied once for each resource type for large cloud estates.
> - Meta policy support has been added.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65a822cf0620ac00011a9496
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-17 19:08:11 UTC
- **Merged At**: 2024-01-17 19:46:17 UTC
- **Modified Policies**: azure_reserved_instance_recommendations.pt, azure_reserved_instance_recommendations_meta_parent.pt

### PR [#1735](): POL-993 Azure Long Stopped Instances Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65a05adf246c290001558dd6
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-11 21:21:32 UTC
- **Merged At**: 2024-01-16 13:37:44 UTC
- **Modified Policies**: long_stopped_instances_azure.pt, long_stopped_instances_azure_meta_parent.pt

### PR [#1730](): POL-992 AWS Long Stopped Instances Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=659d4a5a7cc18300018b7730
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-10 14:55:34 UTC
- **Merged At**: 2024-01-16 13:24:26 UTC
- **Modified Policies**: aws_long_stopped_instances.pt, aws_long_stopped_instances_meta_parent.pt

### PR [#1738](): POL-1045 Azure Reserved Instances Recommendations: Term Parameter Fix

#### Description

> ### Description
> 
> This fixes an issue where the policy was returning all reservation recommendations instead of either 1 year or 3 year based on the parameter.
> 
> ### Link to Example Applied Policy
> 
> (Tested in client environment successfully. Not able to easily test in a test environment due to lack of recommendations in those environments)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-12 18:05:57 UTC
- **Merged At**: 2024-01-16 10:25:36 UTC
- **Modified Policies**: azure_reserved_instance_recommendations.pt

### PR [#1736](): POL-1043 Update Meta Policies

#### Description

> ### Description
> 
> The script for generating meta policies has been updated. This is just a PR to regenerate some of the meta policies using this script.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-12 13:17:54 UTC
- **Merged At**: 2024-01-12 14:28:44 UTC
- **Modified Policies**: azure_instances_not_running_flexnet_inventory_agent_meta_parent.pt, aws_upgrade_to_gp3_volume_meta_parent.pt, aws_object_storage_optimization_meta_parent.pt, lambda_functions_with_high_error_rate_meta_parent.pt, azure_certificates_meta_parent.pt, aws_unencrypted_volumes_meta_parent.pt, aws_publicly_accessible_rds_instances_meta_parent.pt

### PR [#1732](): POL-1043 Meta Policy Substring Support

#### Description

> ### Description
> 
> This adds support for substrings when filtering dimensions in the parent policies. 
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65a001ca0620ac00011a9415
> 
> (dimension filter is vendor_account_name=~Datalake and if you look at the policies created incident, the only child is for an account whose name contains Datalake)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [ ] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-11 15:01:55 UTC
- **Merged At**: 2024-01-12 13:12:37 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1731](): POL-1015 Meta Policy Escalation Name Fixes

#### Description

> ### Description
> 
> This changes the name of escalation blocks so that the meta policy generator can properly generate meta policies for these policies. I also removed some strange whitespace characters that were in one of the policies for some reason and replaced them with standard spaces.
> 
> Meta policies themselves are unchanged since separate work is being done to update the meta policy templates for new functionality, which will in turn automatically update the meta policies.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-10 16:17:09 UTC
- **Merged At**: 2024-01-11 19:13:28 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1718](): POL-991 AWS Disallowed Regions Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=659c42e39f8a200001eceef0
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-02 21:50:13 UTC
- **Merged At**: 2024-01-10 14:40:43 UTC
- **Modified Policies**: aws_disallowed_regions.pt, aws_disallowed_regions_meta_parent.pt

### PR [#1719](): FOPTS-2229 Added a way to url decode the skiptoken

#### Description

> ### Description
> 
> Replaced the jq function used from rt
> 
> ### Issues Resolved
> 
> [FOPTS-2229](https://flexera.atlassian.net/browse/FOPTS-2229)
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/28576/automation/applied-policies/projects/126887?policyId=659c762c9f8a200001ecef8a
> 
> If you don't have access to testing org 28576, you can watch the following GIF that shows the fixed error related to pagination:
> 
> ![itam_report_fixed_demo](https://github.com/flexera-public/policy_templates/assets/54189123/3381ea20-a6e2-484a-b326-3b68a4a3c2ee)
> 
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-03 18:59:30 UTC
- **Merged At**: 2024-01-09 13:36:56 UTC
- **Modified Policies**: schedule-itam-report.pt

### PR [#1727](): POL-958 Add 'Minimum Age' to Azure Rightsize SQL

#### Description

> ### Description
> 
> Added optional `Minimum Age (Days)` parameter to filter results by age. This is for users that want to avoid reporting on freshly created databases that, as a result of their newness, have not had any connections and would therefore be seen as "unused" by the policy.
> 
> This is not a breaking change since the default value of this parameter is 0 and this functions just like the policy did without the parameter.
> 
> From the README:
> 
> - *Minimum Age (Days)* - The minimum age, in days, since a SQL database was created to produce recommendations for it. Set to 0 to ignore age entirely.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=659c1da07cc18300018b73f7
> 
> (Note: The above does not produce an incident because we don't have any old SQL servers in our test account. If you review the log, you'll see that `ds_azure_sql_databases` returns two system databases, and the filter correctly filters out one of them based on age for `ds_azure_sql_databases_age_filtered`)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-08 16:11:09 UTC
- **Merged At**: 2024-01-08 18:05:59 UTC
- **Modified Policies**: azure_rightsize_sql_instances.pt, azure_rightsize_sql_instances_meta_parent.pt

### PR [#1725](): feat: add cluster id filtering for databricks PT

#### Description

> ### Description
> 
> - Add `param_databricks_cluster_list` for filtering to a specific Databricks Cluster within a Databricks Workspace
> - Add `p90`,`p95`,`p99` Threshold Statistic choices
> - Fixed subscription ID and Name output in recommendation
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6596fc79d1dc74000182cef0
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2024-01-04 18:45:07 UTC
- **Merged At**: 2024-01-08 13:17:33 UTC
- **Modified Policies**: azure_databricks_rightsize_compute.pt, azure_databricks_rightsize_compute_meta_parent.pt, azure_databricks_rightsize_compute_meta_parent_cluster.pt

### PR [#1716](): POL-989 Azure Old Snapshots Policy Action Revamp

#### Description

> ### Description
> 
> This updates the policy actions to follow current conventions and have better error logging outside of NAM. Functionality is unchanged.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=6594150a9f8a200001eccfdb
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-02 13:57:18 UTC
- **Merged At**: 2024-01-04 13:10:00 UTC
- **Modified Policies**: azure_delete_old_snapshots.pt, azure_delete_old_snapshots_meta_parent.pt

### PR [#1717](): POL-990 Azure Rightsize SQL Policy Action Revamp

#### Description

> ### Description
> 
> This updates the policy actions to follow current conventions and have better error logging outside of NAM. Functionality is unchanged.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65941b569f8a200001eccfe1
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-02 14:28:07 UTC
- **Merged At**: 2024-01-04 13:09:53 UTC
- **Modified Policies**: azure_rightsize_sql_instances.pt, azure_rightsize_sql_instances_meta_parent.pt

### PR [#1720](): POL-988 AWS Unused Volumes Policy Action Revamp

#### Description

> ### Description
> 
> This updates the policy actions to follow current conventions and have better error logging outside of NAM. Functionality is unchanged.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=6595c5b97cc18300018b587e
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-03 20:47:19 UTC
- **Merged At**: 2024-01-04 13:09:41 UTC
- **Modified Policies**: aws_delete_unused_volumes.pt, aws_delete_unused_volumes_meta_parent.pt

### PR [#1678](): POL-981 Azure Untagged Resources Revamp / Untagged Virtual Machines

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=658c560e9f8a200001ecbc27
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=658c559e7cc18300018b402d
> 
> Note: Azure Untagged Resources policy has been slightly modified from this PR for testing in order to use the `/data/azure/resource_types.json` file in this branch since it won't exist in the master branch until after this PR is merged.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-08 14:12:27 UTC
- **Merged At**: 2024-01-03 20:48:02 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1713](): POL-986 AWS Old Snapshots Policy Action Revamp

#### Description

> ### Description
> 
> This non-breaking change updates the policy actions for the AWS Old Snapshots policy. Functionality is identical, but now the error logging is modernized and should work as expected in EU and APAC.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=658efa8f7cc18300018b4687
> (Actions have been tested. The "failed" action for the above incident is because the snapshot was created via automation and thus does not qualify to be deleted, not because of any issue with the API call made by CWF)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-29 18:06:22 UTC
- **Merged At**: 2024-01-02 13:09:45 UTC
- **Modified Policies**: aws_delete_old_snapshots.pt, aws_delete_old_snapshots_meta_parent.pt

### PR [#1714](): POL-987 AWS Unused IP Policy Action Revamp

#### Description

> ### Description
> 
> This non-breaking change updates the policy actions for the AWS Unused IP policy. Functionality is identical, but now the error logging is modernized and should work as expected in EU and APAC.
> 
> The verbiage for a parameter was also updated to be more clear and the parameter in question was added to the README
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=658f1c657cc18300018b469f
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-29 19:27:30 UTC
- **Merged At**: 2024-01-02 13:09:34 UTC
- **Modified Policies**: aws_unused_ip_addresses.pt, aws_unused_ip_addresses_meta_parent.pt

### PR [#1704](): POL-1010 Scheduled Report Policy Revamp

#### Description

> ### Description
> 
> This is a revamp of the Scheduled Report policy that streamlines it and extends functionality. From the CHANGELOG:
> 
> - Added ability to specify custom dimensions for the graph in the report
> - Added ability to filter costs in report by any user-specified dimension
> - Improved incident output for readability and removed references to Optima
> - Incident table now shows the raw data used to create the graph in the report
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6581d9c0530963000172984c
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-19 18:00:18 UTC
- **Merged At**: 2023-12-29 14:11:13 UTC
- **Modified Policies**: scheduled_report.pt

### PR [#1708](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7338799914)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-12-27 13:31:30 UTC
- **Merged At**: 2023-12-27 13:39:41 UTC
- **Modified Policies**: azure_hybrid_use_benefit_meta_parent.pt

### PR [#1706](): POL-982 Hybrid Use Benefit Policy - currency separator symbol shown as undefined

#### Description

> ### Description
> 
> n the incident of Hybrid Use Benefit Policy, currency separator is shown as undefined:
> 
> ### Issues Resolved
> 
> [POL-982](https://flexera.atlassian.net/browse/POL-982)
> 
> ### Link to Example Applied Policy
> 
> [Applied policy](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=658230b65ec8620001b97922)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-12-20 00:11:48 UTC
- **Merged At**: 2023-12-27 13:30:57 UTC
- **Modified Policies**: azure_hybrid_use_benefit.pt

### PR [#1700](): FOPTS-2702 Enabling hyperlinks in Turb policies for incidents.

#### Description

> ### Description
> 
> Enabling hyperlinks in Turbonomics policies for incidents.
> 
> ### Issues Resolved
> 
> [FOPTS-2702](https://flexera.atlassian.net/browse/FOPTS-2702)
> ### Link to Example Applied Policy
> 
> [E.g. Applied Policy](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65806cba5f57b900018a9282)
> 
> - Rightsize Databases
>       - aws
>       - azure
>       - gcp
> 
> - Allocate Virtual Machines
>       - NA
> 
> - Buy RI
>        - aws
>        - azure
> 
> - Delete Virtual Volumes
>         - aws
>         - azure
>         - gcp
> 
> - Rightsize Virtual Volumes
>          - aws
>          - azure
>          - gcp NA
> 
> - Scale Virtual Machines
>           - aws
>           - azure
>           - gcp
> 
> Changelog and version updated on each policy.
>  
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-18 16:37:25 UTC
- **Merged At**: 2023-12-19 19:46:41 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1697](): POL-1008 Google Idle Persistent Disk Recommender: Add 'Days Unattached' Parameter

#### Description

> ### Description
> 
> This adds the ability to filter the results by how long a disk has been unattached for. GCP produces recommendations based on whether a disk has been detached for 15 days, and this allows the user to filter those results further, going back to 90 days, by using GCP's native event logging.
> 
> This is a non-breaking change; the default value for the relevant parameter is 15 days, equivalent to what GCP already checks for, and if the user has not granted their GCP credential the permissions to access the above logs, then the policy will simply report all of the recommendations as it did before rather than fail.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=657ca1bc7cc18300018b0b66
> (Note: The above has no results because its non-trivial to make GCP produce recommendations ad hoc for testing. That said, this has also been tested in a client environment with permission and it should work as expected)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-15 19:07:37 UTC
- **Merged At**: 2023-12-19 15:26:01 UTC
- **Modified Policies**: google_idle_persistent_disk_recommendations.pt, google_idle_persistent_disk_recommendations_meta_parent.pt

### PR [#1701](): POL-1012 AWS Rightsize RDS Dash Fix

#### Description

> ### Description
> 
> This fixes an issue where the policy was not correctly identifying unused instances if they had dashes in the name. The policy was incorrectly using the instance id, rather than the instance name, to find the instance in the Cloudwatch data.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6581a75fd1dc74000182cdbb
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-19 14:30:29 UTC
- **Merged At**: 2023-12-19 14:42:36 UTC
- **Modified Policies**: aws_rightsize_rds_instances.pt, aws_rightsize_rds_instances_meta_parent.pt

### PR [#1695](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7225989438)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-12-15 19:00:52 UTC
- **Merged At**: 2023-12-15 19:11:13 UTC
- **Modified Policies**: aws_schedule_instance_meta_parent.pt

### PR [#1693](): feat: improved logging error handling schedule instance PTs

#### Description

> ### Description
> 
> Improved logging and error handling in the Scheduled Instance Policy Templates (AWS, Google)
> 
> ### Link to Example Applied Policy
> 
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-15 18:56:47 UTC
- **Merged At**: 2023-12-15 19:00:19 UTC
- **Modified Policies**: aws_schedule_instance.pt, google_schedule_instance.pt

### PR [#1683](): POL-566 Policy Update Notification Revamp

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65774d7555d35d0001a932e1
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-11 17:59:33 UTC
- **Merged At**: 2023-12-13 18:39:14 UTC
- **Modified Policies**: policy_update_notification.pt

### PR [#1666](): POL-971 Azure Reserved Instances Utilization - update to use Modern Azure APIs

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
> https://app.flexera.com/orgs/33693/automation/applied-policies/projects/135064?policyId=6570714a55d35d0001a9053c
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [ ] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-05 15:48:09 UTC
- **Merged At**: 2023-12-12 15:15:08 UTC
- **Modified Policies**: azure_reserved_instance_utilization.pt

### PR [#1681](): POL-757 Azure Rightsize Compute Fixes/Improvements

#### Description

> ### Description
> 
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
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65771cbf666365000101a729
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-11 14:53:29 UTC
- **Merged At**: 2023-12-11 18:59:28 UTC
- **Modified Policies**: azure_compute_rightsizing.pt, azure_compute_rightsizing_meta_parent.pt

### PR [#1667](): POL-836 AWS Unused Classic Load Balancers Revamp

#### Description

> ### Description
> 
> This is a revamp of the AWS Unused Classic Load Balancers that includes the usual updates and improvements. From the CHANGELOG:
> 
> - Assessment algorithm now more consistently identifies unused Classic Load Balancers
> - Added parameter to exclude recently created Classic Load Balancers
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65708b4299745e00015883c3
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-06 15:19:45 UTC
- **Merged At**: 2023-12-07 13:11:07 UTC
- **Modified Policies**: aws_delete_unused_clb.pt, aws_unused_clbs.pt, aws_unused_clbs_meta_parent.pt

### PR [#1669](): POL-945 Currency Conversion Backfill Support

#### Description

> ### Description
> 
> This update adds the ability to backfill previous months when applying the policy. From the README:
> 
> - *Backfill Adjustments* - Whether to add/modify currency conversion to just the current month or to backfill previous months.
> 
> - *Backfill Start Date* - The month and year in YYYY-MM format to backfill adjustments to. Only applicable if `Backfill Previous Months` is selected for the `Backfill Adjustments` parameter.
>  
> - *Backfill Exchange Rates* - Whether or not to use the current exchange rate, or the exchange rate at the time, when applying currency conversion to previous months. Only applicable if `Backfill Previous Months` is selected for the `Backfill Adjustments` parameter.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6570d8ff99745e00015883c7
> 
> (Results can be assessed by viewing the adjustments on this account.)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-06 20:54:33 UTC
- **Merged At**: 2023-12-07 13:10:33 UTC
- **Modified Policies**: currency_conversion.pt

### PR [#1663](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7065172364)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-12-01 19:57:12 UTC
- **Merged At**: 2023-12-01 21:08:09 UTC
- **Modified Policies**: azure_databricks_rightsize_compute_meta_parent.pt, aws_public_buckets_meta_parent.pt

### PR [#1583](): POL-853 - Azure Databricks Rightsize Compute Instances

#### Description

> ### Description
> 
> This policy checks all the instances associated with Azure Databricks workspaces in Azure Subscriptions for the average or maximum CPU and/or memory usage over a user-specified number of days. If the usage is less than the user provided Idle Instance CPU and/or memory percentage threshold then the Virtual Machine is recommended for deletion. 
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/POL-853
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=653fe3d8e947000001d93586
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, New Policy
- **Created At**: 2023-10-30 21:49:45 UTC
- **Merged At**: 2023-12-01 21:04:24 UTC
- **Modified Policies**: azure_databricks_rightsize_compute.pt, azure_databricks_rightsize_compute_meta_parent.pt

### PR [#1655](): POL-889 AWS Open S3 Buckets Revamp / Meta

#### Description

> ### Description
> 
> This is a revamp of the AWS Open Buckets policy to clean up the code/functionality and to enable meta policy support.
> 
> From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by region
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if bucket owner has changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6568f20399745e0001588354
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-30 20:36:24 UTC
- **Merged At**: 2023-12-01 19:56:40 UTC
- **Modified Policies**: aws_public_buckets.pt, aws_public_buckets_meta_parent.pt

### PR [#1625](): POL-745 SaaS Manager - Deactivated Users for Integrated Applications Revamp

#### Description

> ### Description
> 
> This is part of a broader initiative to update our SaaS Manager FSM policies to use up to date APIs. The policy itself has also been revamped along similar lines to other policies. The name has also been changed to better reflect the policy's functionality.
> 
> From the CHANGELOG:
> 
> - Policy renamed to `SaaS Manager - Deactivated Users for Integrated Applications` to better reflect its functionality
> - Added `Inactive Days Threshold` to allow user to filter out recently deactivated users
> - Added `Applications` parameter to allow user to filter results by application
> - Updated policy to use public SaaS Manager API
> - Added support for APAC API endpoint
> - Policy now uses and requires a general Flexera One credential
> - Incident summary now includes applied policy name
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6564f1db99745e0001588315
> 
> Note: Applied policy will not contain an incident. This is because our test environment only has one integrated application and it has no users. That said, the proper functionality of most of the policy can be verified via the logs, and the remaining functionality is identical to the existing "SaaS Manager - Deactivated Users" policy.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 14:18:57 UTC
- **Merged At**: 2023-12-01 16:01:48 UTC
- **Modified Policies**: deactivated_users_for_integrated_apps.pt, inactive_users_for_integrated_apps.pt

### PR [#1656](): POL-977 AWS Rightsize RDS: Change Parameter Default Value

#### Description

> ### Description
> 
> This just changes the default value of the `Underutilized Instance CPU Threshold (%)` parameter to 40% to match other policies and ensure that our recommendations won't cause performance issues.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-01 13:19:40 UTC
- **Merged At**: 2023-12-01 16:00:36 UTC
- **Modified Policies**: aws_rightsize_rds_instances.pt, aws_rightsize_rds_instances_meta_parent.pt

### PR [#1657](): POL-978 Update Default Frequency of Children to "Weekly"

#### Description

> ### Description
> 
> The default frequency for child policies is currently "daily", which is excessive in most cases and does not align with most child policies. This PR is to change it to "weekly"
> 
> This also fixes an issue where one of the meta policy parameters would refer to the Tag Cardinality policy instead of the name of the actual policy the meta policy is for.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-01 13:25:29 UTC
- **Merged At**: 2023-12-01 15:59:38 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1649](): POL-975 Google Old Snapshots Revamp / Meta Policy

#### Description

> ### Description
> 
> This is a revamp of the Google Old Snapshots policy that also adds meta policy support for it.
> 
> Note: This policy does not report savings (identical to previous version) because we do not ingest GCP billing data at a granular enough level to obtain costs for specific resources. This policy should be updated if/when that changes.
> 
> From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added ability to filter resources by project
> - Added ability to use wildcards when filtering resources by label
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added additional fields to incident export
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera One credential
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65660e9c99745e0001588323
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-28 16:01:34 UTC
- **Merged At**: 2023-11-29 16:55:04 UTC
- **Modified Policies**: google_delete_old_snapshots.pt, google_delete_old_snapshots_meta_parent.pt

### PR [#1646](): POL-974 Deprecate AWS Unused RDS Policy

#### Description

> ### Description
> 
> The AWS Unused RDS policy is being deprecated due to the Rightsize RDS policy now containing identical functionality. This is similar to what has been done with other similar policies.
> 
> ### Link to Example Applied Policy
> 
> N/A. Changes do not impact policy execution.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-27 19:16:38 UTC
- **Merged At**: 2023-11-29 13:04:02 UTC
- **Modified Policies**: unused_rds.pt, unused_rds_meta_parent.pt

### PR [#1629](): POL-745 Deprecate SaaS Manager - User Status Change Policy

#### Description

> ### Description
> The SaaS Manager - User Status Change policy is not functionally distinct from the SaaS Manager - Deactivated Users policy. For this reason, rather than updating it, it is being deprecated.
> 
> ### Link to Example Applied Policy
> 
> N/A. Changes do not impact policy execution.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 20:39:37 UTC
- **Merged At**: 2023-11-29 13:03:46 UTC
- **Modified Policies**: fsm-user_status_change.pt

### PR [#1624](): POL-745 SaaS Manager - Deactivated Users Revamp

#### Description

> ### Description
> 
> This is part of a broader initiative to update our SaaS Manager FSM policies to use up to date APIs. The policy itself has also been revamped along similar lines to other policies. The policy has also been renamed to better reflect what it actually checks for.
> 
> From the CHANGELOG:
> 
> - Policy renamed to `SaaS Manager - Deactivated Users` to better reflect its functionality
> - Reduced minimum value of `Inactive Days Threshold` parameter from 60 to 0
> - Added `Applications` parameter to allow user to filter results by application
> - Updated policy to use public SaaS Manager API
> - Added support for APAC API endpoint
> - Policy now uses and requires a general Flexera One credential
> - Incident summary now includes applied policy name
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=654bea14e947000001d9372a
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 13:57:56 UTC
- **Merged At**: 2023-11-21 22:26:33 UTC
- **Modified Policies**: deactivated_users.pt, inactive_users_by_dept.pt

### PR [#1640](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6949742626)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-11-21 21:25:20 UTC
- **Merged At**: 2023-11-21 21:27:42 UTC
- **Modified Policies**: aws_rightsize_rds_instances_meta_parent.pt

### PR [#1609](): POL-964 Email Cost Optimization Recommendations

#### Description

> ### Description
> 
> This is a new policy that retrieves recommendations from the Flexera API and emails them to the specified list of email users. This offers functionality that can't currently be obtained within individual policies, such as the ability to send recommendations from multiple source policies in a single email, and the ability to email recommendations from child policies at any cadence the user wishes.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65452f9a99745e0001587f6f
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, New Policy
- **Created At**: 2023-11-03 17:36:57 UTC
- **Merged At**: 2023-11-21 21:25:49 UTC
- **Modified Policies**: email_recommendations.pt

### PR [#1619](): POL-968 AWS Rightsize RDS Instances Revamp

#### Description

> ### Description
> 
> This is a revamp of the AWS Rightsize RDS Instances policy. The changes here are pretty numerous, but the short version is that the policy now has parity with the equivalent Azure policy and reports recommendations for both underutilized and unused databases. From the CHANGELOG:
> 
> - Added parameter to specify how far back to check instances for activity
> - Several parameters altered to be more descriptive and human-readable
> - Policy now reports on both unused and underutilized RDS instances
> - Policy now reports savings for both unused and underutilized RDS instance recommendations
> - Fixed issue where policy would sometimes recommend downsizing to unsupported instance types
> - Added ability to choose between different CPU metrics for assessing utilization
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by multiple tag key:value pairs
> - Added ability to downsize instances immediately or during next maintenance window
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6553e799e947000001d937fb
> 
> Note: Through testing, I've confirmed that both the underutilized and unused incidents work, as do the downsize and terminate actions. 
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-14 21:49:03 UTC
- **Merged At**: 2023-11-21 21:24:48 UTC
- **Modified Policies**: rds_instance_cloudwatch_utilization.pt, aws_rightsize_rds_instances.pt, aws_rightsize_rds_instances_meta_parent.pt

### PR [#1620](): feat: Meta Policy Consolidated Incident Actions

#### Description

> ### Description
> 
>  - Enables triggering policy escalation actions from the Meta Parent "Consolidated Incident"
>  - Fixes the Incident Summary for some policies `with index 0` -> `AWS EC2 Volumes Found` ( [example](https://github.com/flexera-public/policy_templates/pull/1620/files#diff-622ba01a4d2f8338f7ab763d1d660e1b052ceaf93d800da5a71da2f93e45314fL971-R1013) )
> 
> 
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6553ef7099745e00015880dc
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6553ef6c99745e00015880db
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> 
> 
> Validated that actions work on AWS... using ARN/Credential in `586789346966` on a child policy applied for `638914988530`:
> > fpt -a 116186 run aws_unused_ip_addresses_meta_parent.pt -C auth_flexera=BKaraffa-flexera-com_RefreshToken -C auth_aws=arn-aws-iam--586789346966-role-FlexeraAutomationAccessRole 'param_dimension_filter_includes=["vendor_account=638914988530"]' 'param_regions_list=["us-east-1","us-east-2","us-west-1","us-west-2"]' param_days_unattached=0 -kr
> 
> and
> 
> > fpt -a 116186 run aws_rightsize_ec2_instances_meta_parent.pt -C auth_flexera=BKaraffa-flexera-com_RefreshToken -C auth_aws=arn-aws-iam--586789346966-role-FlexeraAutomationAccessRole 'param_dimension_filter_includes=["vendor_account=638914988530"]' 'param_regions_list=["us-west-2"]' param_stats_idle_threshold_cpu_value=50 param_stats_underutil_threshold_cpu_value=100 -kr
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-11-14 22:39:07 UTC
- **Merged At**: 2023-11-21 00:21:43 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1635](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6936774725)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-11-20 22:56:24 UTC
- **Merged At**: 2023-11-20 23:49:32 UTC
- **Modified Policies**: aws_volumes_rightsizing_meta_parent.pt, aws_unused_ip_addresses_meta_parent.pt

### PR [#1632](): feat: add param for AWS Pricing API Endpoint

#### Description

> ### Description
> 
> Added parameter to override the AWS Pricing API Endpoint.
> 
> This will enable us to change the API endpoint being used by the Policy Template in case a customer is using an AWS Service Control Policy to deny `us-east-1` which we previously had hard-coded.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/35917/automation/applied-policies/projects/137860?noIndex=1&policyId=655bbca055d35d0001a8c051
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-11-20 21:21:52 UTC
- **Merged At**: 2023-11-20 22:55:52 UTC
- **Modified Policies**: aws_volumes_rightsizing.pt, aws_unused_ip_addresses.pt

### PR [#1627](): POL-745 SaaS Manager - Unsanctioned Spend Revamp

#### Description

> ### Description
> 
> This is part of a broader initiative to update our SaaS Manager FSM policies to use the correct API endpoints for APAC. The policy itself has also been revamped along similar lines to other policies.
> 
> Note: This policy still uses the now-deprecated internal SaaS Manager API. This is because the new API does not yet support the requests this policy needs to make to function. This functionality will be brought to the new API before the old one is decommissioned, and this policy will need to be updated again at that time.
> 
> From the CHANGELOG:
> 
> - Added support for APAC API endpoint
> - Policy now uses and requires a general Flexera One credential
> - Incident summary now includes applied policy name
> - `Expense Sum` and `Currency` are now separate incident fields
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65551e3be947000001d9380a
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 19:41:22 UTC
- **Merged At**: 2023-11-20 22:19:01 UTC
- **Modified Policies**: fsm-unsanctioned_spend.pt

