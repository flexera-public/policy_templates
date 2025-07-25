# Changelog

## v3.7.5

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.7.4

- Policy template metadata modified so that it is no longer published in the catalog.

## v3.7.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.7.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v3.7.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

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

## v2.6

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.5

- Updated policy "summary_template" name, changed legend font size, changed x-axis label to diagonal
- Updated image-charts url
- Updated "Functional Details" in readme file

## v2.4

- Updated policy template name and documentation link in policy template description

## v2.3

- Added functionality to break costs down by 4 dimensions (category, service, region, vendor account name)

## v2.2

- Use provided keyword for Optima endpoint

## v2.1

- URIEncode all the image-charts options

## v2.0

- Initial Release
