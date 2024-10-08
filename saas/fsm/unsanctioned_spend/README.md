# SaaS Manager - Unsanctioned Spend

## What It Does

This policy will create an incident when Flexera SaaS Manager identifies unsanctioned spend on SaaS applications.

## How It Works

This policy integrates with the Flexera SaaS Manager API to retrieve the expense data that has been flagged as unsanctioned. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with expense system connected
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Unsanctioned Application Names* - List of SaaS Application names that the policy will target for identifying unsanctioned spend. Note: if left blank, the policy will detect all unsanctioned spend.
- *Number of Days Back* - Any unsanctioned expenses discovered during this time period will raise an incident.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following Flexera SaaS Manager permissions:
  - `SaaS Manager: Viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
