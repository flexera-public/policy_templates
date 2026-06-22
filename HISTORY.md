# Published Policy Change History

## Description

This document contains the last 100 policy template merges for the `flexera-public/policy_templates` repository. Only merges that modify policy templates are included. Changes are sorted by the date the pull request was merged into the `master` branch, with the most recent changes listed first. A [JSON version](https://github.com/flexera-public/policy_templates/blob/master/data/change_history/change_history.json) with the full history all merges, not just the last 100 policy merges, is also available.

## History

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

### PR [#4281](https://github.com/flexera-public/policy_templates/pull/4281): POL-1747 Meta Parent Fixes

#### Description

> Fixes the meta parent templates with the following:
>
> - Refactored `js_take_in_parameters` to solve multiple bugs, including one that prevented the meta parent from deleting child policy templates.
> - Added pagination support to `﻿ds_get_existing_policies`; without this, a meta parent could have issues in cases where 1000+ child policies are returned.
>

#### Metadata

- **Policies**: Not displayed due to PR with > 5 policies. Please see [Github Pull Request](https://github.com/flexera-public/policy_templates/pull/4281) for these details.
- **Merged At**: 2026-04-07 17:02:39 UTC

---

### PR [#4270](https://github.com/flexera-public/policy_templates/pull/4270): POL-1740 Vendor Spend Commitment Forecast: Longer Date Range Support

*Minor Update*

#### Description

> Updates the `Vendor Spend Commitment Forecast` policy template to support longer data ranges by making multiple API calls to the costs/aggregated endpoint as needed.
>
> Also makes a minor tweak to the `policy_summary_template_missing_policy_name?` Dangerfile test to avoid false positives.
>

#### Metadata

- **Policies**: [Vendor Spend Commitment Forecast](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/forecasting/commitment_forecast/README.md)
- **Merged At**: 2026-04-07 12:15:50 UTC

---

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

