# Changelog

## v0.1.4

- Fixed an issue where the policy could fail with a "must be a string" error due to how the root compartment parameter was used in some API requests.

## v0.1.3

- Fixed a bug introduced in v0.1.2 where the policy would fail to evaluate with an "invalid argument in join" error due to how the primary region and root compartment parameters were sanitized.

## v0.1.2

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.1.1

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.0

- Initial release
