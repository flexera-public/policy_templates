# Changelog

## v1.3

- Renamed `Savings Plan` policy_set from info block to `Savings Plans`.
- Renamed `commitmentAmount` incident field to `recommendedQuantity`.
- Rounded `costWithoutBenefit` incident field to three decimals.
- Removed 'N/A' value from `subscriptionId` incident field when `scope` incident field is set to 'Shared'.

## v1.2

- Replaced the term **whitelist** with **allowed list**.

## v1.1

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v1.0

- Initial release
