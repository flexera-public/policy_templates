# SaaS Manager - Redundant Apps

## What It Does

This policy will create an incident when Flexera SaaS Manager identifies application categories with an excessive number of applications.

## How It Works

This policy uses the [SaaS Management API](https://developer.flexera.com/docs/api/saas/v1) to retrieve a list of managed SaaS applications and their categories. The policy then counts the number of applications in each category, raising an incident with a list of application categories where the number of applications exceeds a user-specified threshold.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Category Application Limit* - The number of SaaS applications within a single category required to report on the category.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following Flexera SaaS Manager permissions:
  - Administrator, Application Administrator, Viewer, or Security Administrator

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any cloud costs.
