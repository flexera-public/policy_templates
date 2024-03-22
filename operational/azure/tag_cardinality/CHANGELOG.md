# Changelog

## v3.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v3.0

- Added "Subscription Allowed List" parameter to enable Subscription filtering
- Added logic required for "Meta Policy" use-cases
- Added parameter for Azure API endpoint to support Azure China
- Policy now requires a valid Flexera credential to facilitate "Meta Policy" use-cases

## v2.3

- A list of the unique tag values is now included as a column in the incident

## v2.2

- policy now reports cardinality proper instead of tag values directly

## v2.1

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v2.0

- initial release
