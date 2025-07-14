# Changelog

## v0.3.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.3.1

- Fixed issue that would cause policy template to fail when "Last 30 Days" was selected for the "Date Range" parameter.

## v0.3.0

- Fixed issue that would cause policy template to fail when "Last 7 Days" was selected for the "Date Range" parameter.
- "Dimensions List" parameter now accepts both dimension names and dimension IDs as valid inputs.
- Markdown tables in incident now uses pretty names for various fields to improve readability.

## v0.2.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.2.1

- Fixed broken README link in policy template description

## v0.2.0

- Fixed bug that related to Summarized Unallocated amount and Unallocated Percent of Total in report
- Added filter for excluding rows that are below a certain percent of total costs
- Added Time Period and Filters to report output
- Added `unallocated` (bool) and `unallocated_details` (string) columns to report output
- Report column order will match the order user provided in parameter input

## v0.1.0

- Initial release
