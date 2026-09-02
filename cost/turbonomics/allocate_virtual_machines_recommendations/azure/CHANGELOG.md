# Changelog

## v2.3.10

- Fixed an issue where some allocation recommendations could fail when coverage data was missing or had no baseline capacity.

## v2.3.9

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v2.3.8

- Added `hash_exclude` for volatile savings and utilization fields so that recalculated estimates alone no longer cause incidents to be treated as changed/reopened.

## v2.3.7

- Fixed an issue that could cause the policy to fail when retrieving business unit information

## v2.3.6

- Updated documentation link in policy description. Functionality unchanged.

## v2.3.5

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v2.3.4

- Updated label of email parameter to "Email Addresses" to match other policy templates. Functionality unchanged.

## v2.3.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.3.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.3.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.3.0

- Switched from cookie-based authentication to token-based authentication

## v2.2

- Shows the actual name of the compute instance at field **Current Compute Tier**.
- Fixes the Virtual Machine RI Coverage Before and Virtual Machine RI Coverage Before shown in the report.

## v2.1

- Field **source** was added to the template.
