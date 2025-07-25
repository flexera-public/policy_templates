# Changelog

## v3.1.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.1.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.1.0

- Added link to Resource Analyzer Dashboard to incident table to facilitate easy viewing of resources

## v3.0.0

- Policy template renamed to `Low Usage Report`
- Costs can now be sliced against any cost dimension rather than just vendor account
- Costs can now be assessed based on various cost metrics
- Costs are gathered for a user-specified number of days rather than across the current month
- Costs can be filtered by Billing Center as either an allow list or a deny list
- Incident table now provides additional contextual data
- Streamlined code for better readability and faster execution

## v2.6

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.5

- Updated description to account for new file path in Github repository

## v2.4

- Added `Account ID` incident field.

## v2.3

- Added filters to API calls to reduce response body lenght.
- Removed unused vars and fields.
- Reduced execution time by removing unnecessary loops and functions.

## v2.2

- Reduced execution time avoiding repetitive loops and request fields.

## v2.1

- Made `Billing Center Name` parameter optional

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.9

- Use provided keyword for Optima endpoint

## v1.8

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.7

- Updated js_format_costs script for vendor_account_name error comparing ds_cloud_vendor_account name to new_bc_cost_obj vendor account name

## v1.6

- Modified escalation label and description for consistency

## v1.5

- Added Resource tabel

## v1.4

- Updating path for ds_cloud_vendor_accounts

## v1.3

- Added tenancy "single" in metadata

## v1.2

- removing check statement, and checking javascript
- summing up violations and modifying templates
- removing APNFee from calculation

## v1.1

- Adding Billing Center
- Adding Minimum Savings threshold
- changing from sum to run rate.

## v1.0

- initial release
