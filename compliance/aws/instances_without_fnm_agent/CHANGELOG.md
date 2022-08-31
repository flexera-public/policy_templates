# Changelog

## v2.10

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## 2.9

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
