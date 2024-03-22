# Changelog

## v5.5

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.4

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v5.3

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v5.2

- Corrected issue with policy, tags were being sent in an unsupported format

## v5.1

- Corrected issue with policy not retrieving cost data on orgs using newer Azure bill connections

## v5.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases

## v4.8

- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v4.7

- Added `Lookback Period` incident field.
- Added `Threshold` incident field.
- Added `Platform` incident field.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v4.6

- New escalations are no longer created if Estimated Monthly Savings or CPU Average have changed, but nothing else has.

## v4.5

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v4.4

- Fixed error that prevented Cloud Workflow actions from completing as expected.

## v4.3

- Replaced the term **whitelist** with **allowed list**.

## v4.2

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v4.1

- Fixed bug when filtering by tag key when Azure API does not return tag data for an instance

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.1

- remove duplicate data fields for subscriptionID and subscriptionName

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- fixed issue with potential nil pointer type error issue
- updated savings field to round to 3rd decimal
- Normalizing fields for recommendations:
  - updated 'tags' field to slice of string values
  - Renamed 'id' to 'resourceID'
  - Added 'accountID' field with subscriptionID value
  - Added 'accountName' field with subscriptionName value
  - Changed 'savings' to be a plain number
  - Added 'savingsCurrency' to record the currency symbol.
  - Added 'service' field
  - Renamed 'rg' to 'resourceGroup'
  - Added 'resourceType' field
  - Renamed 'location' to 'region'
  - Renamed 'vmname' to 'resourceName'
  - Renamed 'averagecpu' to 'averageCPU'

## v2.14

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.13

- Added "ignore-status" for 400, 403, 404 errors

## v2.12

- Fix non-optimal array searching for costs

## v2.11

- Adding subscription filter to deal with timeout

## v2.10

- Debug param added (off by default, for EU app); use rs_optima_host, not hardcoded hostname

## v2.9

- Added default_frequency "daily"

## v2.8

- Use the right API version to get the monitor/metrics, and use the biggest interval (ie "P1D", ie one-day)

## v2.7

- Updated policy to fetch cost details for multiple subscription ids from Optima
- Modified escalation label and description for consistency

## v2.6

- formatted the incident detail message to display if no savings data available

## v2.5

- Included Estimated Monthly Savings to each resource.
- Included Total Estimated Monthly Savings in the incident message details.

## v2.4

- Updated escalation block

## v2.3

- Fixed unhandled error

## v2.2

- adding incident resource table

## v2.1

- Changes to replicate Subscription Name in the final response

## v2.0

- Changes to support the Credential Service

## v1.0

- initial release
