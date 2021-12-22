# Expiring Azure Certificates

## What it does

This policy will raise an incident if there are expired and almost expired certificates on the Azure account in active use.

## Functional Details

This policy checks all the certificates on the Azure account in active use. If there are expired and/or almost expired certificates, an incident is raised, and a report listing the relevant certificates is provided.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tag Key* - Cloud native tag key to ignore instances. Example: exclude_utilization
- *Email addresses* - Email addresses of the recipients you wish to notify.
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Whitelist* - Whitelisted Subscriptions, if empty, all subscriptions will be checked
- *Days* - Number of days from expiration that should trigger the policy to raise an incident.

## Actions

- Sends an email notification

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Subscription/aliases/read
- Microsoft.Web/certificates/Read

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
