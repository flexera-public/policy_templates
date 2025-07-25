# Changelog

## v4.1.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.1.0

- Added support for filtering system and Google Apps Script projects from the results.

## v4.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.0

- Added support for regex when filtering resources by label

## v3.0

- Several parameters altered to be more descriptive and human-readable
- Added more robust ability to filter resources by project
- Added ability to filter resources by region
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Streamlined code for better readability and faster execution
- Meta policy support added
- Policy now requires a valid Flexera credential

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Updated to fix exclusionary construct and correct report

## v2.4

- Modified escalation label and description for consistency

## v2.3

- Added Resource tabel

## v2.2

- Bug fixes on unhandled errors when executing

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services.
- Added new datasource for google project ID

## v1.0

- initial release
