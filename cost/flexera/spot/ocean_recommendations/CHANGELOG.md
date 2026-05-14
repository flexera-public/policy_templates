# Changelog

## v0.4.1

- Added error detection for Ocean clusters that fail to return rightsizing recommendations, with a separate incident that includes the specific error code, affected cluster details, troubleshooting steps, and links to Spot documentation
- Fixed Allow/Deny Spot Accounts filter so that the "Deny" option correctly excludes the listed accounts

## v0.4.0

- Added workload summary table to incident report, grouped by cluster, showing workload name, type, namespace, vCPU change, memory change, and potential monthly savings
- Fixed error that caused policy to fail when a cluster returns an error for rightsizing recommendations

## v0.3.1

- Category of policy template updated to "Cost". Functionality unchanged.

## v0.3.0

- Improved incident report formatting to use currency from Flexera Org
- Improved formatting and context in the "Recommendation Details" for each recommendation
- Added Minimum Savings Threshold input parameter to filter out recommendations below the specified estimated monthly savings
- Fixed bug preventing Azure recommendations from being pulled
- Estimated Savings is being provided by Recommendations Spot API instead of calculated from aggregated costs

## v0.2.3

- Updated documentation link in policy description. Functionality unchanged.

## v0.2.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.2.1

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.2.0

- Added support for collecting Azure and GCP cluster rightsizing recommendations

## v0.1.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v0.1.0

- Initial release
