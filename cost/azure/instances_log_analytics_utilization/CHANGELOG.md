# Changelog

## v2.20.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v2.20.1

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v2.20

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.19

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v2.18

- Replaced the term **whitelist** with **allowed list**.

## v2.17

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.16

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.15

- Added 'timespan' parameter
- Updated README.md 'input parameters' section to reflect added 'timespan' parameter

## v2.14

- Updated README.md rightscale documentation links with docs.flexera documentation links

## v2.13

- Adding subscription filter to deal with timeout

## v2.12

- Fixed bug causing incompatible rightsizing recommendations

## v2.11

- Debug via param (off by default, for EU app)

## v2.10

- Added default_frequency "daily"

## v2.9

- Modified escalation label and description for consistency

## v2.8

- Added handling for log analytics workspaces that don't exist

## v2.7

- Updated policy to check for log analytics and diagnostic enabled VM using resource properties field

## v2.6

- Updated escalation block
- Fix spelling in path

## v2.5

- Modified policy for handling 404 error

## v2.4

- Adjusted Log Analytics auth provider tag

## v2.3

- Adding incident resource table

## v2.2

- Remove unnecessary permissions block

## v2.1

- Fixed bug where Azure returns instance details without MemoryGB field

## v2.0

- Removed the tagging escalation/action
- Added Resize action for underutilized instances
- Changed the authentication to credential services

## v1.1

- Added Approval block

## v1.0

- Initial release
