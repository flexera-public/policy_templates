# Changelog

## v3.3.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.3.0

- Update tag resource action to use Azure Tags API, which enables `Tag Contributor` role to be used for enabling action capabilities with minimum scope.

## v3.2.2

- Fixed issue where prompt for adding tags incorrectly said to use "key:value" instead of "key=value" format.
- Fixed issue where tags would fail to apply to Azure subscriptions.

## v3.2.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.2.0

- Added option to include Azure subscriptions and resource groups in the results alongside Azure resources

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Added ability to filter resources by tag key, tag key==value, or using regex
- Added ability to filter resources by region
- Added ability to filter resources by Azure resource type
- Added ability to use all filters as an allow list or a deny list
- Added additional context to incident description
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera One credential

## v2.13

- Updated `param_tags_to_check` parameter to take a list of tag keys, as opposed to a list of tag key-value pairs
- Updated tag logic to return 'Missing Tag Keys' as well as 'Tag Keys with Missing Tag Values' in incident

## v2.12

- Replaced the term **whitelist** with **allowed list**.

## v2.11

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.10

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.9

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.8

- Added subscription filter option and ability to specify Azure API endpoint

## v2.7

- Convert resource type to lower case for comparison (Microsoft is not consistent with the case)

## v2.6

- Drop namespace from resource type when looking up supported API versions

## v2.5

- Removed the sys_log function as it was not used

## v2.4

- Get the type from the resource object, and check whether it supports tags

## v2.3

- fix broken link to the README file

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Fixed README link in short_description
- Updated category values from "compliance" to Compliance

## v2.0

- initial release
