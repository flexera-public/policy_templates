# Changelog

## v4.0.0

- Renamed policy template to `Vendor Spend Commitment Forecast` to avoid confusion with policy templates for RIs/SPs
- Added ability to specify a cost metric to use when gathering spend data
- Several parameters altered to be more descriptive and human-readable
- Streamlined code for better readability and faster execution

## v3.5

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v3.4

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.3

- Updated description to account for new file path in Github repository

## v3.2

- Updated indentation for chart url so it renders corrrectly in the policy incident email

## v3.1

- Removed `encodeURI()` function on `spend_data` variable

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v2.2

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.1

- Updated policy "summary_template" to better reflect policy template name
- Updated image-charts url

## v2.0

- Initial Release
