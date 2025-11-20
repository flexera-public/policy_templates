# Changelog

## v6.2.0

- Added support for attaching CSV files to incident emails.

## v6.1.6

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v6.1.5

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v6.1.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v6.1.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v6.1.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v6.1.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v6.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v6.0

- Added support for regex when filtering resources by tag

## v5.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v5.0

- Added option to either gracefully or forcefully power off instances
- Renamed policy actions to conform with Azure's own terminology and documentation
- Policy action error logging modernized and now works as expected in EU/APAC

## v4.2

- Fixed error where policy would sometimes report on stopped instances
- Fixed minor language error in incident output

## v4.1

- Added `Operating System` incident field.
- Renamed field from `osType` to `platform`

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter resources by multiple tag key:value pairs
- Added several fields to incident export to provide additional context
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Policy no longer raises new escalations for the same resource if incidental metadata has changed
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential
- Added logic required for "Meta Policy" use-cases

## v3.0

- Renamed Subscription List parameter for consistency and accuracy
- Added logic required for "Meta Policy" use-cases
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.0

- initial release
