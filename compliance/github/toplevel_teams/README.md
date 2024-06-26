# GitHub Top-Level Teams

## What It Does

This policy template reports any GitHub teams under the user-specified GitHub organizations that are top-level (have no parent) and are not on a user-specified list of permitted top-level teams. Optionally, it emails this report.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *GitHub Organizations* - A list of GitHub Organizations to check.
- *Allowed Top-Level Teams* - Teams that are permitted to be top-level and should not be included in the results.

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**GitHub Credential**](https://docs.flexera.com/flexera/EN/Automation/GenericCredentials.htm#automationadmin_1982464505_1121389) (*provider=github*) which has the following permissions:
  - `admin:org`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- GitHub

## Cost

This Policy Template does not incur any cloud costs.
