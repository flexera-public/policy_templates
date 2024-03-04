# Azure Databricks Optimizations Policy

## What it does

This Policy Template is used to identify workspaces/clusters that do not have auto-terminate enabled, or set to a threshold > the desired auto-terminate threshold.

## Functional Details

- The policy identifies workspaces/clusters that do not have auto-terminate enabled, or has auto terminate set to a greater threshold than the desired, defined in the parameter. It raises an incident with the workspaces that meet the criteria.
- The Exclusion Tag parameter is a string value. Supply the Tag Key only. Tag Values are not analyzed and therefore are not needed. If the exclusion tag key is used on an Instance, that Instance is presumed to be exempt from this policy.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Exclusion Tag Key* - Only supply the tag key. The policy assumes that the tag value is irrelevant.
- *Email addresses* - A list of email addresses of the recipients you wish to notify
- *Azure Endpoint* - Azure Endpoint to access resources
- *Subscription Allowed List* - Allowed Subscriptions, if empty, all subscriptions will be checked
- *Automatic Actions* - When this value is set, this policy will automatically take the selected action(s).

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy, you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

For administrators [creating and managing credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) to use with this policy, the following information is needed:

- [**Azure Resource Manager Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_109256743_1124668) (*provider=azure_rm*) which has the following permissions:
  - `Microsoft.Compute/virtualMachines/read`
  - `Microsoft.Compute/virtualMachines/write`

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

## Supported Clouds

- Azure Resource Manager

## Cost

This Policy Template does not incur any cloud costs.
