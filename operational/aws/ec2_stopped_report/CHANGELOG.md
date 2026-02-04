# Changelog

## v0.3.2

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v0.3.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.3.0

- Added support for attaching CSV files to incident emails.

## v0.2.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.5

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.2.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.2.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.2.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.2.0

- Added `Estimated Hourly Cost` and `Currency` to the incident table for added context

## v0.1.2

- Fixed bug that would sometimes cause tiny negative percentage values in results

## v0.1.1

- Policy no longer raises new incident if the incident details have changed but nothing else has.
- Removed unnecessary comments from code.

## v0.1.0

- Initial release
