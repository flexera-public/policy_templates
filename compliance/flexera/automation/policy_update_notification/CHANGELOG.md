# Changelog

## v2.2.1

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v2.2

- Updated policy metadata to ensure that it does not publish to the catalog

## v2.1

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v2.0

- Policy now works in all Flexera orgs regardless of zone
- Policy now requires a valid Flexera One credential
- Policy no longer makes use of deprecated APIs
- Policy no longer reports on multiple accounts within a Flexera organization
- Policy no longer raises new escalations if applied policy name or catalog template version number changed but nothing else has
- Improved incident export for clarity and detail
- Streamlined code for better readability and faster execution

## v1.1

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.0

- initial release
