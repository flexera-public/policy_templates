# SaaS Manager - Unsanctioned Applications with Existing Contract

## What it does

This policy will create an incident when Flexera SaaS Manager identifies unsanctioned SaaS purchases for managed applications under an existing license contract.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve managed SaaS applications and unsanctioned purchases. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `flexera_fsm`

Required permissions in the provider:

- Administrator, Application Administrator, Viewer, or Security Administrator in FSM

## Policy Actions

- Sends an email notification
