# Changelog

## v0.3.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default.

## v0.2.3

- Replaced non-ASCII punctuation (em dashes, curly quotes, etc.) with standard ASCII equivalents for consistent rendering in the Flexera UI. No functional changes.

## v0.2.2

- Updated policy logic for internal consistency; no functional or user-facing changes.

## v0.2.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.0

- Added error incident if no Google projects are returned by the credential, to alert users to potential permission issues.

## v0.1.1

- Fixed issue with incident table that cause policy execution to fail

## v0.1.0

- Initial release.
