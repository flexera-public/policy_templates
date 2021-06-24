# Changelog

## v2.7

- Debug via param (off by default, for EU app); use rs_optima_host, not hardcoded hostname

## v2.6

- Adding Azure China

## v2.5

- Added default_frequency "daily"

## v2.4

- Updated policy to fetch cost details for multiple subscription ids from Optima
- Modified escalation label and description for consistency

## v2.3

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.2

- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.1

- Include Estimated Monthly Savings to each resource
- Include Total Estimated Monthly Savings in the incident summary
- Added Selectable resources and actions

## v2.0

- initial release
