# Changelog

## v6.3.9

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v6.3.8

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v6.3.7

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v6.3.6

- Fixed issue where Currency Conversion messaging in policy incident would stop policy execution because of an error. Functionality unchanged.

## v6.3.5

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v6.3.4

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v6.3.3

- Fixed issue where Currency Conversion messaging in policy incident would show incorrectly. Functionality unchanged.

## v6.3.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v6.3.1

- Fixed issue where `New Monthly List Price` and `Estimated Monthly Savings` were being incorrectly reported in the policy incident.

## v6.3.0

- Added `Resource ARN` to incident table.

## v6.2.0

- Policy Template name renamed from `AWS Rightsize EBS Volumes` to `AWS Superseded EBS Volumes`

## v6.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v6.0

- Updated AWS Pricing API parameter to be more descriptive and user-friendly

## v5.0

- Added support for regex when filtering resources by tag

## v4.5

- Fixed issue where currency conversion would sometimes not work as expected.

## v4.4

- Added parameter to override the AWS Pricing API Endpoint

## v4.3

- Corrected API issue when executing policy in APAC

## v4.2

- Updated description of `Account Number` parameter

## v4.1

- Fixed issue where list prices reported in incident were inflated

## v4.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to take automated actions to upgrade GP2 volumes to GP3
- Added additional context to incident description
- Removed unneeded `IOPS Average %` and `Lookback Period` fields from incident export
- Removed unneeded API calls to CloudWatch
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if statistics or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v3.3

- Updated logic to filter out GP3 volumes from recommendations as currently unsupported.
- Updated the data used for the policy incident to ensure a policy incident is not created when there are no recommendations

## v3.2

- Added `Resource Name` incident field
- Added `Account Name` incident field
- Added `IOPS Average %` incident field
- Added `Lookback Period` incident fields
- Changed the internal name of the `Volume Status` incident field to ensure proper scraping for the recommendation dashboard

## v3.1

- Modified incident output to facilitate scraping of incidents for Recommendations dashboard

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions
- Made changes to the description

## v2.0

- Initial Release
