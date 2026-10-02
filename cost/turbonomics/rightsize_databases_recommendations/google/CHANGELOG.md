# Changelog

## v0.5.11

- Fixed an issue where the policy could error out or report a missing resource ID for a recommendation whose underlying resource had more than one associated cloud identifier.

## v0.5.10

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.
- Fixed `run_script` parameter order for the filtered recommendations script (datasources before parameters).

## v0.5.9

- Added `hash_exclude` for volatile savings and utilization fields so that recalculated estimates alone no longer cause incidents to be treated as changed/reopened.

## v0.5.8

- Fixed an issue that could cause the policy to fail when retrieving business unit information
- Minor code formatting cleanup. No functional or user-facing changes.

## v0.5.7

- Minor code formatting fixes. Functionality unchanged.

## v0.5.6

- Updated documentation link in policy description. Functionality unchanged.

## v0.5.5

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.5.4

- Updated label of email parameter to "Email Addresses" to match other policy templates. Functionality unchanged.

## v0.5.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.5.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.5.1

- Switched from cookie-based authentication to token-based authentication

## v0.5

- Added Hyperlinks for `System Details URL` incident field.

## v0.4

- Renamed `Created Time` incident field to `Recommendation Created Time`.
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
- Added `New CPU Utilization (%)` incident field.
- Added `Throughput (MB/s)` incident field.
- Added `Throughput Utilization (%)` incident field.
- Added `New Throughput (MB/s)` incident field.
- Added `New Throughput Utilization (%)` incident field.
- Added `Connections` incident field.
- Added `New Connections` incident field.

## v0.3

- Updates provider from GCP to Google

## v0.2

- Links to documentation were added to the short description of the policy.

## v0.1

- Initial Release
