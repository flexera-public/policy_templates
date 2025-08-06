# Changelog

## v3.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Policy template renamed to `Azure Publicly-Accessible SQL Managed Instances` to better reflect its functionality
- Added ability to filter results by subscription, region, or tags
- Added additional fields to incident output for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.9

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.8

- Replaced the term **whitelist** with **allowed list**.

## v2.7

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added "ignore-status" for 400, 403, 404 errors

## v2.4

- Added subscription filter option and ability to specify Azure API endpoint

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Added resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.2

- rename policy

## v1.1

- Added Permission block

## v1.0

- initial release
