# Changelog

## v0.6.5

- Updated label of email parameter to "Email Addresses" to match other policy templates. Functionality unchanged.

## v0.6.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.6.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.6.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.6.1

- Switched from cookie-based authentication to token-based authentication

## v0.6

- Added Hyperlinks for `System Details URL` incident field.

## v0.5

- Renamed `Storage Access` incident field to `Provisioned IOPs`.
- Renamed `Storage Amount` incident field to `Size`.
- Renamed `Attachment State` incident field to `State`.
- Renamed `Created Time` incident field to `Action Created Time`.
- Renamed `Last Attached VM` incident field to `Last VM`.
- Renamed `Unused Days` parameter to `Days Unattached`.
- Removed hardcoded host on business units path.

## v0.4

- Added `Storage Access` incident field.
- Added `Last Attached VM` incident field.
- Added `Action State` incident field.
- Added `Disruptiveness` incident field.
- Added `Reversibility` incident field.
- Added `System Details URL` incident field.
- Renamed `Size` incident field to `Storage Amount`.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v0.3

- Fixed readme Link in the policy.

## v0.2

- Links to documentation were added to the short description of the policy.

## v0.1

- Initial release
