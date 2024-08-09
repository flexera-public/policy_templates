# Changelog

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
