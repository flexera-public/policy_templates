# Changelog

## v0.4.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default. This only affects new applications of the policy; existing applied policies keep their current setting unless updated.

## v0.3.4

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.3.3

- Fixed issue with incident table that cause policy execution to fail

## v0.3.2

- Updated documentation link in policy description. Functionality unchanged.

## v0.3.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.3.0

- Added support for attaching CSV files to incident emails.

## v0.2.2

- Fixed issue where estimated savings value had all fractional values rounded away

## v0.2.1

- Fixed issue where estimated savings value would sometimes be incorrectly inflated

## v0.2.0

- Added additional metadata to incidents
- Fixed policy actions to work when changing CPU/Memory but not the shape of a resource

## v0.1.0

- Initial release
