# Changelog

## v2.0.6

- Changed description to say "policy template" for clarity. Functionality unchanged.

## v2.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v2.0.4

- Deprecated: This policy template is no longer being updated. Please see policy README for more information.

## v2.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v2.0.2

- Minor code improvements to bring template in line with current standards. Functionality unchanged.

## v2.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.0.0

- Policy now supports `Previous Month` for `Month To Ingest` parameter
- Reworked parameters to be more clear and consistent with other policy templates
- Streamlined code for better readability and faster execution

## v1.1

- Updated template metadata `service` and `policy_set` fields to be in line with other CBI policies.
- Added parameter to allow user to specify the billing period as either the current month or a specific historical month.
- Removed `permission` declaration as is deprecated.

## v1.0

- initial release
