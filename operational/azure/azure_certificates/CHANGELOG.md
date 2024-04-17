# Changelog

## v3.2.1

## v3.2

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.1

- Changed internal name of escalation code to ensure "Meta Policy" works as expected

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.5

- Replaced the term **whitelist** with **allowed list**.

## v2.4

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.3

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.1

- Added subscription filter option and ability to specify Azure API endpoint

## 2.0

- Initial Release
