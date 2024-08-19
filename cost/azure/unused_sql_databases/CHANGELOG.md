# Changelog

## v5.4.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v5.4.1

- Added default value for parameters that do not require user input

## v5.4

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.3

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v5.2

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v5.1

- Corrected issue with policy not retrieving cost data on orgs using newer Azure bill connections

## v5.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases

## v4.6

- Added `Lookback Period` incident field.
- Added `Platform` incident field.
- Updated value ouput from `Resource Type` incident field.

## v4.5

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v4.4

- Fixed the comparison made to match the instance's costs with the instance's usage; this caused some instances not to show savings, although they were added to the incident.

## v4.3

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v4.2

- Replaced the term **whitelist** with **allowed list**.

## v4.1

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.2

- remove duplicate data fields for subscriptionID and subscriptionName

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
