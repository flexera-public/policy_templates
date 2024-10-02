# SaaS Manager - Renewal Reminder

## What It Does

This policy will create an incident when Flexera SaaS Manager identifies application licenses whose expiration date is approaching.

## How It Works

This policy uses the [SaaS Management API](https://developer.flexera.com/docs/api/saas/v1) to retrieve a list of managed SaaS applications and their licenses. The policy then determines how many days away the licenses are from expiration.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Applications* - A list of application names and/or IDs to check. Leave blank to check all applications.
- *Days Until Expiration* - The number of days before the license expires. All licenses set to expire in fewer days than the specified value will be included in the report.

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

This Policy Template does not incur any cloud costs.
