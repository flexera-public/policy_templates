# Changelog

## v3.4

- Use provided keyword for Optima endpoint

## v3.3

- updated savings_currency to savingsCurrency

## v3.2

- Added default to aws_account_number parameter to enable existing API users.

## v3.1

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Normalizing fields for recommendations:
  - Renamed 'tag_set' to 'tags'
  - Renamed 'accountId' to 'accountID'
  - Renamed 'id' to 'resourceID'
  - Renamed 'instanceType' to 'resourceType'
  - Changed 'savings' to be a plain number
  - Added 'savings_currency' to record the currency symbol.
  - Added a 'service' field, hardcoded to "RDS"

## v2.11

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.10

- Fix non-optimal array searching for costs

## v2.9

- Added default_frequency "daily"

## v2.8

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.7

- Modified escalation label and description for consistency

## v2.6

- Added AWS Account ID to resource table

## v2.5

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.4

- Include Estimated Monthly Savings to each resource.
- Include Total Estimated Monthly Savings in the incident message details.

## v2.3

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.0

- initial release
