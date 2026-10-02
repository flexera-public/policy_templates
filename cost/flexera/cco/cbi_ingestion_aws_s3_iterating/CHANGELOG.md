# Changelog

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
