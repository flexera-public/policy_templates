# Changelog

## v2.12

- Added default to aws_account_number parameter to enable existing API users.

## v2.11

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.10

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.9

- Updated next instance size logic to account for missing instance type in instance_types.json

## v2.8

- Debug log via param (off by default)

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

- Adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.1

- Fixing path for json

## v1.0

- initial release
