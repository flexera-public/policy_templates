# Changelog

## v5.6.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v5.6.1

- Added default value for parameters that do not require user input

## v5.6

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.5

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v5.4

- Updated description of `Account Number` parameter

## v5.3

- Changed service metadata to "Compute" to ensure proper incident scraping

## v5.2

- Fixed output of `Tags` incident field
- Added `Resource Name` incident field
- Added `CPU Threshold` incident field
- Added `Memory Threshold` incident field
- Added `Threshold Type` incident fields
- Added `Lookback Period` incident fields
- Changed the internal names of several incident fields to ensure proper scraping for recommendations dashboard

## v5.1

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v5.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v4.3

- Added logic required for "Meta Policy" use-cases

## v4.2

- Added the following options to `param_threshold_statistic`: `p95` `p90`

## v4.1

- Added `param_threshold_statistic` which can be used to select the statistic used in determining an instance idle

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`). This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied. Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.7

- Added accountName field

## v3.6

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v3.5

- GetMetricData is now used to gather metrics data in batches for faster policy execution.
- Added parameter to allow user to decide whether both CPU and memory need to be under the specified threshold for an instance to be considered idle.
- Added an instance launch time field.

## v3.4

- fixed issue with multiple datapoints on cpu_usage to not show duplicate, incorrect cpu data
- updated memory usage fields to map with correct field and return value.
- updated output fields:
  - added "mem_minimum"
  - added "cpu_minimum"
  - changed "mem_maximum_value" to mem_maximum"
  - changed "mem_average_value" to "mem_average"

## v3.3

- updated savings_currency to savingsCurrency and fixed possible N/A value to 0.0

## v3.2

- Added default to aws_account_number parameter to enable existing API users.

## v3.1

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Normalizing fields for recommendations:
  - Renamed 'accountId' to 'accountID'
  - Renamed 'id' to 'resourceID'
  - Added 'resourceType' field
  - Changed 'savings' to be a plain number
  - Added 'savings_currency' to record the currency symbol.
  - Added a 'service' field, hardcoded to "EC2"

## v2.14

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.13

- Fix non-optimal array searching for costs

## v2.12

- Debug logs via param (off by default); use Optima host, not hardcoded hostname

## v2.11

- Added default_frequency "daily"

## v2.10

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.9

- Modified escalation label and description for consistency

## v2.8

- Added AWS Account ID to resource table

## v2.7

- formatted the incident detail message to display if no savings data available

## v2.6

- Include Total Estimated Monthly Savings in the incident message details
- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.5

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.4

- Updated escalation block

## v2.3

- add Estimated Monthly Savings

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.2

- update short_description

## v1.1

- Updating handle error.
- Change exclude tag description and regex
- changed default values to -1

## v1.0

- initial release
