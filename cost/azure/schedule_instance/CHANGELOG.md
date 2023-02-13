# Changelog

## v3.0

- Changed `'.statuses[1].code/"/"|.[1]'` to `'.statuses[] | select( .code | match("PowerState")) | .code[11:50]'` so that the right item in an array is selected for status

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
