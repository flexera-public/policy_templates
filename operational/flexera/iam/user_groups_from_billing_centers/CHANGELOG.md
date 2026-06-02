# Changelog

## v0.2.1

- Updated group grant and revoke actions to use the newer Flexera IAM API (`PUT /iam/v1/orgs/{org_id}/access-rules/grant` and `/access-rules/revoke`) instead of the deprecated billing center grant/revoke endpoints.
- Removed unused `ds_access_rules` and `ds_role_ids` datasources.

## v0.2.0

- Added support for attaching CSV files to incident emails.

## v0.1.0

- Initial release
