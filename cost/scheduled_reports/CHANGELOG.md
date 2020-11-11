# Changelog

## v1.22

- Modified escalation label and description for consistency
- Added incident resource table

## v1.21

- Added "Billing Centers" as a reportable dimension

## v1.20

- Fixed date value issue.

## v1.9

- Fix for Bug Dimension Information Missing for DAY and WEEK.
- Added default_frequency "monthly"

## v1.8

- Provided option to display chart with different granularity.

## v1.7

- Added tenancy "single" in metadata

## v1.6

- added "Resource Group", "Cloud Vendor", "Cloud Vendor Account", and "Cloud Vendor Account Name" as a dimensions
- added support to report on child Billing Centers
- forced chart legend to bottom of chart
- fixed the billing data api call that was leaving off a days worth of costs
- Added currency symbol support
- Added thousands separator support based on currency

## v1.5

- added the ability to select any "common" dimension for the chart image
- changed the chart image to only show the "top 10" values for the current month, and group the rest of the data into "Other"

## v1.4

- added chart with previous 6 months utilization, based on [category](https://docs.rightscale.com/optima/reference/rightscale_dimensions.html#category)

## v1.3

- allow user to select all billing centers
- allow user to enter billing center names

## v1.2

- update date calculation logic in current week datasource and current month datasource
- update summary_template and detail_template with org details

## v1.1

- update short and long long_description

## v1.0

- initial release
