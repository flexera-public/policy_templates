# Changelog

## v1.18.0

- Added parameters for the Policy Template Github Repo to enable this to be used for other repos without modifying Policy Template

## v1.17

- Changed the source of active policy list from S3 to GitHub

## v1.16

- Added additional checking if policy long description or policy version are not defined

## v1.15

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.14

- Add `auth: $$auth_rs` to `upload_template()` definition

## v1.13

- updating for flexera-public

## v1.12

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.11

- Adding `param_branch` to support automatic publishing to the EU Shard.

## v1.10

- fix an issue with publishing

## v1.9

- use the info field for version.

## v1.8

- update github org in path

## v1.7

- refactoring version comparison logic.

## v1.6

- Adding in changelog url

## v1.5

- use the update path if you get a code 409
- Excluding Policy Sync from publish
- Updated policy template to not publish Policy Template Synchronization template

## v1.4

- Updating policy sync to use s3
- Updating Policy Template Name

## v1.3

- Update email subject with account name and ID, and change actions and/or resolution name to be more descriptive. Issues #75 & #83

## v1.2

- Updating input parameter name for email

## v1.1

- Making email required.

## v1.0

- Initial Release
