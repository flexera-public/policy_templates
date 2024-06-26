# GitHub Repositories without Admin Team

## What It Does

This policy template reports on any repositories under the user-specified GitHub organizations that do not have any associated teams with the `admin` role. Optionally, it emails this report.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *GitHub Organizations* - A list of GitHub Organizations to check.
- *Allow/Deny GitHub Repositories* - Whether to treat Allow/Deny GitHub Repositories List parameter as allow or deny list. Has no effect if Allow/Deny GitHub Repositories List is left empty.
- *Allow/Deny GitHub Repositories List* - Filter results by GitHub repository, either only allowing this list or denying it depending on how the above parameter is set. Leave blank to consider all the GitHub repositories in the specified organizations.

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
