# Changelog

## v4.3.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v4.3.1

- Added default value for parameters that do not require user input

## v4.3

- Updated description of `Account Number` parameter

## v4.2

- Changed service metadata to "Compute" to ensure proper incident scraping

## v4.1

- Added logic required for "Meta Policy" use-cases

## v4.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v3.0

- Updated policy to use Flexera One ITAM SOAP APIs. Full details here: [Flexera One ITAM SOAP APIs Transitioning to Flexera One IAM](https://community.flexera.com/t5/Flexera-One-Blog/Flexera-One-ITAM-SOAP-APIs-Transitioning-to-Flexera-One-IAM/ba-p/229399)
- Removed support for on-premise deployments (with or without wstunnel)

## v2.10

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.8

- Added default to aws_account_number parameter to enable existing API users.

## v2.7

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.4

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.3

- adding incident resource table

## v2.2

- Merged Cloud and On premise into one policy.

## v2.1

- remove unnecessary permissions block

## v2.0

- Added support for on-premise FlexNet Manager (NTLM auth).
- Changes to support the Credential Service.

## v1.0

- initial release
