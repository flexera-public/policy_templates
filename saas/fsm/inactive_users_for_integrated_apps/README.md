# SaaS Manager - Inactive Users for Integrated Applications

## What it does

This policy retrieves inactive users for the Integrated Applications of the specified Managed SaaS Application and creates an incident with the output.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve inactive users for Integrated Applications of a Managed SaaS Application that facilitates this application discovery through such integration.. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with HR roster connected
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify
- *Application Name* - Name of the managed application for which you wish to retrieve inactive users for its integrated applications.

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

Other prerequisites:

- Ensure that the Application integration task is successfully configured and executing its application discovery task for the Managed SaaS Application.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `flexera_fsm`

Required permissions in the provider:

- Administrator, Application Administrator, Viewer, or Security Administrator in FSM

## Policy Actions

- Sends an email notification
