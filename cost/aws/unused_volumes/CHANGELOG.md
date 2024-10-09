# Changelog

## v8.3.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v8.3.0

- Added `Resource ARN` to incident table.

## v8.2.0

- Modified internal names for incident fields for more accurate scraping into Optimization dashboard
- Deprecated: This policy is no longer being updated.

## v8.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v8.0

- Added support for regex when filtering resources by tag

## v7.4

- Policy action error logging modernized and now works as expected in EU/APAC

## v7.3

- Corrected API issue when executing policy in APAC

## v7.2

- Updated description of `Account Number` parameter

## v7.1

- Added ability to filter resources by tag key alone without regard for tag value
- Fixed issue with correctly reading tags from volumes

## v7.0

- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to include attached volumes in the incident and to action on them
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v6.1

- Added `Resource Name` incident field
- Added `Age` incident field
- Added `Lookback Period` incident fields
- Changed the internal name of the `Status` incident field to ensure proper scraping for the recommendation dashboard

## v6.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v5.1

- Changed "Id" field in incident output to "ID" to match other policies and ensure proper reporting.

## v5.0

- Added support for reporting and acting on attached volumes via an optional parameter.

## v4.2

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v4.1

- Added logic required for "Meta Policy" use-cases

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`). This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied. Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.8

- Added accountName field

## v3.7

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v3.6

- Refactored datasources from `cloudwatch:GetMetricStatistics` to `cloudwatch:GetMetricData` to improve efficiency of metric data collection
- Added `param_api_wait` - The amount of time in seconds to wait between requests to the CloudWatch API to avoid being throttled by AWS

## v3.5

- Updating to keyword from string

## v3.4

- Use provided keyword for Optima endpoint

## v3.3

- updated savings_currency to savingsCurrency and fixed possible N/A value to 0.0

## v3.2

- Added default to aws_account_number parameter to enable existing API users.

## v3.1

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Normalizing fields for recommendations:
  - added 'tags field
  - Renamed 'accountId' to 'accountID'
  - Renamed 'id' to 'resourceID'
  - Renamed 'instanceType' to 'resourceType'
  - Changed 'savings' to be a plain number
  - Added 'savings_currency' to record the currency symbol.
  - Added a 'service' field, hardcoded to "EBS"

## v2.19

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.18

- Fix non-optimal array searching for costs

## v2.17

- Added default_frequency "daily"

## v2.16

- Increase the sleep time between calls to AWS for snapshot status in order to decrease the likelihood of hitting a Cloud Workflow event limit

## v2.15

- Improve error handling and debug logging so that errors from taking action are actually surfaced
- Add a `param_log_to_cm_audit_entries` parameter to control whether action debug logging is sent to CM Audit Entries; this should be left set to No on Flexera EU

## v2.14

- Add a parameter to override the Flexera One org ID to use when querying Optima for cases when the project is not in the same org where the AWS bill is registered in Optima

## v2.13

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.12

- Modified escalation label and description for consistency

## v2.11

- Require a minimum value of `1` on the `param_unattached_days` parameter

## v2.10

- Adding AWS Account Id

## v2.9

- Use `DescribeVolumes` instead of `DescribeRegions` to more accurately check if the call is enabled by the Service Control Policy in each region

## v2.8

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.7

- added total estimated monthly savings in the incident detail message
- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.6

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.5

- Updated escalation block

## v2.4

- add Estimated Monthly Savings

## v2.3

- adding incident resource table

## v2.2

- Bug fixes
- The policy is renamed to unused volumes and that it now uses cloudwatch to determine if it's unused.

## v2.1

- rename policy

## v2.0

- initial release
