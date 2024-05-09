# Changelog

## v3.0.0

- Added ability to filter report by project
- Added ability to filter recommendations by region
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.8

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.7

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.6

- Added default_frequency "daily"

## v2.5

- Fixed a bug where we would only report on a single CUD in a region where there is more than one.
- Refactored formatting, added section headers, and fixed indents.

## v2.4

- Modified escalation label and description for consistency

## v2.3

- Added resource table

## v2.2

- Bug fixes on unhandled errors when executing

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services
- Added new datasource for google project ID

## v1.2

- Added Permission block

## v1.1

- update short_description

## v1.0

- initial release
