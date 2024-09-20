# Changelog

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
