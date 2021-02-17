# Changelog

## v2.14

- Improve error handling and debug logging so that errors from taking action are actually surfaced
- Add a `param_log_to_cm_audit_entries` parameter to control whether action debug logging is sent to CM Audit
  Entries; this should be left turned off on Flexera EU

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
