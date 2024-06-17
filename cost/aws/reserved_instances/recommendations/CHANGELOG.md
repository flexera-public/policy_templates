# Changelog

## v3.5

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.4

- Corrected API issue when executing policy in APAC

## v3.3

- Updated description of `Account Number` parameter

## v3.2

- Fixed issue with currency conversion check when array is empty

## v3.1

- Fixed issue where policy would fail to do proper currency conversion

## v3.0

- Policy now automatically converts savings to local currency when appropriate
- Removed parameter to do the above manually via a user-specified exchange rate
- Added exchange rate context to incident to allow user to derive unmodified values when needed
- Several parameters altered to be more descriptive and intuitive to use
- `ElasticSearch` is now referred to as `OpenSearch` in keeping with current AWS naming conventions
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.20

- Changed service metadata to "Compute" to ensure proper incident scraping

## v2.19

- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.18

- Changed policy set from `Reserved Instance` to `Reserved Instances` to match other similar policies.
- Added `Resource Type` incident field.
- Added `Term` incident field.
- Updated `Platform` incident field to avoid empty values.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.17

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard
- Modified incident output to facilitate scraping of incidents for Recommendations dashboard

## v2.16

- Added new selection "All Except EC2" for the service input list, Updated new option as default value, And Updated the datasources.

## v2.15

- change the `auth_rs` Credential to `auth_flexera` name and label to `flexera` for consistency with other policy templates

## v2.14

- Added policySet as Reserved Instance to populate the Total Potential Savings

## v2.13

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.12

- Added accountName call and field

## v2.11

- Added default to aws_account_number parameter to enable existing API users.

## v2.10

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.9

- updated policy versions to the correct changelog version

## v2.8

- adding currency adjustment parameter that allows for percentage conversion of monthly estimated savings

## v2.7

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.6

- prevent the incident update when data doesnt change

## v2.5

- Add option to include all Reserved Instance types in one incident

## v2.4

- Added "Account Scope" (PAYER or LINKED) parameter

## v2.3

- Added default_frequency "daily"

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Adding incident resource table

## v2.0

- Changes to support the Credential Service

## v1.2

- change to single tenancy

## v1.1

- fix pagination

## v1.0

- initial release
