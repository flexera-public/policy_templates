# Changelog

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
