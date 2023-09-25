# Changelog

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
