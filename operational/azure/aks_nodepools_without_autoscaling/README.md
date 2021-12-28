# AKS Node Pools Without Autoscaling

## What it does

This policy will raise an incident if there are any AKS clusters with user node pools that do not have autoscaling enabled.

## Functional Details

This policy checks all the user node pools associated with each AKS cluster. If the 'enableAutoScaling' value for a node pool is set to 'false', that node pool is added to the list of problematic pools, and an incident is raised if this list contains any items.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tags* - Cloud native tag keys to ignore instances. Example: exclude_utilization
- *Email addresses* - Email addresses of the recipients you wish to notify.
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Whitelist* - Whitelisted Subscriptions, if empty, all subscriptions will be checked

## Actions

- Sends an email notification

## Prerequisites

This policy uses [credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.rightscale.com/policies/users/guides/credential_management.html) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Subscription/aliases/read
- Microsoft.ContainerService/managedClusters/*

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
