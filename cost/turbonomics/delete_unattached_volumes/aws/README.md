# Turbonomic Delete Unattached Volumes Recommendations AWS

## What It Does

The Turbonomic Delete Unattached Volumes Recommendations AWS policy uses Turbonomic Actions API endpoint (POST xxxx.turbonomic.com/api/v3/markets/Market/actions) and Business Units endpoint (GET xxxx.turbonomic.com/api/v3/businessunits) to provide delete unattached volumes recommendations. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs.

## Functional Details

- The policy queries the /api/v3/market/{market_uuid}/actions endpoint for the Turbonomic API and based on action will return details and savings for unattached volumes for on-boarded cloud instances.

## Input Parameters

- *Provider* - Cloud provider where we get recommendations, it supports Azure.
- *Turbonomic Audience* - Audience configured on the Turbonomic instance
- *Email addresses to notify* - A list of email addresses to notify.
- *Turbonomic endpoint* - Turbonomic endpoint where we'll get all data and authorization validation.
- *Unused days* - The number of days a volume has been unused. The days should be greater than zero.

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

- This Policy Template does not incur any cloud cost
