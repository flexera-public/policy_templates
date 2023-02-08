# Changelog

## v2.12

- Replaced the term **whitelist** with **allowed list**.

## v2.11

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.10

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.8

- Added subscription filter option and ability to specify Azure API endpoint

## v2.7

- Convert resource type to lower case for comparison (Microsoft is not consistent with the case)

## v2.6

- Drop namespace from resource type when looking up supported API versions

## v2.5

- Removed the sys_log function as it was not used

## v2.4

- Get the type from the resource object, and check whether it supports tags

## v2.3

- fix broken link to the README file

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Fixed README link in short_description
- Updated category values from "compliance" to Compliance

## v2.0

- initial release
