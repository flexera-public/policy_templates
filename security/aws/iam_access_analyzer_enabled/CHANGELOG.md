# Changelog

## v4.0.7

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v4.0.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.3

- Updated service field in metadata to "Identity & Access Management". Functionality unchanged.

## v4.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.0.0

- Policy template renamed to `AWS Regions Without Access Analyzer Enabled` to better reflect its functionality
- Expanded region filtering options
- Several parameters altered to be more descriptive and human-readable
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v3.1

- Updated description of `Account Number` parameter

## v3.0

- Added functionality to support region inclusion/exclusion.
- Added parameter to enable Allow or Deny filtering by user entered regions.

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- Added default to aws_account_number parameter to enable existing API users.

## v2.2

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.1

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.0

- initial release
