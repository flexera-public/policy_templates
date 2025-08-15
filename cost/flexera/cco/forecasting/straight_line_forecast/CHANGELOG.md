# Changelog

## v4.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.0

- Fixed issue where graph would not render if dimension name contains an ampersand
- Several parameters altered to be more descriptive and human-readable
- Added support for both simple and linear regression models via parameter
- Added support for splitting cost by any arbitrary dimension
- Added ability to filter by Billing Center via an allow or deny list
- Streamlined code for better readability and faster execution

## v3.7

- Updated policy metadata to make it more clear what Flexera service the policy is for

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
