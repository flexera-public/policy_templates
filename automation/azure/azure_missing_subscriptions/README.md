# Azure Missing Subscriptions

## What It Does

This policy checks the stored Flexera CCO billing data for Azure from 3 days ago to obtain a list of Azure Subscriptions that we have billing data for and compares that to the list of Azure Subscriptions returned by the Azure Resource Manager API. An incident is raised and email sent containing any subscriptions present in Flexera CCO but not returned by the Azure Resource Manager API.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Email Addresses* - Email addresses of the recipients you wish to notify when new incidents are created.
- *Azure Endpoint* - The endpoint to send Azure API requests to. Recommended to leave this at default unless using this policy with Azure China.
- *Subscriptions Ignore List* - A list of Subscription IDs/names to never include in the results. Leave blank to not filter results

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

- [**Azure Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4184813559_1121576) (*provider=azure_rm*) to test. No specific permissions are needed; the purpose of this policy is to reveal which subscriptions the credential does not have access to.

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `billing_center_viewer`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not incur any cloud costs.
