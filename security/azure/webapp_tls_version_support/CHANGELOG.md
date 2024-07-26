# Changelog

## v3.0.0

- Policy template renamed to `Azure Web Apps Without Secure TLS` to better reflect its functionality
- Added ability to filter results by subscription, region, or tags
- Added additional fields to incident output for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.7

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.6

- Replaced the term **whitelist** with **allowed list**.

## v2.5

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.4

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added "ignore-status" for 400, 403, 404 errors

## v2.1

- Added subscription filter option and ability to specify Azure API endpoint

## v2.0

- Initial release
