# Cheaper Regions Policy

## What it does

This Policy Template determines which regions have cheaper alternatives by specifying the expensive region name and the cheaper region name for analysis

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`
  - `policy_designer`
  - `policy_manager`
  - `policy_publisher`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

- This policy uses a hash to determine existing regions and newer compatible cheaper regions. It checks the billing center and reports on cheaper regions.

### Input Parameters

This policy has the following input parameters required when launching the policy.

- *Billing Center Name* - The list of Billing centers to check against
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Supported Clouds

- Azure Resource Manager
- Azure CSP
- Google
- Amazon

## Cost

This Policy Template does not incur any cloud costs.
