# Changelog

## v1.15

- Added resource table

## v1.14

- Included README link in the policy template

## v1.13

- Updated the metadata

## v1.12

- Rename policy to Inefficient Instance Utilization using RightLink
- Add support for VMWare w/RCA-v

## v1.11

- Added aws instance types: memory optimize r5, r5a, r5d, x1e,z1d
- Added aws instance types: compute optimized c5n, c5d
- Added aws instance types: general purpose added m5a, m5d, a1
- Added aws instance types: one f1, one g2, g3 family

## v1.10

- Added cpu and memory datapoint check for instances that are operational, but not sending monitoring data back to the platform.

## v1.9

- Changed total memory calculation to use instance_type memory attribute.

## v1.8

- Upating Policy Template Name

## v1.7

- Update email subject with account name and ID, and change actions and/or resolution name to be more descriptive. Issues #75 & #83

## v1.6

- Updating input parameter name for email

## v1.5

- Adding the count of resources detected in the incident summary and details.

## v1.4

- Filtering to only look at clouds represented in instance_types.json.
- Added current instance type to the output report.

## v1.3

- Adding in downsize actions
- Adding tag validations
- Adding support for RL10 instances only
- Using tag field now instead of tag datasource
- Once a server can no longer be downsized in the current family, its marked NA and tag removed

## v1.2

- Updating email from string to list

## v1.1

- Removing defaults

## v1.0

- initial release
