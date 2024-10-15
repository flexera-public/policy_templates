# Changelog

## v5.0.1

- Removed datasource that was not necessary for results

## v5.0.0

- Remove `next_stop`, `next_start` label requirements
- Remove static zone to region mapping logic
- Add task labels to improve status updates and debugging for CWF actions
- Add error capture, graceful timeout handling for CWF actions

## v4.0

- Added support for regex when filtering resources by label

## v3.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to specify custom label keys for tracking instance schedules
- Added ability to filter resources by project
- Added ability to filter resources by region
- Added ability to filter resources by multiple label key:value pairs
- Added ability for user to start and stop instances directly
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export for additional context
- Streamlined code for better readability and faster execution
- Policy action error logging modernized and now works as expected in EU/APAC
- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

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
