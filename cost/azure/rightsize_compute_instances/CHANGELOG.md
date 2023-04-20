# Changelog

## v2.1

- Added parameter `param_threshold_statistic` to allow selecting between minimum, maximum and average statistics to base rightsizing and idle recomendations on.

## v2.0

- Added Azure Endpoint parameter to enable use with Azure China.
- Fixed issue causing resources without a rightsizing or termination recommendation to appear in the incident.
- Fixed issue affecting calculation of total savings for underutilized resources.
- Removed non-functional downsize escalation from idle compute instance incident.
- General code cleanup and modernization.

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
