# Changelog

## v4.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.0

- Renamed policy template and updated description to better reflect functionality
- Added ability to filter by Billing Center as an allow list or a deny list
- Added logic to ensure redundant Billing Centers don't skew results
- Improvements made to moving average calculation for better accuracy
- Incident table now used to display the moving average data used in the chart
- Streamlined code for better readability and faster execution

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
