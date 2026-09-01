# Changelog

## v0.2.2

- Fixed an issue where, with "Skip Instance Sizes" set to "Yes", a server that qualified for downsizing more than one size could cause the policy to fail to generate an incident instead of recommending the correct target size.

## v0.2.1

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.2.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default.

## v0.1.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.0

- Initial Release
