# Changelog

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0

- Several parameters altered to be more descriptive and human-readable
- Added more robust ability to filter resources by subscription
- Added ability to filter resources by region
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to use regex when filtering resources by tag
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Added logic required for "Meta Policy" use-cases
- To facilitate "Meta Policy" use-cases, policy now requires a Flexera credential

## v2.5

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v2.4

- Replaced the term **whitelist** with **allowed list**.

## v2.3

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.2

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.1

- Adding subscription filter to deal with timeout

## 2.0

- Initial Release
