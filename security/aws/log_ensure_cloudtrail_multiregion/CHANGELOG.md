# Changelog

## v3.0.7

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v3.0.6

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Policy template renamed to `AWS CloudTrail Not Enabled In All Regions` to better reflect its functionality
- Improved readability of incident output with additional formatting and context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.1

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.0

- initial release
