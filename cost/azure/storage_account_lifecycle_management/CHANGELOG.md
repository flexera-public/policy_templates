# Changelog

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
- Removed `Azure API Wait Time` parameter
- Added ability to filter results by subscription, region, or tag
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.6

- Replaced the term **whitelist** with **allowed list**.

## v2.5

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.4

- Added "Azure API Wait Time" parameter to prevent Azure API throttling
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added "ignore-status" for 400, 403, 404 errors

## v2.1

- Added subscription filter option and ability to specify Azure API endpoint

## v2.0

- initial release
