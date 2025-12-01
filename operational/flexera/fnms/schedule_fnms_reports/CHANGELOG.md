# Changelog

## v3.2.5

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v3.2.4

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v3.2.3

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v3.2.2

- Updated names of code blocks to align with current formatting standards. Functionality unchanged.

## v3.2.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v3.2

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v3.1

- Updated description to account for new file path in Github repository

## v3.0

- Updated policy to use Flexera One ITAM SOAP APIs. Full details here: [Flexera One ITAM SOAP APIs Transitioning to Flexera One IAM](https://community.flexera.com/t5/Flexera-One-Blog/Flexera-One-ITAM-SOAP-APIs-Transitioning-to-Flexera-One-IAM/ba-p/229399)
- Removed support for on-premise deployments (with or without wstunnel)

## v2.5

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.4

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.3

- Removed legacy CMP permission validation declaration

## v2.2

- Modified escalation label and description for consistency

## v2.1

- Merged Cloud and On premise into one policy.

## v2.0

- Added support for on-premise FlexNet Manager (NTLM auth).
- Changes to support the Credential Service.

## v1.4

- Added Permission block

## v1.3

- Added tenancy "single" in metadata

## v1.2

- Initial Release. FNMS Cloud only
