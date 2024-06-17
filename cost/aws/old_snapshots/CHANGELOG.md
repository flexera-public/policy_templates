# Changelog

## v8.3.0

- Modified internal names for incident fields for more accurate scraping into Optimization dashboard

## v8.2

- Fixed issue where duplicate results would sometimes occur for RDS DB snapshots.

## v8.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v8.0

- Added support for regex when filtering resources by tag

## v7.5

- Policy action error logging modernized and now works as expected in EU/APAC

## v7.4

- Corrected API issue when executing policy in APAC

## v7.3

- Updated description of `Account Number` parameter

## v7.2

- Fixed issue related to tag key/values not being populated

## v7.1

- Added ability to filter resources by tag key alone without regard for tag value

## v7.0

- Several parameters altered to be more descriptive and human-readable
- Modified and renamed "Deregister Image" parameter to make it more clear and intuitive
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by multiple tag key:value pairs
- Added ability to filter resources by description or service type
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Added additional fields to incident export to facilitate scraping for dashboards
- Policy no longer raises new escalations if snapshot age or savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v6.2

- Renamed `volumeSize` incident field to `size`.
- Renamed `daysOld` incident field to `age`.
- Added `resourceName` incident field.
- Removed repeated code on script `js_snapshots_cost_mapping`.

## v6.1

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard
- Added "Resource Type" to incident output

## v6.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v5.0

- Added support for RDS Snapshots
- Changed Policy Template info field `Service` from `EBS` to `Storage`

## v4.2

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v4.1

- Added logic required for "Meta Policy" use-cases

## v4.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v3.6

- Added accountName field

## v3.5

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v3.4

- Modified Image (AMI) datasource collection to improve policy efficiency
- Modified "Delete Snapshots" Escalation Action to improve execution efficiency

## v3.3

- updated savings_currency to savingsCurrency

## v3.2

- Added default to aws_account_number parameter to enable existing API users.

## v3.1

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v3.0

- applying data normalization updates for spend recommendations api. this change breaks current iterations expecting specific output types being pushed.
- Normalizing fields for recommendations:
  - Renamed 'tagKeyValue' to 'tags'
  - Renamed 'accountId' to 'accountID'
  - Renamed 'id' to 'resourceID'
  - Changed 'savings' to be a plain number
  - Added 'savings_currency' to record the currency symbol.
  - Added a 'service' field, hardcoded to "EBS"

## v2.17

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.16

- Fix non-optimal array searching for costs
- Fix currency bug caused by incorrect parameter being passed

## v2.15

- Use rs_optima_host instead of hardcoded hostname.

## v2.14

- Added default_frequency "daily"

## v2.13

- Improve error handling and debug logging so that errors from taking action are actually surfaced
- Add a `param_log_to_cm_audit_entries` parameter to control whether action debug logging is sent to CM Audit Entries; this should be left set to No on Flexera EU

## v2.12

- Add a parameter to override the Flexera One org ID to use when querying Optima for cases when the project is not in the same org where the AWS bill is registered in Optima

## v2.11

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.10

- Modified escalation label and description for consistency

## v2.9

- Require a minimum value of `1` on the `snapshot_age` parameter

## v2.8

- Added AWS Account ID to resource table

## v2.7

- Use `DescribeSnapshots` instead of `DescribeRegions` to more accurately check if the call is enabled by the Service Control Policy in each region

## v2.6

- Include Estimated Monthly Savings to each resource
- Include Total Estimated Monthly Savings in the incident summary

## v2.5

- Changed the default deregister image action from Yes to No.

## v2.4

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.3

- Updated escalation block

## v2.2

- Bug fix on when the snapshot was unable to delete when attached to AMI

## v2.1

- adding incident resource table

## v2.0

- initial release
