# Changelog

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- fixed issue with potential nil pointer type error issue
- updated savings field to round to 3rd decimal
- updated displayName to subscription name more consistently
- Normalizing fields for recommendations:
  - updated 'tags' field to slice of string values
  - Renamed 'id' to 'resourceID'
  - Added 'subscriptionID' field
  - Added 'accountID' field with subscriptionID value
  - Added 'accountName' field with subscriptionName value
  - Changed 'savings' to be a plain number
  - Added 'savingsCurrency' to record the currency symbol.
  - Added 'service' field
  - Added 'resourceGroup' field
  - Added 'resourceType' field
  - Renamed 'location' to 'region'
  - Renamed 'name' to 'resourceName'

## v2.10

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.9

- Adding `allowed_values "management.azure.com", "management.chinacloudapi.cn"`

## v2.8

- Added subscription filter option and ability to specify Azure API endpoint

## v2.7

- Fix non-optimal array searching for costs

## v2.6

- Debug via param (off by default, for EU app); use rs_optima_host instead of hardcoded hostname

## v2.5

- Added default_frequency "daily"

## v2.4

- Updated policy to fetch cost details for multiple subscription IDs from Optima
- Updated escalation label for consistency

## v2.3

- Updated escalation block

## v2.2

- Adding incident resource table

## v2.1

- Resolved Age field mismatch issue

## v2.0

- initial release
