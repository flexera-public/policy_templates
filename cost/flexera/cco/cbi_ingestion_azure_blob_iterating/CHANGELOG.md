# Changelog

## v0.1.5

- Fixed an issue where the policy would fail with an "unexpected response status" or "invalid argument in join" error when listing or downloading cost files from Azure Blob Storage, caused by internal hostname and container values not being passed to the request correctly.

## v0.1.4

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.1.3

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.1.1

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.0

- Initial release
