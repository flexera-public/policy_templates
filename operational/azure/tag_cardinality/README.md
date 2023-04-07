# Azure Tag Cardinality Report

## What it does

This Policy Template is used to generate a tag cardinality (how many unique values each tag key has) report for Azure. The report includes cardinality for all tag values for Azure Subscriptions, Resource Groups, and Resources.

## Functional Details

This policy performs the following action:

- Connect to the Azure Resource Manager API to get a list of Azure Subscriptions, Resource Groups, and Resources, along with their tags.

## Input Parameters

This policy has the following input parameter required when launching the policy.

- *Email addresses of the recipients you wish to notify* - A list of email addresses to notify

## Policy Actions

This read-only policy is purely for reporting purposes and takes no action.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/resources/read
- Microsoft.Resources/subscriptions/providers/read
- Microsoft.Resources/subscriptions/read
- Microsoft.Resources/resourceGroups/read
- Microsoft.Resources/tags/read

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
