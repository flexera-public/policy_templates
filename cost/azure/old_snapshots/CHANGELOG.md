# Changelog

## v7.0

- Added support for regex when filtering resources by tag

## v6.2

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v6.1

- Policy action error logging modernized and now works as expected in EU/APAC

## v6.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if snapshot age or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v5.1

- Corrected issue with policy not retrieving cost data on orgs using newer Azure bill connections

## v5.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases

## v4.5

- Added `Size` incident field.

## v4.4

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

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

## v3.1

- remove duplicate data fields for subscriptionID and subscriptionName

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
