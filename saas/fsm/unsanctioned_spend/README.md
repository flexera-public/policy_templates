# SaaS Manager - Unsanctioned Spend

## What it does

This policy will create an incident when Flexera SaaS Manager identifies unsanctioned spend on SaaS applications.

## Functional Description

This policy integrates with the Flexera SaaS Manager API to retrieve the expense data that has been flagged as unsanctioned. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with expense system connected
- Retrieve a Flexera IAM refresh token for authentication
- The Flexera IAM refresh token must then be stored as a RightScale Credential in the account in which this policy will be applied. The credential must be named `FSM_TOKEN`.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of Days Back* - Any unsanctioned expenses discovered during this time period will raise an incident
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `flexera_fsm`

Required permissions in the provider:

- Security Administrator or Administrator in FSM

## Policy Actions

- Sends an email notification 
