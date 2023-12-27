# Changelog

## v2.5

- Improved logging, and error capture/handling
- Added default values for params that are not required

## v2.4

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added default_frequency "daily"

## v2.1

- converted list of timezone objects to one object in timezones_list.json
- modified policy for getting timezone value from updated timezones_list.json and handled incorrect timezone format

## v2.0

- initial release
