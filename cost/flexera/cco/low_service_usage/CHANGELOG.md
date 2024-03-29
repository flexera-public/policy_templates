# Changelog

## v2.2

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.1

- Updated description to account for new file path in Github repository

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.8

- Use provided keyword for Optima endpoint

## v1.7

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.6

- Updated date format logic which was causing Error in policy execution on specific date.
- Removed extra code which was causing Error in policy execution for some use cases.
- Changed label and description for "report_instances" escalation to maintaining the consistency.

## v1.5

- Added new resource table

## v1.4

- Updating path for ds_cloud_vendor_accounts

## v1.3

- Added tenancy "single" in metadata

## v1.2

- removing check statement, and checking javascript
- summing up violations and modifying templates
- grouping and recalculating run_rate

## v1.1

- Adding Billing Center
- Adding Minimum Savings threshold
- changing from sum to run rate.

## v1.0

- initial release
