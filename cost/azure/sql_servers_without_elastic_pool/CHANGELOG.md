# Changelog

## v3.0.0

- Policy renamed to more accurately indicate that it reports SQL Servers and not SQL Databases
- Several parameters altered to be more descriptive and human-readable
- Improved and more robust filtering for subscriptions and tags
- Added ability to filter resources by region
- Normalized incident export to be consistent with other policies
- Policy no longer raises new escalations if tag data has changed but nothing else has
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.6

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

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

## v2.0

- Initial Release
