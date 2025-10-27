# Changelog

## v3.3.7

- Changed description to say "policy template" for clarity. Functionality unchanged.

## v3.3.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.3.5

- Removed unnecessarily empty lines from code. Functionality unchanged.

## v3.3.4

- Policy template metadata modified so that it is no longer published in the catalog.

## v3.3.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.3.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v3.3.1

- Deprecated: This policy template is no longer being updated.

## v3.3

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.2

- Replaced the term **whitelist** with **allowed list**.

## v3.1

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- Use provided keyword for Optima endpoint

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added subscription filter option and ability to specify Azure API endpoint

## v2.1

- Modified escalation label and description for consistency
- Added automatic block

## v2.0

- initial release
