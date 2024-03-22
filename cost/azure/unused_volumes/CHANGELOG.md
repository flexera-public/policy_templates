# Changelog

## v8.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v8.0

- Added support for regex when filtering resources by tag

## v7.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v7.0

- Policy now retrieves read/write stats to determine if a volume is unused
- Added ability to include attached volumes in the incident and to action on them
- Added parameters to allow the user to configure the new functionality above

## v6.1

- Refactored the Delete Volume and Create Snapshot Actions to use updated Azure APIs, improve debugging, and error handling

## v6.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Removed ability to filter by how long a policy was detached; see README for more details
- Added ability to filter by volume age
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if ages or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v5.1

- Corrected issue with policy not retrieving cost data on orgs using newer Azure bill connections

## v5.0

- Renamed Subscription List parameter for consistency and accuracy

## v4.10

- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v4.9

- Added logic required for "Meta Policy" use-cases

## v4.8

- Added `lookBackPeriod` incident field grabbing value from `param_unattached_days` parameter.
- Renamed `diskSize` incident field to `size`.

## v4.7

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v4.6

- Fixed issue with subscription filtering not working correctly.
- Fixed issue causing savings values to not be properly shown in incident.
- Formatted tags in incident output to improve readability.

## v4.5

- General code optimization to improve execution time.

## v4.4

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v4.3

- Replaced the term **whitelist** with **allowed list**.

## v4.2

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v4.1

- bugfix for logic regarding activity log and what constitutes unattached/unused. Changed logic to verify that activities length is 0 rather than using "toBeDetached" keyword
- updated max limit on activity log call to 89 days to avoid api day limit
- updated response to contain usable information of resourceID and operation name
- changed ds field responseBody to resourceID

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`). This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied. Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.2

- remove duplicate data fields for subscriptionID and subscriptionName

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
