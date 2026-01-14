# Changelog

## v0.2.4

- Fixed a bug caused by an order of magnitude error which resulted in recommendations not being returned for valid Redshift instances.

## v0.2.3

- Fixed a bug introduced in v0.2.2 that would cause "Cannot access member 'result' of undefined", if the AWS account info does not exist in Flexera.

## v0.2.2

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v0.2.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.2.0

- Added support for attaching CSV files to incident emails.

## v0.1.8

- Fixed issue with `GetMetricData` API request when gathering CloudWatch metrics. Functionality unchanged.

## v0.1.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.6

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.1.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.3

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v0.1.2

- Added `hide_skip_approvals` field to the info section, enabling the UI to dynamically show or hide the "Skip Approval" option. Functionality unchanged.

## v0.1.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.1.0

- Initial release
