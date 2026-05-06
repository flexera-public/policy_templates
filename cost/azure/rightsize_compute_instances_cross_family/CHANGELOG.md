# Changelog

## v0.3.0

- Added disk throughput and IOPS as compatibility sizing gates: `Disk Read/Write Bytes` and `Disk Read/Write Operations/Sec` metrics are collected from Azure Monitor and used to compute peak combined throughput (MB/s) and peak IOPS across the lookback period. Candidate instance types whose `UncachedDiskBytesPerSecond` or `UncachedDiskIOPS` spec falls below the observed peak (multiplied by the safety factor) are excluded from recommendations.
- Added network throughput as an idle detection signal: `Network In Total` and `Network Out Total` metrics are collected from Azure Monitor and used to compute average daily network bytes. An instance is now only considered idle when both its average CPU falls below the size-adjusted threshold AND its average network throughput is below 500 MB/day. If network data is unavailable, only the CPU threshold is applied.
- Added `Disk Peak Throughput (MB/s)`, `Disk Peak IOPS`, and `Network Average (MB/day)` fields to the rightsizing incident report.
- Added `Network Average (MB/day)` field to the idle instances incident report.

## v0.2.5

- Fixed issue where `param_stats_lookback` was passed to the metrics organization script but never used. The parameter is now only passed to the scripts that actually use it.
- Fixed issue where the `has_cpu_data` flag was derived from `cpu_all_stats` (which includes minimum and maximum values) rather than from whether any `average` data points were present. Since idle detection uses only average CPU values, a VM with only min/max data (no averages) would incorrectly have `has_cpu_data = true` and `cpu_average = 0`, causing a false idle classification. The flag is now based on `cpu_avg_count > 0` to be consistent with idle detection logic.
- Fixed API version inconsistency: `ds_azure_instance_statuses` now uses `2024-07-01` to match `ds_azure_instances`, as both call the same Azure Compute VM list endpoint.
- Fixed region coverage: replaced the hardcoded 54-entry region-to-pricing-key table with a dynamic lookup driven by `data/azure/regions.json`. All regions in that file are now mapped automatically; additional regions not in `regions.json` (Austria East, Belgium Central, Chile Central, Denmark East, Indonesia Central, Malaysia West, Sweden South, and US Government regions) are still covered via hardcoded fallbacks.
- Fixed issue where `chartUrlField` was missing from `hash_exclude` in both validate blocks. Because the chart URL contains timestamped metric data, its value changes on every policy run, causing incident hashes to change weekly and incidents to cycle (resolve then reopen) unnecessarily.
- Fixed issue where the Accelerated Networking compatibility gate used the instance type's `AcceleratedNetworkingEnabled` capability flag rather than whether the VM's NICs actually have AccelNet enabled. The gate now checks inline NIC properties from the VM list response. Since the Azure VM list API does not return `enableAcceleratedNetworking` on NIC reference objects, the gate effectively defaults to off, expanding the recommendation pool for VMs whose instance type supports AccelNet but whose NICs do not have it enabled.

## v0.2.4

- Fixed issue where `Memory Data Available` could incorrectly show `"Yes"` when the Azure metrics API returned a timeseries entry with an empty data array. The `has_mem_data` flag is now derived from whether any memory data points were actually processed, rather than whether the timeseries object was present.
- Changed `Current List Price` and `Recommended List Price` incident fields from hourly to monthly values (hourly rate × 730 hours/month) to be consistent with all other cost data in the incident. Field labels updated accordingly.
- Updated Cloud Workflow action API version from `2023-07-01` to `2024-07-01` to match the datasource API version used for reading VM data.
- Replaced the deprecated `/providers/Microsoft.Compute/locations/{region}/vmSizes` endpoint with the Resource SKUs API (`/providers/Microsoft.Compute/skus`). The new API includes restriction data, so VM sizes that are quota-limited or otherwise restricted for the subscription in a region are no longer recommended.

## v0.2.3

- Fixed issue where `Standard_NGads_V620_v1`-style AMD GPU instances were not recognized as AMD by the vendor detection logic. The check now uses a general pattern covering all GPU AMD families where variant letters (`ads`) appear directly after the uppercase family name without intervening size digits (e.g., `Standard_NGads`, `Standard_NVads`).
- Fixed issue where the power-off task audit log URL omitted `skipShutdown=true` when a forced shutdown was requested. The URL is now constructed after the conditional so it accurately reflects the actual request sent.
- Fixed issue where the `Memory Data Available` incident field showed `"No (no memory data)"` instead of simply `"No"`.
- Fixed potential status lookup miss in VM status merging where resource ID casing from the statuses API could differ from the VM list API. Status object keys and lookups are now normalized to lowercase, consistent with the metrics map fix in v0.2.2.

## v0.2.2

- Fixed style violation: removed extra blank line between parameters.
- Fixed potential crash where a resource ID case mismatch between the VM list API and the Azure Monitor batch metrics API could cause an unhandled null reference. The instance map is now keyed and looked up by lowercase resource ID, with an explicit guard against missing entries.
- Fixed issue where `Standard_NVads_A10_v5`-style AMD GPU instances were not recognized as AMD by the vendor detection logic, potentially causing incorrect cross-vendor recommendations when `Allow Intel/AMD Recommendations` was set to `No`.

## v0.2.1

- Fixed issue where superseded (legacy/retired) VM types could be recommended as the target for rightsizing.
- Fixed issue where the `!~` exclusion tag operator incorrectly excluded resources when the tag value matched the regex instead of when it did not match.
- Fixed issue where VMs with AMD EPYC-based HB/HC-series instance types were incorrectly classified as Intel, causing improper vendor-pairing when the `Allow Intel/AMD Recommendations` parameter was set to `No`.
- Fixed issue where VMs with no CPU metrics data were incorrectly flagged as idle.
- Fixed potential crash in chart URL generation when memory metrics were available but CPU metrics were not.
- Raised minimum required memory floor from 0.5 GB to 1.0 GB to better reflect the smallest available VM sizes.
- Removed non-exported fields from `hash_exclude` lists to align with style guide.
- Removed unreachable null guard in idle CPU threshold calculation.

## v0.2.0

- Removed `Idle Instance CPU Threshold (%)` parameter. Idle detection now uses a tiered threshold based on vCPU count, matching the approach used in the AWS cross-family rightsizing template: ≤2 vCPUs → 5%, ≤4 vCPUs → 4%, ≤8 vCPUs → 3%, ≤16 vCPUs → 2%, >16 vCPUs → 1%.

## v0.1.0

- Initial release
