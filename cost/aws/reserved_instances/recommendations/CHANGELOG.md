# Changelog

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
