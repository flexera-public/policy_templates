# Changelog

## v6.4.9

- Modifications were implemented to make the Resource ID globally unique in order to resolve historical recommendation issues. Functionality unchanged.

## v6.4.8

- Fixed issue where estimated savings would sometimes be reported as 0 inaccurately.
- Fixed issue where `Resource ARN` field was malformed.

## v6.4.7

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v6.4.6

- Updated meta policy code to use newer Flexera API. Functionality unchanged.

## v6.4.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v6.4.4

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v6.4.3

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v6.4.2

- Fixed issue with numeric currency values sometimes showing 'undefined' instead of currency separators

## v6.4.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v6.4.0

- Added `Resource ARN` and `Resource Name` to incident table.

## v6.3.0

- Changed default value of `Automatic Actions` parameter to conform with other similar policy templates
- Modified incident title to explicitly indicate `AWS` as the cloud provider

## v6.2.1

- Fixed minor spelling issue in policy template description

## v6.2.0

- Modified internal names for incident fields for more accurate scraping into Optimization dashboard

## v6.1

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v6.0

- Added support for regex when filtering resources by tag

## v5.0

- Assessment algorithm now more consistently identifies unused Classic Load Balancers
- Added parameter to exclude recently created Classic Load Balancers
- Several parameters altered to be more descriptive and human-readable
- Removed deprecated "Log to CM Audit Entries" parameter
- Added ability to only report recommendations that meet a minimum savings threshold
- Added ability to filter resources by multiple tag key:value pairs
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if savings data changed but nothing else has
- Streamlined code for better readability and faster execution

## v4.1

- Updated description of `Account Number` parameter

## v4.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v3.1

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.16

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.15

- Added default to aws_account_number parameter to enable existing API users.

## v2.14

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.13

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.12

- Fix non-optimal array searching for costs

## v2.11

- Debug log via param (off by default); use rs_optima_host instead of hardcoded hostname

## v2.10

- Added default_frequency "daily"

## v2.9

- Added a new input parameter to enter regions in order to support SCP (Service Control Policy) and CIS Standards

## v2.8

- Modified escalation label and description for consistency

## v2.7

- Added AWS Account ID to resource table

## v2.6

- formatted the incident detail message to display if no savings data available
- reverted the toFixed() to Math.round() for displaying savings data

## v2.5

- updated policy to handle and show the error if the user is not having permission for fetching cost data from Optima

## v2.4

- Include Estimated Monthly Savings to each resource
- Include Total Estimated Monthly Savings in the incident summary

## v2.3

- Added EC2 DescribeRegions API action to get only Service Control Policy enabled Regions

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.2

- Use inferred regions in auth method

## v1.1

- Updating the file by removing reference URL

## v1.0

- initial release
