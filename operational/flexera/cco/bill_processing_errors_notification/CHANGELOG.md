# Changelog

## v2.6.0

- Added support for Azure CSP and Azure MCA Enterprise account types.

## v2.5.3

- Fixed error that caused some incident fields to show invalid negative values for memory statistics for recently rightsized instances. Functionality unchanged.

## v2.5.2

- Added `Report Connection With Zero Bills` parameter to help users detect connections without bills and spot potential misconfigurations.

## v2.5.1

- Added `hide_skip_approvals` field to the info section. It dynamically controls "Skip Action Approvals" visibility.

## v2.5.0

- Updated some API requests to use newer internal Flexera API
- Fixed error that sometimes caused functioning bill connections to appear in results
- Fixed error that sometimes caused the policy template to fail
- Modified incident table to include more useful information

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
