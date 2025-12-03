# Changelog

## v2.1.2

- Fixed an issue where applied policy would fail due to an undefined variable.

## v2.1.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v2.1.0

- Added support for attaching CSV files to incident emails.

## v2.0.9

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.0.8

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v2.0.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.0.6

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.0.5

- Minor change to policy template `short_description`. Functionality unchanged.

## v2.0.4

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.0.3

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v2.0.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v2.0.1

- Fixed issue affecting incidents in meta parent policy. Base policy functionality is unchanged.

## v2.0.0

- Renamed policy template to `Azure Rightsize NetApp Resources` to better reflect its functionality
- Added ability to use regex to filter resources by tag
- Added `Recommendation` field to incident table for parity with other Azure policy templates
- Added logic to skip gathering volume-level data if the user selects "Resize Pools"
- Several policy parameters updated to more clearly describe their function
- Incident subject now explicitly indicates that the resources found are oversized
- Fixed issue where policy template would fail to complete if some subscriptions and resources are inaccessible due to credential permissions
- Fixed issue where tag filtering was not working as intended

## v1.2

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v1.1

- Updated the `short_description` of the policy to match with the Flexera documentation.

## v1.0

- Initial release.
