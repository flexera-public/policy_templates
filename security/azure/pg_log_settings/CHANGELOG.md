# Changelog

## v3.0.4

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v3.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Policy template renamed to `Azure PostgreSQL Servers With Bad Log Settings` to better reflect its functionality
- Added ability to check multiple log settings in a single policy run
- Added ability to filter results by subscription, region, and tag
- Added additional fields to incident table for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.2

- fixed link to README in policy description

## v2.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.0

- initial release
