# Changelog

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

## v3.1.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.1.0

- Added option to report/update Google Project labels

## v3.0.0

- Added ability to filter resources by Google Project
- Added ability to filter resources by Google resource type
- Added additional context to incident description
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera One credential

## v2.5

- Updated label logic to return `Missing Label Keys` as well as `Label Keys with Missing Label Values` in incident

## v2.4

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Fixed README link in short_description

## v2.0

- initial release
