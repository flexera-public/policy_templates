# Changelog

## v2.0

- Policy now automatically converts savings from USD to local currency when appropriate
- Added exchange rate context to incident to allow user to derive unmodified USD values when needed
- Added ability to use Subscription list parameter as either an "allow" list or a "deny" list
- Several parameters altered to be more descriptive and intuitive to use
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

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
