# FinOps Dashboards

## What It Does

This policy template creates a series of FinOps cloud dashboards within the Flexera organization. Created dashboards are public and can be accessed at the Dashboards -> Cloud page in Flexera One. Optionally, information about the newly created dashboards can be emailed.

__NOTE: This policy template only needs to execute once to perform the above task. It is recommended that the policy template be terminated after execution completes.__

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new dashboards are created.
- *Dashboards (Built-In)* - The specific built-in dashboards you wish to create.
- *Dashboards (External)* - The full URLs of any external dashboards you wish to also create. External dashboards must be publicly accessible and in JSON format matching the Flexera Dashboard API. Example JSON files can be found [here](https://github.com/flexera-public/policy_templates/tree/master/data/dashboards). Example: https[]()://awebdomain.com/path/dashboard_file.json

## Policy Actions

- Creates selected dashboards
- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `csm_dashboard_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any additional costs.
