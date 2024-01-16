# Changelog

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
