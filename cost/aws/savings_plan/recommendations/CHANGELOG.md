# Changelog

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
