# Changelog

## v3.1.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.1.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.1.0

- Added support for filtering system and Google Apps Script projects from the results.

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Added ability to filter recommendations by project
- Added ability to filter recommendations by region
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added default_frequency "daily"

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

## v1.1

- update policy name

## v1.0

- initial release
