# Changelog

## v5.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.0

- Added support for regex when filtering resources by tag

## v4.3

- Policy action error logging modernized and now works as expected in EU/APAC

## v4.2

- Corrected API issue when executing policy in APAC

## v4.1

- Updated description of `Account Number` parameter

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to filter resources by multiple tag key:value pairs
- Added several fields to incident export to provide additional context
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Policy no longer raises new escalations for the same resource if incidental metadata has changed
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential
- Added logic required for "Meta Policy" use-cases

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

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.4

- Modified escalation label and description for consistency

## v2.3

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.2

- Adding incident resource table

## v2.1

- correct Category value

## v2.0

- initial release
