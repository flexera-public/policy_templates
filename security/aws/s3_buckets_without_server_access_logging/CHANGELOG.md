# Changelog

## v3.0.5

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v3.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Policy no longer allows for automatic actions
- Buckets can now be filtered by region, tag, or name
- Manual actions now allow for unique target bucket and log prefix values per action
- Added additional fields to incident table for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.8

- fixed link to README in policy description

## v2.7

- Updated description of `Account Number` parameter

## v2.6

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.5

- Added default to aws_account_number parameter to enable existing API users.

## v2.4

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Adding incident resource table

## v2.0

- Changes to support the Credential Service
- Changed http method to PUT for define enable_logging.

## v1.2

- Updated region datasources to use github data list

## v1.1

- Added Approval block

## v1.0

- Initial Release
