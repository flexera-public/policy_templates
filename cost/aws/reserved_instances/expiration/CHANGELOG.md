# Changelog

## v2.2

- Updated policy metadata to correctly identify it as an AWS policy

## v2.1

- Deprecated: This policy is no longer being updated.

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.11

- Added default_frequency "daily"

## v1.10

- Modified escalation label and description for consistency

## v1.9

- adding incident resource table

## v1.8

- Updated datasource to leverage new API URI

## v1.7

- Updated the metadata

## v1.6

- update show_description

## v1.5

- using rs_optima_host variable

## v1.4

- Update email subject with account name and ID, and change actions and/or resolution name to be more descriptive. Issues #75 & #83

## v1.3

- Updating input parameter name for email

## v1.2

- Updating email from string to list

## v1.1

- switching from html tables to markdown tables
- removing parameter: org_id for rs_org_id

## v1.0

- initial release
