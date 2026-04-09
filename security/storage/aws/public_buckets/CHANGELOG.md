# Changelog

## v3.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter resources by region
- Added additional context to incident description
- Normalized incident export to be consistent with other policies
- Added human-readable recommendation to incident export
- Policy no longer raises new escalations if bucket owner has changed but nothing else has
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.8

- Updated description of `Account Number` parameter

## v2.7

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- Added default to aws_account_number parameter to enable existing API users.

## v2.5

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.4

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.3

- Modified escalation label and description for consistency

## v2.2

- Updated escalation block
- Support to send a notification to a slack channel is removed

## v2.1

- adding incident resource table

## v2.0

- Changes to support the Credential Service

## v1.9

- Use inferred regions in auth method

## v1.8

- Added Approval block

## v1.7

- Added optional Slack notification support

## v1.6

- Upating Policy Template Name

## v1.5

- Update email subject with account name and ID, and change actions and/or resolution name to be more descriptive. Issues #75 & #83

## v1.4

- Updating input parameter name for email

## v1.3

- Updating email from string to list

## v1.2

- Fixing EU endpoint

## v1.1

- Changing severity to high

## v1.0

- Initial Release
