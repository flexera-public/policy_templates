# Changelog

## v3.0.1

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v3.0.0

- Deprecated policy. This is the final update.
- Added support for Azure China
- Subscription filter can now be used as an allow list or a deny list
- Added additional fields and context to incident output
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera One credential

## v2.10

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.9

- Replaced the term **whitelist** with **allowed list**.

## v2.8

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.7

- Removed unused `sys_log` definition
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added subscription filter option and ability to specify Azure API endpoint

## v2.4

- Fixed bug in iteration over multiple roles/subscriptions

## v2.3

- Fixed bug in displaying role assignment id

## v2.2

- Added Resource table

## v2.1

- fix provider tag for graph Credential

## v2.0

- Changes to support the Credential Service

## v1.3

- Added filter to only gather role assignments from the subscription level

## v1.2

- Added pagination for the Microsoft Graph API users call

## v1.1

- Added Permission block

## v1.0

- initial release
