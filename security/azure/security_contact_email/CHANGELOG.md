# Changelog

## v3.0.0

- Policy template renamed to `Azure Subscriptions Without Security Contact Email` to better reflect its functionality
- Added ability to filter results by subscription
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.3

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.2

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.1

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.0

- initial release
