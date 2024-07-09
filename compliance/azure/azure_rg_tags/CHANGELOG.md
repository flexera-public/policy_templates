# Changelog

## v2.7.1

- Deprecated: This policy is no longer being updated.
- Changed `service` value in policy template metadata to `All`

## v2.7

- fixed link to README in policy description

## v2.6

- Replaced the term **whitelist** with **allowed list**.

## v2.5

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.4

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added subscription filter option and ability to specify Azure API endpoint

## v2.1

- Adding Resource Table

## v2.0

- Changed the authentication to credential services

## v1.3

- Added Permission block

## v1.2

- Added Approval block

## v1.1

- url encode client secret

## v1.0

- initial release
