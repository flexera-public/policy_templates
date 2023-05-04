# Changelog

## v3.1

- Parameter `Savings Plan ARN` is now optional.  If not provided, the policy will return utilization for all Savings Plans in the account.
- Default threshold changed from `70` to `100`.  This is intended to enable the policy to enable the user to easy report on Savings Plan Utilization for all Savings Plans in the account.
- Payer Account ID added to the Incident Summary.  This is helpful for users with multiple AWS Payer Accounts.

## v3.0

- Deprecated `auth_rs` authentication (type: `rightscale`) and replaced with `auth_flexera` (type: `oauth2`).  This is a breaking change which requires a Credential for `auth_flexera` [`provider=flexera`] before the policy can be applied.  Please see docs for setting up [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm)

## v2.2

- Replaced references `github.com/rightscale/policy_templates` and `github.com/flexera/policy_templates` with `github.com/flexera-public/policy_templates`

## v2.1

- Updated policy "summary_template" name
- Updated image-charts url

## v2.0

- Initial release
