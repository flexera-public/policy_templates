# Changelog

## v4.2.0

- Added `Resource Hourly Cost` and `Currency` to incident table for added context

## v4.1.0

- Added ability to filter results by SQL resource type via `SQL Resource Types` parameter
- Added ability to filter results by SQL Virtual Machine image SKU via `SQL Virtual Machine Image SKUs` parameter
- Fixed bug where Elastic Pool recommendations were not properly reported in incident

## v4.0

- Fixed bug where databases ineligible for AHUB would appear in incident
- Added support for Elastic Pool recommendations, including automated actions
- Several parameters altered to be more descriptive and human-readable
- Added improved subscription, region, and tag filtering for results
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Streamlined code for better readability and faster execution

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.8

- Added a filter to exclude SQL Server 2017 Developer and Express versions instances that Microsoft provides as free

## v2.7

- Replaced the term **whitelist** with **allowed list**.

## v2.6

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.5

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added "ignore-status" for 400, 403, 404 errors

## v2.1

- Added subscription filter option and ability to specify Azure API endpoint

## v2.0

- Includes Azure SQL databases, SQL Virtual machines, SQL Managed Instances
- detects eligible instances
- AHUB can automatically be applied

## v1.0

- Initial release
