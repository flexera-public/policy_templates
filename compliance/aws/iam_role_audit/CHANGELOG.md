# Changelog

## v3.0.11

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v3.0.10

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.0.9

- Changed description to say "policy template" for clarity. Functionality unchanged.

## v3.0.8

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.7

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v3.0.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.5

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.4

- Updated service field in metadata to "Identity & Access Management". Functionality unchanged.

## v3.0.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.1

- Add default value for `IAM Role Names/IDs/ARNs` param

## v3.0.0

- Several parameters altered to be more descriptive and human-readable
- `IAM Role Name` parameter renamed to `IAM Role Names/IDs/ARNs` and now accepts role IDs and ARNs
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.6

- Updated description of `Account Number` parameter

## v2.5

- Removed unused `sys_log` definition
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- Added default to aws_account_number parameter to enable existing API users.

## v2.3

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.2

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.1

- Modified escalation label and description for consistency

## v2.0

- initial release
