# Changelog

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.6

- URIEncode all the image-charts options

## v1.5

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.4

- Fixed markdown alignment in validation heredoc

## v1.3

- Added default_frequency "daily"

## v1.2

- Modified escalation label and description for consistency
- Added incident resource table

## v1.1

- Remove budget input details from template short_description

## v1.0

- initial release
