# SaaS Manager - Deactivated Users

## What It Does

This policy will create an incident when Flexera SaaS Manager identifies managed SaaS application user accounts that have been deactivated for longer than a user-specified threshold. An incident is raised with a list of these users.

## How It Works

This policy uses the [SaaS Management API](https://developer.flexera.com/docs/api/saas/v1) to retrieve a list of managed SaaS applications and their users. The policy then filters for users with a `deactivatedAt` date and calculates the number of days since the user was deactivated.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Applications* - A list of application names and/or IDs to check for deactivated users. Leave blank to check all applications.
- *Inactive Days Threshold* - Number of days since user was deactivated to include it in the results.

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
