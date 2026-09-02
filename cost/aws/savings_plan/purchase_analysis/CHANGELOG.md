# Changelog

## v0.2.4

- Fixed an issue where the incident message could display an incorrect currency notice when Flexera's currency conversion data was temporarily unavailable.

## v0.2.3

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.
- Fixed `run_script` parameter ordering in the analysis start and incident datasources.

## v0.2.2

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.2.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.0

- Added `Analysis Type` parameter to support both `Custom Commitment` and `Target Average Coverage` analysis types
- Updated `Hourly Purchase Commitment` parameter description to clarify it is only applicable for the `Custom Commitment` analysis type
- Added `Target Coverage Percentage` parameter to support `SavingsPlansTargetCoverage` when Analysis Type is set to `Target Average Coverage`
- Added `Target Coverage Percentage` field to incident report output
- Added `Analysis Type` field to incident report output

## v0.1.1

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.0

- Initial release
