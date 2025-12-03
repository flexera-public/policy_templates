# Changelog

## v6.3.1

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v6.3.0

- Added support for attaching CSV files to incident emails.

## v6.2.5

- Updated API request for gathering instance costs to only gather costs specific to virtual machines. Functionality unchanged but policy template is now less likely to fail to report costs.

## v6.2.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v6.2.3

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v6.2.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v6.2.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v6.2.0

- Adds utilization chart for each resource to the result if metrics are available

## v6.1.3

- Code refactored to improve performance by gathering metrics in batched requests.

## v6.1.2

- Fixed incorrect calculation for memory related fields "Memory Average %", "Memory p90", Memory p95", and "Memory p99".

## v6.1.1

- Fix for memory stats showing decimal (such as 0.5 for half) instead of showing percentage (such as 50 for half).

## v6.1.0

- Added batch processing for large datasources as a performance enhancement (reduces memory usage) with no changes to logic or functionality.

## v6.0.4

- Fix for v6.0.3, changed the approach for handling memory statics for rightsized instances. Functionality unchanged.

## v6.0.3

- Fixed error that caused showing negative values at the incident fields for memory statistics for recently rightsized instances. Functionality unchanged.

## v6.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v6.0.1

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v6.0.0

- Recommendations now consider number of attached data disks. Sizes that would not support the current number of attached disks for an instance will not be recommended.
- Azure credential now requires `Microsoft.Compute/locations/vmSizes/read` permission to support the above.

## v5.4.0

- Added support for downsizing multiple sizes where appropriate

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
