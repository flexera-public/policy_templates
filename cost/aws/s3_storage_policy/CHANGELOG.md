# Changelog

## v4.1.0

- Added support for attaching CSV files to incident emails.

## v4.0.7

- Updated label of email parameter to "Email Addresses" to match other policy templates. Functionality unchanged.

## v4.0.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.5

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v4.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter buckets by region and tags
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export
- Streamlined code for better readability and faster execution

## v3.1

- Updated description of `Account Number` parameter

## v3.0

- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- Added default to aws_account_number parameter to enable existing API users.

## v2.2

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.1

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.0

- Initial Release
