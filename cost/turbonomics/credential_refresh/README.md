# Turbonomic Credential Refresh Policy

The Turbonomic Credential Refresh policy is designed to refresh the cookie used to authenticate with Turbonomic APIs. It ensures that the authentication token remains up to date for accessing Turbonomic services.

The purpose of this policy is to refresh the authentication cookie used to authenticate with Turbonomic APIs. It addresses the challenge of using a cookie-based authentication method in Turbonomic, which is not supported by Flexera due to its outdated nature and the industry trend of switching to newer and more secure authentication methods. As Turbonomic plans to implement bearer token authentication in the future, this policy serves as a temporary workaround for the integration to connect to Turbonomic APIs.

## What it does

The policy periodically checks for applied policies in the project that are related to Turbonomic. If any Turbonomic policies are found, the policy checks the scheduled run times of these policies and determines if an update is necessary. If the next scheduled run of a Turbonomic policy is before the next refresh by the credential updater, it initiates an escalation process to update the authentication cookie used for Turbonomic APIs. The policy retrieves the necessary credentials and makes API calls to Turbonomic to obtain a fresh cookie. It then updates the applied Turbonomic policies with the new authentication cookie, ensuring seamless authentication for Turbonomic API calls.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (_provider=flexera_)

## Input Parameters

This policy requires the following input parameters:

- **Turbonomic Username** - username associated with your Turbonomic API credentials.
- **Turbonomic Password** - password associated with your Turbonomic API credentials.
- **Turbonomic Host** - turbonomic hostname or IP address.

## Policy Actions

The policy performs the following action:

- Updates the authentication cookie parameter for Turbonomic policies with a refreshed cookie.

### Required Flexera Roles

- policy_manager

## Cost

This Policy Template does not incur any additional costs.
