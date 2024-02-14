# Changelog

## v4.0

- Policy name changed to reference EC2 service directly
- Several parameters altered to be more descriptive and human-readable
- Added ability to filter resources by multiple tag key:value pairs
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export for added context
- Policy no longer raises new escalations if tag data has changed but nothing else has
- Streamlined code for better readability and faster execution
- Added logic required for "Meta Policy" use-cases
- Flexera credential now required to facilitate meta policy use cases

## v3.2

- Updated description of `Account Number` parameter

## v3.1

- Changed service metadata to "Compute" to ensure proper incident scraping

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.12

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.11

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.10

- Added default to aws_account_number parameter to enable existing API users.

## v2.9

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.8

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.7

- Added default_frequency "daily"

## v2.6

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.5

- Modified escalation label and description for consistency

## v2.4

- Added AWS Account ID to resource table

## v2.3

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.0

- initial release
