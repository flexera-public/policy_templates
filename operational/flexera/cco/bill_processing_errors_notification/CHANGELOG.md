# Changelog

## v2.4.0

- Added `Bill Connection Ignore List` parameter to allow user to ignore specific bill connections.

## v2.3.0

- Renamed to `Cloud Bill Processing Error Notification` to better indicate that it is specific to Cloud Cost Optimization
- Parameters altered to be more descriptive and human-readable
- Added additional fields to incident table to provide more context
- Streamlined code for better readability and faster execution

## v2.2

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.1

- Updated description to account for new file path in Github repository

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- General code cleanup and optimization

## v1.1

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.0

- Initial Release
