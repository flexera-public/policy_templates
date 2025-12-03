# Changelog

## v3.0.5

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.0.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.0.0

- Modified credential to correctly match Microsoft Graph credentials in the Flexera platform
- Several parameters altered to be more descriptive and human-readable
- Removed unused `Azure AD Tenant ID` parameter
- Updated Microsoft Graph API call to use production `/v1.0/security/alerts_v2` endpoint
- Fixed issue where policy template would report alerts unrelated to Office 365
- Streamlined code for better readability and faster execution

## v2.4

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Added resource table

## v2.0

- Added credential services

## v1.0

- initial release
