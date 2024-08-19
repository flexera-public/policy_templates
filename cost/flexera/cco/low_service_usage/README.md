# Low Service Usage Policy

## Deprecated

This policy is no longer being updated. The [Low Usage Report](https://github.com/flexera-public/policy_templates/tree/master/cost/flexera/cco/low_usage/) policy has superseded this one and includes significantly more functionality.

## What it does

This Policy Template reports on services with low usage. Low usage of a specific service in a region by an account is often indicative of tests or experiments by users, which often are forgotten and left running. Investigate this usage to determine if it should be terminated or potentially consolidated into a larger account/region for ease of management.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_designer`
  - `policy_manager`
  - `policy_publisher`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy queries optima data to determine low account usage.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Low Service Spend Threshold* - Estimated run-rate below which a service should be reviewed for wasted usage. Example: 100.0
- *Email addresses* - A list of email addresses to notify
- *Billing Center Name* - List of Billing Center Names to check
- *Minimum Savings Threshold* - Specify the minimum monthly savings value required for a recommendation to be issued, on a per resource basis. Note: this setting applies to all recommendations. Example: 1.00

## Supported Clouds

- Azure Resource Manager
- Azure CSP
- Google
- Amazon

## Cost

This Policy Template does not incur any cloud costs.
