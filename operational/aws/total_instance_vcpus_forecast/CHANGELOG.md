# Changelog

## v3.3.8

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.3.7

- Removed unnecessarily empty lines from code. Functionality unchanged.

## v3.3.6

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.3.5

- Policy template metadata modified so that it is no longer published in the catalog.

## v3.3.4

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.3.3

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.3.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v3.3.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v3.3

- Updated policy metadata to correctly identify it as an AWS policy

## v3.2

- Updated indentation for chart url so it renders corrrectly in the policy incident email

## v3.1

- Updated `js_generate_past_month_list` logic to fix bug where start date and end date clash when running policy at the end of January

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v2.1

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.0

- initial release
