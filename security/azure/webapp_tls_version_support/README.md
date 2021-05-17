# Azure Web App Minimum TLS Version

## What it does

This Policy checks for Azure Web Apps with a minimum TLS version less that the value specified when the policy is applied.

## Functional Details

- This Policy identifies all Azure Web Apps where the property `minTlsVersion` is less than the policy parameter *Minimum TLS Version*.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Minimum TLS Version* - The minimum TLS version supported
- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Web App List

## Supported Clouds

- Azure

## Cost

This policy does not incur any cloud costs.
