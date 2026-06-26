# Changelog

## v3.4.0

- Added "Treat Disabled Public Network Access as Compliant" parameter to optionally exclude storage accounts with public network access disabled from results. Default value preserves existing behavior.

## v3.3.1

- Fixed bug where the `!~` exclusion tag operator incorrectly excluded resources whose tag value matched the regex instead of those that did not match

## v3.3.0

- Added `Allow/Deny Resource Groups` and `Allow/Deny Resource Groups List` filter parameters to allow filtering resources by resource group

## v3.2.0

- Added error incident when no Azure Subscriptions are found, indicating a potential credential or permissions issue.

## v3.1.0

- Added support for attaching CSV files to incident emails.

## v3.0.6

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.4

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v3.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Policy template renamed to `Azure Storage Accounts Allowing Default Network Access` to better reflect its functionality
- Added ability to filter results by storage account name, subscription, region, or tags
- Added additional fields to incident output for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.3

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.2

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.1

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.0

- initial release
