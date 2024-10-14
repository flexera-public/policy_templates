# Changelog

## v5.3.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v5.3.0

- Added ability to set metrics granularity when gathering resource metrics from Azure
- Added support for p90, p95, and p99 metrics for both CPU and memory.
- Improved calculations for `Minimum` and `Maximum` for both CPU and memory.

## v5.2.0

- New `Exclude Stopped Virtual Machines` parameter to filter stopped virtual machines from results
- New `Exclude Databricks` parameter to filter Azure Databricks virtual machines from results
- `Power State` field added to results to indicate whether a virtual machine is running or stopped
- Fields related to the image the virtual machine was created with added to results
- Idle Virtual Machines incident now includes a `Recommended Instance Size` field with a value of `Delete Virtual Machine` for ease of analyzing recommendations from the Flexera Optimization dashboard
- Added warning about invalid Databricks recommendations to incident description if `Exclude Databricks` parameter is set to `No`
- Fixed issue that would cause downsize actions to fail

## v5.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.0

- Added support for regex when filtering resources by tag

## v4.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v4.0

- Fixed issue with resource count in incident subject being off by 1
- Fixed minor grammar issue if results only include 1 item
- Renamed policy actions to make it clear whether they are for underutilized or idle instances
- Added ability to filter resources by tag key via wildcard
- Added option to power off idle instances
- Added ability to indicate whether to do a graceful or forced shutdown when powering off instances
- Improved code related to incident export
- Updated and improved code for policy actions

## v3.3

- Added ability to filter resources by region

## v3.2

- Corrected issue with policy not retrieving cost data on orgs using newer Azure bill connections

## v3.1

- Added support for meta policies
- Fixed typo in incident name for idle instances

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
