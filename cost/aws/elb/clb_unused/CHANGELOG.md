# Changelog

## v2.15

- Added default to aws_account_number parameter to enable existing API users.

## v2.14

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.13

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.12

- Fix non-optimal array searching for costs

## v2.11

- Debug log via param (off by default); use rs_optima_host instead of hardcoded hostname

## v2.10

- Added default_frequency "daily"

## v2.9

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.8

- Modified escalation label and description for consistency

## v2.7

- Added AWS Account ID to resource table

## v2.6

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.5

- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.4

- Include Estimated Monthly Savings to each resource
- Include Total Estimated Monthly Savings in the incident summary

## v2.3

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.2

- Use inferred regions in auth method

## v1.1

- Updating the file by removing reference URL

## v1.0

- initial release
