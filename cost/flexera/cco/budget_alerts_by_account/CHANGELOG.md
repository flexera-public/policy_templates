# Changelog

## v2.5.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.5.3

- Policy template metadata modified so that it is no longer published in the catalog.

## v2.5.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.5.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v2.5

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.4

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v2.3

- Updated description to account for new file path in Github repository

## v2.2

- Resolved issues with calculating forecast

## v2.1

- Fixed image-charts url from free service endpoint to our paid service endpoint url

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.8

- Fixed issue with currentSpend subtracting 3 days unnecessarily
- Fixed issue with incorrect API endpoint

## v1.7

- URIEncode all the image-charts options

## v1.6

- Fixed nil account_name, and updated searches to get correct data

## v1.5

- Removed ds_session and synced ds_billing_center from budget alert

## v1.4

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.3

- Fixed markdown alignment in validation heredoc

## v1.2

- Fixed aws account name lookup bug that lead to an error
- Added section headers
- Removed debugging console.log statements
- Refactored Billing Center index call to return Billing Centers the user has access to
- Fixed budget column heading in export table

## v1.1

- Modified escalation label and description for consistency
- Added incident resource table

## v1.0

- initial release
