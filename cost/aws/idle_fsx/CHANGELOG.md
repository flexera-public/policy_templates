# Changelog

## v0.3.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default.

## v0.2.4

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.2.3

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.2

- Fixed bug where the `!~` exclusion tag operator incorrectly excluded resources whose tag value matched the regex instead of those that did not match

## v0.2.1

- Fixed issue with incident table that cause policy execution to fail

## v0.2.0

- Added `Incident Table Rows for Email Body` and `Attach CSV To Incident Email` parameters to support sending a CSV attachment with incident emails.

## v0.1.1

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.0

- Initial release
