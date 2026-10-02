# Changelog

## v0.2.2

- Fixed an issue where the policy could fail to complete if tag information could not be retrieved for one or more Lambda functions.

## v0.2.1

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.2.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default.

## v0.1.5

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.1.4

- Improved the policy's reliability when checking which AWS regions it can access, making it less likely to fail to run due to expected access restrictions in certain regions

## v0.1.3

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.2

- Fixed bug where the `!~` exclusion tag operator incorrectly excluded resources whose tag value matched the regex instead of those that did not match

## v0.1.1

- Fixed issue with incident table that cause policy execution to fail

## v0.1.0

- Initial release
