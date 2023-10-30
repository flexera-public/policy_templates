# Changelog

## v3.4

- Updated `Savings Realized On Compute Savings Plans` incident field to align value with AWS Realized Savings Dashboard.

## v3.3

- Added the following dimensions to get costs and calculate cost per hour average: `operating_system`, `database_engine`, `database_edition`, `license_model`, `deployment_option`

## v3.2

- Updated indentation for chart url so it renders corrrectly in the policy incident email

## v3.1

- Updated description for parameters `param_period_start` and `param_period_end`

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v2.2

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.1

- Updated image-charts url ton include org id and project id

## v2.0

- Initial Release
