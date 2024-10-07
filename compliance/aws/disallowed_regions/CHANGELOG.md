# Changelog

## v5.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v5.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if tag data has changed for an instance
- Policy action error logging modernized and now works as expected in EU/APAC
- Streamlined code for better readability and faster execution

## v4.1

- Updated description of `Account Number` parameter

## v4.0

- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

## v3.1

- Changed service metadata to "Compute" to ensure proper incident scraping

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.8

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.7

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.6

- Flipped parameter to enable user to specify which reasons to allow instead of which to disallow.

## v2.5

- Added default to aws_account_number parameter to enable existing API users.

## v2.4

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.0

- initial release
