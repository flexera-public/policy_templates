# AWS Resources Under or Approaching Extended Support

## What It Does

This policy template uses the AWS APIs (RDS, EKS, and ElastiCache) to identify all resources running versions covered by AWS Extended Support. Extended support start and end dates are determined using the static reference data file at `data/aws/aws_extended_support_dates.json`. Resource-level billing data from the Flexera CCO platform is used to obtain actual extended support costs for resources already incurring those charges. These resources are outdated and AWS charges an extended support fee for continued use. A report is produced containing a list of these resources, and optionally, an email is sent with this report.

**NOTE: This policy template is scoped to extended support *costs*, not maintenance or security posture. It should not be used to determine when a resource stops receiving security updates and bug fixes. Extended support includes critical CVE patches, but individual minor and patch versions reach end of support on their own schedules (often earlier than the major version) so a resource may stop receiving patches well before the dates listed here. For RDS, Aurora, and ElastiCache the template keys on major versions, because AWS offers extended support only at the major version level and bills accordingly. EKS is keyed on Kubernetes minor versions (e.g. 1.31), which is the granularity at which AWS defines the EKS support lifecycle.**

**NOTE: AWS does not maintain a single authoritative source for extended support dates. They are published across per-service release calendars, pricing pages, and What's New announcements, and these sources can disagree; an announcement may change a date weeks before the corresponding calendar is updated. AWS also revises published dates, sometimes extending them by years. The dates in this template are a best-effort consolidation of first-party AWS sources as of the last update and may lag changes on AWS's side.**

## How It Works

- The policy queries the AWS APIs (RDS, EKS, and ElastiCache) across all opted-in regions to enumerate all running resources.
- Region values shown in incidents and exports are reported using AWS API region identifiers (for example, `us-east-1`) for consistency with other AWS optimization policy sets.
- Each discovered resource's version is matched against the reference data file at `data/aws/aws_extended_support_dates.json` to determine if it is currently under extended support or will enter extended support within the number of days specified by the `Days Until Extended Support` parameter.
- For RDS, only `mysql` and `postgres` engine versions are eligible for AWS Extended Support and are checked by this policy. `mariadb` is not eligible for RDS Extended Support and is not reported by this policy.
- For ElastiCache, resources are matched by engine and major version only (for example, all `redis 6.x` patch versions match the `6` reference entry). Only `redis` major versions `4`, `5`, and `6` are currently covered by Extended Support reference data; other engines (such as `valkey`) or newer major versions are not reported.
- RDS Multi-AZ instances are billed for extended support on both the primary and standby instance, so this policy doubles the estimated vCPU count for Multi-AZ instances when calculating estimated savings.
- The policy also pulls resource-level billing data from the Flexera CCO platform from 3 days ago, filtered to resources with a `Usage Type` that contains `ExtendedSupport`. This data is used only for obtaining actual costs for resources already incurring extended support charges. Data from 3 days ago is used to ensure that we have available, processed billing data to search through.

### Data Sources

Extended support dates and pricing in the `data/aws/aws_extended_support_dates.json` reference data file are sourced from official AWS documentation:

- [Amazon RDS for MySQL major version release calendar](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.VersionMgmt.html)
- [Amazon RDS for PostgreSQL release calendar](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-release-calendar.html)
- [Amazon RDS Extended Support overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html)
- [Versions with Amazon RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-versions.html)
- [Amazon RDS for MySQL pricing (Extended Support rates)](https://aws.amazon.com/rds/mysql/pricing/)
- [Amazon RDS for PostgreSQL pricing (Extended Support rates)](https://aws.amazon.com/rds/postgresql/pricing/)
- [Amazon Aurora MySQL release calendars](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.release-calendars.html)
- [Amazon Aurora PostgreSQL release calendars](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/aurorapostgresql-release-calendar.html)
- [Amazon RDS Extended Support with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-overview.html)
- [Amazon Aurora Extended Support rates](https://aws.amazon.com/rds/aurora/pricing/)
- [Amazon EKS Kubernetes version lifecycle and release calendar](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html)
- [Amazon EKS pricing](https://aws.amazon.com/eks/pricing/)
- [Amazon ElastiCache Extended Support](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/extended-support.html)
- [Versions with ElastiCache Extended Support](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/extended-support-versions.html)
- [Amazon ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/)

### Policy Savings Details

The policy includes the estimated monthly savings. The estimated monthly savings is recognized if the resource is migrated to a newer supported version, avoiding the extended support fee.

The `Estimated Monthly Savings` is calculated differently depending on whether the resource is currently under extended support or approaching it:

- For resources **currently under extended support**: the policy first attempts to match the resource against Flexera CCO billing data. If a match is found, the `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month. This reflects the actual extended support fee currently being charged. If no CCO match is found (e.g., due to billing data lag), the estimated rate below is used as a fallback where possible.
  - Since actual costs for resources currently under extended support are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- For resources **approaching extended support** (when the `Days Until Extended Support` parameter is greater than 0), or for resources currently under extended support with no CCO match, `Estimated Monthly Savings` is calculated using the AWS published extended support rates and resource-level data collected from the AWS APIs. AWS Extended Support pricing is tiered: a lower rate applies for the first 2 years, then a higher rate applies starting in year 3. The policy automatically selects the correct tier based on the current date and each engine version's published year-3 start date.
  - **RDS**: `Rate per vCPU-hour x estimated vCPU count x 24 hours x 30.44 days`. Reference rates (US East, N. Virginia; vary by region): `$0.10/vCPU-hour` for years 1-2, `$0.20/vCPU-hour` starting in year 3. The vCPU count is estimated from the instance class (e.g. `db.m5.xlarge` -> 4 vCPUs) and is doubled for Multi-AZ instances, since AWS bills extended support for both the primary and standby instance.
  - **EKS**: `$0.60 per cluster-hour x 24 hours x 30.44 days` (~$438/mo per cluster).
  - **ElastiCache**: AWS prices ElastiCache Extended Support as a percentage premium on the node's on-demand hourly rate (80% for years 1-2, 160% starting in year 3), rather than a flat node-hour fee. Because this policy does not have access to the node's base on-demand rate, no dollar estimate can be produced for ElastiCache resources that lack a Flexera CCO cost match. In that case, `Estimated Monthly Savings` is reported as 0 and the recommendation notes that the estimate is unavailable; actual extended support charges will still appear in Flexera CCO billing data once incurred.
- The `Rate Tier` field in the incident export indicates which pricing tier (years 1-2 or year 3) applies to each resource, or the flat EKS cluster-hour rate.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy template has the following input parameters:

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Account Number* - Leave blank; this is for automated use with Meta Policies. See README for more details.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation. Only applies to resources currently under extended support.
- *Days Until Extended Support* - Report resources that will enter extended support within this many days. Set to 0 to only report resources currently under extended support. Uses static reference data for RDS, EKS, and ElastiCache extended support schedules.
- *Billing Center List* - List of Billing Center names or IDs you want to report on. Leave blank to report on resources in all Billing Centers.
- *Allow/Deny AWS Accounts* - Whether to treat `Allow/Deny AWS Accounts List` parameter as allow or deny list. Has no effect if `Allow/Deny AWS Accounts List` is left empty.
- *Allow/Deny AWS Accounts List* - A list of allowed or denied AWS Account IDs/names. Leave blank to check all AWS Accounts.
- *Allow/Deny Regions* - Whether to treat `Allow/Deny Regions List` parameter as allow or deny list. Has no effect if `Allow/Deny Regions List` is left empty.
- *Allow/Deny Regions List* - A list of allowed or denied regions. Regions can be entered in shorthand format, such as `us-east-2`. Leave blank to check all AWS regions.
- *Exclusion Tags* - Cloud native tags to ignore resources that you don't want to produce recommendations for. Enter the Key name to filter resources with a specific Key, regardless of Value, and enter Key==Value to filter resources with a specific Key:Value pair. Other operators and regex are supported; please see the README for more details.
- *Exclusion Tags: Any / All* - Whether to filter resources containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email. Set to '0' to not show an incident table at all, and '100000' to include all results. Does not impact attached CSV files or the incident as presented in Flexera One.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**AWS Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#aws) (*provider=aws*) which has the following permissions:
  - `ec2:DescribeRegions`
  - `rds:DescribeDBInstances`
  - `rds:ListTagsForResource`
  - `eks:ListClusters`
  - `eks:DescribeCluster`
  - `elasticache:DescribeCacheClusters`
  - `elasticache:ListTagsForResource`

  Example IAM Permission Policy:

  ```json
  {
      "Version": "2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "ec2:DescribeRegions",
                  "rds:DescribeDBInstances",
                  "rds:ListTagsForResource",
                  "eks:ListClusters",
                  "eks:DescribeCluster",
                  "elasticache:DescribeCacheClusters",
                  "elasticache:ListTagsForResource"
              ],
              "Resource": "*"
          }
      ]
  }
  ```

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This policy template does not incur any cloud costs.
