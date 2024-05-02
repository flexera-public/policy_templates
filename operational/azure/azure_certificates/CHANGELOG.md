# Changelog

## v4.0.0

- Added ability to delete Azure certificates automatically or manually
- Several parameters altered to be more descriptive and human-readable
- Added ability to use Subscription filter as an allow or a deny list
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to filter resources by region
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if inconsequential metadata like tag values change
- Streamlined code for better readability and faster execution

## v3.2.1

- Added default value for parameters that do not require user input

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

## v2.0

- Initial Release
