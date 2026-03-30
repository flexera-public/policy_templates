# Google Rightsize Persistent Disks

## What It Does

This policy template identifies Google persistent disks that are either unused (unattached) or underutilized, and generates recommendations accordingly. Unused disks — those that have not been attached to an instance for a user-specified number of days — are recommended for deletion. Underutilized disks — those attached to a VM but consuming only a small fraction of the disk type's available IOPS or throughput capacity — are recommended for downgrade to a lower-cost disk type (e.g., `pd-ssd` → `pd-balanced` → `pd-standard`).

NOTE: Estimated savings will only appear if you are using [Google Detailed Billing](https://docs.flexera.com/flexera-one/administration/cloud-settings/bill-data-connections/bill-connect-configurations/google/) to ingest Google Cloud costs into Flexera CCO. If you have not configured Flexera One to ingest detailed billing information from Google, please do so before using this policy template. Alternatively, use the [Google Idle Persistent Disk Recommender](https://github.com/flexera-public/policy_templates/tree/master/cost/google/idle_persistent_disk_recommendations) policy template, which uses the Google Recommender service rather than Flexera.

## How It Works

### Unused Disks

A persistent disk is considered unused if it has no attached VM instances (`users` field is empty) and has been detached for at least the number of days configured in the *Days Unattached* parameter. If that parameter is set to 0, all unattached disks are considered unused regardless of detachment duration.

### Underutilized Disks

The policy queries Google Cloud Monitoring for disk I/O metrics over the configured lookback period:

- **Read IOPS** (`compute.googleapis.com/disk/read_ops_count`)
- **Write IOPS** (`compute.googleapis.com/disk/write_ops_count`)
- **Read Throughput** (`compute.googleapis.com/disk/read_bytes_count`)
- **Write Throughput** (`compute.googleapis.com/disk/write_bytes_count`)

Total IOPS (read + write) and total throughput (read + write) utilization are calculated as a percentage of the disk type's maximum provisioned performance for the disk's size. A disk is considered underutilized when the utilization falls below the configured threshold for the selected statistic (Average, Maximum, p99, p95, or p90).

If a disk is underutilized, the policy identifies the lowest-cost disk type (`pd-standard` < `pd-balanced` < `pd-ssd`) that can still fully accommodate the observed peak I/O workload, and recommends downgrading to that type. Only `pd-ssd` and `pd-balanced` disks are candidates for downgrade; `pd-standard` disks are already the lowest tier. `pd-extreme` and Hyperdisk types are not included in rightsizing recommendations due to their provisioned-IOPS billing model.

The disk performance limits used for utilization calculations are based on [Google Cloud persistent disk documentation](https://docs.cloud.google.com/compute/docs/disks/performance):

| Disk Type | Max IOPS (combined read+write) | Max Throughput |
| --- | --- | --- |
| `pd-standard` | 0.75 read IOPS/GB (max 3,000) + 1.5 write IOPS/GB (max 15,000) | 0.12 MB/s/GB (max 180 MB/s) |
| `pd-balanced` | 6 IOPS/GB (max 80,000) | 0.28 MB/s/GB (max 240 MB/s) |
| `pd-ssd` | 30 IOPS/GB (max 100,000) | 0.48 MB/s/GB (max 480 MB/s) |

> **Note:** Google Cloud Monitoring only records disk I/O metrics when a disk is actively used by a running VM. Disks attached to stopped VMs will show zero utilization during the periods the VM was stopped. If VMs in your environment are frequently stopped, consider this when interpreting rightsizing recommendations.

### Policy Savings Details

The policy includes the estimated monthly savings for both recommendation types.

**Unused disks:** The estimated monthly savings is recognized if the unused disk is deleted.

- The `Estimated Monthly Savings` is calculated by multiplying the amortized cost of the resource for 1 day, as found within Flexera CCO, by 30.44, which is the average number of days in a month.
- Since the costs of individual resources are obtained from Flexera CCO, they will take into account any Flexera adjustment rules or cloud provider discounts present in the Flexera platform.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.

**Underutilized disks:** The estimated monthly savings is recognized if the disk is downgraded to the recommended type.

- The `Estimated Monthly Savings` is calculated by applying the pricing ratio between the current and recommended disk types to the actual Flexera CCO cost. The pricing ratio is based on approximate Google Cloud list prices (us-central1) for each disk type per GB/month: `pd-standard` ≈ $0.040, `pd-balanced` ≈ $0.100, `pd-ssd` ≈ $0.170.
- Since the base cost is taken from Flexera CCO, the savings estimate already accounts for any Flexera adjustment rules or cloud provider discounts.
- If the resource cannot be found in Flexera CCO, the `Estimated Monthly Savings` is 0.
- The incident message detail includes the sum of each resource `Estimated Monthly Savings` as `Potential Monthly Savings`.
- Both `Estimated Monthly Savings` and `Potential Monthly Savings` will be reported in the currency of the Flexera organization the policy is applied in.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Minimum Savings Threshold* - Minimum potential savings required to generate a recommendation.
- *Days Unattached* - The number of days a disk needs to be detached to be considered unused. If this value is set to 0, all unattached disks will be considered unused.
- *Statistic Lookback Period* - How many days back to look at Cloud Monitoring data when assessing disk utilization. Maximum is 42 days (6 weeks).
- *Threshold Statistic* - The statistic to use when comparing disk utilization to the threshold. Applies to both IOPS and throughput checks. Options: Average, Maximum, p99, p95, p90.
- *IOPS Threshold (%)* - The IOPS utilization threshold (as a percentage of the disk type maximum) below which a disk is considered underutilized for rightsizing. Set to -1 to disable IOPS-based rightsizing recommendations.
- *Throughput Threshold (%)* - The throughput utilization threshold (as a percentage of the disk type maximum) below which a disk is considered underutilized for rightsizing. Set to -1 to disable throughput-based rightsizing recommendations.
- *Allow/Deny Projects* - Whether to treat *Allow/Deny Projects List* as an allow or deny list. Has no effect if the list is empty.
- *Allow/Deny Projects List* - Filter results by project ID/name, either only allowing this list or denying it depending on the above parameter. Leave blank to consider all projects.
- *Ignore System Projects* - Whether or not to automatically ignore system projects (projects whose ID begins with `sys-`).
- *Ignore Google Apps Script Projects* - Whether or not to automatically ignore Google Apps Script projects (projects whose ID begins with `app-`).
- *Allow/Deny Regions* - Whether to treat *Allow/Deny Regions List* as an allow or deny list. Has no effect if the list is empty.
- *Allow/Deny Regions List* - Filter results by region, either only allowing this list or denying it depending on the above parameter. Leave blank to consider all regions.
- *Exclusion Labels* - The policy will filter resources containing the specified labels from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified label key.
  - `Key==Value` - Filter all resources with the specified label key:value pair.
  - `Key!=Value` - Filter all resources missing the specified label key:value pair. This will also filter all resources missing the specified label key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified label key.
- *Exclusion Labels: Any / All* - Whether to filter instances containing any of the specified labels or only those that contain all of them. Only applicable if more than one value is entered in the *Exclusion Labels* field.
- *Create Final Snapshot* - Whether or not to take a final snapshot before deleting an unused disk.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).
- *Attach CSV To Incident Email* - Whether or not to attach the results as a CSV file to the incident email.
- *Incident Table Rows for Email Body (#)* - The number of results to include in the incident table in the incident email.

Please note that the "Automatic Actions" parameter contains a list of action(s) that can be performed on the resources. When it is selected, the policy template will automatically execute the corresponding action on the data that failed the checks, post incident generation. Please leave this parameter blank for *manual* action.
For example if a user selects the "Delete Unused Disks" action while applying the policy template, all unused persistent disks that satisfy the criteria will be deleted.

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report
- Delete unused persistent disks after approval (with optional final snapshot)

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#google) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`
  - `compute.zones.list`
  - `compute.disks.list`
  - `monitoring.timeSeries.list`
  - `compute.disks.createSnapshot`*
  - `compute.disks.delete`*

  \* Only required for taking action (deletion with optional snapshot); the policy will still function in a read-only capacity without these permissions.

- [**Flexera Credential**](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials#flexera) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for meta-policy self-termination; not required if not using the meta parent of this policy template.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera-one/automation/automation-administration/managing-credentials-for-policy-access-to-external-systems/provider-specific-credentials) page in the docs has detailed instructions for setting up Credentials for the most common providers.

Additionally, this policy template requires that the following APIs be enabled in your Google Cloud environment:

- [Cloud Resource Manager API](https://console.cloud.google.com/flows/enableapi?apiid=cloudresourcemanager.googleapis.com)
- [Compute Engine API](https://console.cloud.google.com/flows/enableapi?apiid=compute.googleapis.com)
- [Cloud Monitoring API](https://console.cloud.google.com/flows/enableapi?apiid=monitoring.googleapis.com)

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
