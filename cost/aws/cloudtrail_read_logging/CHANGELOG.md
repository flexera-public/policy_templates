# Changelog

## v0.2.7

- Fixed an issue where the policy could fail when the AWS account identity response was unavailable.

## v0.2.6

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.2.5

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.4

- Fixed issue with "PutEventSelectors" API call that could potentially cause policy actions to fail.

## v0.2.3

- Updated documentation link in policy description. Functionality unchanged.

## v0.2.2

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v0.2.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.2.0

- Added support for attaching CSV files to incident emails.

## v0.1.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.5

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.1.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.1.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.1.0

- Initial Release
