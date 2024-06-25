# Changelog

## v4.0.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to only report specific event types
- Added ability to filter events by how soon they are scheduled to occur
- Added more robust tag filtering
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export
- Policy no longer raises new escalations if incidental metadata about a resource or event has changed
- Streamlined code for better readability and faster execution

## v3.2

- Updated description of `Account Number` parameter

## v3.1

- Changed service metadata to "Compute" to ensure proper incident scraping

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.9

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.8

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.7

- Added default to aws_account_number parameter to enable existing API users.

## v2.6

- Added support for a single AWS STS Cross account role to be used for multiple policies.

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

- Changes to support the Credential Service

## v1.0

- initial release
