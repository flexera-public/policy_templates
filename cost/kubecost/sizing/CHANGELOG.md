# Changelog

## v0.6.0

- Increased the default `Minimum Savings Threshold` from 0 to 1, so that recommendations with no meaningful savings are no longer reported by default. This only affects new applications of the policy; existing applied policies keep their current setting unless updated.

## v0.5.4

- Added `hash_exclude` for volatile savings and utilization fields so that recalculated estimates alone no longer cause incidents to be treated as changed/reopened.
- Corrected the order of fields in the policy validation block to match the standard field ordering convention. No functional changes.

## v0.5.3

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.5.2

- Updated documentation link in policy description. Functionality unchanged.

## v0.5.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.5.0

- Added support for attaching CSV files to incident emails.

## v0.4.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.4.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.4.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.4.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.4.1

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v0.4.0

- Policy template renamed to `Kubecost Container Request Rightsizing Recommendations` to better reflect its functionality
- Kubecost API requests now use HTTPS for added security
- Policy template now falls back to Flexera-configured currency if Kubecost does not report a currency
- Added additional context to incident
- Renamed some incident fields to conform with other recommendations policy templates
- Streamlined code for better readability and faster execution
- Policy template now requires a valid Flexera credential

## v0.3

- Added `Scope` parameter to allow user to gather recommendations per cluster or across the entire account. Previously, the recommendations were always requested overall the account.

## v0.2

- The CPU quantile and Memory quantile parameters are now percentiles.

## v0.1

- Initial release
