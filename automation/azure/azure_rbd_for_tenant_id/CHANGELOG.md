# Changelog

## v0.1.3

- Fixed an issue where the policy's 12 month data lookback window could be shifted by one month when the policy ran on February 29th (leap day).

## v0.1.2

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.
- Updated the summary message to include the policy name.

## v0.1.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.0

- Initial release
