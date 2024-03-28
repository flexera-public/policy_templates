# flexera-public/policy_templates Change History

## Description

This document contains the last 200 policy template merges for the flexera-public/policy_templates repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 200 policy merges, is also available.

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
- **Modified Policies**: automation/aws/aws_missing_regions/aws_missing_regions.pt, automation/aws/aws_missing_regions/aws_missing_regions_meta_parent.pt

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
- **Modified Policies**: cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances.pt, cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances_meta_parent.pt

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
- **Modified Policies**: cost/azure/savings_realized/azure_savings_realized.pt

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
- **Modified Policies**: compliance/policy_update_notification/policy_update_notification.pt

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
- **Modified Policies**: cost/budget_v_actual_spend_report/budget_v_actual_spend_report.pt

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
- **Modified Policies**: cost/cloud_cost_anomaly_alerts/cloud_cost_anomaly_alerts.pt

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
- **Modified Policies**: cost/google/cloud_run_anomaly_detection/google_cloud_run_anomaly_detection.pt

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
- **Modified Policies**: cost/budget_v_actual_spend_report/budget_v_actual_spend_report.pt

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
- **Modified Policies**: automation/flexera/delete_all_billing_centers/delete_all_billing_centers.pt

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
- **Modified Policies**: operational/azure/byol_report/azure_byol_report.pt

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
- **Modified Policies**: cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing.pt, cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing_meta_parent.pt, cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt, cost/aws/unused_ip_addresses/aws_unused_ip_addresses_meta_parent.pt

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
- **Modified Policies**: cost/budget_v_actual/monthly_budget_v_actual.pt, cost/budget_v_actual_spend_report/budget_v_actual_spend_report.pt

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
- **Modified Policies**: security/storage/google/public_buckets/google_public_buckets.pt, security/storage/google/public_buckets/google_public_buckets_meta_parent.pt

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
- **Modified Policies**: cost/aws/rds_instance_license_info/rds_instance_license_info.pt, cost/aws/rds_instance_license_info/rds_instance_license_info_meta_parent.pt, cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances.pt, cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances_meta_parent.pt

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
- **Modified Policies**: cost/azure/unused_ip_addresses/azure_unused_ip_addresses.pt, cost/azure/unused_ip_addresses/azure_unused_ip_addresses_meta_parent.pt

### PR [#1879](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/8071749355)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-27 21:44:42 UTC
- **Merged At**: 2024-02-27 21:48:08 UTC
- **Modified Policies**: cost/azure/rightsize_netapp_files/azure_rightsize_netapp_files_meta_parent.pt

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
- **Modified Policies**: cost/azure/rightsize_netapp_files/azure_rightsize_netapp_files.pt

### PR [#1874](): POL-1070 Deprecate AWS Inefficient Instance Utilization using CloudWatch

#### Description

> ### Description
> 
> The AWS Inefficient Instance Utilization using CloudWatch policy does basically the same thing as the existing Rightsize EC2 policy, so it is being deprecated.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-02-27 20:40:44 UTC
- **Merged At**: 2024-02-27 21:41:58 UTC
- **Modified Policies**: cost/aws/instance_cloudwatch_utilization/aws_instance_cloudwatch_utilization.pt

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
- **Modified Policies**: cost/cloud_cost_anomaly_alerts/cloud_cost_anomaly_alerts.pt

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
- **Modified Policies**: cost/cloud_cost_anomaly_alerts/cloud_cost_anomaly_alerts.pt

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
- **Modified Policies**: cost/azure/rightsize_netapp_files/azure_rightsize_netapp_files.pt, cost/azure/rightsize_netapp_files/azure_rightsize_netapp_files_meta_parent.pt

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
- **Modified Policies**: cost/aws/old_snapshots/aws_delete_old_snapshots.pt, cost/aws/old_snapshots/aws_delete_old_snapshots_meta_parent.pt

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
- **Modified Policies**: cost/aws/burstable_ec2_instances/aws_burstable_ec2_instances.pt, cost/aws/burstable_ec2_instances/aws_burstable_ec2_instances_meta_parent.pt, cost/aws/burstable_instance_cloudwatch_credit_utilization/aws_burstable_instance_cloudwatch_credit_utilization.pt

### PR [#1848](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/8010285881)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-22 20:02:00 UTC
- **Merged At**: 2024-02-22 20:02:39 UTC
- **Modified Policies**: cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing_meta_parent.pt, cost/aws/superseded_instances/aws_superseded_instances_meta_parent.pt, cost/aws/unused_ip_addresses/aws_unused_ip_addresses_meta_parent.pt, cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit_meta_parent.pt, cost/azure/superseded_instances/azure_superseded_instances_meta_parent.pt, cost/google/cloud_sql_idle_instance_recommendations/google_sql_idle_instance_recommendations_meta_parent.pt, cost/google/cud_recommendations/google_committed_use_discount_recommendations_meta_parent.pt, cost/google/idle_ip_address_recommendations/google_idle_ip_address_recommendations_meta_parent.pt, cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations_meta_parent.pt, cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations_meta_parent.pt

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
- **Modified Policies**: operational/azure/byol_report/azure_byol_report.pt

### PR [#1837](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7934272061)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-16 17:46:32 UTC
- **Merged At**: 2024-02-16 18:04:53 UTC
- **Modified Policies**: cost/azure/rightsize_managed_disks/azure_rightsize_managed_disks_meta_parent.pt

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
- **Modified Policies**: cost/azure/rightsize_managed_disks/azure_rightsize_managed_disks.pt

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
- **Modified Policies**: automation/flexera/outdated_applied_policies/outdated_applied_policies.pt

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
- **Modified Policies**: cost/azure/schedule_instance/azure_schedule_instance.pt, cost/azure/schedule_instance/azure_schedule_instance_meta_parent.pt

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
- **Modified Policies**: cost/aws/schedule_instance/aws_schedule_instance.pt, cost/aws/schedule_instance/aws_schedule_instance_meta_parent.pt

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
- **Modified Policies**: cost/google/schedule_instance/google_schedule_instance.pt, cost/google/schedule_instance/google_schedule_instance_meta_parent.pt

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
- **Modified Policies**: automation/azure/azure_missing_subscriptions/azure_missing_subscriptions.pt

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
- **Modified Policies**: cost/azure/blob_storage_optimization/azure_blob_storage_optimization_meta_parent.pt

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
- **Modified Policies**: cost/azure/blob_storage_optimization/azure_blob_storage_optimization.pt, cost/azure/blob_storage_optimization/azure_blob_storage_optimization_meta_parent.pt

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
- **Modified Policies**: cost/azure/object_storage_optimization/azure_object_storage_optimization.pt, cost/azure/object_storage_optimization/azure_object_storage_optimization_meta_parent.pt

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
- **Modified Policies**: cost/aws/object_storage_optimization/aws_object_storage_optimization.pt, cost/aws/object_storage_optimization/aws_object_storage_optimization_meta_parent.pt

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
- **Modified Policies**: operational/azure/azure_long_running_instances/azure_long_running_instances.pt, operational/azure/azure_long_running_instances/azure_long_running_instances_meta_parent.pt

### PR [#1789](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7782044712)
#### Metadata

- **Labels**: automation
- **Created At**: 2024-02-02 22:32:03 UTC
- **Merged At**: 2024-02-05 09:10:27 UTC
- **Modified Policies**: cost/azure/rightsize_managed_disks/azure_rightsize_managed_disks_meta_parent.pt

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
- **Modified Policies**: cost/azure/rightsize_managed_disks/azure_rightsize_managed_disks.pt, cost/azure/rightsize_managed_disks/azure_rightsize_managed_disks_meta_parent.pt

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
- **Modified Policies**: operational/aws/long_running_instances/long_running_instances.pt, operational/aws/long_running_instances/long_running_instances_meta_parent.pt

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
- **Modified Policies**: compliance/azure/azure_disallowed_regions/azure_disallowed_regions.pt, compliance/azure/azure_disallowed_regions/azure_disallowed_regions_meta_parent.pt

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
- **Modified Policies**: compliance/google/long_stopped_instances/google_long_stopped_instances.pt, compliance/google/long_stopped_instances/google_long_stopped_instances_meta_parent.pt

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
- **Modified Policies**: compliance/aws/untagged_resources/aws_untagged_resources.pt, compliance/aws/untagged_resources/aws_untagged_resources_meta_parent.pt

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
- **Modified Policies**: cost/azure/reserved_instances/recommendations/azure_reserved_instance_recommendations.pt, cost/azure/reserved_instances/recommendations/azure_reserved_instance_recommendations_meta_parent.pt

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
- **Modified Policies**: compliance/azure/azure_long_stopped_instances/long_stopped_instances_azure.pt, compliance/azure/azure_long_stopped_instances/long_stopped_instances_azure_meta_parent.pt

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
- **Modified Policies**: compliance/aws/long_stopped_instances/aws_long_stopped_instances.pt, compliance/aws/long_stopped_instances/aws_long_stopped_instances_meta_parent.pt

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
- **Modified Policies**: cost/azure/reserved_instances/recommendations/azure_reserved_instance_recommendations.pt

### PR [#1736](): POL-1043 Update Meta Policies

#### Description

> ### Description
> 
> The script for generating meta policies has been updated. This is just a PR to regenerate some of the meta policies using this script.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2024-01-12 13:17:54 UTC
- **Merged At**: 2024-01-12 14:28:44 UTC
- **Modified Policies**: compliance/azure/instances_without_fnm_agent/azure_instances_not_running_flexnet_inventory_agent_meta_parent.pt, cost/aws/gp3_volume_upgrade/aws_upgrade_to_gp3_volume_meta_parent.pt, cost/aws/object_storage_optimization/aws_object_storage_optimization_meta_parent.pt, operational/aws/lambda_functions_with_high_error_rate/lambda_functions_with_high_error_rate_meta_parent.pt, operational/azure/azure_certificates/azure_certificates_meta_parent.pt, security/aws/ebs_unencrypted_volumes/aws_unencrypted_volumes_meta_parent.pt, security/aws/rds_publicly_accessible/aws_publicly_accessible_rds_instances_meta_parent.pt

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
- **Modified Policies**: compliance/aws/disallowed_regions/aws_disallowed_regions.pt, compliance/aws/disallowed_regions/aws_disallowed_regions_meta_parent.pt

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
- **Modified Policies**: operational/itam/schedule_itam_report/schedule-itam-report.pt

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
- **Modified Policies**: cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances.pt, cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances_meta_parent.pt

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
- **Modified Policies**: cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute.pt, cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute_meta_parent.pt, cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute_meta_parent_cluster.pt

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
- **Modified Policies**: cost/azure/old_snapshots/azure_delete_old_snapshots.pt, cost/azure/old_snapshots/azure_delete_old_snapshots_meta_parent.pt

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
- **Modified Policies**: cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances.pt, cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances_meta_parent.pt

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
- **Modified Policies**: cost/aws/unused_volumes/aws_delete_unused_volumes.pt, cost/aws/unused_volumes/aws_delete_unused_volumes_meta_parent.pt

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
- **Modified Policies**: cost/aws/old_snapshots/aws_delete_old_snapshots.pt, cost/aws/old_snapshots/aws_delete_old_snapshots_meta_parent.pt

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
- **Modified Policies**: cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt, cost/aws/unused_ip_addresses/aws_unused_ip_addresses_meta_parent.pt

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
- **Modified Policies**: cost/scheduled_reports/scheduled_report.pt

### PR [#1708](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7338799914)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-12-27 13:31:30 UTC
- **Merged At**: 2023-12-27 13:39:41 UTC
- **Modified Policies**: cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit_meta_parent.pt

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
- **Modified Policies**: cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit.pt

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
- **Modified Policies**: cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations.pt, cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations_meta_parent.pt

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
- **Modified Policies**: cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances.pt, cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances_meta_parent.pt

### PR [#1695](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7225989438)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-12-15 19:00:52 UTC
- **Merged At**: 2023-12-15 19:11:13 UTC
- **Modified Policies**: cost/aws/schedule_instance/aws_schedule_instance_meta_parent.pt

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
- **Modified Policies**: cost/aws/schedule_instance/aws_schedule_instance.pt, cost/google/schedule_instance/google_schedule_instance.pt

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
- **Modified Policies**: compliance/policy_update_notification/policy_update_notification.pt

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
- **Modified Policies**: cost/azure/reserved_instances/utilization/azure_reserved_instance_utilization.pt

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
- **Modified Policies**: cost/azure/rightsize_compute_instances/azure_compute_rightsizing.pt, cost/azure/rightsize_compute_instances/azure_compute_rightsizing_meta_parent.pt

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
- **Modified Policies**: cost/aws/elb/clb_unused/aws_delete_unused_clb.pt, cost/aws/unused_clbs/aws_unused_clbs.pt, cost/aws/unused_clbs/aws_unused_clbs_meta_parent.pt

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
- **Modified Policies**: cost/currency_conversion/currency_conversion.pt

### PR [#1663](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/7065172364)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-12-01 19:57:12 UTC
- **Merged At**: 2023-12-01 21:08:09 UTC
- **Modified Policies**: cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute_meta_parent.pt, security/storage/aws/public_buckets/aws_public_buckets_meta_parent.pt

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
- **Modified Policies**: cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute.pt, cost/azure/databricks/rightsize_compute/azure_databricks_rightsize_compute_meta_parent.pt

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
- **Modified Policies**: security/storage/aws/public_buckets/aws_public_buckets.pt, security/storage/aws/public_buckets/aws_public_buckets_meta_parent.pt

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
- **Modified Policies**: saas/fsm/deactivated_users_for_integrated_apps/deactivated_users_for_integrated_apps.pt, saas/fsm/inactive_users_for_integrated_apps/inactive_users_for_integrated_apps.pt

### PR [#1656](): POL-977 AWS Rightsize RDS: Change Parameter Default Value

#### Description

> ### Description
> 
> This just changes the default value of the `Underutilized Instance CPU Threshold (%)` parameter to 40% to match other policies and ensure that our recommendations won't cause performance issues.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-12-01 13:19:40 UTC
- **Merged At**: 2023-12-01 16:00:36 UTC
- **Modified Policies**: cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances.pt, cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances_meta_parent.pt

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
- **Modified Policies**: cost/google/old_snapshots/google_delete_old_snapshots.pt, cost/google/old_snapshots/google_delete_old_snapshots_meta_parent.pt

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
- **Modified Policies**: cost/aws/unused_rds/unused_rds.pt, cost/aws/unused_rds/unused_rds_meta_parent.pt

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
- **Modified Policies**: saas/fsm/user_status_change/fsm-user_status_change.pt

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
- **Modified Policies**: saas/fsm/deactivated_users/deactivated_users.pt, saas/fsm/inactive_users_by_dept/inactive_users_by_dept.pt

### PR [#1640](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6949742626)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-11-21 21:25:20 UTC
- **Merged At**: 2023-11-21 21:27:42 UTC
- **Modified Policies**: cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances_meta_parent.pt

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
- **Modified Policies**: cost/email_recommendations/email_recommendations.pt

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
- **Modified Policies**: cost/aws/rds_instance_cloudwatch_utilization/rds_instance_cloudwatch_utilization.pt, cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances.pt, cost/aws/rightsize_rds_instances/aws_rightsize_rds_instances_meta_parent.pt

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
- **Modified Policies**: cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing_meta_parent.pt, cost/aws/unused_ip_addresses/aws_unused_ip_addresses_meta_parent.pt

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
- **Modified Policies**: cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing.pt, cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt

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
- **Modified Policies**: saas/fsm/unsanctioned_spend/fsm-unsanctioned_spend.pt

### PR [#1621](): POL-745 SaaS Manager - Duplicate User Accounts Revamp

#### Description

> ### Description
> 
> This is part of a broader initiative to update our SaaS Manager FSM policies to use up to date APIs. The policy itself has also been revamped along similar lines to other policies.
> 
> From the CHANGELOG:
> 
> - Updated policy to use public SaaS Manager API
> - Added support for APAC API endpoint
> - Policy now uses and requires a general Flexera One credential
> - Incident summary now includes applied policy name
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=654b8824e947000001d93727
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 13:44:22 UTC
- **Merged At**: 2023-11-20 22:18:45 UTC
- **Modified Policies**: saas/fsm/duplicate_users/duplicate_users.pt

### PR [#1622](): POL-745 SaaS Manager - Redundant Apps Revamp

#### Description

> ### Description
> 
> This is part of a broader initiative to update our SaaS Manager FSM policies to use up to date APIs. The policy itself has also been revamped along similar lines to other policies.
> 
> From the CHANGELOG:
> 
> - Updated policy to use public SaaS Manager API
> - Added support for APAC API endpoint
> - Policy now uses and requires a general Flexera One credential
> - Incident summary now includes applied policy name
> - Incident now includes additional fields to provide more context
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65522cc899745e0001588079
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 13:47:53 UTC
- **Merged At**: 2023-11-20 22:18:31 UTC
- **Modified Policies**: saas/fsm/redundant_apps/fsm-redundant_apps.pt

### PR [#1623](): POL-745 SaaS Manager - Renewal Reminder Revamp

#### Description

> ### Description
> 
> This is part of a broader initiative to update our SaaS Manager FSM policies to use up to date APIs. The policy itself has also been revamped along similar lines to other policies.
> 
> From the CHANGELOG:
> 
> - Updated policy to use public SaaS Manager API
> - Added support for APAC API endpoint
> - Policy now uses and requires a general Flexera One credential
> - Added `Applications` parameter to allow user to filter results by application
> - Incident summary now includes applied policy name
> - Incident now includes additional fields to provide more context
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65526b4a99745e0001588087
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 13:50:46 UTC
- **Merged At**: 2023-11-20 22:18:21 UTC
- **Modified Policies**: saas/fsm/renewal_reminder/fsm-renewal_reminder.pt

### PR [#1626](): POL-745 SaaS Manager - Suspicious Users Revamp

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
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65455431e947000001d936ce
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 15:00:59 UTC
- **Merged At**: 2023-11-20 22:18:07 UTC
- **Modified Policies**: saas/fsm/suspicious_users/fsm-suspicious_users.pt

### PR [#1628](): POL-745 SaaS Manager - Unsanctioned Applications with Existing Contract Revamp

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
> - `Currency` is now a separate incident field
> - General code cleanup and normalization
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6555266899745e00015880f1
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-15 20:31:45 UTC
- **Merged At**: 2023-11-20 22:17:40 UTC
- **Modified Policies**: saas/fsm/unsanctioned_apps_with_contract/fsm-unsanctioned_with_contract.pt

### PR [#1605](): POL-745 Fix APAC API Endpoints

#### Description

> ### Description
> 
> This updates policies to point to the correct APAC API endpoints. 
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-02 18:39:37 UTC
- **Merged At**: 2023-11-16 18:51:14 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1617](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6830113114)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-11-10 22:15:25 UTC
- **Merged At**: 2023-11-13 13:15:56 UTC
- **Modified Policies**: cost/aws/object_storage_optimization/aws_object_storage_optimization_meta_parent.pt

### PR [#1610](): FOPTS-2380 Modify S3 Object Policy template to prevent tag calls if user don't input tags

#### Description

> ### Description
> 
> Modify temporally a bucket list to prevent timeout from large buckets, and revert that changes once successfully results
> 
> Additionally, if user did specify exclude tags, retrieve tags only for objects we will be raising incident for, instead of making calls for all discovered objects
> 
> ### Issues Resolved
> 
> [FOPTS-2380](https://flexera.atlassian.net/browse/FOPTS-2380)
> 
> ### Link to Example Applied Policy
> [Applied policy with all buckets](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=654b49063411070001af400a)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-11-06 21:50:40 UTC
- **Merged At**: 2023-11-10 22:14:42 UTC
- **Modified Policies**: cost/aws/object_storage_optimization/aws_object_storage_optimization.pt, cost/aws/object_storage_optimization/aws_object_storage_optimization_meta_parent.pt

### PR [#1613](): POL-966 Azure Rightsize SQL Fix

#### Description

> ### Description
> 
> If the list of databases returned by the Azure API included entries without a valid 'sku' field, the policy would error out instead of completing. This is a fix for that; such entries are now filtered entirely, since it wouldn't be possible to provide meaningful recommendations without knowing the SKU anyway.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=654d2e7e99745e0001588027
> 
> Note: The above does not raise an incident and is just to confirm the policy completes. I have also tested this in the user environment where the issue was originally reported and verified the fix does work as intended.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-09 19:24:30 UTC
- **Merged At**: 2023-11-09 20:29:42 UTC
- **Modified Policies**: cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances.pt, cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances_meta_parent.pt

### PR [#1615](): POL-967 Deprecate AWS GP3 Upgradeable Volumes Policy

#### Description

> ### Description
> 
> This policy is no longer being updated. The [AWS Rightsize EBS Volumes](https://github.com/flexera-public/policy_templates/tree/master/cost/aws/rightsize_ebs_volumes/) policy should be used for these recommendations instead.
> 
> Note that, unlike the AWS Rightsize EBS Volumes policy, this policy reports on IO1 and IO2 volumes. These volumes are high performance volumes, so changing them to GP3 will result in a performance downgrade and may cause issues for workloads that rely on this performance.
> 
> Effectively, this policy was just recommending the above change without regard for actual usage data, which is a bit reckless and shouldn't be done. A future version of the AWS Rightsize EBS Volumes policy may include this functionality, but it would be alongside actual analysis of metrics to determine if the downgrade makes sense.
> 
> ### Link to Example Applied Policy
> 
> N/A. Changes have no impact on functionality or policy execution.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-09 20:18:33 UTC
- **Merged At**: 2023-11-09 20:27:33 UTC
- **Modified Policies**: cost/aws/gp3_volume_upgrade/aws_upgrade_to_gp3_volume.pt, cost/aws/gp3_volume_upgrade/aws_upgrade_to_gp3_volume_meta_parent.pt

### PR [#1602](): POL-960 Update AWS Reserved Instances Utilization - add ability to filter by Billing Center

#### Description

> ### Description
> 
> <!-- Describe what this change achieves below -->
> Adds functionality to the policy so that a user can filter current reservation purchases by Billing Center. 
> 
> As we cannot currently support RBAC on reserved instances within the platform, this will allow for owners of Billing Centers to only receive the list of reservations (and their respective utilizations) that are applicable to their BCs, and not see all reservations at a global level.
> 
> If the user does not specify a specific list of billing centers, the policy operates in the same way it did prior to this change.
> 
> ### Issues Resolved
> 
> <!-- List any existing issues this PR resolves below -->
> - Fixes README title to reflect policy template name.
> - Fixes README "Credential Configuration" section to reflect the credentials required to run the policy.
> 
> ### Link to Example Applied Policy
> 
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6545048599745e0001587f6b 
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-11-02 10:26:43 UTC
- **Merged At**: 2023-11-09 19:30:09 UTC
- **Modified Policies**: cost/aws/reserved_instances/utilization/utilization_ris.pt

### PR [#1612](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6787941490)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-11-07 17:11:50 UTC
- **Merged At**: 2023-11-07 17:12:47 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1604](): POL-963 Deprecate "Azure Inefficient Instance Utilization using Log Analytics" Policy

#### Description

> ### Description
> 
> CPU and memory usage data can now be obtained from Azure resources without the need for Log Analytics. The Azure Rightsize Compute Instances policy now includes this functionality and is the recommended policy for getting recommendations for inefficient instance utilization. As a consequence, the Azure Inefficient Instance Utilization using Log Analytics policy is now being deprecated.
> 
> ### Link to Example Applied Policy
> 
> Not needed. Changes do not affect policy functionality or execution.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-11-02 16:32:12 UTC
- **Merged At**: 2023-11-03 12:22:39 UTC
- **Modified Policies**: cost/azure/instances_log_analytics_utilization/azure_instance_log_analytics_utilization.pt

### PR [#1598](): fix: name `AWS Ensure IAM Users Receive Permissions Only Through Groups`

#### Description

> ### Description
> 
> We have 2 PTs with same name.. that should never happen.  Looks like this one was incorrectly named
> 
> Identified from automation PR for active policy list:
> https://github.com/flexera-public/policy_templates/pull/1597/files
> Two PTs should not have same name
#### Metadata

- **Labels**: bug, small fixes
- **Created At**: 2023-11-01 18:14:11 UTC
- **Merged At**: 2023-11-01 18:24:10 UTC
- **Modified Policies**: security/aws/iam_users_perms_via_groups_only/iam_users_perms_via_groups_only.pt

### PR [#1554](): feat: Add required for "Meta Policy" use-cases for AWS Tag Cardinality Report

#### Description

> ### Description
> 
> Added logic required for "Meta Policy" use-cases
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=652ed5b4e947000001d933b3
> Include filter is `vendor_account=...` intentionaly b/c that 1 test account we granted permissions -- policy status is successful with some tag results.  Current version of CFT has Tag Cardinality in it and if the AWS Org Admins uses/updates to that, then we can use Meta Policies across all Accounts in the AWS Org
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement
- **Created At**: 2023-10-17 18:26:54 UTC
- **Merged At**: 2023-11-01 15:49:57 UTC
- **Modified Policies**: operational/aws/tag_cardinality/aws_tag_cardinality.pt, operational/aws/tag_cardinality/aws_tag_cardinality_meta_parent.pt

### PR [#1576](): POL-944 Fix Azure Savings Realized for new Azure EA Connections

#### Description

> ### Description
> 
> This policy did not work correctly for clients using the new Azure EA bill connect method. This corrects that issue. The policy now obtains a list of bill connections from Optima and tailors the requests to the Optima API based on which bill connections exist. The policy should now work with both old and new connections and collect costs from both if both are present.
> 
> I've done a pretty thorough investigation/testing of this in a client account, and I am confident that we are now pulling the correct data.
> 
> It's likely that this policy will be changed to use the savings value in Optima once that feature is available for Azure, but this PR will ensure the policy at least continues to work as expected for users using the new EA bill connections in the meantime.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=65426cfb99745e0001587dfe
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-26 19:41:55 UTC
- **Merged At**: 2023-11-01 15:43:40 UTC
- **Modified Policies**: cost/azure/savings_realized/azure_savings_realized.pt

### PR [#1526](): feat: Added "Stop Instance" action for Idle resources

#### Description

> ### Description
> 
> Added "Stop Instance" action for Idle resources
> 
> 
> 
> ### Link to Example Applied Policy
> 
> <img width="1390" alt="image" src="https://github.com/flexera-public/policy_templates/assets/1490015/a2e15b83-3e4e-4d47-b867-ae97519828a9">
> https://app.flexera.com/orgs/27018/automation/incidents/projects/116186?incidentId=652085f10a0c27000190eb4f
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-06 22:17:18 UTC
- **Merged At**: 2023-10-31 20:18:22 UTC
- **Modified Policies**: cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt, cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances_meta_parent.pt

### PR [#1579](): POL-959 Deprecate Idle Usage Reduction Policies

#### Description

> ### Description
> 
> The following policies should be flagged as deprecated, as their functionality is now included in other policies:
> 
> AWS Idle Compute Instances (functionality is now part of AWS Rightsize EC2 Instances)
> Azure Idle Compute Instances (functionality is now part of Azure Rightsize Compute Instances)
> Azure Unused SQL Databases (functionality is now part of Azure Rightsize SQL Databases)
> Google Idle VM Recommender (functionality is now part of Google Rightsize VM Recommender)
> 
> This change does *not* remove the policies from the catalog or impact the functionality of existing meta policies that customers may be using. It simply directs users to the more updated and correct policies when browsing the catalog.
> 
> ### Link to Example Applied Policy
> 
> N/A. These changes don't impact policy execution.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-27 18:39:43 UTC
- **Merged At**: 2023-10-31 20:15:42 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1582](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6698980118)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-10-30 21:34:04 UTC
- **Merged At**: 2023-10-30 21:43:19 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1553](): feat: Add Policy Template Source parameter on Meta Parent Policy

#### Description

> ### Description
> 
> Adds a parameter which enables a Meta Parent Policy Template to use the uploaded Policy Template for the child instead of the Published Template.  This is primarily helpful for development, but may also be helpful for customers that use forked versions of our Child Policy Templates.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=652ed5b4e947000001d933b3
> Deployed using uploaded policy template
#### Metadata

- **Labels**: enhancement
- **Created At**: 2023-10-17 18:16:19 UTC
- **Merged At**: 2023-10-30 21:33:28 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1555](): FOPTS-1503 Savings Realized Per Instance Type Report

#### Description

> ### Description
> 
> There used to be a discrepancy between Flexera data sources.
> 
> ### Issues Resolved
> 
> As Savings metric becomes generally available, policy is updated to make use of it to estimate savings accurately and consistently with AWS Realized Savings dashboard.
> 
> ### Link to Example Applied Policy
> 
> Applied policy: https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65386a3d666365000100ca32
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-10-19 18:41:55 UTC
- **Merged At**: 2023-10-30 20:42:46 UTC
- **Modified Policies**: cost/aws/savings_realized/aws_savings_realized.pt

### PR [#1571](): SQ-4937 Broken read me hyperlink for automation policy

#### Description

> ### Description
> 
> The ReadMe link for the AWS Superseded EC2 Instances policy is incorrect.
> 
> ### Issues Resolved
> 
> [SQ-4937](https://flexera.atlassian.net/browse/SQ-4937)
> 
> ### Link to Example Applied Policy
> 
> NA
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-10-25 23:40:03 UTC
- **Merged At**: 2023-10-27 18:47:42 UTC
- **Modified Policies**: cost/aws/superseded_instances/aws_superseded_instances.pt, cost/aws/superseded_instances/aws_superseded_instances_meta_parent.pt

### PR [#1577](): POL-957 AWS Rightsize EC2 CloudWatch Fix

#### Description

> ### Description
> 
> This fixes several issues with how CloudWatch data is pulled that would occasionally cause incorrect results. Specifically, the date range we pull data for is now rounded down to the nearest hour. This is to ensure that the range is neatly sliced by the period we specify so that we only get one result back from CloudWatch for each metric.
> 
> Previously, it would sometimes imperfectly slice the data, giving us two results, the first being for less than an hour of time and the second being the number we actually needed, but when this happened, the policy grabbed the first number instead. As a backup, just in case somehow the above doesn't work, the policy now grabs the last item in the list of values instead of just grabbing [0] every time.
> 
> Additionally, I spotted a couple of issues where the lookback period was not being correctly used to adjust our request to the amount of days the user specified. Those have been fixed as well.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=653bb85099745e0001587d81
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-27 13:22:26 UTC
- **Merged At**: 2023-10-27 13:31:15 UTC
- **Modified Policies**: cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances.pt, cost/aws/rightsize_ec2_instances/aws_rightsize_ec2_instances_meta_parent.pt

### PR [#1536](): FOPTS-842 Google Unlabeled Resources Policy

#### Description

> ### Description
> 
> Policy shows missing label keys, but it also needed to show label values as AWS and Azure do in Untagged policies.
> 
> ### Issues Resolved
> 
> Policy shows missing label keys and values
> 
> ### Link to Example Applied Policy
> 
> - [Applied policy](https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=6538634855d35d0001a84cd6)
> - [Applied policy with mock data](https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65385fcc55d35d0001a84cd5)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-10-11 15:54:12 UTC
- **Merged At**: 2023-10-26 16:40:40 UTC
- **Modified Policies**: compliance/google/unlabeled_resources/unlabeled_resources.pt

### PR [#1552](): POL-719 Better 'Account Number' Parameter Description for AWS Policies

#### Description

> ### Description
> 
> Updating description of Account Number parameter to make it clear that it's for meta policies and users should leave it blank.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-13 18:55:15 UTC
- **Merged At**: 2023-10-26 12:14:24 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1534](): POL-941 Meta Policy Extension

#### Description

> ### Description
> 
> This modifies several policies in order to add meta policies for them. The generator script has also been modified to autogenerate these meta policies going forward.
> 
> ### Link to Example Applied Policy
> 
> No examples, but an "fpt check" was run against all modified policies and the new meta policies. The changes themselves are fairly minimal and should not affect policy execution.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-11 13:32:44 UTC
- **Merged At**: 2023-10-24 15:42:22 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1556](): FOPTS-2328 Low Account Usage Policy: add account ID to incident details

#### Description

> ### Description
> 
> Customers want account ID to be provided in the incident details for Low Account Usage policy
> 
> ### Issues Resolved
> 
> [FOPTS-2328 Jira](https://flexera.atlassian.net/browse/FOPTS-2328)
> 
> ### Link to Example Applied Policy
> 
> [Low Account Usage - Policy template applied](https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=65332b9755d35d0001a84227)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-10-21 06:14:29 UTC
- **Merged At**: 2023-10-24 15:12:11 UTC
- **Modified Policies**: cost/low_account_usage/low_account_usage.pt

### PR [#1564](): POL-955 Azure Long Running Instances Fix

#### Description

> ### Description
> 
> This policy incorrectly reports on stopped instances when it should only report running instances. This PR is to fix this issue. It also fixes a minor language error in the detailed template of the incident output.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6537cd34e947000001d934e5
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-24 12:56:58 UTC
- **Merged At**: 2023-10-24 14:41:07 UTC
- **Modified Policies**: operational/azure/azure_long_running_instances/azure_long_running_instances.pt, operational/azure/azure_long_running_instances/azure_long_running_instances_meta_parent.pt

### PR [#1557](): POL-947 Azure AHUB Utilization with Manual Entry Revamp

#### Description

> ### Description
> 
> This is a revamp of the Azure AHUB Utilization with Manual Entry policy. From the CHANGELOG:
> 
> - Fixed bug that would cause policy to raise error if incident contained no results
> - Added logic required for "Meta Policy" use-cases
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by subscription either via allow or deny list
> - Added ability to filter resources by region
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Policy no longer raises new escalations if irrelevant metadata changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera One credential
> 
> ### Issues Resolved
> 
> Extra fix: I saw a small error in the Azure Unused IP policy's CHANGELOG file. This also corrects that.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/incidents/projects/116186?incidentId=65369141af86a00001290d7e
> 
> (Note: Use case where disabling AHUB would be recommended has been tested in a client environment and also works as expected)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-23 14:22:49 UTC
- **Merged At**: 2023-10-24 11:17:03 UTC
- **Modified Policies**: compliance/azure/ahub_manual/azure_ahub_utilization_with_manual_entry.pt, compliance/azure/ahub_manual/azure_ahub_utilization_with_manual_entry_meta_parent.pt

### PR [#1519](): POL-930/931 New Marketplace Products Policies

#### Description

> ### Description
> 
> AWS New Marketplace Products: This policy compares AWS billing data from 3 days ago to billing data from a user-specified number of days ago (10 by default) to see if any new Marketplace products have been purchased since then. A list of the new products and their estimated monthly cost is raised as an incident and, optionally, emailed.
> 
> Azure New Marketplace Products: This policy compares Azure billing data from 3 days ago to billing data from a user-specified number of days ago (10 by default) to see if any new Marketplace products have been purchased since then. A list of the new products and their estimated monthly cost is raised as an incident and, optionally, emailed.
> 
> Notes:
> - Azure version will work with both the old and new style bill connections and has been tested with both.
> - Since these policies leverage Optima rather than cloud provider APIs, no meta policies were created, as they are not necessary.
> - These have been categorized as "cost" policies since their purpose is to help users find and mitigate unexpected expenses, but since we are not necessarily recommending that they terminate Marketplace services, metadata has not been added to facilitate scraping into the Optimization dashboard.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=651d9e4ce947000001d93205
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=651dc83899745e0001587a11
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-04 17:51:10 UTC
- **Merged At**: 2023-10-23 15:29:48 UTC
- **Modified Policies**: operational/aws/marketplace_new_products/aws_marketplace_new_products.pt, operational/azure/marketplace_new_products/azure_marketplace_new_products.pt

### PR [#1551](): POL-780 Azure Savings Realized Date Change

#### Description

> ### Description
> 
> The month field of this policy, despite just reporting a month, includes a full timestamp with date and time, like so: 
> 
> 2023-06-01T00:00:00Z
> 
> This modification makes it so that the Month field in the incident just contains the month, like so:
> 
> 2023-06
> 
> ### Link to Example Applied Policy
> 
> Verified working in client account.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, small fixes
- **Created At**: 2023-10-13 18:13:42 UTC
- **Merged At**: 2023-10-23 14:49:15 UTC
- **Modified Policies**: cost/azure/savings_realized/azure_savings_realized.pt

### PR [#1523](): POL-838 AWS Savings Plan Recommendations Revamp

#### Description

> ### Description
> 
> This is a revamp of the AWS Savings Plan Recommendations policy. In addition to the usual updates, the policy also now performs currency conversion where appropriate.
> 
> Note on currency conversion:
> 
> - The AWS API that produces the recommendations also includes a currency code. Conversion is done when this currency code does not match the currency code on the Flexera org. A statement in the incident details specifies the currency converted from, the currency converted to, and the exchange rate used. This should enable users to calculate the original unmodified values if desired.
> 
> From the CHANGELOG:
> 
> - Policy now automatically converts savings from USD to local currency when appropriate
> - Removed parameter to do the above manually via a user-specified exchange rate
> - Added exchange rate context to incident to allow user to derive unmodified USD values when needed
> - Several parameters altered to be more descriptive and intuitive to use
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
> 
> ### Link to Example Applied Policy
> 
> Due to the nature of the API request made in this policy, it cannot effectively be tested in our internal testing accounts. I have confirmed it works elsewhere and can provide a sample incident upon request.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-05 19:48:39 UTC
- **Merged At**: 2023-10-23 14:48:24 UTC
- **Modified Policies**: cost/aws/savings_plan/recommendations/aws_savings_plan_recommendations.pt

### PR [#1542](): fix bug in ds_currency check

#### Description

> ### Description
> 
> Fixed an issue where we would get an error on empty array for currency conversion check
> 
> ### Issues Resolved
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-12 22:48:37 UTC
- **Merged At**: 2023-10-13 17:51:33 UTC
- **Modified Policies**: cost/aws/reserved_instances/recommendations/aws_reserved_instance_recommendations.pt

### PR [#1513](): POL-912 Google Idle Cloud SQL Instance Recommender Revamp

#### Description

> ### Description
> 
> This is a revamp of the Google Idle Cloud SQL Instance Recommender policy. In addition to the usual updates, the policy also now performs currency conversion where appropriate, and also allows the user to take action (stop or delete) against idle resources.
> 
> From the CHANGELOG:
> 
> - Policy now requires a Flexera credential
> - Policy now converts savings to local currency when appropriate
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by project and by region via an allow list or a deny list
> - Added ability to filter resources by multiple label key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Added ability to stop or delete Cloud SQL instances from policy/incident
> - Streamlined code for better readability and faster execution
> - Added logic required for "Meta Policy" use-cases
> 
> ### Link to Example Applied Policy
> 
> Due to the nature of how Idle SQL recommendations are produced (only instances >30 days are even considered), it's difficult to produce an incident showing that the policy works as expected. Below is the link to a successful policy execution with no incident; you can view the logs and see that it did indeed find a valid Cloud SQL instance, but no recommendations for it:
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6527e673e947000001d932f6
> 
> Using a dummy entry to create a fake incident, I was also able to test actions successfully:
> 
> Org: 27018 (Flexera Customer One)
> Project: 116186 (Flexera-Sales)
> Stop Action: https://selfservice-4.rightscale.com/designer/processes/6527ea3980786a175ef1103e
> Delete Action: https://selfservice-4.rightscale.com/designer/processes/6527ed17cc383c4fce703066
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-03 20:56:56 UTC
- **Merged At**: 2023-10-13 15:45:41 UTC
- **Modified Policies**: cost/google/cloud_sql_idle_instance_recommendations/google_sql_idle_instance_recommendations.pt, cost/google/cloud_sql_idle_instance_recommendations/google_sql_idle_instance_recommendations_meta_parent.pt

### PR [#1532](): POL-844/POL-845 Azure Reserved Instances/Savings Plan Recommendations Revamp

#### Description

> ### Description
> 
> This is a revamp of the Azure Reserved Instances Recommendations and Savings Plan Recommendations policies. In addition to the usual updates, the policy also now performs currency conversion where appropriate.
> 
> Note on currency conversion for Reserved Instances Recommendations:
> 
> - The Azure API that produces the recommendations does *not* include a currency code. The currency code is found via a call to the Azure Billing API.
> - Conversion is done when the above currency code does not match the currency code on the Flexera org. A statement in the incident details specifies the currency converted from, the currency converted to, and the exchange rate used. This should enable users to calculate the original unmodified values if desired.
> 
> Note on currency conversion for Savings Plan Recommendations:
> 
> - The Azure API that produces the recommendations also includes a currency code. Conversion is done when this currency code does not match the currency code on the Flexera org. A statement in the incident details specifies the currency converted from, the currency converted to, and the exchange rate used. This should enable users to calculate the original unmodified values if desired.
> 
> Reserved Instances Recommendations CHANGELOG:
> 
> - Policy now automatically converts savings from USD to local currency when appropriate
> - Added exchange rate context to incident to allow user to derive unmodified USD values when needed
> - Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
> - Added ability to filter recommendations by region
> - Several parameters altered to be more descriptive and intuitive to use
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
> 
> Savings Plan Recommendations CHANGELOG:
> 
> - Policy now automatically converts savings from USD to local currency when appropriate
> - Added exchange rate context to incident to allow user to derive unmodified USD values when needed
> - Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
> - Several parameters altered to be more descriptive and intuitive to use
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
> 
> ### Link to Example Applied Policy
> 
> Due to the nature of the API request made in these policies, they cannot effectively be tested in our internal testing accounts. I have confirmed they work elsewhere and can provide sample incidents upon request.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-09 20:05:15 UTC
- **Merged At**: 2023-10-13 13:53:57 UTC
- **Modified Policies**: cost/azure/reserved_instances/recommendations/azure_reserved_instance_recommendations.pt, cost/azure/savings_plan/recommendations/azure_savings_plan_recommendations.pt

### PR [#1545](): POL-946 Azure Superseded Compute Instances - Fix Broken Link

#### Description

> ### Description
> 
> This fixes a broken link to the README in the incident description
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-13 13:02:52 UTC
- **Merged At**: 2023-10-13 13:44:15 UTC
- **Modified Policies**: cost/azure/superseded_instances/azure_superseded_instances.pt, cost/azure/superseded_instances/azure_superseded_instances_meta_parent.pt

### PR [#1543](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6507965609)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-10-13 12:05:10 UTC
- **Merged At**: 2023-10-13 12:13:02 UTC
- **Modified Policies**: cost/google/cud_recommendations/google_committed_use_discount_recommendations_meta_parent.pt

### PR [#1533](): POL-916 Google Committed Use Discount Recommender Revamp

#### Description

> ### Description
> 
> This is a revamp of the Google Committed Use Discount Recommender policy. In addition to the usual updates, the policy also now performs currency conversion where appropriate.
> 
> Note on currency conversion:
> 
> - The Google API that produces the recommendations also includes a currency code. Conversion is done when this currency code does not match the currency code on the Flexera org. A statement in the incident details specifies the currency converted from, the currency converted to, and the exchange rate used. This should enable users to calculate the original unmodified values if desired.
> 
> From the CHANGELOG:
> 
> - Policy now converts savings to local currency when appropriate
> - Added exchange rate context to incident to allow user to derive unmodified USD values when needed
> - Added ability to use Project list parameter as either an "allow" list or a "deny" list
> - Added ability to filter recommendations by region
> - Several parameters altered to be more descriptive and intuitive to use
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
> 
> ## Link to Example Applied Policy
> 
> Due to the nature of the API request made in this policy, it cannot effectively be tested in our internal testing accounts. I have confirmed it works elsewhere and can provide a sample incident upon request.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-10 20:29:59 UTC
- **Merged At**: 2023-10-13 12:04:33 UTC
- **Modified Policies**: cost/google/cud_recommendations/google_committed_use_discount_recommendations.pt, cost/google/cud_recommendations/google_committed_use_discount_recommendations_meta_parent.pt

### PR [#1540](): AWS Reserved Instances Recommendation Currency Conversion Fix

#### Description

> ### Description
> 
> Fixed issue where policy would fail to do proper currency conversion
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-12 15:40:54 UTC
- **Merged At**: 2023-10-12 15:42:20 UTC
- **Modified Policies**: cost/aws/reserved_instances/recommendations/aws_reserved_instance_recommendations.pt

### PR [#1520](): POL-837 AWS Reserved Instances Recommendations Revamp

#### Description

> ### Description
> 
> This is a revamp of the AWS Reserved Instances Recommendations policy. In addition to the usual updates, the policy also now performs currency conversion where appropriate.
> 
> Note on currency conversion:
> 
> - The AWS API that produces the recommendations also includes a currency code. Conversion is done when this currency code does not match the currency code on the Flexera org. A statement in the incident details specifies the currency converted from, the currency converted to, and the exchange rate used. This should enable users to calculate the original unmodified values if desired.
> 
> From the CHANGELOG:
> 
> - Policy now automatically converts savings from USD to local currency when appropriate
> - Removed parameter to do the above manually via a user-specified exchange rate
> - Added exchange rate context to incident to allow user to derive unmodified USD values when needed
> - Several parameters altered to be more descriptive and intuitive to use
> - `ElasticSearch` is now referred to as `OpenSearch` in keeping with current AWS naming conventions
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
> 
> ### Link to Example Applied Policy
> 
> Due to the nature of the API request made in this policy, it cannot effectively be tested in our internal testing accounts. I have confirmed it works elsewhere and can provide a sample incident upon request.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-05 14:34:33 UTC
- **Merged At**: 2023-10-12 13:53:04 UTC
- **Modified Policies**: cost/aws/reserved_instances/recommendations/aws_reserved_instance_recommendations.pt

### PR [#1537](): FOPTS-2261 Azure Long Running Instances - add OS incident field

#### Description

> ### Description
> 
> Customers would like to have operating system shown as an additional incident field.
> The policy already have this information, we need to expose it in the incident.
> 
> ### Issues Resolved
> 
> <!-- List any existing issues this PR resolves below -->
> [FOPTS-2261 Jira](https://flexera.atlassian.net/browse/FOPTS-2261)
> 
> ### Link to Example Applied Policy
> 
> [Azure Long Running Instances policy template Applied](https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=6526fc0155d35d0001a8213a)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-10-11 19:56:25 UTC
- **Merged At**: 2023-10-11 20:31:58 UTC
- **Modified Policies**: operational/azure/azure_long_running_instances/azure_long_running_instances.pt, operational/azure/azure_long_running_instances/azure_long_running_instances_meta_parent.pt

### PR [#1512](): POL-929 Google Rightsize VM Policy "Stop" Fix

#### Description

> ### Description
> 
> The ability to stop idle instances instead of deleting them was added late in the development of the revamp as a consequence of discovering that this is what Google recommends for idle VMs. As a result, some of the metadata and README information is inaccurate, as is a small part of the incident export.
> 
> ### Issues Resolved
> 
> The above issues are resolved.
> 
> ### Link to Example Applied Policy
> 
> Changes are marginal and mostly do not affect policy execution.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, small fixes
- **Created At**: 2023-10-03 12:34:39 UTC
- **Merged At**: 2023-10-11 14:26:42 UTC
- **Modified Policies**: cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations.pt, cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations_meta_parent.pt

### PR [#1530](): POL-940 Fix Pricing Info in AWS Rightsize EBS Volumes

#### Description

> ### Description
> 
> The policy was revamped with the assumption that the AWS Price List API would report hourly pricing for EBS volumes, similar to how it reports EC2 pricing. It turns out that this API reports monthly pricing, which means the math to convert it from hourly pricing resulted in highly inflated values.
> 
> ### Issues Resolved
> 
> The above described issue.
> 
> ### Link to Example Applied Policy
> 
> Tested in POC environment where problem was first discovered.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-09 18:42:32 UTC
- **Merged At**: 2023-10-09 18:51:32 UTC
- **Modified Policies**: cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing.pt, cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing_meta_parent.pt

### PR [#1508](): POL-914 Google Idle Persistent Disk Recommender Revamp

#### Description

> ### Description
> 
> This is a revamp of the Google Idle Persistent Disk Recommender policy. In addition to the usual updates, the policy also now performs currency conversion where appropriate.
> 
> From the CHANGELOG:
> 
> - Policy now requires a Flexera credential
> - Policy now converts savings to local currency when appropriate
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Removed ability to filter by zone; filtering by region is now supported
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by project and by region via an allow list or a deny list
> - Added ability to filter resources by multiple label key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Added logic required for "Meta Policy" use-cases
> 
> ### Link to Example Applied Policy
> 
> Due to the nature of Google Recommender service, the example policy running in our test environment does not produce an incident but can be viewed here:
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=651c054755d35d0001a80b14
> 
> The policy has been confirmed to work correctly and produce a valid and expected incident in a POC environment. I can provide the email of this incident upon request.
> 
> I've also successfully tested both the create snapshot and delete actions via a dummy entry added to produce a "fake" incident for a real resource in our GCP test environment.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-02 18:13:07 UTC
- **Merged At**: 2023-10-09 12:13:42 UTC
- **Modified Policies**: cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations.pt, cost/google/idle_persistent_disk_recommendations/google_idle_persistent_disk_recommendations_meta_parent.pt

### PR [#1522](): cheaper regions update

#### Description

> ### Description
> 
> added vendor type for Azure MCA CSP's
> 
> ### Issues Resolved
> 
> Was excluding this vendor type due to it not being included.
> 
> ### Link to Example Applied Policy
> 
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> https://app.flexera.com/orgs/34193/automation/applied-policies/projects/135696?policyId=650c7b21656c530001e17a92
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
> 
> ### Contribution Check List
> 
> - [x ] New functionality includes testing.
> - [x ] New functionality has been documented in the README if applicable
> - [x ] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: 
- **Created At**: 2023-10-05 16:40:58 UTC
- **Merged At**: 2023-10-09 12:13:14 UTC
- **Modified Policies**: cost/cheaper_regions/cheaper_regions.pt

### PR [#1524](): POL-937 Fix String bug in Azure AHUB Linux Policy

#### Description

> ### Description
> 
> This update fixes a bug where policy fails if an instance lacks Image Publisher metadata. The policy now verified that imagePublisher is a string before attempting to invoke the string method toLowerCase() on it.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=6520013a99745e0001587a3d
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-06 12:43:14 UTC
- **Merged At**: 2023-10-06 12:54:04 UTC
- **Modified Policies**: cost/azure/hybrid_use_benefit_linux/ahub_linux.pt, cost/azure/hybrid_use_benefit_linux/ahub_linux_meta_parent.pt

### PR [#1518](): fix: update filter to include Azure MCA

#### Description

> ### Description
> 
> Currently Azure Meta Parent policies will not include subscriptions under an Azure MCA due to the filter.  This updates the filter to use `substring` instead of `equal` for identifying Azure Subscriptions
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-04 15:32:50 UTC
- **Merged At**: 2023-10-04 20:39:34 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1515](): Google Meta Policy Parent Fix

#### Description

> ### Description
> 
> This fixes an issue with Google meta parent policies due to the vendor name in the Optima API being "GCP" instead of "Google"
#### Metadata

- **Labels**: READY-FOR-REVIEW, small fixes
- **Created At**: 2023-10-04 12:13:46 UTC
- **Merged At**: 2023-10-04 13:07:37 UTC
- **Modified Policies**: cost/google/idle_ip_address_recommendations/google_idle_ip_address_recommendations_meta_parent.pt, cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations_meta_parent.pt, tools/meta_parent_policy_compiler/google_meta_parent.pt.template

### PR [#1504](): POL-927 Azure China CBI - Add ability to choose specific billing month

#### Description

> ### Description
> 
> <!-- Describe what this change achieves below -->
> This is a change request for adding a parameter that gives the user the ability to specify a specific month to pull billing data for,. This is useful in the interest of retrieving historical data (i.e., billing data that is not the current month)
> 
> ### Issues Resolved
> 
> <!-- List any existing issues this PR resolves below -->
> 
> - Removed the `permission` declaration as it is deprecated. This fixes the issue which breaks the current policy if it is applied in a tenant from the Catalog.
> 
> ### Link to Example Applied Policy
> 
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
> ~Testing this in a customer tenant, will update when confirmed as working~ Can confirm this policy is working as expected in customer tenant
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [x] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW, small fixes
- **Created At**: 2023-09-28 15:54:56 UTC
- **Merged At**: 2023-10-04 13:03:29 UTC
- **Modified Policies**: cost/azure/azure_china_cbi/azure_china_cbi.pt

### PR [#1511](): FOPTS-1503 Added new cost dimensions for savings calculations

#### Description

> ### Description
> 
> The following dimensions were added to the average cost per hour calculation:
> 
> - operating_system
> - database_engine
> - database_edition
> - license_model
> - deployment_option
> 
> In addition, the way of obtaining the costs per hour for each type of instance was changed. Previously, all possible combinations of instances were obtained, obtaining a cost for each combination of instance_type and region (for example, if we have 100 different instances_type and 15 regions, we would obtain 1500 average costs, even though many were not necessary according to the records obtained from the API). By adding the 5 new dimensions, this approach becomes impractical, since it would increase exponentially for each combination of operating system, database engine, database edition, etc.
> 
> So it was decided to use a map with a key composed of
> ` instance_type---region---operating_system---database_engine---database_edition---license_model---deployment_option`
> to filter the cost records obtained from the API that match that combination, to subsequently calculate the average cost per hour of the records with purchase_option = "On demand" and thus calculate the estimated savings of the records of the other purchase_option (Reserved, Savings Plan, Spot)
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/FOPTS-1503
> 
> ### Link to Example Applied Policy
> 
> [Applied Policy](https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=651b7ebe66636500010089eb)
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-10-02 19:15:08 UTC
- **Merged At**: 2023-10-03 23:18:31 UTC
- **Modified Policies**: cost/aws/savings_realized/aws_savings_realized.pt

### PR [#1506](): POL-915 Google Rightsize VM Recommender Revamp

#### Description

> ### Description
> 
> This is a revamp of the Google Rightsize VM Recommender policy. The policy now reports both idle and underutilized resources and allows the user to take appropriate action on both incidents. The policy also now performs currency conversion where appropriate.
> 
> Note: A "Stop" action is also provided in addition to a "Delete" action for idle VMs. This is because Google's own recommendation is to stop the instance. The user can still opt to select a "Delete" action instead if preferred.
> 
> From the CHANGELOG:
> 
> - Policy now requires a Flexera credential
> - Policy now converts savings to local currency when appropriate
> - Policy now reports on both underutilized and idle instances
> - Downsize action can now be taken on underutilized instances
> - Stop action can now be taken on idle instances
> - Delete action can now be taken on idle instances
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Removed ability to filter by zone; filtering by region is now supported
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by project and by region via an allow list or a deny list
> - Added ability to filter resources by multiple label key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Added logic required for "Meta Policy" use-cases
> 
> ### Link to Example Applied Policy
> 
> Idle: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=651ac7b56393710001c7d630
> Underutilized: https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=651ac814ac11110001c8f329
> 
> All actions (stop, resize, delete) have been tested successfully.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-29 12:58:11 UTC
- **Merged At**: 2023-10-02 18:15:28 UTC
- **Modified Policies**: cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations.pt, cost/google/rightsize_vm_recommendations/google_rightsize_vm_recommendations_meta_parent.pt

### PR [#1502](): POL-926 Deprecate Superseded Instances Policy

#### Description

> ### Description
> 
> This policy only supports AWS and Azure, which both now have cloud-specific versions of this policy with much more functionality. This PR deprecates the old cloud-neutral version of the policy and directs users to the new policies in the associated README.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-28 14:44:44 UTC
- **Merged At**: 2023-10-02 18:14:39 UTC
- **Modified Policies**: cost/superseded_instance/superseded_instance.pt

### PR [#1501](): POL-925 AWS Policies: Update Service Metadata from EC2 to Compute

#### Description

> ### Description
> 
> Our AWS policies are inconsistent; some specify the Service in their info block as "Compute", and some say "EC2". This PR updates all of them to "Compute" for consistency and to ensure that any scraped incident data is properly categorized alongside their equivalents in Azure/GCP/etc.
> 
> ### Link to Example Applied Policy
> 
> Changes are purely to metadata and should not impact policy execution at all.
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-28 14:26:49 UTC
- **Merged At**: 2023-10-02 18:14:11 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1492](): POL-830 AWS Rightsize EBS Volumes Revamp

#### Description

> ### Description
> 
> This is a revamp of the AWS Rightsize EBS Volumes policy that adds new functionality and meta policy support. The most notable changes are:
> 
> - The API calls to CloudWatch, and subsequent calculations for IOPS percentage, were removed because they had no bearing on the recommendations produced and simply added unnecessary permissions requirements for the user.
> - The ability to action on resources directly from the incident has been added. This functionality has been successfully tested.
> 
> From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by multiple tag key:value pairs
> - Added ability to take automated actions to upgrade GP2 volumes to GP3
> - Added additional context to incident description
> - Removed unneeded `IOPS Average %` and `Lookback Period` fields from incident export
> - Removed unneeded API calls to CloudWatch
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Policy no longer raises new escalations if statistics or savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65157f936a972a0001e5269f
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-25 18:54:39 UTC
- **Merged At**: 2023-10-02 18:13:57 UTC
- **Modified Policies**: cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing.pt, cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing_meta_parent.pt

### PR [#1497](): POL-913 Google Idle IP Address Recommender Revamp / Google Meta Policy Automation

#### Description

> ### Description
> 
> This is a revamp of the Google Idle IP Address Recommender policy. The most notable change is that the policy will now convert the savings reported by Google to the Flexera org's currency when appropriate.
> 
> From the CHANGELOG:
> 
> - Policy now requires a Flexera credential
> - Policy now converts savings to local currency when appropriate
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by project and by region via an allow list or a deny list
> - Added ability to filter resources by multiple label key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> - Added logic required for "Meta Policy" use-cases
> 
> Additionally, this pull request also contains changes to our scripting for generating meta policies so that they can be generated for Google policies in a style very similar to what is done for Azure. 
> 
> ### Link to Example Applied Policy
> 
> While we do have a test environment for GCP, recommendations can take some time to actually be generated. I have tested this policy in a client environment and verified it works as expected and can provide the incident it produced upon request.
> 
> An example of the policy running in a test environment without error, but not raising an incident, can be found here:
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65171b69ac11110001c8ed3d
> 
> (I have also tested the CWF by modifying the policy temporarily to report on IP addresses that have no recommendations. The delete action works as expected)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-27 18:17:09 UTC
- **Merged At**: 2023-09-29 20:09:51 UTC
- **Modified Policies**: cost/google/idle_ip_address_recommendations/google_idle_ip_address_recommendations.pt, cost/google/idle_ip_address_recommendations/google_idle_ip_address_recommendations_meta_parent.pt, tools/meta_parent_policy_compiler/google_meta_parent.pt.template

### PR [#1498](): FOPTS-1858 Azure Savings Realized fails for customers with no RI coverage

#### Description

> ### Description
> 
> Azure Savings Realized policy is failing for customer with no RI coverage.
> 
> The failure happens on attempt to access an element of an empty array 
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/FOPTS-1858
> 
> ### Link to Example Applied Policy
> 
> Applied policy with report length 0
> https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=651482604e39ab00016cbf71
> 
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [ ] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-09-27 20:44:08 UTC
- **Merged At**: 2023-09-28 16:16:05 UTC
- **Modified Policies**: cost/azure/savings_realized/azure_savings_realized.pt

### PR [#1483](): POL-923 Azure Superseded Compute Instances

#### Description

> ### Description
> 
> This is a new Azure-specific version of the Superseded Instances policy. This policy requires an Azure credential with permissions similar to the Azure Rightsizing Compute Instances policy, but offers several advantages over the cloud-agnostic version:
> 
> - Completely updated/rebuilt code based on the updated versions of other usage reduction policies with similar functionality where appropriate
> - Since instance metadata is mostly pulled from Azure itself, any instances that are actioned should no longer appear in future incidents since their instance type will no longer be superseded and the policy is gathering this metadata in near real time from the Azure API directly
> - Savings information is included based on Azure list prices for instance types with currency conversion (similar to AWS Unused IP policy)
> - Policy metadata and incident output have been normalized for scraping into the Optimization dashboard
> - Added ability to action on recommendations directly from the incident
> - Meta policy support
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65157a55656c530001e1902a
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-21 17:13:37 UTC
- **Merged At**: 2023-09-28 14:07:39 UTC
- **Modified Policies**: cost/azure/superseded_instances/azure_superseded_instances.pt, cost/azure/superseded_instances/azure_superseded_instances_meta_parent.pt

### PR [#1481](): POL-922 AWS Superseded EC2 Instances

#### Description

> ### Description
> 
> This is a new AWS-specific version of the Superseded Instances policy. This policy requires an AWS credential with permissions similar to the AWS Rightsizing EC2 Instances policy, but offers several advantages over the cloud-agnostic version:
> 
> - Completely updated/rebuilt code based on the updated versions of other usage reduction policies with similar functionality where appropriate
> - Since instance metadata is mostly pulled from AWS itself, any instances that are actioned should no longer appear in future incidents since their instance type will no longer be superseded and the policy is gathering this metadata in near real time from the AWS API directly
> - Savings information is included based on AWS list prices for instance types with currency conversion (similar to AWS Unused IP policy)
> - Policy metadata and incident output have been normalized for scraping into the Optimization dashboard
> - Added ability to action on recommendations directly from the incident
> - Meta policy support
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=651577db656c530001e19023
> (CWF action has been tested and works. The list price/savings calculation also works, but there is no account that we can test in to provide this information because the instances were created today. I've confirmed elsewhere that it does work as expected though.)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-20 20:43:13 UTC
- **Merged At**: 2023-09-28 14:07:24 UTC
- **Modified Policies**: cost/aws/superseded_instances/aws_superseded_instances.pt, cost/aws/superseded_instances/aws_superseded_instances_meta_parent.pt

### PR [#1494](): FOPTS-2108 Rework Low Account Usage Policy Optimization

#### Description

> ### Description
> 
> The policy template can be optimized to reduce evaluation time. We're still getting a timeout happening.
> 
> ### Issues Resolved
> 
> Policy template code is reviewed and optimized to improve performance. More code was removed with same functionality.
> 
> ### Link to Example Applied Policy
> 
> - Low Account Usage Policy: https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=651328286a972a0001e51857
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, DO-NOT-MERGE, READY-FOR-REVIEW
- **Created At**: 2023-09-26 15:59:54 UTC
- **Merged At**: 2023-09-27 21:26:19 UTC
- **Modified Policies**: cost/low_account_usage/low_account_usage.pt

### PR [#1495](): FOPTS-1899 Turbonomic Rightsize Virtual Machines Recommendations do not have "resourceType" incident field

#### Description

> ### Description
> 
> Turbonomic Rightsize Virtual Machines Recommendations for all three cloud providers now have resourceType incident field
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/FOPTS-1899
> 
> ### Link to Example Applied Policy
> 
> https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=6513e37dd80db500016d6d2a
> https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=6513e1e74e39ab00016cbf66
> https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=6513d79b4e39ab00016cbf64
> 
> <img width="635" alt="image" src="https://github.com/flexera-public/policy_templates/assets/22282464/4063c3ab-d578-4040-8214-fc974e9a6368">
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-09-27 15:22:22 UTC
- **Merged At**: 2023-09-27 15:33:25 UTC
- **Modified Policies**: cost/turbonomics/scale_virtual_machines_recommendations/aws/turbonomics_scale_virtual_machines.pt, cost/turbonomics/scale_virtual_machines_recommendations/azure/turbonomics_scale_virtual_machines.pt, cost/turbonomics/scale_virtual_machines_recommendations/gcp/turbonomics_scale_virtual_machines.pt

### PR [#1477](): POL-921 Add Region Filtering to Azure Rightsizing Compute

#### Description

> ### Description
> 
> This non-breaking update adds the ability to filter by region, similar to other Azure usage reduction policies. 
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=6509ac05656c530001e1762e
> (Parameter is set to only allow instances in the eastus region, and this is reflected in the incident)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-19 14:20:30 UTC
- **Merged At**: 2023-09-26 14:37:49 UTC
- **Modified Policies**: cost/azure/rightsize_compute_instances/azure_compute_rightsizing.pt, cost/azure/rightsize_compute_instances/azure_compute_rightsizing_meta_parent.pt

### PR [#1486](): POL-924 Oracle Cloud CBI Broken Upload Fix

#### Description

> ### Description
> 
> If a file upload were to fail for some reason, such as the policy engine running out of memory or a network issue, that individual file would remain in an "in-progress" status indefinitely. This would result in the policy never being able to successfully commit the bill upload as a whole, resulting in the policy stalling out.
> 
> This is a fix for the issue. If such a broken file upload is found, the policy will simply abort the bill upload and create a new one, starting the entire process over.
> 
> ### Link to Example Applied Policy
> 
> This policy has been tested in a client environment that was experiencing the issue this update fixes and has been confirmed to work as expected.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] ~New functionality has been documented in the README if applicable~ (Not applicable)
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-22 13:45:45 UTC
- **Merged At**: 2023-09-22 15:42:23 UTC
- **Modified Policies**: cost/oracle/oracle_cbi/oracle_cbi.pt

### PR [#1487](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6275728146)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-09-22 14:26:00 UTC
- **Merged At**: 2023-09-22 14:47:56 UTC
- **Modified Policies**: operational/azure/azure_long_running_instances/azure_long_running_instances_meta_parent.pt

### PR [#1476](): POL-920 Azure Unused Volumes Read/Write Metrics Support

#### Description

> ### Description
> 
> The Azure Unused Volumes policy has been updated to consider read/write metrics when determining if a volume is unused, similar to the AWS version of the policy. The user can configure how far back to look at these metrics and whether or not to report on attached volumes in the resulting incident. Please see the README for more details.
> 
> New functionality has been thoroughly tested, including the Cloud Workflow to detach a volume from an attached instance before deleting it.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65099dd36a972a0001e50c56
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-19 13:20:30 UTC
- **Merged At**: 2023-09-22 14:44:42 UTC
- **Modified Policies**: cost/azure/unused_volumes/azure_unused_volumes.pt, cost/azure/unused_volumes/azure_unused_volumes_meta_parent.pt

### PR [#1466](): POL-919 Azure Long Running Instances Revamp

#### Description

> ### Description
> 
> This is a revamp of the Azure Long Running Instances policy that adds new functionality and meta policy support. From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to filter resources by multiple tag key:value pairs
> - Added several fields to incident export to provide additional context
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Policy no longer raises new escalations for the same resource if incidental metadata has changed
> - Streamlined code for better readability and faster execution
> - Policy now requires a valid Flexera credential
> - Added logic required for "Meta Policy" use-cases
> 
> ### Link to Example Applied Policy
> 
> The new functionality depends too much on valid Optima data to be easily tested in our internal environments. I've confirmed the policy works as expected in the customer environment that is primarily the driver for these changes.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-18 13:11:55 UTC
- **Merged At**: 2023-09-22 14:25:23 UTC
- **Modified Policies**: operational/azure/azure_long_running_instances/azure_long_running_instances.pt, operational/azure/azure_long_running_instances/azure_long_running_instances_meta_parent.pt

### PR [#1479](): POL-910 AWS Rightsize EBS Volumes - Remove GP3 Recommendations and Empty Recommendations

#### Description

> ### Description
> 
> <!-- Describe what this change achieves below -->
> - Reintroduced logic to filter out gp3 volumes from recommendations
> - Changed data for policy incident to ensure a policy incident is not created when there are no recommendations
> 
> ### Issues Resolved
> 
> <!-- List any existing issues this PR resolves below -->
> - Fixes issue with policy where $0 recommendations are returned for gp3 volumes, which are currently not supported for recommendations.
> - Fixes issue with policy where some child policies have a single recommendation, and that recommendation is completely empty. This was caused by the 'message' field in the data, which is passed even if there are no recommendations.
> 
> ### Link to Example Applied Policy
> 
> <!-- URL to the Applied Policy that was used for dev/testing below -->
> <!-- This can be helpful for a reviewer to validate the changes proposed resulted in the expected behavior. If you do not have access or ability to apply the policy template, please mention this in your PR description.-->
> SE NAM Architects Sandbox - https://app.flexera.com/orgs/32567/automation/applied-policies/projects/133743?policyId=650c09516a972a0001e51044 (example of policy returning 1 GP2 volume recommendation and filtering out GP3 volumes)
> SE Sandbox EU - https://app.flexera.com/orgs/30105/automation/applied-policies/projects/133807?policyId=650c0a2c3a1bb50001990323 (example of policy returning no recommendations)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [x] ~New functionality has been documented in the README if applicable~
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, small fixes
- **Created At**: 2023-09-20 10:16:33 UTC
- **Merged At**: 2023-09-22 12:14:15 UTC
- **Modified Policies**: cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing.pt, cost/aws/rightsize_ebs_volumes/aws_volumes_rightsizing_meta_parent.pt

### PR [#1453](): POL-911 AWS Long Running Instances Revamp

#### Description

> ### Description
> 
> This is a revamp of the AWS Long Running Instances policy that adds new functionality and meta policy support. From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added ability to filter resources by multiple tag key:value pairs
> - Added several fields to incident export to provide additional context
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Policy no longer raises new escalations for the same resource if incidental metadata has changed
> - Streamlined code for better readability and faster execution
> - Added logic required for "Meta Policy" use-cases
> - Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases
> 
> ### Link to Example Applied Policy
> 
> The new functionality depends too much on valid Optima data to be easily tested in our internal environments. I've confirmed the policy works as expected in the customer environment that is primarily the driver for these changes.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-08 19:07:36 UTC
- **Merged At**: 2023-09-21 19:40:20 UTC
- **Modified Policies**: operational/aws/long_running_instances/long_running_instances.pt, operational/aws/long_running_instances/long_running_instances_meta_parent.pt

### PR [#1460](): FOPTS-1815 Low Account Usage Policy optimization

#### Description

> ### Description
> 
> The policy template can be optimized to reduce evaluation time. Currently there's a timeout happening.
> 
> ### Issues Resolved
> 
> Policy template code is reviewed and optimized to improve performance.
> 
> ### Link to Example Applied Policy
> 
> - Low Account Usage Policy: https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=650245280105d50001c4d17e
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-09-13 23:42:21 UTC
- **Merged At**: 2023-09-19 13:30:39 UTC
- **Modified Policies**: cost/low_account_usage/low_account_usage.pt

### PR [#1474](): Azure AHUB Linux README Link Fix

#### Description

> ### Description
> 
> Fixes erroneous README link in the metadata for the Azure AHUB Linux policy.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-19 12:07:53 UTC
- **Merged At**: 2023-09-19 12:50:24 UTC
- **Modified Policies**: cost/azure/hybrid_use_benefit_linux/ahub_linux.pt, cost/azure/hybrid_use_benefit_linux/ahub_linux_meta_parent.pt

### PR [#1463](): fix: Refactor Azure Unused Volume and Unused IP Actions

#### Description

> ### Description
> 
> - Refactored the `Delete Volume` and `Create Snapshot`, and `Delete IP Address` Actions to use updated Azure APIs, improve debugging, and error handling
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/27018/automation/applied-policies/projects/116186?policyId=650304aa3a1bb5000199025d
> 
> Tested actions with single volume, multiple volumes, and volumes that have delete locks (expect error)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: bug
- **Created At**: 2023-09-14 13:36:57 UTC
- **Merged At**: 2023-09-18 19:26:42 UTC
- **Modified Policies**: cost/azure/unused_ip_addresses/azure_unused_ip_addresses.pt, cost/azure/unused_ip_addresses/azure_unused_ip_addresses_meta_parent.pt, cost/azure/unused_volumes/azure_unused_volumes.pt, cost/azure/unused_volumes/azure_unused_volumes_meta_parent.pt

### PR [#1370](): POL-749 Azure Hybrid Use Benefit for Windows/Linux Server Revamp

#### Description

> ### Description
> 
> This is a revamp of the Azure Hybrid Use Benefit for Windows Server policy as part of the general audit on usage and rate reduction policies. In addition to the usual updates to match functionality to the other revamped policies, the policy also now reports savings and has metadata to facilitate scraping into the optimization dashboard.
> 
> (Changes unrelated to reporting savings were also ported to the Azure Hybrid Use Benefit for Linux Server since the effort to do so was minimal. Additional discovery will be needed to determine if and how we can calculate AHUB savings for RHEL or SLES VMs.)
> 
> From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
> - Added ability to filter resources by region
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added estimated savings to incident export
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65049d696a972a0001e50559
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-07-21 17:08:54 UTC
- **Merged At**: 2023-09-18 16:15:30 UTC
- **Modified Policies**: cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit.pt, cost/azure/hybrid_use_benefit/azure_hybrid_use_benefit_meta_parent.pt, cost/azure/hybrid_use_benefit_linux/ahub_linux.pt, cost/azure/hybrid_use_benefit_linux/ahub_linux_meta_parent.pt

### PR [#1455](): POL-840 Azure Rightsize SQL Databases Revamp 

#### Description

> ### Description
> 
> This is a revamp of the Azure Rightsize SQL Databases policy as part of the general audit on usage and rate reduction policies. In order to have parity with the Azure Rightsize Compute policy, and to avoid duplicate recommendations, this policy now reports on both unused and underutilized SQL databases via distinct incidents. A parameter allows the user, if desired, to report on only unused or only underutilized instances, retaining existing functionality.
> 
> The policy now also offers savings estimates for rightsizing opportunities. For underutilized resources, the cost of the instance is divided by the current capacity of the instance and then multiplied by the recommended capacity of the instance to determine the new cost if the instance were downsized. This is then subtracted from the current cost of the resource to determine the savings. This works because pricing for Azure SQL databases is straightforwardly a multiple of the capacity assigned to it within a given tier. For example, a Standard instance with a capacity of 50 costs 5x what a Standard instance with a capacity of 10 costs. 
> 
> From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added potential savings to recommendations
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added incident for unused instances based on lack of connections
> - Added ability to delete unused instances
> - Added ability to configure how many days back to consider when determining if instance is unused or underutilized
> - Added ability to filter resources by multiple tag key:value pairs
> - Added ability to filter resources by region
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if statistics or savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=650069e66a972a0001e4fae6
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=65006a676a972a0001e4fae8
> 
> Note: Both downsize and delete actions have been tested successfully. Cost data has been confirmed to work as well, but this data is not meaningfully available in our Flexera Services test account. CPU average data is also working but reports as 0 in the incident because the average CPU usage for this instance is 0.004032258064516129, which rounds down to 0 when reducing it to 2 decimal points. This can be confirmed by viewing the applied policy log.
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-11 20:34:22 UTC
- **Merged At**: 2023-09-18 14:16:01 UTC
- **Modified Policies**: cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances.pt, cost/azure/rightsize_sql_instances/azure_rightsize_sql_instances_meta_parent.pt

### PR [#1464](): FOPTS-1816 Handle updating applied and aggregated policies

#### Description

> ### Description
> 
> - Bug fix: Previously this policy could only update applied policies (policies added using the Automation > Templates panel) but no aggregated policies like those executed from the Automation > Catalog, now this was fixed and the policy can work with both.
> 
> ### Issues Resolved
> 
> - https://flexera.atlassian.net/browse/FOPTS-1816
> 
> ### Link to Example Applied Policy
> 
> - Applied policy: https://app.flexera.com/orgs/33749/automation/applied-policies/projects/135147?policyId=65038359656c530001e16708
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: bug, READY-FOR-REVIEW, small fixes
- **Created At**: 2023-09-14 22:11:13 UTC
- **Merged At**: 2023-09-15 12:46:02 UTC
- **Modified Policies**: cost/turbonomics/credential_refresh/turbonomic_cred_refresh.pt

### PR [#1447](): FOPTS-1338 Turbonomic Buy RI (Azure) - Bring recommendation supporting information

#### Description

> ### Description
> 
> Azure Buy RI policy needs to show the following information: projected RI utilization and RI coverage, system details URL.
> 
> ### Issues Resolved
> 
> [FOPTS-1338](https://flexera.atlassian.net/browse/FOPTS-1338)
> 
> ### Link to Example Applied Policy
> 
> [Turbonomic Buy Reserved Instances Recommendations Azure - Policy Temp Applied](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/107982?policyId=64ff45527bfcbf0001712076)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-09-05 08:06:43 UTC
- **Merged At**: 2023-09-12 19:15:58 UTC
- **Modified Policies**: cost/turbonomics/buy_reserved_instances_recommendations/azure/turbonomics_buy_reserved_instances.pt

### PR [#1454](): FOPTS-1336 Turbonomic Buy RI (AWS)

#### Description

> ### Description
> 
> AWS Buy RI policy needs to show the following information: projected RI utilization and RI coverage, system details URL.
> 
> ### Issues Resolved
> 
> Added all requested fields and normalized incident fields.
> 
> ### Link to Example Applied Policy
> 
> - Turbonomic Buy Reserved Instances Recommendations AWS: https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=64ffa022beb3db00016c2e1e
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-09-11 15:42:05 UTC
- **Merged At**: 2023-09-12 19:14:32 UTC
- **Modified Policies**: cost/turbonomics/buy_reserved_instances_recommendations/aws/turbonomics_buy_reserved_instances.pt

### PR [#1405](): POL-841 Azure Old Snapshots Revamp

#### Description

> ### Description
> 
> This is a revamp of the Azure Old Snapshots policy as part of the general audit on usage and rate reduction policies. The changes to this policy are roughly analogous to the changes made to the AWS version, using the same code and verbiage where appropriate. From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Policy no longer raises new escalations if snapshot age or savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64f8bff1656c530001e15926
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-08-16 18:37:15 UTC
- **Merged At**: 2023-09-12 13:48:06 UTC
- **Modified Policies**: cost/azure/old_snapshots/azure_delete_old_snapshots.pt, cost/azure/old_snapshots/azure_delete_old_snapshots_meta_parent.pt

### PR [#1436](): FOPTS-1332 Turbonomic Rightsize VMs (GCP) 

#### Description

> ### Description
> 
> GCP Rightsize VMs policy needs to show the following information: RI coverage before/after, VM age, uptime, vCPU capacity before/after, vCPU utilization before/after, Memory capacity before/after, memory utilization before/after, storage throughput capacity before/after, storage throughput utilization before/after, NET throughput capacity and utilization before/after, system details URL.
> 
> ### Issues Resolved
> 
> Added all requested fields and normalized incident fields.
> 
> ### Link to Example Applied Policy
> 
> GCP Turbonomic Rightsize VMs: https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=64ef88ee01dad60001bfe702
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-08-30 18:23:36 UTC
- **Merged At**: 2023-09-06 21:22:47 UTC
- **Modified Policies**: cost/turbonomics/scale_virtual_machines_recommendations/gcp/turbonomics_scale_virtual_machines.pt

### PR [#1448](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/6087831707)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-09-05 17:28:12 UTC
- **Merged At**: 2023-09-05 18:31:54 UTC
- **Modified Policies**: cost/azure/idle_compute_instances/azure_idle_compute_instances_meta_parent.pt

### PR [#1443](): FOPTS-1542 Azure Idle Compute Instances - incident and recommendations showing error for tags

#### Description

> ### Description
> 
> Was added a step to parse the tags received using the Azure API to an array of tags
> 
> ### Issues Resolved
> 
> GUI was unable to parse a map of tags, so now the policy sends an array of tags with format ["key=value"]
> 
> ### Link to Example Applied Policy
> 
> [Applied Policy](https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=64f13e7a4b956f0001f2b4f9)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-09-01 15:58:12 UTC
- **Merged At**: 2023-09-05 17:27:32 UTC
- **Modified Policies**: cost/azure/idle_compute_instances/azure_idle_compute_instances.pt

### PR [#1441](): Azure Unused Volumes Revamp

#### Description

> ### Description
> 
> This is a revamp of the Azure Unused Volumes policy as part of the general audit on usage and rate reduction policies. The changes to this policy are roughly analogous to the changes made to the AWS version, using the same code and verbiage where appropriate. From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Removed ability to filter by how long a policy was detached; see README* for more details
> - Added ability to filter by volume age
> - Added ability to only report recommendations that meet a minimum savings threshold
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Policy no longer raises new escalations if ages or savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> 
> From the README:
> 
> Note: Previous versions of this policy had the option to filter results by how long a volume was detached. This functionality did not work as expected due to Azure volume logs not recording detachment events. Such events are recorded in the logs of the VM the volume was detached from, and there is currently no way to determine the most recently attached VM for a volume through Azure's APIs. For this reason, this functionality was removed.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64f1e85e2d830e000134f7ec
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-09-01 13:45:37 UTC
- **Merged At**: 2023-09-01 14:29:09 UTC
- **Modified Policies**: cost/azure/unused_volumes/azure_unused_volumes.pt, cost/azure/unused_volumes/azure_unused_volumes_meta_parent.pt

### PR [#1433](): FOPTS-1330 Turbonomic Rightsize VMs (AWS)

#### Description

> ### Description
> 
> AWS Rightsize VMs policy needs to show the following information: RI coverage before/after, VM age, uptime, vCPU capacity before/after, vCPU utilization before/after, Memory capacity before/after, memory utilization before/after, storage throughput capacity before/after, storage throughput utilization before/after, NET throughput capacity and utilization before/after, system details URL.
> 
> ### Issues Resolved
> 
> Added all requested fields and normalized incident fields.
> 
> ### Link to Example Applied Policy
> 
> - AWS Turbonomic Rightsize VMs: https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=64ee5c5c01dad60001bfe6e7
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-08-26 03:04:55 UTC
- **Merged At**: 2023-08-30 16:42:43 UTC
- **Modified Policies**: cost/turbonomics/scale_virtual_machines_recommendations/aws/turbonomics_scale_virtual_machines.pt

### PR [#1398](): FOPTS-1335 Turbonomic Rightsize DBs (GCP) - Bring recommendation supporting information

#### Description

> ### Description
> 
> GCP Rightsize DBs policy needs to show the following information: VM age, uptime, vCPU capacity before/after, vCPU utilization before/after, Memory capacity before/after, memory utilization before/after, IOPs capacity and utilization before/after, disk capacity and utilization before/after, connection capacity and utilization before/after, system details URL.
> 
> ### Issues Resolved
> 
> [FOPTS-1335](https://flexera.atlassian.net/browse/FOPTS-1335)
> 
> ### Link to Example Applied Policy
> 
> [Turbonomic Rightsize Databases Recommendations GCP Policy Template Applied](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/107982?policyId=64d5f7ef53379b0001babd41)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-08-11 09:15:36 UTC
- **Merged At**: 2023-08-29 20:46:18 UTC
- **Modified Policies**: cost/turbonomics/rightsize_databases_recommendations/gcp/turbonomics_rightsize_databases_recommendations.pt

### PR [#1419](): FOPTS-1331 Turbonomic Rightsize VMs (Azure) - Bring recommendation supporting information

#### Description

> ### Description
> 
> Azure Rightsize VMs policy needs to show the following information: RI coverage before/after, VM age, uptime, vCPU capacity before/after, vCPU utilization before/after, Memory capacity before/after, memory utilization before/after, storage throughput capacity before/after, storage throughput utilization before/after, NET throughput capacity and utilization before/after, system details URL.
> 
> ### Issues Resolved
> 
> [FOPTS-1331](https://flexera.atlassian.net/browse/FOPTS-1331)
> 
> ### Link to Example Applied Policy
> 
> [Turbonomic Rightsize Virtual Machines Recommendations Azure - Policy Template Applied](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/107982?policyId=64e6ee9953379b0001babe53)
> 
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-08-24 06:13:12 UTC
- **Merged At**: 2023-08-29 20:15:55 UTC
- **Modified Policies**: cost/turbonomics/scale_virtual_machines_recommendations/azure/turbonomics_scale_virtual_machines.pt

### PR [#1431](): FOPTS-1632 Fix the broken link for the README for Schedule ITAM Report policy

#### Description

> ### Description
> 
> The link of the README for Schedule ITAM Report policy was fixed and now it redirects to the actual README page.
> 
> ### Issues Resolved
> 
> - https://flexera.atlassian.net/browse/FOPTS-1632
> 
> ### Link to Example Applied Policy
> 
> No changes were done to policy code, only the version number and description were updated, here's a proof that the policy still compiles:
> - https://app.flexeratest.com/orgs/1105/automation/projects/107982/policy-templates/64e79d7032d8b40001fa4ef9
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, small fixes, documentation
- **Created At**: 2023-08-24 18:16:46 UTC
- **Merged At**: 2023-08-24 18:24:38 UTC
- **Modified Policies**: operational/itam/schedule_itam_report/schedule-itam-report.pt

### PR [#1428](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/5966769960)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-08-24 17:08:42 UTC
- **Merged At**: 2023-08-24 17:10:26 UTC
- **Modified Policies**: cost/aws/unused_ip_addresses/aws_unused_ip_addresses_meta_parent.pt

### PR [#1424](): POL-906 - fix: conditional request for currency conversion

#### Description

> ### Description
> 
> Fixes issue on Currency Conversion API getting too many requests by mitigating the number of requests.  The policy template does not need to make a request to Currency Conversion API when sticking to the USD currency.  This change makes the request to currency conversion API conditional, dependent if the target currency is USD or not.
> 
> ### Issues Resolved
> 
> https://flexera.atlassian.net/browse/POL-906
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64e788fb2d830e000134de6b
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: bug, READY-FOR-REVIEW, small fixes
- **Created At**: 2023-08-24 16:45:46 UTC
- **Merged At**: 2023-08-24 17:08:10 UTC
- **Modified Policies**: cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt

### PR [#1421](): Update Meta Parent Policy Templates

#### Description

> Update Meta Parent Policy Templates from GitHub Actions Workflow [Generate Meta Parent Policy Templates](https://github.com/flexera-public/policy_templates/actions/runs/5964734368)
#### Metadata

- **Labels**: automation
- **Created At**: 2023-08-24 14:00:51 UTC
- **Merged At**: 2023-08-24 16:50:05 UTC
- **Modified Policies**: cost/aws/old_snapshots/aws_delete_old_snapshots_meta_parent.pt

### PR [#1420](): Fix AWS Old Snapshots Version #

#### Description

> This is a simple fix to bump the version number for the AWS Old Snapshots policy. A fix was recently merged but the version number in the policy was not changed. It is now bumped to 7.2 to match the CHANGELOG.
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-08-24 13:47:10 UTC
- **Merged At**: 2023-08-24 14:00:15 UTC
- **Modified Policies**: cost/aws/old_snapshots/aws_delete_old_snapshots.pt

### PR [#1406](): FOPTS-1584 Turbonomic Right size DBs ( Azure ) Need to add request to check Price Model

#### Description

> ### Description
> 
> Turbonomic Right size DBs ( Azure ) Need to add request to check Price Model
> 
> ### Issues Resolved
> 
> [FOPTS-1584](https://flexera.atlassian.net/browse/FOPTS-1584)
> 
> ### Link to Example Applied Policy
> 
> [Turbonomic Rightsize Databases Recommendations Azure - Applied Policy Template](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/107982?policyId=64dd5dc17dac9c0001ef8aff)
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-08-16 23:58:43 UTC
- **Merged At**: 2023-08-24 05:56:09 UTC
- **Modified Policies**: cost/turbonomics/rightsize_databases_recommendations/azure/turbonomics_rightsize_databases_recommendations.pt

### PR [#1415](): POL-905 Update policy_sync.pt to use Github instead of S3

#### Description

> ### Description
> 
> I updated the repository to use Github instead of S3 to publish the policy templates.
> 
> ### Issues Resolved
> 
> - https://flexera.atlassian.net/browse/POL-905
> 
> ### Link to Example Applied Policy
> 
> N/A
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, repo_maintenance, automation
- **Created At**: 2023-08-23 20:45:45 UTC
- **Merged At**: 2023-08-23 20:56:08 UTC
- **Modified Policies**: tools/policy_sync/policy_sync.pt

### PR [#1414](): POL-906: fix `ds_describe_snapshots` tag collect

#### Description

> ### Description
> 
> Fixes issue related to tags not appearing as expected in the resulting incident.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/34608/automation/incidents/projects/136331?incidentId=64e629a96e42ff00014b3c74
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: small fixes
- **Created At**: 2023-08-23 15:50:27 UTC
- **Merged At**: 2023-08-23 18:07:31 UTC
- **Modified Policies**: cost/aws/old_snapshots/aws_delete_old_snapshots.pt

### PR [#1402](): FOPTS-1578 Allow Retrieving Recommendations "per cluster"

#### Description

> ### Description
> 
> As a user I want to be able to configure Kubecost Request Rightsizing Recommendations policy to request recommendations per-cluster or overall, so that I can insure that the responses do not violate limits set up in my environment.
> 
> If per cluster mode is configured, policy will discover clusters, iterate the clusters and request recommendations for each one.
> 
> ### Issues Resolved
> 
> - https://flexera.atlassian.net/browse/FOPTS-1578
> 
> ### Link to Example Applied Policy
> 
> Per cluster: https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/107982?policyId=64dbaaf453379b0001babd96
> Overall: https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/107982?policyId=64dbab4453379b0001babd97
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW, READY FOR APPROVAL, javascript
- **Created At**: 2023-08-15 17:28:11 UTC
- **Merged At**: 2023-08-23 14:41:42 UTC
- **Modified Policies**: cost/kubecost/sizing/kubecost_resizing_recommendation.pt

### PR [#1410](): POL-904 Fixes for AWS Unused IP Policy

#### Description

> ### Description
> 
> This PR fixes two issues with the AWS Unused IPs policy, described below.
> 
> ### Issues Resolved
> 
> - Corrected issue where attached IP addresses were being included in the incident
> - Added logic to ensure policy still completes even if the Flexera currency conversion API is unresponsive
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64e37f112d830e000134c70f
> 
> (Note: Above policy has no incident, but you can view the log and see that it elegantly handles filtering of attached IPs now and doesn't fail simply because the Flexera currency conversion API returned a 502 response)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable (N/A since functionality is unchanged)
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-08-21 15:20:57 UTC
- **Merged At**: 2023-08-21 16:32:14 UTC
- **Modified Policies**: cost/aws/unused_ip_addresses/aws_unused_ip_addresses.pt, cost/aws/unused_ip_addresses/aws_unused_ip_addresses_meta_parent.pt

### PR [#1408](): POL-903 Fixed Cost Data Issue with New Azure APIs

#### Description

> ### Description
> 
> The casing and naming conventions of some dimensions, such as the Service field, are different between the old method of ingesting Azure bills and the new method. For example, “Microsoft.Compute” is now “microsoft.compute”. This update enables our cost optimization policies to pull this data regardless of casing.
> 
> https://flexera.atlassian.net/browse/POL-903
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64e35fc94b956f0001f2864f
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64e3694f2d830e000134c702
> 
> (Note: Since this is a test environment, the savings in the incident will be $0. This is just to demonstrate that the updated Optima API call itself works and does not result in any errors. I have also confirmed that this change works as expected in a client org that I was developing for, which is where I discovered the issue to begin with.)
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in CHANGELOG.MD
> - (No README changes since this is just a bug fix. The policy still works the same from a user POV)
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-08-21 13:33:19 UTC
- **Merged At**: 2023-08-21 14:59:36 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1397](): FOPTS-1328 Turbonomic Rightsize Volumes (Azure)

#### Description

> ### Description
> 
> Azure Rightsize Volumes policy needs to show the following information: current and new storage access IOPs, current and new storage amount, VM volume is attached to, action nature: disruptive or not, reversible or not, current and new throughput capacity, IOPs utilization, disk utilization, throughput utilization, system details URL.
> 
> ### Issues Resolved
> 
> Added all requested fields and normalized incident fields.
> 
> ### Link to Example Applied Policy
> 
> - Azure Turbonomic Rightsize Volumes: https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/60073?policyId=64d50e5e53379b0001babd32
> 
> ### Contribution Check List
> 
> - [x] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-08-10 16:32:29 UTC
- **Merged At**: 2023-08-16 21:36:05 UTC
- **Modified Policies**: cost/turbonomics/rightsize_virtual_volumes_recommendations/azure/turbonomics_rightsize_virtual_volumes_recommendations.pt

### PR [#1404](): POL-842 Azure Unused IPs Revamp

#### Description

> ### Description
> 
> This is a revamp of the Azure Unused IPs policy as part of the general audit on usage and rate reduction policies. The changes to this policy are roughly analogous to the changes made to the AWS version, using the same code and verbiage where appropriate. From the CHANGELOG:
> 
> - Several parameters altered to be more descriptive and human-readable
> - Removed deprecated "Log to CM Audit Entries" parameter
> - Added ability to specify how long an IP address should be unattached to consider it unused
> - Added ability to filter resources by multiple tag key:value pairs
> - Added additional context to incident description
> - Normalized incident export to be consistent with other policies
> - Added human-readable recommendation to incident export
> - Added additional fields to incident export to facilitate scraping for dashboards
> - Policy no longer raises new escalations if savings data changed but nothing else has
> - Streamlined code for better readability and faster execution
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64dd0fd9126883000167d514
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-08-16 18:10:48 UTC
- **Merged At**: 2023-08-16 19:04:31 UTC
- **Modified Policies**: cost/azure/unused_ip_addresses/azure_unused_ip_addresses.pt, cost/azure/unused_ip_addresses/azure_unused_ip_addresses_meta_parent.pt

### PR [#1400](): FOPTS-1329 Turbonomic Rightsize Volumes (GCP)

#### Description

> ### Description
> 
> GCP Rightsize Volumes is not supported on Turbonomic yet.
> 
> ### Issues Resolved
> 
> Unpublished policy from catalog since Turbonomic Rightsize Volumes does not support Google provider yet.
> 
> ### Link to Example Applied Policy
> 
> N/A
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [x] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: enhancement, READY-FOR-REVIEW
- **Created At**: 2023-08-14 15:01:30 UTC
- **Merged At**: 2023-08-16 17:26:39 UTC
- **Modified Policies**: cost/turbonomics/rightsize_virtual_volumes_recommendations/gcp/turbonomics_rightsize_virtual_volumes_recommendations.pt

### PR [#1401](): Support Tag Filtering For Key Without Value ("*" Support)

#### Description

> ### Description
> 
> This adds the ability to filter by key:* on the AWS usage reduction policies to support use cases where the user doesn't enforce a particular value and just needs to filter by the presence of a particular key.
> 
> This also fixes an issue that prevent tag values from being read properly from AWS volumes. This issue actually existed before the recent revamp as well, but has now been fixed.
> 
> Meta policies have also been regenerated, but this only changes the description of the exclusion tags parameter and should have no impact on existing applied meta policies.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64da83b2126883000167cdd3
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64da848b1c05c900018b65df
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64da850e126883000167cdd6
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64da8855126883000167cde1
> https://app.flexera.com/orgs/6/automation/applied-policies/projects/7954?policyId=64da888e126883000167cde2
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-08-14 16:51:24 UTC
- **Merged At**: 2023-08-14 21:14:00 UTC
- **Modified Policies**: > 10 policies modified. Please review the [PR on Github]() for the full list.

### PR [#1394](): FOPTS-1333 Turbonomic Rightsize DBs (AWS) - Bring recommendation supporting information

#### Description

> ### Description
> 
> AWS Rightsize DBs policy needs to show the following information: VM age, uptime, vCPU capacity before/after, vCPU utilization before/after, Memory capacity before/after, memory utilization before/after, IOPs capacity and utilization before/after, disk capacity and utilization before/after, connection capacity and utilization before/after, system details URL.
> 
> ### Issues Resolved
> 
> [FOPTS-1333](https://flexera.atlassian.net/browse/FOPTS-1333)
> 
> ### Link to Example Applied Policy
> [Turbonomic Rightsize Databases Recommendations AWS Policy Template Applied ](https://app.flexeratest.com/orgs/1105/automation/applied-policies/projects/107982?policyId=64d1884d85ab670001ff6d64)
> 
> 
> ### Contribution Check List
> 
> - [ ] New functionality includes testing.
> - [ ] New functionality has been documented in the README if applicable
> - [ ] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW, READY FOR APPROVAL
- **Created At**: 2023-08-08 00:48:48 UTC
- **Merged At**: 2023-08-09 12:23:41 UTC
- **Modified Policies**: cost/turbonomics/rightsize_databases_recommendations/aws/turbonomics_rightsize_databases_recommendations.pt

### PR [#1396](): POL-899 Use New API for AWS RBD Policy

#### Description

> ### Description
> 
> This is a modification of the AWS RBD from Tags policy to use the new API for getting AWS accounts and their tags. This eliminates the need for an AWS credential at all, and also eliminates any concerns around a credential not having access to all of the accounts.
> 
> ### Link to Example Applied Policy
> 
> https://app.flexera.com/orgs/1105/automation/applied-policies/projects/60073?policyId=64d288ce126883000167b558
> 
> ### Contribution Check List
> 
> - [X] New functionality includes testing.
> - [X] New functionality has been documented in the README if applicable
> - [X] New functionality has been documented in CHANGELOG.MD
#### Metadata

- **Labels**: READY-FOR-REVIEW
- **Created At**: 2023-08-08 18:29:12 UTC
- **Merged At**: 2023-08-08 18:45:41 UTC
- **Modified Policies**: automation/aws/aws_rbd_from_tag/aws_rbd_from_tag.pt

