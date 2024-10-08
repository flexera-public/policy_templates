# Changelog

## v6.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v6.0.0

- Remove `next_stop`, `next_start` tag requirements
- Add check after stop/start request to validate expected status change
- Add task labels to improve status updates and debugging for CWF actions
- Add error capture, graceful timeout handling for CWF actions

## v5.0

- Added support for regex when filtering resources by tag

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to specify custom tag keys for tracking instance schedules
- Added ability to use subscription filter as an allow list or a deny list
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to filter resources by region
- Added ability for user to start and stop instances directly
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export for additional context
- Streamlined code for better readability and faster execution
- Policy action error logging modernized and now works as expected in EU/APAC

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

## v2.10

- Fixed bug related to Instance Status in the resulting incident data

## v2.9

- Replaced the term **whitelist** with **allowed list**.

## v2.8

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.7

- Modified cloud workflow Azure API to change `powerOff` to `deallocate` to release resources and start savings
- Mofified Azure API version to most updated `2022-08-01`

## v2.6

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.5

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.4

- Added subscription filter option and ability to specify Azure API endpoint

## v2.3

- "Delete schedule" action now removes the "schedule", "next_start" and "next_stop" tags

## v2.2

- Added default_frequency "daily"

## v2.1

- Modified escalation label and description for consistency

## v2.0

- initial release
