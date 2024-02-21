# AKS Node Pools Without Zero Autoscaling

## What it does

This policy will raise an incident if there are any AKS clusters with user node pools that do not have autoscaling enabled with a minimum node count of 0.

## Functional Details

This policy checks all the user node pools associated with each AKS cluster. If the 'enableAutoScaling' value for a node pool is set to 'false', or the 'minCount' value is not set to 0, that node pool is added to the list of problematic pools, and an incident is raised if this list contains any items.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tags* - The policy will filter resources containing the specified tags from the results. The following formats are supported:
  - `Key` - Filter all resources with the specified tag key.
  - `Key==Value` - Filter all resources with the specified tag key:value pair.
  - `Key!=Value` - Filter all resources missing the specified tag key:value pair. This will also filter all resources missing the specified tag key.
  - `Key=~/Regex/` - Filter all resources where the value for the specified key matches the specified regex string.
  - `Key!~/Regex/` - Filter all resources where the value for the specified key does not match the specified regex string. This will also filter all resources missing the specified tag key.
- *Exclusion Tags: Any / All* - Whether to filter instances containing any of the specified tags or only those that contain all of them. Only applicable if more than one value is entered in the `Exclusion Tags` field.
- *Email addresses* - Email addresses of the recipients you wish to notify.
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked

## Actions

- Sends an email notification

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Subscription/aliases/read
- Microsoft.ContainerService/managedClusters/*

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
