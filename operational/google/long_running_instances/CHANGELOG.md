# Changelog

## v0.2.2

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.2.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.0

- Added error incident if no Google projects are returned by the credential, to alert users to potential permission issues.

## v0.1.3

- Fixed issue with incident table that cause policy execution to fail

## v0.1.2

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.1

- Updated API call for listing Google Projects to speed up policy execution and reduce the number of paginated requests.
- Incident table no longer includes Project Number. This is not supported by the above API and only has limited utility.

## v0.1.0

- Initial release
