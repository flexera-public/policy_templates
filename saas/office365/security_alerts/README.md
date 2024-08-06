# Office 365 Security Alerts

## What It Does

This policy template reports any Security Alerts that have been raised in Office 365. Optionally, this report can be emailed.

## How It Works

The [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/api/security-list-alerts_v2?view=graph-rest-1.0&tabs=http#http-request) is used with appropriate filters to retrieve Office 365 security alerts.

## Input Parameters

- *Email Addresses* - Email addresses of the recipients you wish to notify
- *Alert Severity* - The alert severity levels to report.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Microsoft Graph Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_1982464505_1121576) (*provider=azure_graph*) which has the following permissions:
  - `SecurityEvents.Read.All`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Microsoft Office 365

## Cost

This Policy Template does not incur any cloud costs.
