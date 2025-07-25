# Changelog

## v3.0.5

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.4

- Policy template metadata modified so that it is no longer published in the catalog.

## v3.0.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.2

- Deprecated: This policy is no longer being updated. See README for more details.

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter resources by project
- Added ability to use wildcards and regex when filtering resources by label
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera One credential

## v2.7

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
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

## v1.0

- initial release
