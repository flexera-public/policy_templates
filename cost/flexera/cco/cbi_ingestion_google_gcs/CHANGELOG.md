# Changelog

## v0.1.4

- Fixed an issue where the policy would fail with an "invalid argument in join" error when downloading cost files from Google Cloud Storage, caused by an internal bucket name value not being passed to the request correctly.

## v0.1.3

- Fixed an issue where uploads could fail to complete when no billing files were found for the selected period.

## v0.1.2

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.1.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.1.0

- Initial release
