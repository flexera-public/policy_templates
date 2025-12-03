# Changelog

## v0.3.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.3.1

- Updated email escalation declaration for new "Errors Identified" incident to prevent error `failed make a CSV attachment with data: unable to collect csv data from nil export`

## v0.3.0

- Policy now continues execution for accessible regions when some regions return permission errors
- Added separate incident report to identify regions with access issues and provide remediation guidance

## v0.2.0

- Added support for attaching CSV files to incident emails.

## v0.1.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.6

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.1.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.1.2

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v0.1.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.1.0

- Initial release
