# Changelog

## v4.0.3

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v4.0.2

- Added `doc_link` field to policy template metadata for future UI enhancements. Functionality unchanged.

## v4.0.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v4.0.0

- Specific roles can now be ignored via the `Role Ignore List` parameter
- Policy template renamed to `Flexera Users With Explicit Roles` to better reflect its functionality
- Policy template now uses newer [Flexera IAM APIs](https://developer.flexera.com/docs/api/iam/v1)
- Incident table now includes additional fields for added context
- Streamlined code for better readability and faster execution

## v3.2

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v3.1

- Updated description to account for new file path in Github repository

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.1

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.0

- improved policy output

## v1.0

- initial release
