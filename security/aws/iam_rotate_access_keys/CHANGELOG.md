# Changelog

## v3.0.0

- Policy template renamed to `AWS IAM Users With Old Access Keys` to better reflect its functionality
- Added ability to set a specific age to consider access keys old
- Added additional incident fields to provide context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.7

- Updated description of `Account Number` parameter

## v2.6

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.5

- Added default to aws_account_number parameter to enable existing API users.

## v2.4

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- fixed issue with email text

## v2.1

- updated metadata

## v2.0

- initial release
