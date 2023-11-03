# SaaS Manager - User Status Change

## What it does

This policy will create an incident when Flexera SaaS Manager identifies users whose status in the HR roster changes to inactive. The data includes user details as well as department so a third party admin can forward the notification to managers responsible for a user in a particular department.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve user details. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with HR roster connected
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Number of Days Back* - If a user's status changes to inactive during this time period, those user accounts will raise an incident

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following permissions:
  - Administrator, Application Administrator, Viewer, or Security Administrator in FSM
