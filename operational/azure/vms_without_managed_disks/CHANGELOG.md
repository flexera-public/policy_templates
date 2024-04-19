# Changelog

## v3.1.1

- Added default value for parameters that do not require user input

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.9

- Replaced the term **whitelist** with **allowed list**.

## v2.8

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added subscription filter option and ability to specify Azure API endpoint

## v2.4

- Modified escalation label and description for consistency

## v2.3

- Added Resource table

## v2.2

- Fix incident table rendering issue
- Add VM tags to incident table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services

## v1.2

- Added Permission block

## v1.1

- Adding in additional details

## v1.0

- initial release
