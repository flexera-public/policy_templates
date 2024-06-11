# Changelog

## v2.0.3

- Fixed a bug related to the Premium ssd price calculation with low throughput

## v2.0.2

- Fixed bug related to disk name calculation

## v2.0.1

- Fixed bug that caused wrong calculations for ultra tier disks

## v2.0

- Added support for regex when filtering resources by tag

## v1.2

- Updated the descriptions and labels of the IOPS and throughput parameters in the README and policy template files.
- Updated the short description of the policy.
- Fixed the functionality of *Minimum Savings Threshold* parameter. This parameter is used to suppress recommendations with potential savings below the specified threshold.

## v1.1

- Fixed error where policy would fail completely when trying to access resources credential does not have access to. Policy will now simply skip these resources.

## v1.0

- Initial release.
