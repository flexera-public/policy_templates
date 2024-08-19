# ITAM Missing Active Machines

This policy uses the ITAM Inventories API to look up machines, when it finds a machine that is active we compare it's `lastInventoryDate` to the current time and
if it has not reported in during that time period an incident is triggered.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `fnms_user`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Days missing while active* - Number of missing for a machine to be reported
- *Email addresses of the recipients you wish to notify* - A list of email addresse(s) to notify

## Policy Actions

- Send an email report

## Cost

This Policy Template does not incur any additional cloud costs.
