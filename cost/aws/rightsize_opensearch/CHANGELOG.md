# Changelog

## v0.2.1

- Fixed idle detection unit mismatch: `SearchRate` and `IndexingRate` are in requests/minute; threshold is now correctly converted before comparison so the user-facing "Requests/Day" unit is accurate
- Fixed region accessibility probe incorrectly using `MaxRecords=5` for the ElastiCache API call, which would cause a 400 error; changed to `MaxResults=5` (matching the pattern used by other templates)
- Fixed JVM memory export field labels from "OldGenJVM" to "JVM Memory" to accurately reflect that the values represent the higher of both `OldGenJVMMemoryPressure` and `JVMMemoryPressure`
- Fixed `Average Daily Requests` export field to display values in requests/day (was incorrectly showing requests/minute)
- Fixed truncated idle incident export block (missing final fields after `jvmP99` that were accidentally removed during a previous edit)

## v0.2.0

- Fixed idle detection to correctly flag domains with zero traffic (no CloudWatch data returned now treated as zero requests)
- Fixed savings estimate for underutilized domains to use the larger of vCPU or memory reduction ratio, improving accuracy for memory-optimized instance families
- Fixed `JVMMemoryPressure` metric now used alongside `OldGenJVMMemoryPressure`; the higher value is used for rightsizing, improving coverage for OpenSearch v1.x+ domains
- Added "Incomplete Data Risk" flag for downsize recommendations based on only one utilization metric (CPU or memory); replaces non-functional "Tiered Storage Risk" flag
- Fixed `hash_exclude` to cover all volatile metric fields in both incidents, preventing spurious incident re-opens on every policy run
- Removed `Create Final Snapshot Before Deletion` parameter and associated snapshot action; the underlying AWS API endpoint does not exist and the feature was non-functional
- Updated `Exclude Recommendations with Risk Flags` parameter to replace "Tiered Storage Risk" (removed) with "Incomplete Data Risk" (new)

## v0.1.0

- Initial release
