# Changelog

## v3.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Policy is no longer deprecated
- Added ability to filter results by Billing Center
- Additional fields added to incident to provide more context
- Streamlined code for better readability and faster execution

## v2.2.1

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v2.2

- Deprecated: This policy template is no longer being updated.

## v2.1

- Bug fix: Already expired reserved instances are no longer included.

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.6

- Added default_frequency "daily"

## v1.5

- Modified escalation label and description for consistency

## v1.4

- Added resource table

## v1.3

- Updated the metadata

## v1.2

- Update Optima API endpoint

## v1.1

- Update the short_description

## v1.0

- initial release
