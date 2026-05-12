# Changelog

## v0.2.0

- Added "AI/ML Views" dashboard to the built-in dashboards added by this policy template.
- Fixed an issue where selecting a dashboard name not recognized by the policy could cause the policy to fail with an error.
- Fixed an issue where dashboards that failed to download (e.g. due to an invalid or inaccessible URL) could cause unnecessary failed creation attempts.
- Fixed an issue where dashboards that already existed in Flexera would incorrectly appear in the incident report as newly created.
- The incident report title now correctly displays the name of the applied policy.

## v0.1.4

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.3

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.1.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.0

- Initial Release
