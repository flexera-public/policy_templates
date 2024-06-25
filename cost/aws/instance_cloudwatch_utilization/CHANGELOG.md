# Changelog

## v3.3.1

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v3.3

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v3.2

- Updated description of `Account Number` parameter

## v3.1

- Changed service metadata to "Compute" to ensure proper incident scraping

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.16

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.15

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.14

- Added default to aws_account_number parameter to enable existing API users.

## v2.13

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.12

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.11

- Debug log via parameter, off by default (for EU compatibility)

## v2.10

- Added default_frequency "daily"

## v2.9

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.8

- Modified escalation label and description for consistency

## v2.7

- Added AWS Account ID to resource table

## v2.6

- Fix issue with duplicate records displayed in the detail template

## v2.5

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.4

- Updated regex for param_exclusion_tag_key to allow for null
- Updated next instance size logic to account for missing instance type in instance_types.json

## v2.3

- Updated escalation block

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service
- Removed tagging action
- Added downsize action

## v1.5

- Added Approval block

## v1.4

- Fixing Readme

## v1.3

- Adding in better regex
- Updating inputs

## v1.2

- Adding windows support

## v1.1

- Adding Tag Exclusion
- Adding Average used memory percentage, Average used CPU percentage, Action Tag Key:Value
- Adding Action to tag instances

## v1.0

- initial release
