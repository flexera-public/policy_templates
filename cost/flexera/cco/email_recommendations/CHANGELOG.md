# Changelog

## v0.10.3

- Fixed an issue where filtering by cloud account could fail with an error for recommendations that do not include a cloud account name.
- Fixed an issue where filtering by billing center could fail with an error for recommendations that do not include a billing center name.
- Fixed an issue where the policy could fail with an error while processing recommendation types that do not include extended recommendation details.

## v0.10.2

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.10.1

- Added `hash_exclude` for volatile savings and utilization fields so that recalculated estimates alone no longer cause incidents to be treated as changed/reopened.
- Corrected the order of fields in the policy validation block to match the standard field ordering convention. No functional changes.

## v0.10.0

- Added support for AWS and Azure cross-family compute recommendations.
- Added support for Kubernetes recommendations.

## v0.9.0

- New `Dimension List` parameter allows filtering recommendations by Rule-Based Dimensions and Tag Dimensions.
- `Billing Center List` parameter now supports all Billing Centers instead of just top-level ones.
- Incident table now shows both top-level and bottom-level Billing Center for each recommendation.
- Added option to filter for only active recommendations.
- Added support for additional recommendation types.

## v0.8.2

- Updated documentation link in policy description. Functionality unchanged.

## v0.8.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.8.0

- Added support for Oracle recommendations.
- Added support for additional recommendations for AWS, Azure, and Google.

## v0.7.0

- Added support for attaching CSV files to incident emails.

## v0.6.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.6.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.6.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v0.6.0

- Added support for additional recommendation policy templates
- Changed "Disk" option to "Storage" for `Recommendation List` parameter to better reflect functionality
- Added "PaaS" option to `Recommendation List` parameter

## v0.5.0

- Added parameter `Always Email Incident` that forces incident to always be emailed if enabled
- Added support for `AWS Rightsize EBS Volumes` recommendations
- Added support for `AWS Unused Classic Load Balancers` recommendations
- Added support for `Azure Rightsize Managed Disks` recommendations
- Added support for `Azure Rightsize NetApp Files` recommendations
- Added support for `Google Old Snapshots` recommendations

## v0.4

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v0.3

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v0.2

- Updated description to account for new file path in Github repository

## v0.1

- Initial Release
