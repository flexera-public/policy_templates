# Changelog

## v4.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.0.0

- Policy template renamed to `AWS Internet-Accessible Elastic Load Balancers` to better reflect its functionality
- Added more robust tag-filtering options
- Added additional fields to incident table for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

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

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.1

- Use inferred regions in auth method

## v1.0

- initial release
