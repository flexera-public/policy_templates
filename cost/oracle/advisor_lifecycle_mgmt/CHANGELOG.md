# Changelog

## v0.3.2

- Fixed a bug introduced in v0.3.1 where the policy would fail to evaluate with an "invalid argument in join" error due to how the primary region parameter was sanitized.

## v0.3.1

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.3.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default.

## v0.2.4

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.3

- Fixed issue with incident table that cause policy execution to fail

## v0.2.2

- Updated documentation link in policy description. Functionality unchanged.

## v0.2.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.2.0

- Added support for attaching CSV files to incident emails.

## v0.1.0

- Initial release
