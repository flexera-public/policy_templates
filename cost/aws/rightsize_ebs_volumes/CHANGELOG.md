# Changelog

## v0.6.2

- Fixed an issue where recommendations for older standard volumes could fail when a rightsize recommendation was generated without any existing provisioned IOPS.

## v0.6.1

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.6.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default.

## v0.5.10

- Minor code formatting cleanup. No functional or user-facing changes.

## v0.5.9

- Improved the policy's reliability when checking which AWS regions it can access, making it less likely to fail to run due to expected access restrictions in certain regions

## v0.5.8

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.5.7

- Fixed bug where the `!~` exclusion tag operator incorrectly excluded resources whose tag value matched the regex instead of those that did not match

## v0.5.6

- Fixed issue with incident table that cause policy execution to fail

## v0.5.5

- Updated documentation link in policy description. Functionality unchanged.

## v0.5.4

- Fixed a bug introduced in v0.5.3 that would cause "Cannot access member 'result' of undefined", if the AWS account info does not exist in Flexera.

## v0.5.3

- Added fallback mechanism for retrieving AWS account information when the Flexera List Cloud Accounts API does not return relevant account info.

## v0.5.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.5.1

- Updated email escalation declaration for new "Errors Identified" incident to prevent error `failed make a CSV attachment with data: unable to collect csv data from nil export`

## v0.5.0

- Policy now continues execution for accessible regions when some regions return permission errors
- Added separate incident report to identify regions with access issues and provide remediation guidance

## v0.4.0

- Added support for attaching CSV files to incident emails.

## v0.3.9

- Fixed issue with `GetMetricData` API request when gathering CloudWatch metrics. Functionality unchanged.

## v0.3.8

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.3.7

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.3.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.3.5

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.3.4

- Added batch processing for large datasources as a performance enhancement (reduces memory usage) with no changes to logic or functionality.

## v0.3.3

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v0.3.2

- Added `hide_skip_approvals` field to the info section, enabling the UI to dynamically show or hide the "Skip Approval" option. Functionality unchanged.

## v0.3.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.3.0

- Added `Exclusion Types` parameter to allow the user to exclude certain volume types from the results.

## v0.2.0

- Added `Resource ARN` to incident table.

## v0.1.0

- Initial release
