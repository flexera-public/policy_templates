# Changelog

## v3.0.8

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v3.0.7

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.0.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.3

- Updated service field in metadata to "Identity & Access Management". Functionality unchanged.

## v3.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Policy template renamed to `AWS IAM User Accounts Without MFA` to better reflect its functionality
- Added toggle to include or ignore user accounts without a console password
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.7

- fixed link to README in policy description

## v2.6

- Updated description of `Account Number` parameter

## v2.5

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- Added default to aws_account_number parameter to enable existing API users.

## v2.3

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.2

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.1

- updated metadata

## v2.0

- initial release
