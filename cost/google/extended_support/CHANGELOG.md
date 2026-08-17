# Changelog

## v0.3.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default. This only affects new applications of the policy; existing applied policies keep their current setting unless updated.

## v0.2.2

- Replaced non-ASCII punctuation (em dashes, curly quotes, etc.) with standard ASCII equivalents for consistent rendering in the Flexera UI. No functional changes.

## v0.2.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.0

- Added `Ignore System Projects` parameter to automatically exclude projects whose ID begins with `sys-`
- Added `Ignore Google Apps Script Projects` parameter to automatically exclude projects whose ID begins with `app-`

## v0.1.0

- Initial release
