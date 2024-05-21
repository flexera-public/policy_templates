# Changelog

## v3.0.0

- Billing Center list can now be used as an allow list or a deny list
- Added logic to prevent duplicate results due to overlapping child/parent billing centers
- Added additional context to incident output
- Normalized incident output for parity with other policy templates
- Streamlined code for better readability and faster execution

## v2.2

- Updated policy metadata to correctly identify it as an AWS policy

## v2.1

- Added new parameter to allow users to filter reservations by a list of specific billing centers.
- Updated `param_utilization` parameter to have a clearer description, and to set the default utilization threshold to 100%.
- Removed `permission` declaration block as no longer needed.
- Updated README title to reflect policy template name.
- Updated "Credential Configuration" section in README to reflect the correct credentials required to run the policy.

## v2.0

- Deprecated `rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.14

- Added default_frequency "daily"

## v1.13

- Modified escalation label and description for consistency

## v1.12

- Adding incident resource table

## v1.11

- Updated datasource to leverage new API URI

## v1.10

- Updated the metadata

## v1.9

- Updated policy name to reflect supported cloud.

## v1.8

- Add `scope` and `type` to incident report

## v1.7

- Updated percentage to rounded version
- Updated Label to be more descriptive

## v1.6

- Fixed email format

## v1.4

- Updating email from string to list

## v1.3

- switching from html tables to markdown tables
- removing parameter: org_id for rs_org_id

## v1.2

- Changing Severity from medium to high

## v1.1

- fixing data source path to use org_id

## v1.0

- initial release
