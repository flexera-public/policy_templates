# Changelog

## v1.0.0

- The policy template now creates the CBI endpoint (bill connect) automatically if it does not already exist. Previously, the CBI endpoint had to be created in advance using the Flexera Bill Connect API.
- Added the `CBI (Common Bill Ingestion) Endpoint Type` parameter, which determines whether a newly created CBI endpoint uses the Common Bill Ingestion Format or the FOCUS Format.
- Added the required `Cloud Vendor` parameter, which sets the `Cloud Vendor` dimension for a newly created CBI endpoint. A value must now be provided when applying the policy template.
- The `CBI (Common Bill Ingestion) Endpoint ID` parameter is now optional. If it is left blank, the endpoint ID is generated automatically from the endpoint type and cloud vendor.
- Creating a CBI endpoint requires the `org_owner` role on the Flexera credential. The role is not required if the CBI endpoint already exists. See the README for details.

## v0.1.6

- Fixed an issue where the policy would fail with an "unexpected response status" or "cannot unmarshal object into Go struct field" error when listing or downloading cost files from S3, caused by an internal hostname value not being passed to the request correctly.

## v0.1.5

- Fixed an issue where the policy could fail to determine which files still needed to be uploaded once all files for a billing period had already been uploaded, preventing the bill upload from progressing to completion.
- Fixed an issue where selecting "Previous Month" as the billing period could cause the policy to compute the wrong billing period on certain calendar dates (the 1st of January, April, June, August, and November), causing it to look for and upload the wrong month's cost files.

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
