# Changelog

## v5.4.2

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v5.4.1

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v5.4.0

- Adds utilization chart for each resource to the result if metrics are available

## v5.3.2

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v5.3.1

- Added `hide_skip_approvals` field to the info section, enabling the UI to dynamically show or hide the "Skip Approval" option. Functionality unchanged.

## v5.3.0

- Added support for downsizing multiple sizes where appropriate

## v5.2.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v5.2.0

- Added `Resource ARN` to incident table.

## v5.1.2

- Fix bug preventing Memory metrics from being included in result for some EC2 Instances created by Autoscaling Group

## v5.1.1

- Idle EC2 Instances incident now includes a `Recommended Instance Size` field with a value of `Terminate EC2 Instance` for ease of analyzing recommendations from the Flexera Optimization dashboard

## v5.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v5.0

- Added support for regex when filtering resources by tag

## v4.5

- Corrected API issue when executing policy in APAC

## v4.4

- Added "Stop Instance" action for Idle resources
- Improved debugging and error handling of Policy Actions

## v4.3

- Fixed issue with gathering and interpreting CloudWatch metrics

## v4.2

- Updated description of `Account Number` parameter

## v4.1

- Added ability to filter resources by tag key alone without regard for tag value

## v4.0

- Policy name changed to reference EC2 service directly
- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to configure how many days to consider CPU/memory statistics for
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to take automated actions to resize or delete resources
- Added ability to make recommendations based on maximum CPU/memory usage
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if statistics or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v3.1

- Fixed issue where savings would always be 0 if policy were executed at the end of the month.

## v3.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v2.0

- Initial release
