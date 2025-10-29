# Changelog

## v0.5.1

- Updated Azure URL in policy template description. Functionality unchanged.

## v0.5.0

- Improved Incident and Recommendation Details
- Adds resource utilization chart URLs to the resulting incidents. This mitigates/prevents need to use cloud vendor console or another observability tool outside Flexera to validate the recommendation is true.
- Removed batch processing for large datasources to improve policy reliability and performance.

## v0.4.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.4.3

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.4.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.4.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.4.0

- Improved tag validation logic to ensure required tags exist before proceeding, helping prevent errors.

## v0.3.0

- Added batch processing for large datasources.

## v0.2.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.2.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.2.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v0.2.0

- Add `param_databricks_cluster_list` for filtering to a specific Databricks Cluster within a Databricks Workspace
- Add `p90`,`p95`,`p99` Threshold Statistic choices
- Fixed subscription ID and Name output in recommendation

## v0.1.0

- Initial release
