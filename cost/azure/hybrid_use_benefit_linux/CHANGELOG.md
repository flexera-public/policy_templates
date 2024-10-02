# Changelog

## v5.1.1

- Fixed issue where policy actions were not properly reporting errors

## v5.1.0

- Added `Resource Hourly Cost` and `Currency` to incident table for added context

## v5.0

- Added support for regex when filtering resources by tag

## v4.3

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v4.2

- Fixed issue where policy fails if an instance lacks Image Publisher metadata

## v4.1

- Fixed README link in policy metadata

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
- Added ability to filter resources by region
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export
- Streamlined code for better readability and faster execution

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
