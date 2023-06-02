# Changelog

## v2.11

Optimized the execution time of the policy by using the following approaches:

- CPU utilization data is now retrieved using GCP Monitoring Query Language; before, the Flexera platform did the calculations, but now those are done faster on GCP resources.
- Memory utilization data is now retrieved using GCP Monitoring Query Language; before, the Flexera platform did the calculations, but now those are done faster on GCP resources.
- Instance data is now retrieved using a much faster API endpoint that retrieves the data of all the instances in every zone.

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
