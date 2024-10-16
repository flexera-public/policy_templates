# Changelog

## v4.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.0

- Added support for regex when filtering resources by tag

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Fixed issue where error occurred on policy execution if incident contained no results
- Fixed issue where more AHUB licenses are recommended than there are VMs to enable them on
- Added logic required for "Meta Policy" use-cases
- Several parameters altered to be more descriptive and human-readable
- Added ability to filter resources by subscription either via allow or deny list
- Added ability to filter resources by region either via allow or deny list
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Policy no longer raises new escalations if irrelevant metadata changed but nothing else has
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera One credential

## v2.9

- Replaced the term **whitelist** with **allowed list**.

## v2.8

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added "ignore-status" for 400, 403, 404 errors

## v2.4

- Added subscription filter option and ability to specify Azure API endpoint

## v2.3

- adding incident resource table

## v2.2

- Bug fix on the formatting of email incident

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services

## v1.1

- Added Permission block

## v1.0

- initial release
