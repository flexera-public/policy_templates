# Changelog

## v3.1.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.1.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.1.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.1

- Policy updated so that policy is correctly identified as a Flexera policy

## v3.0

- Policy renamed to `SaaS Manager - Deactivated Users for Integrated Applications` to better reflect its functionality
- Added `Inactive Days Threshold` to allow user to filter out recently deactivated users
- Added `Applications` parameter to allow user to filter results by application
- Updated policy to use public SaaS Manager API
- Added support for APAC API endpoint
- Policy now uses and requires a general Flexera One credential
- Incident summary now includes applied policy name
- General code cleanup and normalization

## v2.1

- added "host" logic to support both NAM or EU endpoints

## v2.0

- initial release
