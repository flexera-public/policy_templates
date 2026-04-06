# Changelog

## v1.0.0

- Policy template is now named `AWS Resources Under or Approaching Extended Support`.
- Policy template now required an AWS credential and has a meta parent for use with multiple AWS accounts.
- Added `Days Until Extended Support` parameter to report resources approaching extended support within a user-specified number of days.
- Added `Resource Type`, `Status`, `Extended Support Start Date`, `Extended Support End Date`, and `Days Until Extended Support` fields to the incident export.

## v0.3.3

- Updated documentation link in policy description. Functionality unchanged.

## v0.3.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.3.1

- Fixed issue that was preventing the policy template from being updated in the catalog. Functionality unchanged.

## v0.3.0

- Added support for attaching CSV files to incident emails.

## v0.2.7

- Updated label of email parameter to "Email Addresses" to match other policy templates. Functionality unchanged.

## v0.2.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

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
