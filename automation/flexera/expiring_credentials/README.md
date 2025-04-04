# Flexera Automation Expiring Credentials

## What It Does

This policy template checks for expiring credentials in Flexera Automation and notifies users before the credentials expire. Optionally, expired or expiring credentials can be deleted.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Credential Scope* - Whether to report on Organization-level or Project-level credentials. Select both to report both. Only Project-level credentials in the specific project this policy template is applied in will be reported.
- *Report Credentials With No Expiration Date* - Whether or not to consider credentials with no expiration date as expired and report on them.
- *Days Until Expiration* - The number of days before expiration to report on an expiring credential. Set to 0 to only report on already-expired credentials.
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Policy Actions

- Sends an email notification
- Delete expiring credential after approval

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential Configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `governance:published_template:index`
  - `governance:published_template:show`
  - `governance:policy_aggregate:index`
  - `governance:policy_aggregate:show`
  - `governance:applied_policy:index`
  - `governance:applied_policy:show`
  - `governance:policy_aggregate:create`*
  - `governance:policy_aggregate:delete`*
  - `governance:applied_policy:create`*
  - `governance:applied_policy:delete`*

\* Only required for taking action (updating applied policies); the policy will still function in a read-only capacity without these permissions.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
