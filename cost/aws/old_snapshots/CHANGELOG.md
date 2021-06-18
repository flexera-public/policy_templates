# Changelog

## v2.15

- Use rs_optima_host instead of hardcoded hostname.

## v2.14

- Added default_frequency "daily"

## v2.13

- Improve error handling and debug logging so that errors from taking action are actually surfaced
- Add a `param_log_to_cm_audit_entries` parameter to control whether action debug logging is sent to CM Audit
  Entries; this should be left set to No on Flexera EU

## v2.12

- Add a parameter to override the Flexera One org ID to use when querying Optima for cases when the project is not
  in the same org where the AWS bill is registered in Optima

## v2.11

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.10

- Modified escalation label and description for consistency

## v2.9

- Require a minimum value of `1` on the `snapshot_age` parameter

## v2.8

- Added AWS Account ID to resource table

## v2.7

- Use `DescribeSnapshots` instead of `DescribeRegions` to more accurately check if the call is enabled by the
  Service Control Policy in each region

## v2.6

- Include Estimated Monthly Savings to each resource
- Include Total Estimated Monthly Savings in the incident summary

## v2.5

- Changed the default deregister image action from Yes to No.

## v2.4

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.3

- Updated escalation block

## v2.2

- Bug fix on when the snapshot was unable to delete when attached to AMI

## v2.1

- adding incident resource table

## v2.0

- initial release
