# Changelog

## v2.15

- Improve error handling and debug logging so that errors from taking action are actually surfaced
- Add a `param_log_to_cm_audit_entries` parameter to control whether action debug logging is sent to CM Audit
  Entries; this should be left set to No on Flexera EU

## v2.14

- Add a parameter to override the Flexera One org ID to use when querying Optima for cases when the project is not
  in the same org where the AWS bill is registered in Optima

## v2.13

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.12

- Modified escalation label and description for consistency

## v2.11

- Require a minimum value of `1` on the `param_unattached_days` parameter

## v2.10

- Adding AWS Account Id

## v2.9

- Use `DescribeVolumes` instead of `DescribeRegions` to more accurately check if the call is enabled by the
  Service Control Policy in each region

## v2.8

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.7

- added total estimated monthly savings in the incident detail message
- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.6

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.5

- Updated escalation block

## v2.4

- add Estimated Monthly Savings

## v2.3

- adding incident resource table

## v2.2

- Bug fixes
- The policy is renamed to unused volumes and that it now uses cloudwatch to determine if it's unused.

## v2.1

- rename policy

## v2.0

- initial release
