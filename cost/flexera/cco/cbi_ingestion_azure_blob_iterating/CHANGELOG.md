# Changelog

## v1.0.0

- The policy template now creates the CBI endpoint (bill connect) automatically if it does not already exist. Previously, the CBI endpoint had to be created in advance using the Flexera Bill Connect API.
- Added the `CBI (Common Bill Ingestion) Endpoint Type` parameter, which determines whether a newly created CBI endpoint uses the Common Bill Ingestion Format or the FOCUS Format.
- Added the required `Cloud Vendor` parameter, which sets the `Cloud Vendor` dimension for a newly created CBI endpoint. A value must now be provided when applying the policy template.
- The `CBI (Common Bill Ingestion) Endpoint ID` parameter is now optional. If it is left blank, the endpoint ID is generated automatically from the endpoint type and cloud vendor.
- Creating a CBI endpoint requires the `org_owner` role on the Flexera credential. The role is not required if the CBI endpoint already exists. See the README for details.

## v0.1.5

- Fixed an issue where the policy would fail with an "unexpected response status" or "invalid argument in join" error when listing or downloading cost files from Azure Blob Storage, caused by internal hostname and container values not being passed to the request correctly.

## v0.1.4

- Added input sanitization to trim leading and trailing whitespace from string and list parameter values.

## v0.1.3

- Updated documentation link in policy description. Functionality unchanged.

## v0.1.2

- Updated heredocs in policy template code to conform to best practices. Functionality unchanged.

## v0.1.1

- Updated API requests to use newer Flexera API. Functionality unchanged.

## v0.1.0

- Initial release
