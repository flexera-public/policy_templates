# SaaS Manager - User Status Change

## Deprecated

This policy is no longer being updated. The [SaaS Manager - Deactivated Users](https://github.com/flexera-public/policy_templates/tree/master/saas/fsm/deactivated_users/) policy now includes this functionality and is the recommended policy for finding users whose status has changed.

## What It Does

This policy will create an incident when Flexera SaaS Manager identifies users whose status in the HR roster changes to inactive. The data includes user details as well as department so a third party admin can forward the notification to managers responsible for a user in a particular department.

## How It Works

This policy integrates with the Flexera SaaS Manager API to retrieve user details. Therefore the following are prerequisites for this policy to execute:

- Flexera SaaS Manager implementation with HR roster connected
- Please contact your Flexera Customer Success Manager for assistance to generate your FSM token.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of Days Back* - If a user's status changes to inactive during this time period, those user accounts will raise an incident
- *Email addresses to notify* - Email addresses of the recipients you wish to notify

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
