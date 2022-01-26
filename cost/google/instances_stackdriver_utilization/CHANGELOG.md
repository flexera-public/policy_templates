# Changelog

## v2.11

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.10

- Debug via param (off by default, for EU app)

## v2.9

- Added default_frequency "daily"

## v2.8

- Fixed a bug where calculating maximum and minimum numbers in an array returns NaN

## v2.7

- Modified escalation label and description for consistency

## v2.6

- Updated escalation block

## v2.5

- move cpu calculations from jmespath to javascript
- removed disk utilization metrics
- added additional filter to StackDriver API call to increase efficiency

## v2.4

- Adding incident resource table

## v2.3

- Bug fixes on unhandled errors when executing

## v2.2

- remove unnecessary permissions block

## v2.1

- Added new datasource for google project ID

## v2.0

- Removed the tagging escalation/action
- Added parameters for Avg CPU and memory
- Added Resize action for underutilized instances
- Changed the authentication to credential services
- changed name of policy to Google Inefficient Instance Utilization using StackDriver

## v1.3

- New action added to downsize the instances whose memory and CPU utilisation is less.

## v1.2

- fix readme link

## v1.1

- Fixing nil error in calculations

## v1.0

- initial release
