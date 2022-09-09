# Changelog

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.6

- Added default_frequency "daily"

## v1.5

- Modified escalation label and description for consistency

## v1.4

- Added resource table

## v1.3

- Updated the metadata

## v1.2

- Update Optima API endpoint

## v1.1

- Update the short_description

## v1.0

- initial release
