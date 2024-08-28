# GitHub Available Seats

## What It Does

This policy template checks the user-specified GitHub organizations and reports any that are outside of the user-specified thresholds for available seats. Optionally, these reports can be emailed.

## Input Parameters

- *Email Addresses* - A list of email addresses to notify.
- *GitHub Organizations* - A list of GitHub Organizations to check.
- *Minimum Available Seats Required* - The minimum number of available seats to require. Set to `0` to not require any minimum.
- *Maximum Available Seats Allowed* - The maximum number of available seats to allow. Set to `-1` to have no maximum.

## Policy Actions

- Sends an email notification.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**GitHub Credential**](https://docs.flexera.com/flexera/EN/Automation/GenericCredentials.htm#automationadmin_1982464505_1121389) (*provider=github*) which has the following permissions:
  - `admin:org`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- GitHub

## Cost

This Policy Template does not incur any cloud costs.
