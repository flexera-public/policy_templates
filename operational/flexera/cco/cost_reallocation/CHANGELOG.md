# Changelog

## v0.1.8

- Fixed an issue where the policy could produce invalid allocated cost and usage values for destination cost slices that had no total spend to allocate against.
- Fixed an issue where the policy would fail with an unclear error instead of a helpful message when "Specific Month" was selected for the Billing Period without also specifying which month.

## v0.1.7

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.1.6

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.1.5

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.4

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.3

- Updated URLs in policy template description. Functionality unchanged.

## v0.1.2

- Fixed bug that was preventing the destination cost line items from being generated.

## v0.1.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.1.0

- Initial release
