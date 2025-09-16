# Changelog

## v4.0.8

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.7

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v4.0.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.5

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.4

- Policy template metadata modified so that it is no longer published in the catalog.

## v4.0.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.2

- Deprecated: This policy is no longer being updated. See README for more details.

## v4.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.0

- Added support for regex when filtering resources by tag

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to assess blobs in multiple storage accounts
- Added ability to filter storage accounts by subscription
- Added ability to filter storage accounts by region
- Added ability to filter storage accounts by multiple tag key:value pairs
- Added ability to delete blobs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if tag data changed but nothing else has
- Streamlined code for better readability and faster execution
- Policy now correctly requires both Azure Resource Manager and Azure Storage credentials

## v2.6

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.5

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.4

- Added default_frequency "daily"

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Added Resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.0

- initial release
