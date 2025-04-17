# Flexera Automation Disallowed Credentials

## What It Does

This policy template reports credentials in Flexera Automation that are not in a user-specified list of allowed credentials. Optionally, the list can be emailed and disallowed credentials can be deleted.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Credential Scope* - Whether to report on Organization-level or Project-level credentials. Select both to report both. Only Project-level credentials in the specific project this policy template is applied in will be reported.
- *Credential Allow List* - The names/IDs of credentials that are allowed to exist in Flexera Automation. If a credential is not on this list, it will be reported as disallowed.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Policy Actions

- Sends an email notification
- Delete disallowed credential after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `credential_viewer`
  - `iam_admin`*

  \* Only required for taking action; the policy will still function in a read-only capacity without these permissions.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
