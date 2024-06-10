# Turbonomic Allocate Virtual Machine Recommendations AWS

## What It Does

The Turbonomic Allocate Virtual Machines Recommendations AWS policy utilizes Turbonomic (POST `https://turbonomic.com/api/v3/markets/{market_uuid}/actions`) endpoint to provide AWS VM allocation recommendations for Reserved Instance coverage. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs

## Functional Details

- The policy queries the `/api/v3/markets/{market_uuid}/actions` endpoint for the Turbonomic API and based on action will return action details and savings for on-boarded cloud instances

## Input Parameters

- *Turbonomic Audience* - Audience configured on the Turbonomic instance
- *Turbonomic Host* - Host of the Turbonomic endpoint.
- *Email addresses* - A list of email addresses to notify

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Turbonomic Credential**] The policy requires basic Turbonomic authentication credentials, ensure your Turbonomic credentials meet the following OAuth 2.0 authentication criteria:
  - On the Turbonomic side:
    - Ensure OAuth 2.0 authentication is enabled for your Turbonomic instance by adding `spec.oauth2.enabled: true` to your custom resource (CR) file.
    - Specify a unique audience value (`spec.properties.global.oauth2.audience`) in the custom resource (CR) file. This policy template use defualt value of `flexera` for audience parameter, but you can customize it with any unique string value and use that value.
    - Utilize the Turbonomic API to create an OAuth 2.0 client, configuring it with `role:OBSERVER` and using `client_secret_basic` for `clientAuthenticationMethods`.
  - On the Flexera side:
    - Add Turbonomic credentials using the provided `clientId` and `clientSecret`.
    - Ensure the credential is tagged with `provider=turbonomic` and use `Basic Auth` for Credential Type.
The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- AWS

## Cost

This Policy Template does not incur any cloud costs.
