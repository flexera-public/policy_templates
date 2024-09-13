# Changelog

## v3.1.2

- Fixed issue that returned a `TypeError: Cannot access member 'toFixed' of undefined` when calculating the utilization of the virtual machines.

## v3.1.1

- Idle VM Instances incident now includes a `Recommended Resource Type` field with a value of `Delete VM Instance` for ease of analyzing recommendations from the Flexera Optimization dashboard

## v3.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.0

- Added support for regex when filtering resources by label

## v2.2

- Fixed issue where currency conversion would sometimes not work as expected.

## v2.1

- Policy metadata and incident export now correctly state that the recommendation for idle instances is to stop them rather than delete them

## v2.0

- Policy now requires a Flexera credential
- Policy now converts savings to local currency when appropriate
- Policy now reports on both underutilized and idle instances
- Downsize action can now be taken on underutilized instances
- Stop action can now be taken on idle instances
- Delete action can now be taken on idle instances
- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Removed ability to filter by zone; filtering by region is now supported
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by project and by region via an allow list or a deny list
- Added ability to filter resources by multiple label key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if savings data changed but nothing else has
- Streamlined code for better readability and faster execution
- Added logic required for "Meta Policy" use-cases

## v1.1

- Modified the number of GCP recommender API calls that can be done before waiting to prevent a quota limit error: 100 request per minute.

## v1.0

- Initial release.
