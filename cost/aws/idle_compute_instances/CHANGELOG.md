# Changelog

## v2.13

- Fix non-optimal array searching for costs

## v2.12

- Debug logs via param (off by default); use Optima host, not hardcoded hostname

## v2.11

- Added default_frequency "daily"

## v2.10

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.9

- Modified escalation label and description for consistency

## v2.8

- Added AWS Account ID to resource table

## v2.7

- formatted the incident detail message to display if no savings data available

## v2.6

- Include Total Estimated Monthly Savings in the incident message details
- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.5

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.4

- Updated escalation block

## v2.3

- add Estimated Monthly Savings

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.2

- update short_description

## v1.1

- Updating handle error.
- Change exclude tag description and regex
- changed default values to -1

## v1.0

- initial release
