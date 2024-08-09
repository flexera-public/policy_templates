# Changelog

## v3.0.0

- Policy template renamed to `AWS S3 Buckets Without Default Encryption Configuration` to better reflect its functionality
- Buckets can now be filtered by region, tag, or name
- Buckets can now be deleted as an automatic action
- Added additional fields to incident table for added context
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.9

- Updated description of `Account Number` parameter

## v2.8

- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.7

- Added default to aws_account_number parameter to enable existing API users.

## v2.6

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.5

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.4

- Added CIS metadata to policy

## v2.3

- Modified escalation label and description for consistency

## v2.2

- adding incident resource table

## v2.1

- remove unnecessary permissions block

## v2.0

- Changed the authentication to credential services

## v1.0

- initial release
