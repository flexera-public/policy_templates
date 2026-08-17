# Changelog

## v1.3.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default. This only affects new applications of the policy; existing applied policies keep their current setting unless updated.

## v1.2.3

- Updated policy logic for internal consistency; no functional or user-facing changes.

## v1.2.2

- Improved the policy's reliability when checking which AWS regions it can access, making it less likely to fail to run due to expected access restrictions in certain regions

## v1.2.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v1.2.0

- Updated cost estimation to reflect AWS's tiered Extended Support pricing: a lower rate for years 1-2 and a higher rate starting in year 3, selected automatically based on the current date.
- Estimated savings for Multi-AZ RDS instances now account for both the primary and standby instance vCPUs, since AWS bills extended support for both.
- Added a `Rate Tier` field to the incident export showing which pricing tier applies to each resource.
- ElastiCache Extended Support is now correctly modeled as a percentage premium on the node's on-demand rate rather than a flat node-hour fee.
- MariaDB instances are no longer reported by this policy; they are not eligible for AWS RDS Extended Support.

## v1.1.0

- Updated incident/export region reporting to use AWS API region identifiers (for example, `us-east-1`) for consistency with other AWS optimization policy sets.

## v1.0.1

- Fixed issue with incident table that cause policy execution to fail

## v1.0.0

- Policy template is now named `AWS Resources Under or Approaching Extended Support`.
- Policy template now required an AWS credential and has a meta parent for use with multiple AWS accounts.
- Added `Days Until Extended Support` parameter to report resources approaching extended support within a user-specified number of days.
- Added `Resource Type`, `Engine Version`, `Status`, `Extended Support Start Date`, `Extended Support End Date`, and `Days Until Extended Support` fields to the incident export.
- Added `Exclusion Tags` and `Exclusion Tags: Any / All` parameters to allow filtering resources by tag

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
