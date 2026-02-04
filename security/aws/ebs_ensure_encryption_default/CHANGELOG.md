# Changelog

## v4.0.7

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v4.0.6

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v4.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.4

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v4.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.0

- Policy template renamed to `AWS Regions Without Default EBS Encryption` to better reflect its functionality
- Expanded region filtering options
- Several parameters altered to be more descriptive and human-readable
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.3

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.1

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.0

- initial release
