# Flexera IAM Explicit User Roles

This policy identifies users in Flexera IAM that have explicit user roles assigned.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `enterprise_manager`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Functional Details

This policy leverages the Flexera IAM API to collect a list of users that have explicit roles assigned.
Best practices dictate that role sbe assigned to groups and users be added/removed from groups based on the level of access they require.

## Input Parameters

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Actions

- Emails a report of users with explicit permissions assigned.

### Credential Configuration

This policy uses pass-thru authentication and does not require a credential to be configured.

## Supported Services

- Flexera IAM

## Cost

This Policy Template does not incur any cloud costs.
