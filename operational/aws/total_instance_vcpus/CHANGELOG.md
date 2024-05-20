# Changelog

## v4.1.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

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
