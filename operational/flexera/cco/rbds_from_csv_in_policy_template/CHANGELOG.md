# Changelog

## v0.1.7

- Fixed an issue where generating rule-based dimensions could fail with an error when the "Dimensions for Rules" parameter did not match any column in the CSV data.
- Fixed an issue where a rule's matching value could be missing or contain unintended extra spaces when only one rule dimension column was configured.

## v0.1.6

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.1.5

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.1.4

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.3

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.1.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.0

- Initial Release
