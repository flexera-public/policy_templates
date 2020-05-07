# SaaS Manager - User Status Change

## What it does

This policy will create an incident when Flexera SaaS Manager identifies users whose status in the HR roster changes to inactive. The data includes user details as well as department so a third party admin can forward the notification to managers responsible for a user in a particular department.


## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve user details. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with HR roster connected
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of Days Back* - If a user's status changes to inactive during this time period, those user accounts will raise an incident
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

