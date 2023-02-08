# Changelog

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
