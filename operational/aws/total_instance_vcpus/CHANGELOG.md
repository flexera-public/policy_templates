# Changelog

## v4.1.8

- Changed description to say "policy template" for clarity. Functionality unchanged.
- Updated label of email parameter to "Email Addresses" to match other policy templates. Functionality unchanged.

## v4.1.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.1.6

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.1.5

- Policy template metadata modified so that it is no longer published in the catalog.

## v4.1.4

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.1.3

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.1.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v4.1.1

- Deprecated: This policy template is no longer being updated. Please see policy README for more information.

## v4.1.0

- Fixed issue where only top-level billing centers could be filtered on. Policy now additionally supports filtering on child billing centers.

## v4.0

- Added ability to filter the report for a list of Billing Centers that can either be allowed or denied.
- Added ability to filter the report for a list of Regions that can either be allowed or denied.

## v3.2

- Updated policy metadata to correctly identify it as an AWS policy

## v3.1

- Updated indentation for chart url so it renders correctly in the policy incident email

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v2.3

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- Updated policy "summary_template" name, changed legend font size, changed x-axis label to diagonal
- Updated image-charts url

## v2.1

- Updated policy template name and description

## v2.0

- Initial release
