# Changelog

## v3.0.0

- Policy can now be run against an arbitrary number of days in the past
- Policy incident now presented in a more human-readable fashion
- Streamlined code for better readability and faster execution
- Policy now requires valid Flexera credential

## v2.12

- Updated policy metadata to correctly identify it as a `Reserved Instances` policy

## v2.11

- Updated description of `Account Number` parameter

## v2.10

- Changed service metadata to "Compute" to ensure proper incident scraping

## v2.9

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.8

- Added default to aws_account_number parameter to enable existing API users.

## v2.7

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.6

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.5

- Added default_frequency "daily"

## v2.4

- Modified escalation label and description for consistency

## v2.3

- updated minimum required permission in the README
- modified label and description in both Policy Template and README files to be similar

## v2.2

- Added resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changes to support the Credential Service

## v1.3

- Update email subject with account name and ID, and change actions and/or resolution name to be more descriptive. Issues #75 & #83

## v1.2

- Show coverage field as percent

## v1.1

- Adding permissions required to run the policy

## v1.0

- initial release
