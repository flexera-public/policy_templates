# Changelog

## v2.10.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.10.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v2.10.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v2.10

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.8

- Ignoring Custom Tiers from google results

## v2.7

- Debug via param (off by default, for EU app)

## v2.6

- Added default_frequency "daily"

## v2.5

- Modified escalation label and description for consistency

## v2.4

- Moved CPU calculations and memory calculations from jmespath to jq inside datasource

## v2.3

- Added resource table

## v2.2

- Bug fixes on unhandled errors when executing

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services
- Added new datasource for google project ID
- Removed Extra authentication

## v1.1

- update policy name and short description

## v1.0

- Initial Release
