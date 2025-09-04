# Changelog

## v3.0.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.6

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v3.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.4

- Fixed an issue where applied policy would fail in certain scenarios due to an undefined field.
- Fixed an issue where applied policy would return false positives in the policy incident.

## v3.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Policy template renamed to `AWS S3 Buckets Accepting HTTP Requests` to better reflect its functionality
- Buckets can now be filtered by region, tag, or name
- Added additional fields to incident table for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.5

- Updated description of `Account Number` parameter

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
