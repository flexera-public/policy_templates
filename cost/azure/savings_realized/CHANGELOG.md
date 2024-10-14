# Changelog

## v3.9.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.9.0

- Added parameter to select between showing the currency code or the currency symbol in the incident report
- Fixed a bug introduced at v3.8 that made the policy show greater savings: if there were no MCA bill connections the policy still pulled aggregated costs thus making the savings bigger.

## v3.8

- Added support for organizations with Microsoft MCA accounts
- Policy incident report now presents the savings in the same currency as the organization

## v3.7

- Added support for organizations with no Microsoft Azure Enterprise Agreement (Legacy) bill connects

## v3.6

- Incident subject is now the name of the applied policy
- Policy metadata updated to better categorize the policy
- Additional corrections around retrieving cost data on orgs using new EA bill connection
- Streamlined code for better readability and faster execution

## v3.5

- Policy incident no longer includes extraneous information about date and time in `Month` field

## v3.4

- Added a condition to prevent null report chart array

## v3.3

- Corrected issue with policy not retrieving cost data on orgs using newer Azure bill connections

## v3.2

- Updated indentation for chart url so it renders corrrectly in the policy incident email

## v3.1

- Updated description for parameters `param_period_start` and `param_period_end`

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v2.3

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- Updated image-charts url ton include org id and project id

## v2.1

- Updated policy "summary_template" name, changed legend position
- Updated image-charts url

## v2.0

- Initial Release
