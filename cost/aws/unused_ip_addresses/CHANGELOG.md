# Changelog

## 5.2

- Added `Resource Name` incident field

## v5.1

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v5.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v4.1

- Added logic required for "Meta Policy" use-cases

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`). This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied. Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.6

- Added accountName call and field
- updated fields to match new field conventions of camel-case

## v3.5

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v3.4

- Updated savings_currency to savingsCurrency

## v3.3

- Added default to aws_account_number parameter to enable existing API users.

## v3.2

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v3.1

- Improve savings calculations by using the AWS Pricing API which is significantly faster and more memory efficient than retrieving the AWS price sheet JSON file

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Normalizing fields for recommendations:
  - Renamed 'all_tags' to 'tags'
  - Renamed 'accountId' to 'accountID'
  - Renamed 'id' to 'resourceID'
  - Changed 'savings' to be a plain number
  - Added 'savings_currency' to record the currency symbol.
  - Added a 'service' field, hardcoded to "EC2"

## v2.16

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.15

- Added default_frequency "daily"

## v2.14

- Improve error handling and debug logging so that errors from taking action are actually surfaced
- Add a `param_log_to_cm_audit_entries` parameter to control whether action debug logging is sent to CM Audit
  Entries; this should be left set to No on Flexera EU

## v2.13

- Modified policy to use per hour cost for unused IP from AWS pricing document for calculating estimated savings.

## v2.12

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.11

- Modified escalation label and description for consistency

## v2.10

- Uncommenting allowed_values for `param_automatic_action`

## v2.9

- Added AWS Account ID to resource table
- Exclude Elastic IPs that have an Association ID

## v2.8

- Use `DescribeAddresses` instead of `DescribeRegions` to more accurately check if the call is enabled by the
  Service Control Policy in each region

## v2.7

- formatted the incident detail message to display if no savings data available

## v2.6

- Included Total Estimated Monthly Savings in the incident detail messages

## v2.5

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.4

- corrected the Exclude Tags parameter description

## v2.3

- corrected the tag format

## v2.2

- fix description

## v2.1

- Fix typo in parameter name to `param_exclude_tags`

## v2.0

- initial release
