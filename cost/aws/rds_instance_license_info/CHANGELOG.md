# Changelog

## v4.2.8

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.2.7

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v4.2.6

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.2.5

- Policy template metadata modified so that it is no longer published in the catalog.

## v4.2.4

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.2.3

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.2.2

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v4.2.1

- Added default value for parameters that do not require user input

## v4.2

- Deprecated: This policy template is no longer being updated. Please see policy README for more information.

## v4.1

- Updated description of `Account Number` parameter

## v4.0

- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.10

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

- Added default_frequency "daily"

## v2.4

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.3

- Modified escalation label and description for consistency
- Added incident resource table

## v2.2

- Added AWS Account ID to resource table

## v2.1

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.0

- Initial release
