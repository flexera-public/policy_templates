# SaaS Manager - Duplicate User Accounts

## What it does

This policy will create an incident when Flexera SaaS Manager identifies duplicate user accounts within a single managed SaaS application.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve SaaS Applications and will generate reminders for applications whose renewals are approaching. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following permissions:
  - Administrator, Application Administrator, Viewer, or Security Administrator in FSM
