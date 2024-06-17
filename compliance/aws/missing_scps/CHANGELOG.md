# Changelog

## v3.0.0

- Changed policy template name to `AWS Accounts Missing Service Control Policies` to better reflect its functionality
- Added ability to audit for multiple Service Control Policies in a single execution
- Policy no longer reports suspended AWS accounts
- Streamlined code for better readability and faster execution
- Policy template now requires a valid Flexera credential

## v2.7

- Updated description of `Account Number` parameter

## v2.6

- Removed unused `sys_log` definition
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.5

- Added default to aws_account_number parameter to enable existing API users.

## v2.4

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Updated pagination to add `NextToken` to the body instead of query parameters on subsequent calls

## v2.1

- Modified escalation label and description for consistency

## v2.0

- initial release
