# Changelog

## v0.4.4

- Fixed a bug introduced in v0.4.4 that would cause "Cannot access member 'result' of undefined", if the AWS account info does not exist in Flexera.

## v0.4.3

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v0.4.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.4.1

- Updated email escalation declaration for new "Errors Identified" incident to prevent error `failed make a CSV attachment with data: unable to collect csv data from nil export`

## v0.4.0

- Policy now continues execution for accessible regions when some regions return permission errors
- Added separate incident report to identify regions with access issues and provide remediation guidance

## v0.3.0

- Added support for attaching CSV files to incident emails.

## v0.2.8

- Fixed issue where estimated savings would sometimes be reported as 0 inaccurately.

## v0.2.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.6

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.2.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.2.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.2.2

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v0.2.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.2.0

- Added `Resource ARN` to incident table.

## v0.1.0

- Initial release
