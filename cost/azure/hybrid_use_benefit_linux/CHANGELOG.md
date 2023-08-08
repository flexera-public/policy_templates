# Changelog

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.10

- Replaced the term **whitelist** with **allowed list**.

## v2.9

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.8

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.7

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.6

- Added "ignore-status" for 400, 403, 404 errors

## v2.5

- Adding `allowed_values "management.azure.com", "management.chinacloudapi.cn"`

## v2.4

- Added subscription filter option and ability to specify Azure API endpoint

## v2.3

- Added default_frequency "daily"

## v2.2

- corrected buggy filter to find only RHEL and SLES Linux AHub eligible vms

## v2.1

- modified headline and links to docs

## v2.0

- applicable to RHEL and SLES Linux
- includes automatic actions
- exclude free linux distributions like Ubuntu
