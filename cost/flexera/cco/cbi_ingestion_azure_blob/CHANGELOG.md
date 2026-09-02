# Changelog

## v0.2.9

- Fixed an issue where the policy would fail with an "unexpected response status" or "cannot unmarshal object into Go struct field" error when downloading cost files from Azure Blob Storage, caused by an internal hostname value not being passed to the request correctly.

## v0.2.8

- Fixed an issue where the "Current Month" and "Previous Month" billing period options could resolve to the wrong month, most likely to occur on the first day of a calendar month.

## v0.2.7

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.2.6

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.2.5

- Updated documentation link in policy description. Functionality unchanged.

## v0.2.4

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.2.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.2.0

- Added support for cost files to use daily granularity instead of monthly.
- Fixed issue that would sometimes cause the policy template to abort its own bill upload and fail execution.

## v0.1.2

- Minor code improvements to bring template in line with current standards. Functionality unchanged.

## v0.1.1

- Fixes a bug where the policy is unable to use Microsoft Entra OAuth token for authentication.

## v0.1.0

- Initial release
