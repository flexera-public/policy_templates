# Changelog

## v0.3.0

- Fixed issue where valid CBI Endpoint IDs were not being accepted when applying the policy template.
- Increased precision of daily cost calculation to avoid rounding errors producing slightly incorrect results.

## v0.2.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.2.1

- Minor code improvements to bring template in line with current standards. Functionality unchanged.

## v0.2.0

- Policy template will no longer fail if there is an incomplete bill upload. Incomplete bill uploads are now aborted prior to creating a new bill upload.

## v0.1.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.1.0

- Initial release
