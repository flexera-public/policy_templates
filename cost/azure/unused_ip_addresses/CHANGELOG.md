# Changelog

## v3.1

- API endpoint fix

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- fixed issue with potential nil pointer type error issue
- updated savings field to round to 3rd decimal
- updated displayName to subscription name more consistently
- Normalizing fields for recommendations:
  - updated 'tags' field to slice of string values
  - Renamed 'ipAddressID' to 'resourceID' field
  - Added 'subscriptionID' field
  - Added 'accountID' field with subscriptionID value
  - Added 'accountName' field with subscriptionName value
  - Changed 'savings' to be a plain number
  - Added 'savingsCurrency' to record the currency symbol.
  - Added 'service' field
  - Renamed 'resourceGroupName' to 'resourceGroup'
  - Added 'resourceType' field
  - Renamed 'location' to 'region'
  - Renamed 'ipAddressName' to 'resourceName'

## v2.8

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.7

- Added subscription filter option and ability to specify Azure API endpoint

## v2.6

- Fix non-optimal array searching for costs

## v2.5

- Added default_frequency "daily"

## v2.4

- Updated policy to fetch cost details for multiple subscription ids from Optima
- updated escalation label for consistency

## v2.3

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.2

- Include Estimated Monthly Savings to each resource.
- Include Total Estimated Monthly Savings in the incident message details.
- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima.

## v2.1

- Fixed README link in short_description

## v2.0

- Initial release
