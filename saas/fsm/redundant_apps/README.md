# SaaS Manager - Redundant Apps

## What it does

This policy will create an incident when Flexera SaaS Manager identifies application categories with an excessive number of applications.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve Managed SaaS Application details. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with HR roster connected
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Excessive Number of Apps in a Single Category* - Threshold to trigger detection of excessive SaaS applications in a single category

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following permissions:
  - Administrator, Application Administrator, Viewer, or Security Administrator in FSM
