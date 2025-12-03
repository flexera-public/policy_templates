# Changelog

## v3.2.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.2.1

- Updated email escalation declaration for new "Errors Identified" incident to prevent error `failed make a CSV attachment with data: unable to collect csv data from nil export`

## v3.2.0

- Policy now continues execution for accessible regions when some regions return permission errors
- Added separate incident report to identify regions with access issues and provide remediation guidance

## v3.1.0

- Added support for attaching CSV files to incident emails.

## v3.0.1

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.0

- Changed savings calculation to improve accuracy. See README for more details.

## v2.4.3

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v2.4.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.4.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.4.0

- Policy template now uses dynamically updated list of instance types.
- Fixed issue where incident would not contain pricing information for Linux instances.

## v2.3.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.3.2

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v2.3.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v2.3.0

- Added `Resource ARN` to incident table.

## v2.2.0

- Fixed bug where invalid recommendations with no new resource type would sometimes be included in results
- Added `Fallback Instance Type Category` parameter to provide alternate recommendations when the selected category is not available

## v2.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v2.0

- Added support for regex when filtering resources by tag

## v1.4

- Fixed issue where currency conversion would sometimes not work as expected.

## v1.3

- Corrected API issue when executing policy in APAC

## v1.2

- updated short description README link

## v1.1

- Updated description of `Account Number` parameter

## v1.0

- initial release
