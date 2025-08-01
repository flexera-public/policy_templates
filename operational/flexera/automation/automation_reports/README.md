# Automation Reports

## What It Does

This policy template generates reports on various aspects of automation within the Flexera One platform. The user can select to generate reports on applied policies, policy templates, and incidents. Optionally, these reports can be emailed.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *Reports* - A list of reports you wish to generate.
  - **Applied Policies** - Reports all active applied policies.
  - **Policy Templates** - Reports all uploaded policy templates.
  - **Incidents** - Reports all active policy incidents.
- *Child Policies* - Whether to include child policies/incidents in the Applied Policies and Incident reports. Child policies are created when using meta parent policies but are hidden from view in the Flexera One UI.
- *Aggregates* - Whether to include aggregates in the Applied Policies and Incident reports. Aggregates are created when a policy template is applied at the organization level across multiple projects.

## Policy Actions

- Send an email report.
- Terminate applied policy after approval.
- Resolve incident after approval.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `policy_viewer`
  - `policy_manager`*

  \* Only required for taking action (terminating applied policies and resolving incidents); the policy will still function in a read-only capacity without these permissions.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
