# Changelog

## v3.1.0

- Improved policy execution speed by batching CloudWatch requests.
- Fixed issue where policy execution would fail when trying to retrieve bucket regions.

## v3.0

- Several parameters altered to be more descriptive and human-readable
- `Size Threshold (GiB)` parameter no longer expects user to specify size in bytes
- Added ability to filter buckets by region and tags
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.10

- Updated description of `Account Number` parameter

## v2.9

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.8

- Added default to aws_account_number parameter to enable existing API users.

## v2.7

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added default_frequency "daily"

## v2.4

- Adding AWS Account Id

## v2.3

- fix description

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.2

- Updated region datasources to use github data list

## v1.1

- Added Permission block

## v1.0

- initial release
