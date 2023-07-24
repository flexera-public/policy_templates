# Changelog

## v4.0

- Added logic required for "Meta Policy" use-cases
- Updated template and readme to reflect addition of `auth_flexera`

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.9

- Updated `param_tags_to_check` parameter to take a list of tag keys, as opposed to a list of tag key-value pairs
- Updated tag logic to return 'Missing Tag Keys' as well as 'Tag Keys with Missing Tag Values' in incident

## v2.8

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.7

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.6

- Added default to aws_account_number parameter to enable existing API users.

## v2.5

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.4

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.3

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.0

- initial release
