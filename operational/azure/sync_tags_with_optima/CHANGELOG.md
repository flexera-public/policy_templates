# Changelog

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Modified `sys_log` definition to disable `rs_cm.audit_entry.create` outside Flexera NAM

## v2.4

- Use provided keyword for Optima endpoint

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Added subscription filter option and ability to specify Azure API endpoint

## v2.1

- Modified escalation label and description for consistency
- Added automatic block

## v2.0

- initial release
