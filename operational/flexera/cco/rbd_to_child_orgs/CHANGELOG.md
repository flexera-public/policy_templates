# Changelog

## v0.1.4

- Fixed a bug introduced in v0.1.3 where the policy would fail to evaluate with an "invalid argument in join" error due to how the effective date parameter was sanitized.

## v0.1.3

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.
- Fixed `run_script` parameter order for `js_parent_rbd_selection` (datasources before parameters).

## v0.1.2

- Replaced non-ASCII punctuation (em dashes, curly quotes, etc.) with standard ASCII equivalents for consistent rendering in the Flexera UI. No functional changes.

## v0.1.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.0

- Initial release
