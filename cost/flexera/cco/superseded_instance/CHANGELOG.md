# Changelog

## v3.4

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.3

- Updated description to account for new file path in Github repository

## v3.2

- Deprecated: This policy is no longer being updated. See README for more information.

## v3.1

- Added check to determine if the instance has been upgraded or not

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.1

- Added Google expression blob for /bill-analysis/orgs/" + org_id + "/costs/select request

## v2.0

- Bug fix for Optima cloud vendor account name API changes
- Added currency reference to incident table
- Fixed access of 'name' issue

## v1.12

- Ensure at least a month worth of costs are retrieved

## v1.11

- Fixed cloud account vendor URL, and use name instead of id

## v1.10

- Fixed the Run Rate label

## v1.9

- Modified escalation label and description for consistency

## v1.8

- adding incident resource table

## v1.7

- Updating path for ds_cloud_vendor_accounts

## v1.6

- Updated the metadata

## v1.5

- Fixed the date format issue

## v1.4

- don't raise error if instance type doesn't appear in the mapping

## v1.3

- added region to output

## v1.2

- Changing run rate to monthly estimated cost.

## v1.1

- Fixing Table

## v1.0

- Initial Release
