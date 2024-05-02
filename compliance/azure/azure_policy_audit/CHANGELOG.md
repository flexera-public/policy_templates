# Changelog

## v3.0.0

- Several parameters altered to be more descriptive and human-readable
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.7

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.6

- Replaced the term **whitelist** with **allowed list**.

## v2.5

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added subscription filter option and ability to specify Azure API endpoint

## v2.1

- Modified escalation label and description for consistency

## v2.0

- initial release
