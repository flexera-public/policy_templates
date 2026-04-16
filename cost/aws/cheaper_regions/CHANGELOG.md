# Changelog

## v1.2.1

- Fixed issue with incident table that cause policy execution to fail

## v1.2.0

- Added `Incident Table Rows for Email Body` and `Attach CSV To Incident Email` parameters to support sending a CSV attachment with incident emails.

## v1.1.0

- Added `Estimated Monthly Savings` field to incident report, calculated by multiplying total region spend by `(1 - cheaper_ratio)` using the cost ratio from the AWS regions reference data
- Added `Total Estimated Monthly Savings` to the incident detail, showing the sum of estimated savings across all reported regions

## v1.0.6

- Updated documentation link in policy description. Functionality unchanged.

## v1.0.5

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v1.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v1.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v1.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v1.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v1.0.0

- Initial release
