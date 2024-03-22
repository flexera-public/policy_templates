# Changelog

## v3.0

- Policy renamed to `SaaS Manager - Deactivated Users` to better reflect its functionality
- Reduced minimum value of `Inactive Days Threshold` parameter from 60 to 0
- Added `Applications` parameter to allow user to filter results by application
- Updated policy to use public SaaS Manager API
- Added support for APAC API endpoint
- Policy now uses and requires a general Flexera One credential
- Incident summary now includes applied policy name
- General code cleanup and normalization

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- Added pagination for API call
- Refactored script 'js_format_data'

## v2.5

- Updated README.md rightscale documentation links with docs.flexera documentation links

## v2.4

- Updated to set SaaS API host dynamically in EU and non-EU zone

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Update API endpoint

## v2.1

- add parameter to filter inactive users based on number of days of inactivity

## v2.0

- initial release
