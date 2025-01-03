# ITAM Asset Report

## What It Does

This policy produces a report of assets stored in Flexera ITAM based on the specified filters. Optionally, the report can be emailed.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Asset Status* - Only report assets with the selected status. Select 'All' to not filter results by asset status.
- *Asset Type* - Only report assets of the selected type. Select 'All' to not filter results by asset type.
- *Asset Location* - Only report assets in the specified location. Leave blank to not filter results by location.

## Policy Actions

- Sends an email report with the list of assets.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `di_viewer`
  - `policy_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
