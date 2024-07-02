# Changelog

## v2.4

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.3

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v2.2

- Updated description to account for new file path in Github repository

## v2.1

- Deprecated: This policy is no longer being updated.

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.11

- Use provided keyword for Optima endpoint

## v1.10

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.9

- Fixed `report` variable type in js_format_costs script
- Added back in detail template to more easily show billing centers, currency, and the provided parameters

## v1.8

- Modified escalation label and description for consistency

## v1.7

- Updating resource table to iterate thru data and show all items in incident.

## v1.6

- Added Resource table

## v1.5

- Fixed no data table report

## v1.4

- Added a new parameter "Minimum Period Spend" for the user to indicate a minimum amount a billing center must have to be included in the report
- Added info field

## v1.3

- Updated the metadata

## v1.2

- Added a new parameter "Billing Center List" to create an incident based on input billing centers.
- added info field

## v1.1

- Added tenancy "single" in metadata

## v1.0

- initial release
