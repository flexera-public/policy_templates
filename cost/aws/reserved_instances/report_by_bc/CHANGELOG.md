# Changelog

## v2.0.5

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.0.4

- Policy template metadata modified so that it is no longer published in the catalog.

## v2.0.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.0.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v2.0.1

- Deprecated: This policy is no longer being updated.

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.7

- Use provided keyword for Optima endpoint

## v1.6

- Added default_frequency "daily"

## v1.5

- Modified escalation label and description for consistency

## v1.4

- Added resource table

## v1.3

- Updated datasource to leverage new API URI

## v1.2

- Updated the metadata

## v1.1

updated short description

## v1.0

- initial release
