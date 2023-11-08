# SaaS Manager - Duplicate User Accounts

## What It Does

This policy will create an incident when Flexera SaaS Manager identifies duplicate user accounts within a single managed SaaS application. An incident is raised with a list of duplicate users.

## Functional Description

This policy uses the [SaaS Management API](https://developer.flexera.com/docs/api/saas/v1) to retrieve a list of managed SaaS applications and their users. The policy then looks for duplicate users within each application. Users are considered duplicates if they share the same first name, last name, and email address. These fields are normalized to lowercase and have extraneous whitespace removed to ensure matching occurs when appropriate.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - Administrator, Application Administrator, Viewer, or Security Administrator in FSM

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.
