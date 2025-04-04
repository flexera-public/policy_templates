# Flexera Automation Expiring Credentials

## What It Does

This policy template reports expired or soon-to-expire credentials in Flexera Automation. Optionally, the list can be emailed and expired or soon-to-expire credentials can be deleted.

NOTE: Credential expiration dates must be manually entered for the credential in Flexera One on the Automation -> Credentials page for this policy template to correctly discern when the credential is going to expire.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Credential Scope* - Whether to report on Organization-level or Project-level credentials. Select both to report both. Only Project-level credentials in the specific project this policy template is applied in will be reported.
- *Report Credentials With No Expiration Date* - Whether or not to consider credentials with no expiration date expired and report on them.
- *Days Until Expiration* - The number of days before expiration to report on an expiring credential. Set to 0 to only report on already-expired credentials.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Policy Actions

- Sends an email notification
- Delete expiring credential after approval

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
