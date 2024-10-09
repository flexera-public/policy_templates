# Changelog

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Policy template renamed to `AWS Unused IAM Credentials` to better reflect its functionality
- Added ability to specify the minimum age of a credential to consider it unused
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.5

- Updated description of `Account Number` parameter

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- Added default to aws_account_number parameter to enable existing API users.

## v2.2

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.1

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.0

- initial release
