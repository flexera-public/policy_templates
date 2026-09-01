# Changelog

## v0.1.13

- Fixed an issue where the "Enable Automatic Action" check for outdated applied policies always reported as non-compliant, even when the automatic update option was correctly configured.
- Fixed an issue where the unallocated cost percentage for rule-based dimensions could display as "NaN%" instead of 0% for organizations with no recorded cost during the analysis period.

## v0.1.12

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.1.11

- Replaced non-ASCII punctuation (em dashes, curly quotes, etc.) with standard ASCII equivalents for consistent rendering in the Flexera UI. No functional changes.

## v0.1.10

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.1.9

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.8

- Removed suffix from Service Account created by Onboarding policy template to better support Policy Manager use-cases

## v0.1.7

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.6

- Fixed issue where no Google policies were listed even when a GCP bill connect was present.

## v0.1.5

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.1.4

- Fixed issue where policy execution would fail with error if no bill connects have been configured.

## v0.1.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.1

- Fix error `Cannot access member 'length' of undefined` when no Tag Dimensions, or Rule-Based Dimensions exist

## v0.1.0

- Initial release
