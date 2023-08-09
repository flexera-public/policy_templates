# Google Rule-Based Dimension From Project Labels

## What it does

This policy creates and updates custom Rule-Based Dimensions that surface the specified Google Project label keys in the Flexera One platform. This allows costs to be sliced by the values of the label keys in question.

## Input Parameters

This policy has the following input parameters required when launching the policy.

- *Effective Date* - The month and year in YYYY-MM format that you want the rules to apply. This should be left at its default value in most cases to ensure that the rules apply to all costs, including historical costs.
- *Label Keys* - A list of Google Project label keys to create custom Rule-Based Dimensions for.

## Prerequisites

This policy uses [credentials](https://docs.flexera.com/flexera/EN/Automation/ManagingCredentialsExternal.htm) for connecting to the cloud -- in order to apply this policy you must have a credential registered in the system that is compatible with this policy. If there are no credentials listed when you apply the policy, please contact your cloud admin and ask them to register a credential that is compatible with this policy. The information below should be consulted when creating the credential.

### Credential configuration

- [**Google Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm#automationadmin_4184813559_1121577) (*provider=gce*) which has the following permissions:
- The `resourcemanager.projects.get` permission

- [**Flexera Credential**](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) (*provider=flexera*) which has the following roles:
  - `common:org:own`
  - `optima:rule_based_dimension`

The [Provider-Specific Credentials](https://docs.flexera.com/flexera/EN/Automation/ProviderCredentials.htm) page in the docs has detailed instructions for setting up Credentials for the most common providers.

## Supported Clouds

- Google

## Cost

This Policy Template does not launch any instances, and so does not incur any cloud costs.
