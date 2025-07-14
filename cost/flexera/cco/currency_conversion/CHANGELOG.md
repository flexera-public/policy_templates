# Changelog

## v5.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v5.0.2

- Fixed issue where policy template execution would fail if the user builds off of the currency conversion adjustment created by this policy template.

## v5.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v5.0.0

- Multiple dimension/value pairs can now be used when applying currency conversion

## v4.0.0

- Policy now accepts any arbitrary cost dimension/value instead of requiring that currency conversion be done for a specific cloud provider

## v3.0

- Fixed issue where policy would fail if org has existing adjustment rules for future months
- Removed unused `Email Addresses` parameter
- Added `Set Organization Currency` parameter to automatically set the Flexera organization's currency

## v2.3

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.2

- Updated description to account for new file path in Github repository

## v2.1

- Added parameters to allow the user to configure currency conversion for previous months

## v2.0

- Removed requirement for dedicated xe.com credential
- Added Oracle Cloud support
- Added support for user-specified sources of cloud cost
- All parameters now have a default value
- Improvements to underlying policy code

## v1.0

- Initial release
