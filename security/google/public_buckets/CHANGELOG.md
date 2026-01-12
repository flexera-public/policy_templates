# Changelog

## v3.2.6

- Updated API call for listing Google Projects to speed up policy execution and reduce the number of paginated requests.
- Incident table no longer includes Project Number. This is not supported by the above API and only has limited utility.

## v3.2.5

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.2.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.2.3

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v3.2.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.2.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.2.0

- Added support for filtering system and Google Apps Script projects from the results.

## v3.1.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.1.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.1

- fixed link to README in policy description

## v3.0

- Fixed issue where some open buckets were not being reported on
- Added ability to filter resources by project
- Added ability to filter resources by region
- Added ability to filter resources by label
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export
- Streamlined code for better readability and faster execution
- Added logic required for "Meta Policy" use-cases
- Flexera credential now required to facilitate meta policy use cases.

## v2.5

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Added resource table

## v2.1

- Bug fixes on unhandled errors when executing

## v2.0

- Changed the authentication to credential services
- Added new datasource for google project ID

## v1.3

- Upating Policy Template Name

## v1.2

- Update email subject with account name and ID, and change actions and/or resolution name to be more descriptive. Issues #75 & #83

## v1.1

- Updating input parameter name for email

## v1.0

- Initial Release
