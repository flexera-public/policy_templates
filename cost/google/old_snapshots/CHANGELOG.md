# Changelog

## v3.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to filter resources by project
- Added ability to use wildcards when filtering resources by label
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera One credential

## v2.12

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.11

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.10

- Check for the case where labels is null (or undefined) on a snapshot

## v2.9

- Debug via param (off by default, for EU app)

## v2.8

- Added default_frequency "daily"

## v2.7

- Added missing pagination to the request for snapshot list

## v2.6

- Removing unused ds, js and start_date and end_date variables

## v2.5

- Modified escalation label and description for consistency

## v2.4

- Updated escalation block

## v2.3

- add ignore_status block to snapshot API call

## v2.2

- rounded off Age in Days column to Whole number
- adding incident resource table

## v2.1

- rename policy

## v2.0

- initial release
