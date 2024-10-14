# Changelog

## v3.1.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.1

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v3.0

- Billing Center filter condensed to a single parameter and now supports both names and IDs
- Incident summary is now derived from the name of the applied policy
- Streamlined code for better readability and faster execution

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.7

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.6

- Modified escalation label and description for consistency

## v1.5

- Added Resource Table

## v1.4

- Updated the metadata

## v1.3

- Added tenancy "single" in metadata

## v1.2

- Added link to Billing Center in E-mail Report

## v1.1

- Updating category

## v1.0

- initial release
