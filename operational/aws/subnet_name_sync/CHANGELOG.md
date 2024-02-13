# Changelog

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added several fields to incident export to provide additional context
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy action error logging modernized and now works as expected in EU/APAC
- Policy now requires a valid Flexera credential
- Added logic required for "Meta Policy" use-cases

## v3.1

- Updated description of `Account Number` parameter

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.10

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.8

- Added default to aws_account_number parameter to enable existing API users.

## v2.7

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.6

- Removing Publish for EU, no longer updating NAM

## v2.5

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.4

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.1

- adding incident resource table

## v2.0

- Changed the authentication to credential services

## v1.3

- Use inferred regions in auth method

## v1.2

- Added Approval block

## v1.1

- update policy name

## v1.0

- initial release
