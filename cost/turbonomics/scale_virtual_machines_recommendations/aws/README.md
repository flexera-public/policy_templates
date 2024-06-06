# Turbonomic Rightsize Virtual Machines Recommendations AWS

## What It Does

The Turbonomic Rightsize Virtual Machines Recommendations AWS policy utilizes Turbonomic Actions endpoint (POST xxxx.turbonomic.com/api/v3/markets/Market/actions), Business Units endpoint (GET xxxx.turbonomic.com/api/v3/businessunits) and Actions Details endpoint (POST xxxx.turbonomic.com/api/v3/actions/details) to provide Scale Virtual Machines Recommendations. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs.

## Input Parameters

- *Provider* - Cloud provider. Allows AWS.
- *Turbonomic Audience* - Audience configured on the Turbonomic instance
- *Email addresses* - A list of email addresses to notify.
- *Turbonomic Endpoint* - Host of the Turbonomic endpoint.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Turbonomic Credential**] which has the following roles:
  - `OBSERVER`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
