# Flexera One User Access Report

## What It Does

This policy template provides a report of every role assigned to a user in Flexera One. Optionally, this report can be emailed.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify.
- *Report Inactive Roles* - Whether to include roles that are not active for users in the results. If enabled, the report will contain an entry for every possible role for every user, regardless of whether it is active for that user. The `Role Status` field will indicate if the role is active or not.

## Policy Actions

- Sends an email notification

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

### Credential configuration

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `iam_admin`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This policy template does not incur any cloud costs.
