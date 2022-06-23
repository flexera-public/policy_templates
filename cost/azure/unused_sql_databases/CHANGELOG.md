# Changelog

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v3.1

- Use provided keyword for Optima endpoint

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Added Optima cost and billing center api calls to provide savings data
- fixed issue with potential nil pointer type error issue
- updated savings field to round to 3rd decimal
- Added total savings summary message
- updated displayName to subscription name more consistently
- Normalizing fields for recommendations:
  - updated 'tags' field to slice of string values
  - Renamed 'id' to 'resourceID'
  - Added 'subscriptionID' field
  - Added 'accountID' field with subscriptionID value
  - Added 'accountName' field with subscriptionName value
  - Added 'savings' field
  - Added 'savingsCurrency' to record the currency symbol.
  - Added 'service' field
  - Renamed 'resource_group' to 'resourceGroup'
  - Renamed 'type' to 'resourceType'
  - Renamed 'location' to 'region'
  - Renamed 'name' to 'resourceName'
  - Renamed 'kind' to 'resourceKind'

## v2.10

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.9

- removing extra automatic action

## v2.8

- Added subscription filter option and ability to specify Azure API endpoint

## v2.7

- Debug via param (off by default, for EU app)

## v2.6

- Added default_frequency "daily"

## v2.5

- Modified escalation label and description for consistency

## v2.4

- Added Resource table

## v2.3

- fix tag exclusion logic

## v2.2

- fix null error for sku.name

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.0

- initial release
