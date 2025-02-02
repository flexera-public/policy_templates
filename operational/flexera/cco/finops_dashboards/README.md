# FinOps Dashboards

## What It Does

This policy template creates a series of FinOps cloud dashboards within the Flexera organization. Created dashboards are public and can be accessed at the Dashboards -> Cloud page in Flexera One. Optionally, information about the newly created dashboards can be emailed.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new dashboards are created.
- *Dashboards* - The specific dashboards you wish to create.

## Policy Actions

- Creates selected dashboards
- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `csm_dashboard_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any additional costs.
