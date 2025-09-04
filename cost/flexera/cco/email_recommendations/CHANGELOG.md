# Changelog

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
