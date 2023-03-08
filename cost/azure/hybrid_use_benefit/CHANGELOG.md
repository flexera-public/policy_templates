# Changelog

## v2.12

- Replaced the term **whitelist** with **allowed list**.

## v2.11

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.10

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.8

- Adding `allowed_values "management.azure.com", "management.chinacloudapi.cn"`

## v2.7

- Added subscription filter option and ability to specify Azure API endpoint

## v2.6

- Added default_frequency "daily"

## v2.5

- Modified escalation label and description for consistency

## v2.4

- updated the policy to check for AHUB in Windows Server using licenseType

## v2.3

- modified policy to check for AHUB in Windows Server Instances only

## v2.2

- Added resource Table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services

## v1.3

- Updated Permission block

## v1.2

- Added Permission block

## v1.1

- url encode client secret

## v1.0

- initial release
