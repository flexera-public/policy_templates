# Changelog

## v0.4.1

- Added `resourceType` in violation data. This is to have "All Recommendations" to show correct "Resource Type".

## v0.4.0

- Updated API endpoint for cluster sizing.
- Added parameter `Shared Core` to indicate whether shared cores should be considered in the cluster sizing calculation.
- Added parameter `Architecture` to optimize cost calculations and resource allocation based on hardware architecture.

## v0.3.3

- Currency values in incident table are automatically converted to the local currency of the Flexera organization using the most recent exchange rate.

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
