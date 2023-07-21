# Changelog

## v3.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added support for memory metrics along with relevant parameters
- Added ability to configure how many days to consider CPU/memory statistics for
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to make recommendations based on maximum CPU/memory usage
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if statistics or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v2.4

- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.3

- Added `Lookback Period` incident field.
- Added `Threshold` incident field.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.2

- Fixed bug with parameter_subscription_allowlist script

## v2.1

- Added parameter `threshold statistic` to allow selecting between minimum, maximum and average statistics to base rightsizing and idle recommendations on.

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
