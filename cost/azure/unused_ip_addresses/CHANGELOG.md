# Changelog

## v7.1

- Added IP allocation type (Dynamic or Static) to incident output
- Added ability to filter results by allocation type via parameter
- Added ability to filter results by minimum savings via parameter

## v7.0

- Added support for regex when filtering resources by tag

## v6.3

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v6.2

- Refactored code for Delete IP Address Action to improve debugging and error handling

## v6.1

- Corrected issue with policy not retrieving cost data on orgs using newer Azure bill connections

## v6.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to specify how long an IP address should be unattached to consider it unused
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v5.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Fixed issue with incident not properly including messaging

## v4.7

- Fixed an issue causing some incidents to raise an error instead of populating correctly

## v4.6

- New escalations are no longer created if Estimated Monthly Savings or Savings Currency have changed, but nothing else has

## v4.5

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v4.4

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v4.3

- Replaced the term **whitelist** with **allowed list**.

## v4.2

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v4.1

- Added `ignore_status` for 400 and 404 to Azure API calls
- Added logic to handle where `resourceType` is null

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.4

- Removed duplicate data fields for subscriptionID and subscriptionName

## v3.3

- Updated policy template to make fewer calls to Azure APIs
- Added 'ipAddress' field to policy export
- Changed default_frequency to "monthly"

## v3.2

- Added new check properties.natGatway == null for unused IP check

## v3.1

- Use provided keyword for Optima endpoint

## v3.0

- Applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Fixed issue with potential nil pointer type error issue
- Updated savings field to round to 3rd decimal
- Updated displayName to subscription name more consistently
- Normalizing fields for recommendations:
  - Updated 'tags' field to slice of string values
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

- Updated README.md rightscale documentation links with docs.flexera documentation links

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
