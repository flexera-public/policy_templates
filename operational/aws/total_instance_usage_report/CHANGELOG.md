# Changelog

## v1.1.8

- Fixed an issue where the reported start of the usage period could be off by a month when the policy ran near the end of certain calendar months.
- Fixed an issue where the policy could fail to generate a report when no instance usage data was found for the selected billing centers, regions, and time period.

## v1.1.7

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v1.1.6

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v1.1.5

- Updated documentation link in policy description. Functionality unchanged.

## v1.1.4

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v1.1.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v1.1.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v1.1.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v1.1.0

- Policy template now uses dynamically updated list of instance types.

## v1.0.4

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v1.0.3

- Minor code improvements to conform with current standards. Functionality unchanged.

## v1.0.2

- Fixed issue with URL encoding causing the chart to not render in emails in some instances.

## v1.0.1

- Fixed issue with Billing Center filter so users can now successfully allow/deny Billing Centers from the Usage Report.

## v1.0.0

- Initial release
