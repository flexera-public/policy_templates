# Changelog

## v0.4.10

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.
- Fixed `run_script` parameter order for the filtered recommendations script (datasources before parameters).

## v0.4.9

- Added `hash_exclude` for volatile savings and utilization fields so that recalculated estimates alone no longer cause incidents to be treated as changed/reopened.

## v0.4.8

- Fixed an issue that could cause the policy to fail when retrieving business unit information

## v0.4.7

- Updated documentation link in policy description. Functionality unchanged.

## v0.4.6

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.4.5

- Updated label of email parameter to "Email Addresses" to match other policy templates. Functionality unchanged.

## v0.4.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.4.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.4.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.4.1

- Switched from cookie-based authentication to token-based authentication

## v0.4

- Added Hyperlinks for `System Details URL` incident field.

## v0.3

- Added `Recommendation Created Time` incident field.
- Added `System Details URL` incident field.
- Added `Storage (GB)` incident field.
- Added `Storage Utilization (%)` incident field.
- Added `New Storage (GB)` incident field.
- Added `New Storage Utilization (%)` incident field.
- Added `DTU Capacity` incident field.
- Added `DTU Utilization (%)` incident field.
- Added `New DTU Capacity` incident field.
- Added `New DTU Utilization (%)` incident field.
- Added `IOPs Capacity` incident field.
- Added `IOPs Utilization (%)` incident field.
- Added `New IOPs Capacity` incident field.
- Added `New IOPs Utilization (%)` incident field.
- Added `Memory (GB)` incident field.
- Added `Memory Utilization (%)` incident field.
- Added `New Memory (GB)` incident field.
- Added `New Memory Utilization (%)` incident field.
- Added `CPU (GHz)` incident field.
- Added `CPU Utilization (%)` incident field.
- Added `New CPU (GHz)` incident field.
- Added `new CPU Utilization (%)` incident field.
- Added `Throughput (MB/s)` incident field.
- Added `Throughput Utilization (%)` incident field.
- Added `New Throughput (MB/s)` incident field.
- Added `New Throughput Utilization (%)` incident field.
- Added `Connections` incident field.
- Added `New Connections` incident field.

## v0.2

- Links to documentation were added to the short description of the policy.

## v0.1

- Initial Release
