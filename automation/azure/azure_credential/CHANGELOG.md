# Changelog

## v0.5.0

- Migrated the Meta Parent policy from the legacy governance API to the current Flexera policy API for applied policy management (self policy lookup, published/uploaded template lookup, and child policy create/update/delete). No change in behavior; child policy management, credential status reporting, and the single-child-policy design remain the same. Also added the "Attach CSV To Consolidated Incident Email", "Consolidated Incident Table Rows for Email Body", and "Skip Consolidated Incident" parameters, and a "Delete Child Policies" approval action for child policies that report an error, for consistency with other meta parent policies.

## v0.4.0

- The Meta Parent policy now updates the child policy whenever the "Policy Schedule" parameter is changed, in addition to updating on other parameter changes. Previously, changing the schedule alone did not trigger an update of the child policy's run frequency.

## v0.3.3

- Improved reliability when consolidating credential test results that may be missing summary details.

## v0.3.2

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.3.1

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v0.3.0

- Added error incident when no Azure Subscriptions are found, indicating a potential credential or permissions issue.

## v0.2.0

- Added `Incident Table Rows for Email Body` and `Attach CSV To Incident Email` parameters to support sending a CSV attachment with incident emails.

## v0.1.7

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.6

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.1.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.4

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v0.1.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.1

- Updated service field in metadata to "Identity & Access Management". Functionality unchanged.

## v0.1.0

- Initial release
