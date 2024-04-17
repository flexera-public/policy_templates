# Changelog

## v4.4.1

- Added default value for parameters that do not require user input

## v4.4

- Changed internal name of escalation code to ensure "Meta Policy" works as expected

## v4.3

- Deprecated: This policy is no longer being updated. Please see policy README for more information.

## v4.2

- Updated description of `Account Number` parameter

## v4.1

- Added logic required for "Meta Policy" use-cases

## v4.0

- Added parameter to enable Allow or Deny filtering by user entered regions

## v3.1

- Raised API limit to handle situations where more than 10,000 line items need to be retrieved.

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)
- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.6

- Added filter for DescribeRegion to only return regions that are `opted-in` or `opt-in-not-required` [exclude `not-opted-in`] in the current AWS account.

## v2.5

- Added default to aws_account_number parameter to enable existing API users.

## v2.4

- Added support for a single AWS STS Cross account role to be used for multiple policies.

## v2.3

- updated README.md rightscale documentation links with docs.flexera documentation links

## v2.2

- Improve savings calculations based on pricing from the AWS Pricing API

- Determine Enterprise Discount Program ratio based on Optima costs or a parameter

- Support upgrading from io2 volumes as well

## v2.1

- Fix non-optimal array searching for costs

## v2.0

- Initial Release
