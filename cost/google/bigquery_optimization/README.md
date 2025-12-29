# Google BigQuery Optimization

## What It Does

This policy template analyzes Google BigQuery tables and identifies compute and storage optimization opportunities to reduce costs and improve performance. It implements 11 best practice checks from Google Cloud's official documentation, providing actionable recommendations for optimizing BigQuery resources.

## How It Works

The policy template performs comprehensive analysis across 11 optimization categories:

1. **Long-term Storage Optimization**: Identifies tables with data older than the specified threshold (default 90 days) that can be moved to cheaper long-term storage, reducing storage costs by 50%

2. **Partitioning Recommendations**: Detects large unpartitioned tables (above the minimum size threshold) and recommends adding partitioning to improve query performance and reduce compute costs. **With query statistics**: Calculates actual savings based on query patterns. **Without query statistics**: Provides conservative estimates.

3. **Clustering Optimization**: Identifies large tables without clustering that could benefit from clustering to optimize query performance. **With query statistics**: Calculates actual savings. **Without query statistics**: Provides recommendations only.

4. **Table Expiration Policies**: Flags tables without expiration settings that may accumulate unnecessary data over time. Estimates future costs based on table growth rate.

5. **Time Travel Optimization**: Detects tables where time travel storage exceeds 50% of total size and recommends optimizing retention settings (conservative 30% reduction estimate)

6. **Large Table Review**: Highlights very large tables (>100 GB) that may benefit from manual review and optimization strategies

7. **View Optimization**: Identifies views using `SELECT *` without `EXCEPT` clauses, which prevents column pruning and increases query costs. **With query statistics**: Calculates actual savings. **Without query statistics**: Provides conservative estimates.

8. **Partition Expiration Settings**: Checks partitioned tables for missing partition-level expiration policies to automatically remove old partitions

9. **Date-Sharded Table Detection**: Scans for tables with date suffixes (e.g., `table_20250101`, `table_2025_01_01`) and recommends migrating to time-partitioned tables for better performance. **With query statistics**: Calculates compute overhead savings.

10. **Table Oversharding Detection**: Identifies datasets with 10+ tables sharing the same base name and recommends consolidating into a single partitioned table

11. **Primary/Foreign Key Constraints**: Analyzes table schemas to identify potential key columns without constraints, which can help the query optimizer improve performance

### Analysis Process

1. **Retrieves BigQuery Metadata**: Collects information about BigQuery projects, datasets, and tables
2. **Gathers Storage Details**: Fetches detailed storage metrics including active vs. long-term storage usage, physical storage, time travel data, and table schemas
3. **Analyzes Query Patterns**: Queries INFORMATION_SCHEMA.JOBS to get actual query statistics per table (queries per month, bytes processed, slot utilization)
4. **Cost Analysis**: Calculates current storage costs and potential savings based on BigQuery pricing and actual or estimated query patterns
5. **Pattern Detection**: Groups tables by dataset to detect sharding patterns and naming conventions
6. **Schema Analysis**: Examines table schemas for optimization opportunities
7. **Generates Recommendations**: Provides prioritized recommendations with calculated or estimated cost savings and confidence levels

### Confidence Levels

The policy provides three confidence levels for savings estimates:

- **HIGH CONFIDENCE**: Calculations based on actual query statistics from INFORMATION_SCHEMA.JOBS (requires query lookback period data)
- **MEDIUM CONFIDENCE**: Calculations based on table metadata and conservative industry estimates (30% reduction factors)
- **LOW CONFIDENCE**: Estimates based on assumptions about query patterns when no query data is available

### Conservative Reduction Factors

To ensure realistic savings estimates, the policy uses conservative reduction factors based on industry best practices:

- **Partitioning**: 70% reduction in bytes scanned (conservative; can be 80-95% in practice)
- **Clustering**: 25% reduction in bytes scanned (conservative; can be 30-60% in practice)
- **View Column Pruning**: 35% of columns typically unused (conservative estimate)
- **Time Travel Optimization**: 30% storage reduction with optimized retention
- **Date-Sharding Overhead**: 15% query performance improvement when consolidating

Source: [Google Cloud BigQuery Best Practices](https://cloud.google.com/bigquery/docs/best-practices-performance-compute)

### Storage Cost Analysis

The policy calculates potential savings based on BigQuery's storage pricing tiers:

- **Active Storage**: $0.02 per GB per month
- **Long-term Storage**: $0.01 per GB per month (after 90 days)
- **Physical Storage**: $0.04 per GB per month (for time travel and other features)
- **Analysis (on-demand)**: $6.25 per TB processed

### Policy Savings Details

The policy includes estimated monthly savings calculations where applicable:

**Recommendations with Calculated Savings (HIGH CONFIDENCE):**
- **Long-term Storage Migration**: Exact calculation based on pricing difference between active ($0.02/GB) and long-term ($0.01/GB) storage
- **Partitioning/Clustering** (with query data): Based on actual query patterns, bytes processed, and query frequency
- **View Optimization** (with query data): Based on actual query patterns and schema analysis
- **Date-Sharded Tables** (with query data): Based on actual query overhead and compute costs

**Recommendations with Estimated Savings (MEDIUM CONFIDENCE):**
- **Time Travel Optimization**: Estimated 30% reduction in time travel storage costs
- **Table Expiration**: Projected future costs based on observed growth rate

**Recommendations with Estimated Savings (LOW CONFIDENCE):**
- **Partitioning/Clustering** (without query data): Conservative estimates based on table size and assumed query frequency
- **View Optimization** (without query data): Conservative estimates based on schema analysis and assumed query frequency

**Recommendations without Direct Cost Savings (Performance Improvements):**
- Oversharding detection recommendations improve management overhead and query planning efficiency
- Primary/Foreign key constraints improve query performance but don't have direct storage costs

Savings estimates are based on current BigQuery pricing and may vary based on your specific billing arrangements.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - A list of email addresses to notify
- *Minimum Savings Threshold* - Minimum potential monthly savings required to generate a recommendation (default: $0)
- *Long-Term Storage Threshold (Days)* - Number of days since last modification to consider moving data to long-term storage (default: 90 days)
- *Minimum Table Size for Partitioning (GB)* - Minimum table size in GB to recommend partitioning optimizations (default: 1 GB)
- *Query Analysis Lookback Period (Days)* - Number of days to analyze historical query patterns for accurate savings calculations (1-180 days, default: 30 days). Longer periods provide more stable averages but increase analysis time.
- *Allow/Deny Projects* - Whether to treat Allow/Deny Projects List parameter as allow or deny list. Has no effect if Allow/Deny Projects List is left empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all projects.
- *Ignore System Projects* - Whether or not to automatically ignore system projects e.g. projects whose id begins with `sys-`
- *Ignore Google Apps Script Projects* - Whether or not to automatically ignore Google Apps Script projects e.g. projects whose id begins with `app-`

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report with detailed optimization recommendations and cost savings estimates

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `bigquery.datasets.get`
  - `bigquery.tables.get`
  - `bigquery.tables.list`
  - `bigquery.jobs.listAll` (required for query statistics analysis)
  - `bigquery.jobs.get` (required for query statistics analysis)

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this Policy Template requires that the following APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [BigQuery API](https://console.cloud.google.com/flows/enableapi?apiid=bigquery.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
