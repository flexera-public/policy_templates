# Changelog

## v0.3.3

- Updated from /model/savings/clusterSizing to /model/savings/clusterSizingETL.
- Created new functions to handle the modified response format from the updated endpoint.
- Modified functionality to generate incident correctly based on the new response structure.
- New Parameters:
  - param_allow_shared_core: Specifies whether shared cores should be considered in the cluster sizing calculation.
  - param_include_overhead: Ensures overhead costs are correctly included in the cost calculations.

## v0.3.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.3.1

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v0.3.0

- Policy template renamed to `Kubecost Cluster Rightsizing Recommendation` to better reflect its functionality
- Kubecost API requests now use HTTPS for added security
- Policy template now falls back to Flexera-configured currency if Kubecost does not report a currency
- Added additional context to incident
- Renamed some incident fields to conform with other recommendations policy templates
- Streamlined code for better readability and faster execution
- Policy template now requires a valid Flexera credential

## v0.2

- Renamed 'monthlySavings' incident field to 'savings'
- Renamed 'accountId' incident field to 'accountID'

## v0.1

- Initial Release
