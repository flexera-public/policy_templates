# Changelog

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
