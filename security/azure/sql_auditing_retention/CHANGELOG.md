# Changelog

## v3.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Policy template renamed to `Azure SQL Servers With Insufficient Auditing Retention` to better reflect its functionality
- Added ability to filter results by subscription, region, or tags
- Added ability to specify a number of days to require for auditing retention
- Added additional fields to incident output for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.2

- fixed link to README in policy description

## v2.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.0

- initial release
