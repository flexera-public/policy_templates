# Changelog

## v3.2

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v3.1

- Corrected API issue when executing policy in APAC

## v3.0

- Policy now automatically converts savings to local currency when appropriate
- Removed parameter to do the above manually via a user-specified exchange rate
- Added exchange rate context to incident to allow user to derive unmodified values when needed
- Several parameters altered to be more descriptive and intuitive to use
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.17

- Added `Term` incident field.
- Added `Purchasing Option` incident field.
- Added `Resource Type` incident field.
- Added `Lookback Period` incident field.
- Changed policy set from `Savings Plan` to `Savings Plans` to match other similar policies.
- Changed internal names of several incident fields to ensure that they are properly scraped for dashboards.

## v2.16

- Updated policy metadata to facilitate scraping of incidents for Recommendations dashboard
- Modified incident output to facilitate scraping of incidents for Recommendations dashboard

## v2.15

- change the `auth_rs` Credential to `auth_flexera` name and label to `flexera` for consistency with other policy templates

## v2.14

- Added policySet as Savings Plan to populate the Total Potential Savings

## v2.13

- Added accountName call and field

## v2.12

- Added SageMaker to param_savings_plan_type list of allowed values
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

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

- prevent updating the incident if the data doesn't change

## v2.5

- Added "Account Scope" (PAYER or LINKED) parameter

## v2.4

- Added default_frequency "daily"

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services

## v1.0

- initial release
