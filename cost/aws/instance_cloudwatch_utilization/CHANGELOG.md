# Changelog

## v2.9

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.8

- Modified escalation label and description for consistency

## v2.7

- Added AWS Account ID to resource table

## v2.6

- Fix issue with duplicate records displayed in the detail template

## v2.5

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.4

- Updated regex for param_exclusion_tag_key to allow for null
- Updated next instance size logic to account for missing instance type in instance_types.json

## v2.3

- Updated escalation block

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service
- Removed tagging action
- Added downsize action

## v1.5

- Added Approval block

## v1.4

- Fixing Readme

## v1.3

- Adding in better regex
- Updating inputs

## v1.2

- Adding windows support

## v1.1

- Adding Tag Exclusion
- Adding Average used memory percentage, Average used CPU percentage, Action Tag Key:Value
- Adding Action to tag instances

## v1.0

- initial release
