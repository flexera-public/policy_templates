# Changelog

## v1.4

- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v1.3

- Changed policy set from `Savings Plan` to `Savings Plans` to match other similar policies.
- Rounded numeric value in `Cost Without Benefit (Over Lookback Period)` incident field to three decimals.
- Removed 'N/A' value from `Subscription ID` incident field when `Scope` incident field is set to 'Shared'.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v1.2

- Replaced the term **whitelist** with **allowed list**.

## v1.1

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v1.0

- Initial release
