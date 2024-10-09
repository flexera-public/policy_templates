# Changelog

## v6.5.2

- Minor code improvements to conform with current standards. Functionality unchanged.

## v6.5.1

- Added `deprecated` field to policy metadata. Functionality is unchanged.

## v6.5

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v6.4

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v6.3

- Corrected API issue when executing policy in APAC

## v6.2

- Updated description of `Account Number` parameter

## v6.1

- Added ability to filter resources by tag key alone without regard for tag value

## v6.0

- Added parameter to specify how far back to check instances for activity
- Several parameters altered to be more descriptive and human-readable
- Removed unnecessary "CloudWatch API Wait Time" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## 5.2

- Added `Database Engine` incident field
- Added `Engine Version` incident field
- Added `Platform` incident field
- Added `Lookback Period` incident fields
- Changed the internal names of several incident fields to ensure proper scraping for recommendations dashboard

## v5.1

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard

## v5.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v4.2

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v4.1

- Added logic required for "Meta Policy" use-cases

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`). This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied. Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.7

- Added accountName field

## v3.6

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v3.5

- Improved accuracy of metric collection by using a different Statistic to identify idle resources
- Fixed bug with Tag Exclusion Key parameter in `v3.x`. Resources once again get excluded from results if containing provided `key:value` tag
- Refactored datasources from `cloudwatch:GetMetricStatistics` to `cloudwatch:GetMetricData` to improve efficiency of metric data collection
- Added `param_api_wait` - The amount of time in seconds to wait between requests to the CloudWatch API to avoid being throttled by AWS

## v3.4

- Use provided keyword for Optima endpoint

## v3.3

- updated savings_currency to savingsCurrency

## v3.2

- Added default to aws_account_number parameter to enable existing API users.

## v3.1

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Normalizing fields for recommendations:
  - Renamed 'tag_set' to 'tags'
  - Renamed 'accountId' to 'accountID'
  - Renamed 'id' to 'resourceID'
  - Renamed 'instanceType' to 'resourceType'
  - Changed 'savings' to be a plain number
  - Added 'savings_currency' to record the currency symbol.
  - Added a 'service' field, hardcoded to "RDS"

## v2.11

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.10

- Fix non-optimal array searching for costs

## v2.9

- Added default_frequency "daily"

## v2.8

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.7

- Modified escalation label and description for consistency

## v2.6

- Added AWS Account ID to resource table

## v2.5

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.4

- Include Estimated Monthly Savings to each resource.
- Include Total Estimated Monthly Savings in the incident message details.

## v2.3

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.0

- initial release
