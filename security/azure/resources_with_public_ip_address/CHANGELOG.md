# Changelog

## v2.6.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.6.5

- Removed unnecessarily empty lines from code. Functionality unchanged.

## v2.6.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.6.3

- Policy template metadata modified so that it is no longer published in the catalog.

## v2.6.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.6.1

- Deprecated: This policy is no longer being updated

## v2.6

- fixed link to README in policy description

## v2.5

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.4

- Replaced the term **whitelist** with **allowed list**.

## v2.3

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.2

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.1

- Added subscription filter option and ability to specify Azure API endpoint

## v2.0

- initial release
