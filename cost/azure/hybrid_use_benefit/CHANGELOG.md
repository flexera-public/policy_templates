# Changelog

## v5.2.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v5.2.6

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v5.2.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v5.2.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v5.2.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v5.2.2

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v5.2.1

- Fixed issue where policy actions were not properly reporting errors

## v5.2.0

- Added `Resource Hourly Cost` to incident table for added context

## v5.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.0

- Added support for regex when filtering resources by tag

## v4.3

- Fixed issue where currency conversion would sometimes not work as expected.

## v4.2

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v4.1

- Added the currency separator for savings message

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
- Added ability to filter resources by region
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added estimated savings to incident export
- Added additional fields to incident export to facilitate scraping for dashboards
- Streamlined code for better readability and faster execution

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

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
