# Low Account Usage Policy

## What it does

This Policy Template reports on accounts with low usage. Accounts with very low usage often stem from tests or experiments and it is typical for users to forget to shut down all servers and services in such accounts. Investigate these accounts to determine if they should be cancelled or could be consolidated into larger accounts for ease of management.

## Prerequisites

This policy uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_designer`
  - `policy_manager`
  - `policy_publisher`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy queries optima data to determine low account usage. Because AWS `APNFee` is not a usage item, we have removed it from this policy. This will cause some of the recommendations to not match optima recommendations.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Low Account Spend Threshold* - All accounts below this budget will trigger an incident
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
