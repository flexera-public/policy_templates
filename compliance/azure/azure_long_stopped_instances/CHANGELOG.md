# Changelog

## v5.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v5.0

- Added support for regex when filtering resources by tag

## v4.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added more robust ability to filter resources by subscription
- Added ability to filter resources by region
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Streamlined code for better readability and faster execution

## v3.0

- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

## v2.9

- Replaced the term **whitelist** with **allowed list**.

## v2.8

- Added `ignore_status [400,403,404]` to mitigate errors from certain legacy subscription types

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added subscription filter option and ability to specify Azure API endpoint

## v2.4

- Modified escalation label and description for consistency

## v2.3

- Added resource table

## v2.2

- Modified policy for handling 404 error

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.3

- Removed need for `rg` tag
- Added additional logic to account for multiple statuses

## v1.2

- Added Permission block

## v1.1

- update short description

## v1.0

- initial release
