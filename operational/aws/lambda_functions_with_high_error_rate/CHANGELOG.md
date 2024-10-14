# Changelog

## v5.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v5.0.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter resources by multiple tag key:value pairs and using regex
- Added ability to specify how many hours back to gather error data for
- Policy now uses more efficient and modern method for gathering error data
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export for added context
- Policy no longer raises new escalations if inconsequential metadata has changed
- Streamlined code for better readability and faster execution

## v4.2.1

- Added default value for parameters that do not require user input

## v4.2

- Changed internal name of escalation code to ensure "Meta Policy" works as expected

## v4.1

- Updated description of `Account Number` parameter

## v4.0

- Added logic required for "Meta Policy" use-cases
- Flexera credential now required to facilitate meta policy use cases.

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.5

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.3

- Added default to aws_account_number parameter to enable existing API users.

## v2.2

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.1

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.0

- initial release
