# Changelog

## v2.11

- Updated policy README file with a deeper explanation of how the GCP recommender works and the roles required to use it.

## v2.10

- Modified the number of GCP recommender API calls that can be done before waiting to prevent a quota limit error: 100 request per minute.

## v2.9

- Added `IP Address` incident field.

## v2.8

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard
- Added "Tags" to incident output

## v2.7

- Fix: Duplicated entries from incident report were removed.

## v2.6

- Changed list API to aggregatedList API to get addresses
- Modified filters, previously applied in code, now those are applied in request
- Fix: Wrong number of rows in incident

## v2.5

- Added policySet as Unused IP Addresses to populate the Total Potential Savings

## v2.4

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- remove duplicate data fields for subscriptionID and subscriptionName

## v2.2

- added project name/id/number fields and moved account versions to end

## v2.1

- Fixed missing savings field

## v2.0

- Initial Release
