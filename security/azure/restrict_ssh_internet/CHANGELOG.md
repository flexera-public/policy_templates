# Changelog

## v3.0.0

- Policy template renamed to `Azure Network Security Groups With Inbound SSH Open` to better reflect its functionality
- Added more robust subscription and region filtering
- Added additional fields to incident output for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.4

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.3

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.2

- Fixed policy error due to not being able to do `.split function` on an undefined value that is sometimes returned.

## v2.1

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.0

- initial release
