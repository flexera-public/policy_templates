# Google Credential

## What It Does

This policy template tests whether the selected Google credential is able to successfully make a "projects.list" REST API request to the Google Cloud Resource Manager API. If this request succeeds, an incident is raised reporting the success, and optionally, this incident can be emailed. If this request fails, the policy template will fail to complete and will show an error in Flexera One.

__NOTE: This policy template is intended to be used in conjunction with its associated meta parent policy template. Please see the [Meta README](https://github.com/flexera-public/policy_templates/tree/master/automation/google/google_credential/META_README.md) for more information.__

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Google Cloud Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4083446696_1121577) (*provider=gce*) which has the following:
  - `resourcemanager.projects.get`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
