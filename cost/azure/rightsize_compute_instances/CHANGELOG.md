# Changelog

## v1.6

- Fixed issue causing resources without a rightsizing or termination recommendation to appear in the incident.

## v1.5

- Fixed issue causing resources to be reported as both underutilized and idle instead of one or the other.

## v1.4

- Fixed check for underutilized compute instances
- Added default values for parameters that are not required

## v1.3

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v1.2

- Replaced the term **whitelist** with **allowed list**.

## v1.1

- Added `ignore_status [400,403,404]` for API calls to Azure API to ignore errors related to legacy subscription types

## v1.0

- Initial release
