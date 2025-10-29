# ITAM Expiring Licenses

## What It Does

Generates report of licenses expiring and sends the result as an email.

## How It Works

This policy template uses the ITAM API to look up Active IT Asset Manager Licenses Expiring within set Time Period and sends the result as an email.

The report / Mail output looks like this:
ITAM Expiring Licenses

| licenseId | publisher | licenseName | version | edition | licenseStatus | licenseDuration | licenseType | expiryDate |
| --------- | --------- | ----------- | ------- | ------- | ------------- | --------------- | ----------- | ---------- |
| 12345 | Adobe | Acrobat Pro | 2022 | Professional | [Active] | [Subscription] | [Named User] | 2022-03-31T00:00:00Z |
| 54321 | Microsoft | Visio Pro | 2019 | Professional | [Active] | [Subscription] | [Named User] | 2021-08-31T00:00:00Z |

Current limitations:

- Output is limited to max 100000 rows.

## Input Parameters

This policy template has the following input parameters:

- *Time Period of Expiration* - Time Period, in days, to find licenses expiring within
- *Email addresses of the recipients you wish to notify* - A list of email address(es) to notify

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy template you must have a Credential registered in the system that is compatible with this policy template. If there are no Credentials listed when you apply the policy template, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy template. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `fnms_user`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Flexera

## Cost

This Policy Template does not incur any additional cloud costs.
