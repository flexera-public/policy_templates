# Azure Rule-Based Dimension From Resource Group Tags

## What it does

This policy creates and updates custom Rule-Based Dimensions that surface the specified Azure Resource Group tag keys in the Flexera One platform. This allows costs to be sliced by the values of the tag keys in question.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Effective Date* - The month and year in YYYY-MM format that you want the rules to apply. This should be left at its default value in most cases to ensure that the rules apply to all costs, including historical costs.
- *Tag Keys* - A list of Azure Resource Group tag keys to create custom Rule-Based Dimensions for.
- *Dimension Names* - A list of names to give the Rule-Based Dimensions in the Flexera platform. Enter names in the same order as the tag keys in the `Tag Keys` field. Dimension names will be derived from tag keys directly if this list is left empty.
- *Subscription Fallback Rules* - Whether or not to create rules for Subscription tags as a fallback for untagged Resource Groups. These rules have the lowest priority; rules created for Resource Group tags will always take precedence.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

- [**Azure Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4184813559_1121576) (*provider=azure_rm*) which has the following permissions:
- Microsoft.Resources/subscriptions/resources/read
- Microsoft.Resources/subscriptions/providers/read
- Microsoft.Resources/resourceGroups/read
- Tag Contributor or Contributor [more details](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json)

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `common:org:own`
  - `optima:rule_based_dimension`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Azure

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
