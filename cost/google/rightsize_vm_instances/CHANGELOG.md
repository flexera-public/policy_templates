# Changelog

## v0.4.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default.

## v0.3.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.3.0

- Added error incident if no Google projects are returned by the credential, to alert users to potential permission issues.

## v0.2.5

- Fixed issue with incident table that cause policy execution to fail

## v0.2.4

- Updated documentation link in policy description. Functionality unchanged.

## v0.2.3

- Updated API call for listing Google Projects to speed up policy execution and reduce the number of paginated requests.
- Incident table no longer includes Project Number. This is not supported by the above API and only has limited utility.

## v0.2.2

- Corrected issue that would prevent meta policy from being generated correctly. Functionality unchanged.

## v0.2.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.2.0

- Added support for attaching CSV files to incident emails.

## v0.1.0

- Initial release.
