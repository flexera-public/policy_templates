# Changelog

## v7.0.2

- Minor changes to policy template to pass lint tests. No functional changes.

## v7.0.1

- Minor changes to policy template to pass lint tests. No functional changes.

## v7.0.0

- Remove `next_stop`, `next_start` label requirements
- Add task labels to improve status updates and debugging for CWF actions
- Add error capture, graceful timeout handling for CWF actions

## v6.0

- Added support for regex when filtering resources by tag

## v5.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to specify custom tag keys for tracking instance schedules
- Added ability to filter resources by multiple tag key:value pairs
- Added ability for user to start and stop instances directly
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export for additional context
- Streamlined code for better readability and faster execution
- Policy action error logging modernized and now works as expected in EU/APAC

## v4.2

- Improved logging, and error capture/handling

## v4.1

- Updated description of `Account Number` parameter

## v4.0

- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

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

- modified the policy to handle start or stop time without minute value

## v2.1

- fix description

## v2.0

- initial release
