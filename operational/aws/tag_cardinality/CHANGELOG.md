# Changelog

## v3.3.5

- Combined reports now skip child incidents that do not include result rows instead of failing intermittently.

## v3.3.4

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v3.3.3

- Improved the policy's reliability when checking which AWS regions it can access, making it less likely to fail to run due to expected access restrictions in certain regions

## v3.3.2

- Updated the `ds_flexera_api_hosts` datasource to support an additional internal testing environment. No functional changes for existing users.

## v3.3.1

- Updated AWS Organizations API calls to ensure compatibility with upcoming changes to AWS APIs. Functionality unchanged.

## v3.3.0

- Added graceful error handling for inaccessible AWS regions

## v3.2.2

- Updated documentation link in policy description. Functionality unchanged.

## v3.2.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.2.0

- Added support for attaching CSV files to incident emails.

## v3.1.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.1.6

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v3.1.5

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.1.4

- Added batch processing for large datasources as a performance enhancement (reduces memory usage) with no changes to logic or functionality.

## v3.1.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.1.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.1.1

- Fixed bug related to pagination on the AWS Tagging API

## v3.1

- Added parameter to enable region filtering

## v3.0

- Added logic required for "Meta Policy" use-cases

## v2.3

- A list of the unique tag values is now included as a column in the incident

## v2.2

- fixed issue with inconsistent cardinality results

## v2.1

- policy now reports cardinality proper instead of tag values directly

## v2.0

- initial release
