# Turbonomic Buy Reserved Instances Recommendations Azure

## What It Does

The Turbonomic Buy Reserved Instances Recommendations AWS policy utilizes Turbonomic Actions API endpoint (POST `https://turbonomic.com/api/v3/markets/{market_uuid}/actions`) to provide AWS RI purchase recommendations.

## Functional Details

- The policy queries the /api/v3/markets/{market_uuid}/actions endpoint for the Turbonomic api and based on action will return action details and savings for on-boarded cloud instances

## Input Parameters

- *Turbonomic Audience* - Audience configured on the Turbonomic instance
- *Turbonomic Host* - Host of the Turbonomic endpoint.
- *Email addresses* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Turbonomic Credential**] which has the following roles:
  - `OBSERVER`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
