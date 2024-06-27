# Changelog

## v5.4.0

- Added `Threshold Statistic` parameter to assess utilization based on CPU maximum, p90, p95, or p99 metrics
- Added CPU minimum, maximum, p90, p95, and p99 metrics to incident table

## v5.3.0

- Modified internal names for incident fields for more accurate scraping into Optimization dashboard

## v5.2.1

- Fixed a bug causing $0 recommendations

## v5.2.0

- New fields added to incident output: `Last Accessed` and `Status`

## v5.1.1

- Unused SQL Databases incident now includes a `Recommended Capacity` field with a value of `Delete Instance` for ease of analyzing recommendations from the Flexera Optimization dashboard

## v5.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.0

- Added support for regex when filtering resources by tag

## v4.4

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v4.3

- Added optional `Minimum Age (Days)` parameter to filter results by age

## v4.2

- Policy action error logging modernized and now works as expected in EU/APAC

## v4.1

- Fixed issue where policy would fail if databases were found with no SKU

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added potential savings to recommendations
- Added ability to only report recommendations that meet a minimum savings threshold
- Added incident for unused instances based on lack of connections
- Added ability to delete unused instances
- Added ability to configure how many days back to consider when determining if instance is unused or underutilized
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to filter resources by region
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if statistics or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.13

- Added `Lookback Period` incident field.
- Added `Subscription ID` incident field.
- Added `Resource Type` incident field.
- Added `Threshold` incident field.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.12

- Replaced the term **whitelist** with **allowed list**.

## v2.11

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.10

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.8

- Added subscription filter option and ability to specify Azure API endpoint

## v2.7

- Debug via param (off by default, for EU app)

## v2.6

- Added default_frequency "daily"

## v2.5

- Ignored Elastic pool databases getting listed in incident.
- Display Recommendation as Change tier when SQL database can not downsize because it's already at it's min size or can not upsize because it's already at it's max

## v2.4

- Removed recommendation capacity for minimun capacity value.

## v2.3

- Added Resource table

## v2.2

- Skip resources that do not return a SKU value

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.2

- Included Update action for Downsize or Upsize SQL Databases after user approval

## v1.1

- Readme link fixed.
- Only show instances that has a recommendation

## v1.0

- Initial Release
