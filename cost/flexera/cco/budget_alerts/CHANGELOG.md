# Changelog

## v2.6.1

- Updated policy to use internal Flexera API for generating charts. Policy functionality is unchanged.

## v2.6

- Updated policy metadata to make it more clear what Flexera service the policy is for

## v2.5

- Updated policy to use new source for currency information. Policy functionality is unchanged.

## v2.4

- Updated description to account for new file path in Github repository

## v2.3

- Added Deprecated description in the short description

## v2.2

- Deprecating this policy as it's replaced by [the new version](../budget_report_alerts)

## v2.1

- Resolved issues with calculating forecast
- Fixed issue with currentSpend subtracting 3 days unnecessarily

## v2.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`). This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied. Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v1.19

- Use provided keyword for Optima endpoint

## v1.18

- URIEncode all the image-charts options

## v1.17

- updated README.md rightscale documentation links with docs.flexera documentation links

## v1.16

- Adding budget threshold to policy.

## v1.15

- Fixed markdown alignment in HERE doc, which was causing the conversion to HTML in the email to fail.

## v1.14

- Modified escalation label and description for consistency
- Added incident resource table

## v1.13

- Added the ability to provide either Billing center name or Id.

## v1.12

- Fixed missing budget alert incident graph

## v1.11

- Fix first day issue with month

## v1.10

- Fix error when the policy run within the first 3 days of the month.

## v1.9

- Fixed evaluation exceeded maximum time
- Removed param_budget_scope

## v1.8

- Set timeframe to today - 3

## v1.7

- Updated the metadata

## v1.6

- Modified graph representation of the Actual budget alert

## v1.5

- Added graph representation of the Forecasted Full Month Spend/Actual Full Month Spend

## v1.4

- Added tenancy "single" in metadata

## v1.3

- ignore changing amounts when creating incidents so that emails are sent less frequently

## v1.2

- update policy to latest version of bill-analysis API
- update incident summary name

## v1.1

- round spend to 2 decimal places

## v1.0

- initial release
