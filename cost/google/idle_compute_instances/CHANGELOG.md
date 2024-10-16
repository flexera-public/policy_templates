# Changelog

## v2.11.3

- Minor code improvements to conform with current standards. Functionality unchanged.

## v2.11.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v2.11.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v2.11

- CPU and memory utilization data is now retrieved using GCP Monitoring Query Language
- Instance data is now retrieved in bulk requests per zone

## v2.10

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.8

- Debug via param (off by default, for EU app)

## v2.7

- Added default_frequency "daily"

## v2.6

- Modified escalation label and description for consistency

## v2.5

- Updated escalation block

## v2.4

- Bug fix for when metrics are absent in a project

## v2.3

- Adding incident resource table

## v2.2

- Bug fixes on unhandled errors when executing

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services
- Added new datasource for google project ID

## v1.1

- update short_description

## v1.0

- initial release
