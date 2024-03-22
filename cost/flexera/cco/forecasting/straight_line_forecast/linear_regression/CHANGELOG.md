# Changelog

## v3.6

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.5

- fixed link to README in policy description

## v3.4

- Updated description to account for new file path in Github repository

## v3.3

- Updated policy to take only top-level billing center costs
- Fixed 'Vendor Account Name' option for `param_dimension`
- Added 'Billing Center' as an option for `param_dimension`

## v3.2

- Updated indentation for chart url so it renders corrrectly in the policy incident email

## v3.1

- Updated `js_generate_past_month_list` logic to fix bug where start date and end date clash when running policy at the end of January

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v2.3

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- Updated policy "summary_template" name, changed legend font size, changed x-axis label to diagonal
- Updated image-charts url

## v2.1

- Updated policy template name and documentation link in policy template description

## v2.0

- Initial Release
