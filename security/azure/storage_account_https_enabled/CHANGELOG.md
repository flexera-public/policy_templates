# Changelog

## v2.7.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v2.7

- fixed link to README in policy description

## v2.6

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.5

- Replaced the term **whitelist** with **allowed list**.

## v2.4

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.3

- Removed unused `sys_log` definition
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.1

- Added subscription filter option and ability to specify Azure API endpoint

## v2.0

- Initial release
