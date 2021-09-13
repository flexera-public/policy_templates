# Changelog

## v2.11

- Debug via param (off by default, for EU app)

## v2.10

- Added default_frequency "daily"

## v2.9

- Modified escalation label and description for consistency

## v2.8

- Added handling for log analytics workspaces that don't exist

## v2.7

- updated policy to check for log analytics and diagnostic enabled VM using resource properties field

## v2.6

- Updated escalation block
- fix spelling in path

## v2.5

- modified policy for handling 404 error

## v2.4

- adjusted Log Analytics auth provider tag

## v2.3

- adding incident resource table

## v2.2

- remove unnecessary permissions block

## v2.1

- Fixed bug where Azure returns instance details without MemoryGB field

## v2.0

- Removed the tagging escalation/action
- Added Resize action for underutilized instances
- Changed the authentication to credential services

## v1.1

- Added Approval block

## v1.0

- initial release
