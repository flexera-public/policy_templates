# Changelog

## v3.4

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v3.3

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.2

- Updated description to account for new file path in Github repository

## v3.1

- Updated `js_generate_past_month_list` logic to fix bug where start date and end date clash when running policy at the end of January

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- Updated policy "summary_template" name
- Updated image-charts url

## v2.1

- Updated documentation link in policy template description

## v2.0

- Initial release
