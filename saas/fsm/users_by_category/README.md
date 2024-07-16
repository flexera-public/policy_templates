# SaaS Manager - Redundant Apps

## What It Does

This policy will create an incident when Flexera SaaS Manager identifies users entitled to SaaS apps within a specified department.

## How It Works

This policy integrates with the Flexera SaaS Manager API to retrieve Managed SaaS Application details. The following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with HR roster connected.
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Department* - Department to report on entitled SaaS subscription users

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera SaaS Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera_fsm*) which has the following Flexera  permissions:
  - Administrator, Application Administrator, Viewer, or Security Administrator

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
