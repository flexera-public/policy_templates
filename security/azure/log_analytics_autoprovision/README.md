# Azure Ensure Log Analytics Auto-Provisioning

## What it does

This policy checks all Azure subscriptions to ensure that, by default, they provision new VMs with the Log Analytics agent. An incident is raised with a list of the offending subscriptions if any subscriptions are found that are not configured this way.

## Functional Details

A list of subscriptions and their autoProvisioningSettings is obtained via the Azure REST API. For the default configuration of each subscription, properties.autoProvision is checked to make sure it is set to "On".

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email addresses to notify* - Email addresses of the recipients you wish to notify when new incidents are created
- *Azure Endpoint* - Azure Endpoint to access resources

## Prerequesites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

Provider tag value to match this policy: `azure_rm`

Required permissions in the provider:

- Microsoft.Resources/subscriptions/read
- Microsoft.Security/autoProvisioningSettings/read

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
