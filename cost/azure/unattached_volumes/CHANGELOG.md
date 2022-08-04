# Changelog

## v3.1

- update policy for optimization, changes go as follows:
  - removal of filtering on events and combining data of disks and activity
  - iterate through filtered unattached disks rather than subscriptions to lower number of api requests due to pagination
  - changed Azure insight filter from event resource type to resource id

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- fixed issue with potential nil pointer type error issue
- updated savings field to round to 3rd decimal
- updated displayName to subscription name more consistently
- Normalizing fields for recommendations:
  - updated 'tags' field to slice of string values
  - Added 'resourceID' field
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

## v2.12

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.11

- Added "ignore-status" for 400, 403, 404 errors

## v2.10

- Fix non-optimal array searching for costs

## v2.9

- Adding subscription filter to deal with timeout

## v2.8

- Added `and resourceProvider eq 'Microsoft.Compute' and resourceType eq 'Microsoft.Compute/VirtualMachines'` to event filter
  to get smaller but more specific result set to help with ExecutionTimeout.

## v2.7

- Debug via param (off by default, for EU app); use rs_optima_host, not hardcoded hostname

## v2.6

- Adding Azure China

## v2.5

- Added default_frequency "daily"

## v2.4

- Updated policy to fetch cost details for multiple subscription ids from Optima
- Modified escalation label and description for consistency

## v2.3

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.2

- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.1

- Include Estimated Monthly Savings to each resource
- Include Total Estimated Monthly Savings in the incident summary
- Added Selectable resources and actions

## v2.0

- initial release
