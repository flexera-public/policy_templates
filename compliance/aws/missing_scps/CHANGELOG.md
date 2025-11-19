# Changelog

## v3.1.0

- Added support for attaching CSV files to incident emails.

## v3.0.5

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.2

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.1

- Minor code improvements to conform with current standards. Functionality unchanged.

## v3.0.0

- Changed policy template name to `AWS Accounts Missing Service Control Policies` to better reflect its functionality
- Added ability to audit for multiple Service Control Policies in a single execution
- Policy template no longer reports suspended AWS accounts
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
