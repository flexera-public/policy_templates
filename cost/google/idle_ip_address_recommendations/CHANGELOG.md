# Changelog

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
