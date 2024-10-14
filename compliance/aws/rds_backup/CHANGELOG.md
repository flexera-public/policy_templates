# Changelog

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Policy template category changed to `Compliance`
- Resources can be filtered via region using either an allow or deny list
- Resources can now be filtered by tag
- Resources can now be tested for backup window or retention period in isolation
- Added additional incident fields to add context
- Normalized incident export to be consistent with other policies
- Policy template no longer raises new escalations if tag data changed but nothing else has
- Streamlined code for better readability and faster execution
- Policy template now requires a valid Flexera credential

## v2.8

- fixed link to README in policy description

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.5

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.4

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.1

- Adding incident resource table

## v2.0

- Changes to support the Credential Service

## v1.2

- Use inferred regions in auth method

## v1.1

- removing icons from short description as icons break automated documentation

## v1.0

- initial release
