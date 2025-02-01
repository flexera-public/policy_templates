# Changelog

## v2.3.2

- Fixed issue where tag keys that were not lowercase would not be properly detected and used

## v2.3.1

- Fixed issue that would sometimes cause execution to fail if an AWS Account had no tag keys

## v2.3.0

- Added option to retain original casing of tag values instead of normalizing them all to lowercase

## v2.2.1

- Updated policy template to use newer API endpoints. Functionality is unchanged.

## v2.2

- added ability to specify names for the newly created dimensions

## v2.1

- Corrected API issue when executing policy in APAC

## v2.0

- Removed requirement for AWS credential
- Internal API is now used to gather AWS account and tag information

## v1.0

- initial release
