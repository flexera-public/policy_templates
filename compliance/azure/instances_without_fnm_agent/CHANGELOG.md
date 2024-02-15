# Changelog

## v4.2

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v4.1

- Changed internal name of escalation code to ensure "Meta Policy" works as expected

## v4.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases

## v3.0

- Updated policy to use Flexera One ITAM SOAP APIs. Full details here: [Flexera One ITAM SOAP APIs Transitioning to Flexera One IAM](https://community.flexera.com/t5/Flexera-One-Blog/Flexera-One-ITAM-SOAP-APIs-Transitioning-to-Flexera-One-IAM/ba-p/229399)
- Removed support for on-premise deployments (with or without wstunnel)

## v2.10

- Case-insensitive matching of computerName from report with Azure VM name

## v2.9

- Replaced the term **whitelist** with **allowed list**.

## v2.8

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- Updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added subscription filter option and ability to specify Azure API endpoint

## v2.4

- Modified escalation label and description for consistency

## v2.3

- Added resource table

## v2.2

- Merged Cloud and On premise into one policy.

## v2.1

- Remove unnecessary permissions block

## v2.0

- Added support for on-premise FlexNet Manager (NTLM auth).
- Changes to support the Credential Service.

## v1.0

- Initial release
