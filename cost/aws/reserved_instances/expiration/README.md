# AWS Expiring Reserved Instances

## Deprecated

This policy is no longer being updated.

## What it does

This Policy Template leverages the Optima Bill Data for AWS Reserved Instances. It will notify only if expiration is within the timeframe specified in `Number of days to prior to expiration date to trigger incident` field. It will email the user specified in `Email addresses of the recipients you wish to notify`.

## Prerequisites

This Policy Template uses [Credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for authenticating to datasources -- in order to apply this policy you must have a Credential registered in the system that is compatible with this policy. If there are no Credentials listed when you apply the policy, please contact your Flexera Org Admin and ask them to register a Credential that is compatible with this policy. The information below should be consulted when creating the credential(s).

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `actor`
  - `observer`
  - `credential_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Number of days to prior to expiration date to trigger incident* - enter the number of days you want before the Reserved Instance expires.
- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

The following policy actions are taken on any resources found to be out of compliance.

- Send an email report

## Supported Clouds

- AWS

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
