# Changelog

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Several parameters altered to be more descriptive and human-readable
- Added ability to filter results by repository
- Normalized incident export to be consistent with other policies
- Added additional fields to incident table for more context
- Added ability to require owner reviews when protecting branches
- Added ability to dismiss stale reviews when protecting branches
- Streamlined code for better readability and faster execution
- Policy now requires a valid Flexera credential

## v2.5

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.3

- Use GitHub GraphQL API to decrease the number of API calls
- Add option to include default branch regardless of branch selection

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Adding incident resource table

## v2.0

- Added credential services

## v1.3

- Added escalation action to update branch protection rule

## v1.2

- Added tenancy "single" in metadata

## v1.1

- update readme link

## v1.0

- initial release
