# Changelog

## v0.2.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.2.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.2.2

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v0.2.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v0.2

- Modified policy to correctly report cost as potential savings
- Added `Minimum Savings Threshold` parameter to filter out recommendations with low savings potential
- Added total `Potential Monthly Savings` to incident description
- Extended policy to include resources outside of RDS and EKS where applicable

## v0.1

- Initial Release
