# Turbonomic Rightsize Databases Recommendations Google

## What It Does

The Turbonomic Rightsize Databases Recommendations Google policy uses Turbonomic Actions endpoint (POST xxxx.turbonomic.com/api/v3/markets/Market/actions) and Business Units endpoint (GET xxxx.turbonomic.com/api/v3/businessunits) to provide rightsize Database/DatabaseServer recommendations. From these recommendations we provide monthly savings estimates based on Turbonomic per hour costs.

## Input Parameters

- *Provider* - Cloud provider where we get recommendations, it supports GCP.
- *Turbonomic Audience* - Audience configured on the Turbonomic instance
- *Email addresses to notify* - A list of email addresses to notify.
- *Turbonomic endpoint* - Turbonomic endpoint where we'll get all data and authorization validation.

## Policy Actions

- Send an email report

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Turbonomic Credential**] The policy requires basic Turbonomic authentication credentials, ensure your Turbonomic credentials meet the following OAuth 2.0 authentication criteria:
  - On the Turbonomic side:
    - Ensure OAuth 2.0 authentication is enabled for your Turbonomic instance by adding `spec.oauth2.enabled: true` to your custom resource (CR) file.
    - Specify a unique audience value (`spec.properties.global.oauth2.audience`) in the custom resource (CR) file. This policy template use default value of `flexera` for audience parameter, but you can customize it with any unique string value and use that value.
    - Utilize the Turbonomic API to create an OAuth 2.0 client, configuring it with `role:OBSERVER` and using `client_secret_basic` for `clientAuthenticationMethods`.
  - On the Flexera side:
    - Add Turbonomic credentials using the provided `clientId` and `clientSecret`.
    - Ensure the credential is tagged with `provider=turbonomic` and use `Basic Auth` for Credential Type.

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This policy template does not incur any cloud costs.
