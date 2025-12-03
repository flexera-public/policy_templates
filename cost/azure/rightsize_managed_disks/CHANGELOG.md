# Changelog

## v2.7.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v2.7.1

- Fixed issue where incident would never include results.

## v2.7.0

- Added support for attaching CSV files to incident emails.

## v2.6.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.6.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.6.2

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v2.6.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.6.0

- Policy template no longer raises an incident if user does not set any thresholds for determining underutilization.
- Defaults changed for `IOPS Threshold (%)` and `Throughput Threshold (%)` parameters to something a typical user would expect.

## v2.5.1

- Added batch processing for large datasources as a performance enhancement (reduces memory usage) with no changes to logic or functionality.

## v2.5.0

- Savings are now calculated using cost data stored in Flexera Cloud Cost Optimization instead of only via Azure list price.
- Currency conversion functionality has been removed. It is no longer needed due to actual cost data stored in Flexera Cloud Cost Optimization being used to assess cost and savings.

## v2.4.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.4.1

- Fixed a bug that showed wrong calculations for changing the disk capacity, IOPS and throughput.

## v2.4.0

- Added a parameter to select the interval to use when gathering Azure metrics data.
- Added more options for parameters *IOPS Threshold Statistic* and *Throughput Threshold Statistic*: p90, p95 and p99.
- Fixed a bug that caused the incident fields "New Disk IOPS" and "New Disk Throughput (MB/s)" to be miscalculated when "Premium SSD v2" was the recommended disk type.

## v2.3.0

- Implemented automatic currency detection and conversion, ensuring recommendations are displayed in the currency configured in the user's settings.

## v2.2.0

- Added a parameter to make recommendations or not for changing a disk tier to Standard HDD.

## v2.1.0

- Added ability to filter results by disk SKU

## v2.0.3

- Fixed a bug related to the Premium ssd price calculation with low throughput

## v2.0.2

- Fixed bug related to disk name calculation

## v2.0.1

- Fixed bug that caused wrong calculations for ultra tier disks

## v2.0

- Added support for regex when filtering resources by tag

## v1.2

- Updated the descriptions and labels of the IOPS and throughput parameters in the README and policy template files.
- Updated the short description of the policy.
- Fixed the functionality of *Minimum Savings Threshold* parameter. This parameter is used to suppress recommendations with potential savings below the specified threshold.

## v1.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v1.0

- Initial release.
